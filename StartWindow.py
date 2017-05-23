import sys
from SettingsWindow import SettingsWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QAction, qApp  # Main application classes
from PyQt5.QtWidgets import QLabel, QPushButton, QSizePolicy, QSpacerItem, QLineEdit, QMenu, QGroupBox  # Tools for GUI
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


class RecentProjectLabel(QLabel):
    """
    Create a clickable label
    """
    def __init__(self, text, link, parent=None):
        """
        
        :param text: project name 
        :param link: link to project
        :param parent: parent widget
        """
        super().__init__(parent)
        self.text = text
        self.link = link
        self.setText(self.text+"\n"+self.link)
        self.setStyleSheet("""QLabel:hover {background-color:#E0FFFF}
                              """
                           )
        self.action = QAction()
        self.action.triggered.connect(self.mousePressEvent)
        self.addAction(self.action)

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == 1:
            print (self.text)
            print (self.link)


class StartWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.recent_Projects = {"Project1": "C:\\ProgramFiles"}
        self.setting_window_active = False

        self.setFixedSize(QSize(560, 410))
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
                                margin-top: 0.3ex;
                                }
                            QGroupBox:title 
                                {subcontrol-origin: margin;
                                 subcontrol-position: top center;
                                 padding: 0 3px;
                                 background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                                                        stop: 0 #FF0ECE, stop: 1 #FFFFFF);
                                 }
                        """
        recent_projects_group.setStyleSheet(groupbox_style)
        recent_projects_group.setMinimumSize(self.width()/2, self.height()/2)
        for i in range(1, 11):
            project = RecentProjectLabel("TestProject"+str(i), "TestProject"+str(i)+"Link", self.central_widget)
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

    def action_open(self):
        print(self.minimumHeight())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    startwindow = StartWindow()
    sys.exit(app.exec_())
