import sys
import os
import os.path
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QAction, qApp  # Main application classes
from PyQt5.QtWidgets import QLabel, QPushButton, QSizePolicy, QSpacerItem, QLineEdit, QMenu, QGroupBox  # Tools for GUI
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout  # Layouts
from PyQt5.QtCore import QSize, QSettings
from databasework import Database


class Button(QPushButton):
    """
    Base class for button creation
    """

    def __init__(self, text, connect, parent=None, fixed=False):
        """

        :param text: Button name
        :param connect: database_path name
        :param parent: parent name
        :param fixed: if true => fixed size is (40,35) 
        """
        super().__init__(text, parent)
        self.clicked.connect(connect)
        if fixed:
            self.setFixedSize(24, 20)


class Action(QAction):
    """
    Class for create actions in one line
    """

    def __init__(self, text: str, connect, shortcut: str = None, statustip: str = None,
                 parent: QMainWindow = None):
        """

        :param text: Action name
        :param connect: function to execute
        :param shortcut: Shortcut for executing action
        :param statustip: Status tip in status bar
        :param parent: QMainWidget item
        """

        super(Action, self).__init__(text, parent)
        if shortcut:
            self.setShortcut(shortcut)
        if statustip:
            self.setStatusTip(statustip)
        self.triggered.connect(connect)


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
        self.link = link.split("/")
        self.link = "\\".join([self.link[0], self.link[1]]) + "\\...\\" + \
                    "\\".join([self.link[len(self.link) - 2], self.link[len(self.link) - 1]])
        if len(self.link) <= 40:
            self.setText(self.text + "\n" + self.link)
        self.setStyleSheet("""
                            QLabel{
                                border: 0.5px solid grey;
                                font-family: Calibri;
                                font-size: 12px;
                            }
                            QLabel:hover{
                                background-color:#00FF00;
                                font-family: Calibri;
                            }
                            """)
        self.action = QAction()
        self.action.triggered.connect(self.mousePressEvent)
        self.addAction(self.action)

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == 1:
            print(self.text)
            print(self.link)


class Styles:
    def __init__(self):
        self.errorLineEdit = """QLineEdit 
                                        {
                                            border : 2px solid red;
                                            border-radius: 5px;
                                         } 
                                         """
        self.validLineEdit = """QLineEdit 
                                        {
                                            border : 2px inset green;
                                            border-radius: 2px;
                                        }
                                        """
    
    def compare_styles(self, compared, type_stylesheet: str) -> bool:
        """
        
        :param compared: styleSheet from target widget
        :param type_stylesheet: Can be "error" or "valid"
        :return: bool
        """
        if type_stylesheet.lower() == "error":
            if compared == self.errorLineEdit:
                return True
            else:
                return False
        elif type_stylesheet.lower() == "valid":
            if compared == self.validLineEdit:
                return True
            else:
                return False


class Update_Projects:
    def __init__(self, updated_dict= None, database = None):

        self.database_connected = Database(database)
        if updated_dict is None:
            self.top_menu = {}
        else:
            self.top_menu = updated_dict

    def update_database(self):
        with self.database_connected.con:
            cur = self.database_connected.con.cursor()
            self.last_open = [i for i in list(cur.execute('''Select ProjectName, ProjectPath, LastOpened from 
                                             (Select * from AllProjects JOIN Project on AllProjects.id = Project.id
                                                             ) as New ORDER BY New.LastOpened DESC LIMIT 10'''))]
            for i in self.last_open:
                self.top_menu.update({i[0]: i[1]})
        return self.top_menu