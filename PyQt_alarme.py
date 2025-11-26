import sys
from PyQt5.QtWidgets import (
    QApplication, QLabel, QVBoxLayout, QMainWindow, QTimeEdit, QPushButton, QWidget
)
from PyQt5.QtCore import (
    QTimer, QTime
)
from PyQt5.QtGui import QFont
from PyQt5.QtMultimedia import QSound

alarm_time  = None

def set_alarm():
    global alarm_time
    alarm_time = time_entry.time()
    alarm_label.setText("Alarme posto para as " + alarm_time.toString("hh:mm"))

def trigger_alarm():
    global alarm_time
    alarm_label.setText("Alarme a tocar!")
    QSound.play("alarm.wav")
    alarm_time = None

def showTime():
    current_time = QTime.currentTime()
    time_label.setText(current_time.toString('hh:mm:ss'))

    if alarm_time is not None and current_time.toString("hh:mm") == alarm_time.toString("hh:mm"):
        trigger_alarm()


app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle('Alarm clock')
window.setGeometry(200, 200, 400, 200)

layout = QVBoxLayout()
central = QWidget()
central.setLayout(layout)

time_label = QLabel('Error', central)
time_label.setFont(QFont('Times', 75))
layout.addWidget(time_label)

label = QLabel('Selecione a hora do alarme', central)
layout.addWidget(label)

time_entry = QTimeEdit()
layout.addWidget(time_entry)

button = QPushButton('Ligar alarme')
layout.addWidget(button)
button.clicked.connect(set_alarm)

alarm_label = QLabel('‎ ‎ ‎ ', central)
alarm_label.setStyleSheet("color: red; font-size: 17px")
layout.addWidget(alarm_label)

timer = QTimer()
timer.timeout.connect(showTime)
timer.start(1000)

showTime()

window.setCentralWidget(central)
window.show()
sys.exit(app.exec_())