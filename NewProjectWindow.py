import sys
import datetime
import arrow        # datatime utility
from Samples import Button, Action, RecentProjectLabel
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QAction, qApp  # Main application classes
from PyQt5.QtWidgets import QLabel, QPushButton, QSizePolicy, QSpacerItem, QLineEdit, QMenu, QGroupBox  # Tools for GUI
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout  # Layouts
from PyQt5.QtCore import QSize, QSettings


class NewProjectWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setFixedSize(QSize(560, 410))
        self.setWindowTitle("Create new project")


        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    newprojectwindow = NewProjectWindow()
    utc = arrow.utcnow().to('local').format("MM.DD.YYYY")
    print(utc)
    sys.exit(app.exec_())

