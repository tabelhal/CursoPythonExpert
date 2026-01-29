import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QScrollArea,
    QFrame, QPushButton, QLineEdit, QDialog
)

class StartDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Insira o seu nome")
        self.setFixedSize(250, 100)

        layout = QVBoxLayout(self)

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Nome")
        layout.addWidget(self.name_input)

        button = QPushButton("Continue")
        button.clicked.connect(self.accept)  # closes dialog
        layout.addWidget(button)

    def get_name(self):
        return self.name_input.text()


class MainWindow(QWidget):
    def __init__(self, user_name):
        super().__init__()
        self.setWindowTitle('Start Menu')
        self.setGeometry(500, 250, 750, 650)

        layout = QVBoxLayout()

        label = QLabel(f'Bem-vindo de volta, {user_name}!')
        label.setStyleSheet("font-size: 35px;")
        layout.addWidget(label)

        label = QLabel('')
        layout.addWidget(label)

        weather_label = QLabel('Tempo')
        layout.addWidget(weather_label)

        full_weather_label = QLabel('{Estado do Tempo}, {Temperatura}ºC em {Local}')
        layout.addWidget(full_weather_label)
        full_weather_label.setStyleSheet('font-size: 22px')

        label = QLabel('')
        layout.addWidget(label)

        news_label = QLabel('Notícias')
        layout.addWidget(news_label)

        news_scroll = QScrollArea()
        news_scroll.setWidgetResizable(True)
        news_content = QWidget()
        news_content_layout = QVBoxLayout(news_content)

        for i in range(10):
            box = QFrame()
            box.setFrameShape(QFrame.Box)
            box_layout = QVBoxLayout(box)
            title_news_label = QLabel(f"Title #{i+1}")
            box_layout.addWidget(title_news_label)
            title_news_label.setStyleSheet("font-size: 20px; font-weight: bold;")
            small_news_label = QLabel("{Source} | {Date}")
            box_layout.addWidget(small_news_label)
            small_news_label.setStyleSheet("font-size: 12px;")
            box_layout.addWidget(QLabel("{Description}"))
            news_content_layout.addWidget(box)

        news_scroll.setWidget(news_content)
        layout.addWidget(news_scroll)

        label = QLabel('')
        layout.addWidget(label)

        stock_label = QLabel('Bolsa de Valores')
        layout.addWidget(stock_label)


        stock_scroll = QScrollArea()
        stock_scroll.setWidgetResizable(True)
        stock_content = QWidget()
        stock_content_layout = QVBoxLayout(stock_content)

        for i in range(10):
            box = QFrame()
            box.setFrameShape(QFrame.Box)
            box_layout = QVBoxLayout(box)
            box_layout.addWidget(QLabel(f"Title #{i+1}"))
            box_layout.addWidget(QLabel("From {Source}, {Date}"))
            box_layout.addWidget(QLabel("{Description}"))
            stock_content_layout.addWidget(box)

        stock_scroll.setWidget(stock_content)
        layout.addWidget(stock_scroll)

        self.setLayout(layout)


app = QApplication(sys.argv)

dialog = StartDialog()
if dialog.exec_() == QDialog.Accepted:
    user_name = dialog.get_name() or "Usuário"
    main_window = MainWindow(user_name)
    main_window.show()
    sys.exit(app.exec_())
