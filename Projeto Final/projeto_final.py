import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QScrollArea, QFrame
)
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Start Menu')
window.setGeometry(400, 150, 600, 500)

layout = QVBoxLayout()
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

    content_layout.addWidget(box)

scroll.setWidget(content)
layout.addWidget(scroll)

window.setLayout(layout)
window.show()
sys.exit(app.exec_())