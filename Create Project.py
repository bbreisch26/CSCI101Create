#   Ben Breisch
#   CSCI 101 – Section E
#   Create Project Code
#   References: PyQT5 documentation
#   Time: 30 minutes

from PyQt5.QtWidgets import QApplication, QLabel
import os
app = QApplication([])

label = QLabel('Hello World!')
label.show()
app.exec_()

filepath = input("Please input the name of the name and definition file csv")
vocab = []
definitions = []
with open(filepath) as f:
    for x in f:
        x.strip()
        y = x.split(",")
        vocab.append(y[0])
        definitions.append(y[1])
        print(y)
print(vocab)