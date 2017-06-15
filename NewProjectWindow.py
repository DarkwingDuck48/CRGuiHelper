import sys
import os
import arrow        # datatime utility
# PyQt5 imports
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QAction, qApp  # Main application classes
from PyQt5.QtWidgets import QLabel, QPushButton, QSizePolicy, QSpacerItem, QLineEdit, QMenu, QGroupBox,QCommonStyle  # Tools for GUI
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout, QFormLayout # Layouts
from PyQt5.QtWidgets import QFileDialog,QMessageBox
from PyQt5.QtCore import QSize, QSettings, QObject
# Custom
from Samples import Button, Action, RecentProjectLabel,Styles
from databasework import Database

styles = Styles()


class NewProjectWindow(QMainWindow):
    def __init__(self, parent=None, database=False):
        QMainWindow.__init__(self, parent)

        if database == False:
            self.msg_err = QMessageBox()
            self.msg_err.setIcon(QMessageBox.Critical)
            self.msg_err.setWindowTitle("Critical Error!")
            self.msg_err.setText("Data base is NOT created!")
            self.msg_err.setStandardButtons(QMessageBox.Ok)
            self.msg_err.exec_()

        self.setFixedSize(QSize(560, 410))
        self.setWindowTitle("Create new project")
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.statusBar()
        self.all_box = QVBoxLayout()
        self.central_widget.setLayout(self.all_box)

        # CR Number
        self.form1 = QHBoxLayout()
        self.crnumber_label = QLabel("CR Number")
        self.crnumber_line = QLineEdit()
        # self.crnumber_line.setValidator(QIntValidator(1, 10000, self.central_widget))
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
        self.form5 = QHBoxLayout()
        self.impactedarea_label = QLabel("Impacted area")
        self.impactedarea_line = QLineEdit()
        self.impactedarea_line.setToolTip("All area must be entered with semi-colon separator")
        self.impactedarea_line.setStatusTip("All area must be entered with semi-colon separator")

        self.form5.addWidget(self.impactedarea_label)
        self.form5.addWidget(self.impactedarea_line)

        self.buttons = QHBoxLayout()
        self.ok_but = Button("OK", self.ok_button, self.central_widget)
        self.cancel_but = Button("Cancel", self.cancel_button, self.central_widget)

        self.buttons.addStretch(1)
        self.buttons.addWidget(self.ok_but)
        self.buttons.addWidget(self.cancel_but)

        self.all_box.addLayout(self.form1)
        self.all_box.addLayout(self.form2)
        self.all_box.addLayout(self.form3)
        self.all_box.addLayout(self.form5)
        self.all_box.addLayout(self.form4)
        self.all_box.addLayout(self.buttons)

        self.all_box.addStretch(1)

        self.show()

    def openfile_docs(self):
        filename = QFileDialog.getExistingDirectory(self.central_widget, "Folder to save", str(os.getcwd()))
        self.docs_folder_line.setText(filename)

    def formJiralink(self):
        if self.crnumber_line.text() != "" and self.crnumber_line.text().isdigit():
            self.crnumber_line.setStyleSheet(styles.validLineEdit)
            self.jira_link.setStyleSheet(styles.validLineEdit)
            self.jira_link.setText("https://servicedesk.vimpelcom.com/projects/GRSCM/issues/GRSCM-"
                                   + self.crnumber_line.text())
        else:
            self.jira_link.setStyleSheet(styles.errorLineEdit)
            self.crnumber_line.setStyleSheet(styles.errorLineEdit)

            self.jira_link.setText("No CR number")

    def cancel_button(self):
        print(self.sender().text())

    def ok_button(self):
        print(self.sender().text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    newprojectwindow = NewProjectWindow()
    utc = arrow.utcnow().to('local').format("MM.DD.YYYY")
    print(utc)
    sys.exit(app.exec_())

