import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel
)

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Start Menu')
window.setGeometry(600, 300, 600, 600)

layout = QVBoxLayout()
text_entry = QLineEdit()
button = QPushButton('Dizer olá!')
label = QLabel('')
layout.addWidget(text_entry)
layout.addWidget(button)
layout.addWidget(label)

window.setLayout(layout)
window.show()
sys.exit(app.exec_())

# Ver se existe caixas com scroll bars para as cenas de notícias/bolsa/other