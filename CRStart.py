import sys
from PyQt5.QtWidgets import (QMainWindow, QPushButton, QApplication, QWidget, QGridLayout, QAction,
                             qApp, QFileDialog)


class Button(QPushButton):
    def __init__(self, text, connect, parent=None, fixed=False):
        super().__init__(text, parent)
        self.clicked.connect(connect)
        if fixed:
            self.setFixedSize(40, 35)


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        # Window settings
        self.setWindowTitle('CR Helper')
        self.centWidget = QWidget()
        self.setCentralWidget(self.centWidget)

        grid = QGridLayout()
        self.centWidget.setLayout(grid)
        self.setGeometry(300, 300, 300, 300)

    # Actions in menu
        #Exit
        exitAction = QAction('&Exit', self)
        exitAction.triggered.connect(qApp.quit)
        #File
        filechoise = QAction('&New', self)
        filechoise.triggered.connect(self.filedialog)

    # Menu bar
        upmenu = self.menuBar()
        file = upmenu.addMenu('&File')
        file.addAction(filechoise)
        file.addAction(exitAction)

    def filedialog(self):
        print('Here will be file dialog!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
