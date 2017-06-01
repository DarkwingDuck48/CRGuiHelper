import sys
import os
import datetime
import arrow        # datatime utility
from Samples import Button, Action, RecentProjectLabel
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QAction, qApp  # Main application classes
from PyQt5.QtWidgets import QLabel, QPushButton, QSizePolicy, QSpacerItem, QLineEdit, QMenu, QGroupBox  # Tools for GUI
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout, QFormLayout # Layouts
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QSize, QSettings, QObject


class NewProjectWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setFixedSize(QSize(560, 410))
        self.setWindowTitle("Create new project")
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.all_box = QVBoxLayout()
        self.central_widget.setLayout(self.all_box)
        #CR Number
        self.form1 = QHBoxLayout()
        self.crnumber_label = QLabel("CR Number")
        self.crnumber_line = QLineEdit()
        self.crnumber_line.editingFinished.connect(self.formJiralink)
        self.crnumber_line.setFixedSize(50, 20)
        self.form1.addWidget(self.crnumber_label)
        self.form1.addWidget(self.crnumber_line)
        self.form1.addStretch(0)

        # CR Title
        self.form2 = QHBoxLayout()
        self.crtitle_label = QLabel("CR title")
        self.crtitle_line = QLineEdit()
        self.crtitle_line.setFixedSize(483, 20)
        self.form2.addWidget(self.crtitle_label)
        self.form2.addWidget(self.crtitle_line)

        # CR Jira's Link
        self.form3 = QHBoxLayout()
        self.jira_link_label = QLabel("Jira's link")
        self.jira_link = QLineEdit()
        self.jira_link.setFixedSize(483, 20)
        self.form3.addWidget(self.jira_link_label)
        self.form3.addWidget(self.jira_link)

        # Docs Folder
        self.form4 = QHBoxLayout()
        self.docs_folder_line = QLineEdit()
        self.docs_foler_label = QLabel("Docs folder")
        self.filebut = Button("...", self.openfile_docs, self.central_widget, True)
        self.form4.addWidget(self.docs_foler_label)
        self.form4.addWidget(self.docs_folder_line)
        self.form4.addWidget(self.filebut)

        # Impacted Area
        self.impactedarea_label = QLabel("Impacted area")
        self.impactedarea_line = QLineEdit()

        self.all_box.addLayout(self.form1)
        self.all_box.addLayout(self.form2)
        self.all_box.addLayout(self.form3)
        self.all_box.addLayout(self.form4)

        self.all_box.addStretch(1)

        self.show()

    def openfile_docs(self):
        filename = QFileDialog.getExistingDirectory(self.central_widget, "Folder to save", str(os.getcwd()))
        self.docs_folder_line.setText(filename)

    def formJiralink(self):
        self.jira_link.setText("https://servicedesk.vimpelcom.com/projects/GRSCM/issues/GRSCM-"
                               + self.crnumber_line.text())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    newprojectwindow = NewProjectWindow()
    utc = arrow.utcnow().to('local').format("MM.DD.YYYY")
    print(utc)
    sys.exit(app.exec_())

