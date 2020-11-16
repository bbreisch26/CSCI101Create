#   Ben Breisch
#   CSCI 101 – Section E
#   Create Project Code
#   References: PyQT5 documentation
#   Time: 30 minutes

from PyQt5.QtWidgets import QApplication, QLabel

app = QApplication([])

label = QLabel('Hello World!')
label.show()
app.exec_()