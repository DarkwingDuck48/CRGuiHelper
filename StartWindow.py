import sys
from SettingsWindow import SettingsWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QAction, qApp  # Main application classes
from PyQt5.QtWidgets import QLabel, QPushButton, QSizePolicy, QSpacerItem, QLineEdit, QMenu  # Tools for GUI
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout  # Layouts
from PyQt5.QtCore import QSize, QSettings


class Button(QPushButton):
    """
    Base class for button creation
    """

    def __init__(self, text, connect, parent=None, fixed=False):
        """

        :param text: Button name
        :param connect: connection name
        :param parent: parent name
        :param fixed: if true => fixed size is (40,35) 
        """
        super().__init__(text, parent)
        self.clicked.connect(connect)
        if fixed:
            self.setFixedSize(40, 35)


class StartWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.recent_Projects = {"Project1": "C:\\ProgramFiles"}
        self.setting_window_active = False

        self.setMinimumSize(QSize(560, 380))
        self.setWindowTitle("CR Helper")
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.statusBar()

        # Actions for menubar

        create_project_menubar = QAction("&New project", self)
        create_project_menubar.setShortcut("Ctrl+N")
        create_project_menubar.setStatusTip("Create new CR project")

        open_project_menubar = QAction("&Open project", self)
        open_project_menubar.setShortcut("Ctrl+O")
        open_project_menubar.setStatusTip("Open project")

        settings_menubar = QAction("&Settings", self)
        settings_menubar.setStatusTip("Settings for application")
        settings_menubar.triggered.connect(self.settings_open)

        exit_menubar = QAction("&Exit", self)
        exit_menubar.setStatusTip("Exit apllication")
        exit_menubar.triggered.connect(qApp.quit)
        
        # menubar
        self.top_menu = self.menuBar()
        project_menubar = self.top_menu.addMenu("&File")
        project_menubar.addAction(create_project_menubar)
        project_menubar.addAction(open_project_menubar)
        recent_projects_menubar = project_menubar.addMenu("Recent Project")
        recent_projects = self.create_recent(self.recent_Projects)
        if isinstance(recent_projects, str):
            recent_projects_menubar.addAction(recent_projects)
        elif isinstance(recent_projects, list):
            for recent in recent_projects:
                recent_projects_menubar.addAction(recent)
        project_menubar.addSeparator()
        project_menubar.addAction(settings_menubar)
        project_menubar.addSeparator()
        project_menubar.addAction(exit_menubar)

        grid_layout = QGridLayout(self)

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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    startwindow = StartWindow()
    sys.exit(app.exec_())
