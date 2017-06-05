import sys
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
        self.link = link
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