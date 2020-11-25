#   Ben Breisch
#   CSCI 101 – Section E
#   Create Project Code
#   References: PyQT5 documentation
#   Time: 30 minutes
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog
from PyQt5 import QtCore
import os

class Gui(QWidget):
    def __init__(self):
        super().__init__()
        # Define variables
        self.flashcard = QPushButton(self)

        self.lbl = QLabel("fuck", self.flashcard)
        self.lbl.setWordWrap(True)

        self.left = QPushButton("<", self)
        self.right = QPushButton(">", self)
        self.words = []
        self.definitions = []
        self.onword = 0
        self.initUI()
    def initUI(self):

        vbox = QVBoxLayout()

        #Button to open file connected to getfile definition
        pathbutton = QPushButton("Open File", self)
        pathbutton.clicked.connect(self.getfile)

        # Set size of flashcard button
        self.flashcard.setFixedSize(200, 200)
        self.flashcard.move(100, 100)
        self.flashcard.clicked.connect(self.flip)
        # Set size and pos of left button
        self.left.setFixedSize(50,50)
        self.left.move(150, 300)
        # Set size and pos of right button
        self.right.setFixedSize(50, 50)
        self.right.move(200, 300)

        vbox.addWidget(pathbutton)
        vbox.addWidget(self.flashcard)

        self.setGeometry(50, 50, 500, 500)
        self.setWindowTitle("PyQt5 Button Click Example")

        self.show()

    def flip(self):
        print(self.flashcard.text())
        if self.flashcard.text() == self.words[self.onword]:
            self.flashcard.setText(self.definitions[self.onword])
        else:
            self.flashcard.setText(self.words[self.onword])


    def getfile(self):
        home_dir = str(sys.path)
        filename = QFileDialog.getOpenFileName(self, 'Open file', home_dir)
        print(filename[0])
        with open(filename[0]) as f:
            for x in f:
                print(x)
                x.strip()
                line = x.split(",")
                self.words.append(line[0])
                self.definitions.append(line[1])

        self.left.clicked.connect(self.moveleft)
        self.right.clicked.connect(self.moveright)
        self.flashcard.setText(self.words[self.onword])

    def moveleft(self):
        if self.onword >= 1:
            self.onword -= 1
        self.flashcard.setText(self.words[self.onword])

    def moveright(self):
        if self.onword < len(self.words) - 1:
            self.onword += 1
        self.flashcard.setText(self.words[self.onword])


def main():
    app = QApplication(sys.argv)
    gui = Gui()
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

