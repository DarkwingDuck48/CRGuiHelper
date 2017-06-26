import sys
import os
import os.path
#PyQt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QAction, qApp  # Main application classes
from PyQt5.QtWidgets import QSizePolicy, QSpacerItem, QLineEdit, QMenu, QGroupBox  # Tools for GUI
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout  # Layouts
from PyQt5.QtCore import QSize, QSettings
# Custom
from SettingsWindow import SettingsWindow
from NewProjectWindow import NewProjectWindow
from Samples import Button, Action, RecentProjectLabel,Update_Projects
from databasework import Database

#todo dynamic update of recent projects

class StartWindow(QMainWindow):
    def __init__(self, database_path):
        self.database_path = database_path
        QMainWindow.__init__(self)
        # init special variables
        self.top_menu = None
        self.setting_window_active = False
        self.newproject_window_active = False
        self.database_con = Database(self.database_path)

        self.setFixedSize(QSize(560, 410))
        self.setWindowTitle("CR Helper")
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.statusBar()

        x = Update_Projects(database=self.database_path)
        self.recent_Projects = x.update_database()
        self.menubar_create()

        hbox_layout = QHBoxLayout(self)
        vbox_left = QVBoxLayout()
        vbox_right = QVBoxLayout()
        self.central_widget.setLayout(hbox_layout)

        # Recent projects left tab
        recent_projects_group = QGroupBox("Recent projects")
        recent_projects_group.setLayout(vbox_left)
        # Take fixed size from window and resize group
        groupbox_style = """QGroupBox 
                                {background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                                                stop: 0 #E0E0E0, stop: 1 #FFFFFF);
                                border: 1px solid gray;
                                border-radius: 5px;
                                padding: 5px;
                                margin-top: 0.3ex;
                                font-family: Calibri;
                                font-size: 12px;
                                }
                            QGroupBox:title 
                                {subcontrol-origin: border;
                                 subcontrol-position: top center;
                                 padding: 0 3px;
                                 }
                        """
        recent_projects_group.setStyleSheet(groupbox_style)
        recent_projects_group.setMinimumSize(self.width()/2, self.height()/2)
        # todo replace this to select from database
        print(self.recent_Projects)
        for i in self.recent_Projects.keys():
            project = RecentProjectLabel(i, self.recent_Projects[i], self.central_widget)
            vbox_left.addWidget(project)
        vbox_left.addStretch(1)

        x_but = Button("Test button", self.action_open, self.central_widget)
        vbox_right.addWidget(x_but)
        hbox_layout.addWidget(recent_projects_group)
        hbox_layout.addLayout(vbox_left)
        hbox_layout.addLayout(vbox_right)
        hbox_layout.addStretch(1)

        self.show()

    def create_recent(self, projects):
        if len(projects) == 0:
            list_project = "No recent projects"
        else:
            list_project = []
            for project in projects.keys():
                link_to_project = QAction(str(project), self)
                list_project.append(link_to_project)
        return list_project

    def settings_open(self):
        if not self.setting_window_active:
            self.setting_window = SettingsWindow()
            self.setting_window.show()

    def newproject_open(self):
        if not self.newproject_window_active:
            self.newproject_window = NewProjectWindow(database_path=self.database_path)
            self.newproject_window.show()

    def action_open(self):
        print(self.minimumHeight())

    def menubar_create(self):
        self.top_menu = self.menuBar()
        project_menubar = self.top_menu.addMenu("&File")

        project_menubar.addAction(Action("&New project", self.newproject_open, "Ctrl+N",
                                         "Create new CR Project", parent=self))
        project_menubar.addAction(Action("&Open project", self.action_open, "Ctrl+O",
                                         "Open project", parent=self))

        recent_projects_menubar = project_menubar.addMenu("Recent Project")
        recent_projects = self.create_recent(self.recent_Projects)

        if isinstance(recent_projects, str):
            recent_projects_menubar.addAction(recent_projects)
        elif isinstance(recent_projects, list):
            for recent in recent_projects:
                recent_projects_menubar.addAction(recent)
        project_menubar.addSeparator()
        project_menubar.addAction(Action(text="&Settings", connect=self.settings_open,
                                         statustip="Settings for application", parent=self))
        project_menubar.addSeparator()
        project_menubar.addAction(Action(text="&Exit", connect=qApp.quit,
                                         statustip="Exit Application", parent=self))


if __name__ == '__main__':
    path = os.path.join(os.getcwd(), "resources", "database_test.db")
    data = Database(path)
    connect_database = data.checkDatabase()
    if connect_database:
        app = QApplication(sys.argv)
        startwindow = StartWindow(database_path=path)
        sys.exit(app.exec_())
