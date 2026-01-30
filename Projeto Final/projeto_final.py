import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QScrollArea, QHBoxLayout, QFrame, QPushButton, QLineEdit, QDialog
)
import feedparser
from datetime import datetime

RSS_FEEDS = [
    "https://www.rtp.pt/noticias/rss",
]

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
        self.setGeometry(500, 250, 950, 650)

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

        def news():
            all_entries = []

            for url in RSS_FEEDS:
                feed = feedparser.parse(url)
                for entry in feed.entries:
                    title = getattr(entry, "title", "Sem título")
                    description = getattr(entry, "summary", "Sem descrição")
                    published = getattr(entry, "published", "Sem data")

                    try:
                        if hasattr(entry, "published_parsed") and entry.published_parsed:
                            published = datetime(*entry.published_parsed[:6]).strftime("%Y-%m-%d %H:%M")
                    except Exception:
                        pass

                    all_entries.append({
                        "title": title,
                        "description": description,
                        "published": published,
                    })

            all_entries.sort(key=lambda x: x["published"], reverse=True)

            return all_entries


        news_label = QLabel("Notícias - RTP Notícias")
        layout.addWidget(news_label)

        news_scroll = QScrollArea()
        news_scroll.setWidgetResizable(True)

        news_content = QWidget()
        news_content_layout = QVBoxLayout(news_content)

        entries = news()

        for entry in entries[:15]:
            box = QFrame()
            box.setFrameShape(QFrame.Box)

            box_layout = QVBoxLayout(box)

            title_news_label = QLabel(entry["title"])
            title_news_label.setStyleSheet("font-size: 18px; font-weight: bold;")
            box_layout.addWidget(title_news_label)

            date_news_label = QLabel(entry["published"])
            date_news_label.setStyleSheet("font-size: 12px;")
            box_layout.addWidget(date_news_label)

            description_label = QLabel(entry["description"])
            description_label.setWordWrap(True)
            box_layout.addWidget(description_label)

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

        from PyQt5.QtCore import Qt

        for i in range(10):
            box = QFrame()
            box.setFrameShape(QFrame.Box)

            box_layout = QHBoxLayout(box)

            # LEFT COLUMN
            left_layout = QVBoxLayout()
            ticker_symbol_label = QLabel('{Ticker symbol}')
            ticker_symbol_label.setStyleSheet("font-size: 20px; font-weight: bold;")
            left_layout.addWidget(ticker_symbol_label)

            company_name_label = QLabel('{Company Name}')
            company_name_label.setStyleSheet("font-size: 15px;")
            left_layout.addWidget(company_name_label)

            # RIGHT COLUMN
            right_layout = QVBoxLayout()
            share_price_label = QLabel('{XXX.XX}€')
            share_price_label.setStyleSheet("font-size: 20px; font-weight: bold;")
            share_price_label.setAlignment(Qt.AlignRight)
            right_layout.addWidget(share_price_label)

            share_percentage_label = QLabel('-/+ {XX.XX}%')
            share_percentage_label.setAlignment(Qt.AlignRight)
            right_layout.addWidget(share_percentage_label)

            # Assemble
            box_layout.addLayout(left_layout)
            box_layout.addLayout(right_layout)

            box_layout.setStretch(0, 3)
            box_layout.setStretch(1, 1)

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
