# -*- coding: utf-8 -*-
import sys
import os
import os.path
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QAction                     # Main application classes
from PyQt5.QtWidgets import QLabel, QPushButton, QSizePolicy, QSpacerItem, QLineEdit        # Tools for GUI
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout                           # Layouts
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QSize


class Button(QPushButton):
    """
    Base class for button creation
    """
    def __init__(self, text, connect, parent=None, fixed=False):
        """
        
        :param text: Button name
        :param connect: connection name
        :param parent: parent name
        :param fixed: if true => fixed size is (24,20) 
        """
        super().__init__(text, parent)
        self.clicked.connect(connect)
        if fixed:
            self.setFixedSize(24, 20)


class SettingsWindow(QMainWindow):
    """
    Window for creation of test users
    """

    def __init__(self):
        QMainWindow.__init__(self)

        self.setFixedSize(QSize(740, 290))
        self.setWindowTitle("Settings")
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        #grid_layout = QGridLayout(self)
        vbox_all = QVBoxLayout(self)
        self.central_widget.setLayout(vbox_all)
        # HFM
        hbox_hfm = QHBoxLayout(self)
        hfm_path_but = Button("...", self.get_HFM_settings, self.central_widget, fixed=True)
        self.path_to_secHFM = QLineEdit()
        self.path_to_secHFM.setFixedSize(600, 20)
        hbox_hfm.addWidget(QLabel("GRSHFM sec file"))
        hbox_hfm.addWidget(self.path_to_secHFM)
        hbox_hfm.addWidget(hfm_path_but)
        #HPL
        hbox_hpl = QHBoxLayout(self)
        hpl_path_but = Button("...", self.get_HPL_settings, self.central_widget, fixed=True)
        self.path_to_secHPL = QLineEdit()
        self.path_to_secHPL.setFixedSize(600, 20)
        hbox_hpl.addWidget(QLabel("GRSHPL sec file"))
        hbox_hpl.addWidget(self.path_to_secHPL)
        hbox_hpl.addWidget(hpl_path_but)
        # VDP
        hbox_vdp = QHBoxLayout(self)
        vdp_path_but = Button("...", self.get_VDP_settings, self.central_widget, fixed=True)
        self.path_to_secVDP = QLineEdit()
        self.path_to_secVDP.setFixedSize(600, 20)
        hbox_vdp.addWidget(QLabel("VDP sec file"))
        hbox_vdp.addWidget(self.path_to_secVDP)
        hbox_vdp.addWidget(vdp_path_but)
        # ownCloud
        hbox_owncloud = QHBoxLayout(self)
        owncloud_path_but = Button("...", self.get_owncloud_settings, self.central_widget, fixed=True)
        self.path_to_owncloud = QLineEdit()
        self.path_to_owncloud.setFixedSize(600,20)
        hbox_owncloud.addWidget(QLabel("OwnCloud file"))
        hbox_owncloud.addWidget(self.path_to_owncloud)
        hbox_owncloud.addWidget(owncloud_path_but)

        hbox_buttons = QHBoxLayout()
        self.save_but = Button("Save", self.save_settings, self.central_widget)
        self.save_but.setFixedSize(60, 25)
        self.cancel_but = Button("Cancel", self.cancel_settings, self.central_widget)
        self.cancel_but.setFixedSize(60, 25)
        hbox_buttons.addStretch(1)
        hbox_buttons.addWidget(self.save_but)
        hbox_buttons.addWidget(self.cancel_but)

        #Layout
        vbox_all.addLayout(hbox_hfm)
        vbox_all.addLayout(hbox_hpl)
        vbox_all.addLayout(hbox_vdp)
        vbox_all.addLayout(hbox_owncloud)
        vbox_all.addStretch(1)
        vbox_all.addLayout(hbox_buttons)

        self.show()

    def get_HFM_settings(self):
        filename = QFileDialog.getOpenFileName(self.central_widget, "Choose security file for GRSHFM",
                                                  str(os.getcwd()), 'HFM SecFiles(*.sec)')
        filepath, extention = filename
        self.path_to_secHFM.setText(os.path.split(filepath)[1])
        self.path_to_secHFM.setToolTip(filepath)

    def get_HPL_settings(self):
        filename = QFileDialog.getOpenFileName(self.central_widget, "Choose security file for GRSHPL",
                                                  str(os.getcwd()), 'HPL Filters(*.txt)')
        filepath, extention = filename
        self.path_to_secHPL.setText(os.path.split(filepath)[1])
        self.path_to_secHPL.setToolTip(filepath)

    def get_VDP_settings(self):
        filename = QFileDialog.getOpenFileName(self.central_widget, "Choose security file for VDP",
                                               str(os.getcwd()), 'VDP Filters(*.txt)')
        filepath, extention = filename
        self.path_to_secVDP.setText(os.path.split(filepath)[1])
        self.path_to_secVDP.setToolTip(filepath)

    def get_owncloud_settings(self):
        filename = QFileDialog.getOpenFileName(self.central_widget, "Choose excel file",
                                               str(os.getcwd()), 'Excel(*.xlsx)')
        filepath, extention = filename
        self.path_to_owncloud.setText(os.path.split(filepath)[1])
        self.path_to_owncloud.setToolTip(filepath)

    def save_settings(self):
        pass

    def cancel_settings(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    startwindow = SettingsWindow()
    sys.exit(app.exec_())
