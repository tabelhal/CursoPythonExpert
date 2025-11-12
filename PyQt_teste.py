import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel
)

def greeting():
    value = text_entry.text()
    label.setText('Olá '+value+'! :D')


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Hello World!')

layout = QVBoxLayout()
text_entry = QLineEdit()
button = QPushButton("Dizer olá!")
label = QLabel('')
layout.addWidget(text_entry)
layout.addWidget(button)
layout.addWidget(label)

button.clicked.connect(greeting)

window.setLayout(layout)
window.show()
sys.exit(app.exec_())