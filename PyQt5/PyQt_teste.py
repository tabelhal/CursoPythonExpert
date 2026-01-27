import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QScrollArea, QFrame
)

def greeting():
    value = text_entry.text()
    label.setText('Olá '+value+'! :D')


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Hello World!')
window.setGeometry(500, 300, 600, 600)

layout = QVBoxLayout()
text_entry = QLineEdit()
button = QPushButton("Dizer olá!")
label = QLabel('')
layout.addWidget(text_entry)
layout.addWidget(button)
layout.addWidget(label)
scroll = QScrollArea()
scroll.setWidgetResizable(True)
content = QWidget()
content_layout = QVBoxLayout(content)


for i in range(10):
    box = QFrame()
    box.setFrameShape(QFrame.Box)

    box_layout = QVBoxLayout(box)
    box_layout.addWidget(QLabel(f"Title #{i+1}"))
    box_layout.addWidget(QLabel("From {Source}, {Date}"))
    box_layout.addWidget(QLabel("{Description}"))
    box_layout.addWidget(QPushButton("Action"))

    content_layout.addWidget(box)

scroll.setWidget(content)
layout.addWidget(scroll)


button.clicked.connect(greeting)

window.setLayout(layout)
window.show()
sys.exit(app.exec_())