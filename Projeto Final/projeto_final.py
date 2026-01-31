import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QScrollArea, QHBoxLayout, QFrame, QPushButton, QLineEdit, QDialog
)
from PyQt5.QtCore import Qt
import feedparser
import yfinance as yf
from datetime import datetime
import python_weather
import asyncio

RSS_FEEDS = [
    "https://www.rtp.pt/noticias/rss",
]

tickers = {
    "GOOGL": "Alphabet Inc.",
    "AAPL": "Apple Inc.",
    "MSFT": "Microsoft Corporation",
    "META": "Meta Platforms, Inc.",
    "AMZN": "Amazon.com, Inc.",
    "IBM": "International Business Machines Corporation",
    "TSLA": "Tesla, Inc.",
    "NVDA": "NVIDIA Corporation",
    "NFLX": "Netflix, Inc.",
    "DIS": "The Walt Disney Company"
}

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
        self.setGeometry(500, 250, 945, 650)

        layout = QVBoxLayout()

        label = QLabel(f'Bem-vindo de volta, {user_name}!')
        label.setStyleSheet("font-size: 35px;")
        layout.addWidget(label)

        label = QLabel('')
        layout.addWidget(label)

        weather_label = QLabel('Tempo')
        layout.addWidget(weather_label)

        full_weather_label = QLabel()
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

        stock_label = QLabel('Bolsa de Valores - Yahoo! Finance')
        layout.addWidget(stock_label)

        stock_scroll = QScrollArea()
        stock_scroll.setWidgetResizable(True)
        stock_content = QWidget()
        stock_content_layout = QVBoxLayout(stock_content)

        eurusd = yf.Ticker("EURUSD=X").info.get("regularMarketPrice")
        usd_to_eur = 1 / eurusd

        for symbol, name in tickers.items():
            stock = yf.Ticker(symbol)
            info = stock.info

            price_usd = info.get("currentPrice")
            change = info.get("regularMarketChangePercent")

            if price_usd is None or change is None:
                continue

            price_eur = price_usd * usd_to_eur
            sign = "+" if change >= 0 else ""
            color = "green" if change >= 0 else "red"

            box = QFrame()
            box.setFrameShape(QFrame.Box)

            box_layout = QHBoxLayout(box)

            left_layout = QVBoxLayout()
            ticker_symbol_label = QLabel(symbol)
            ticker_symbol_label.setStyleSheet("font-size: 22px; font-weight: bold;")
            left_layout.addWidget(ticker_symbol_label)

            company_name_label = QLabel(name)
            company_name_label.setStyleSheet("font-size: 15px;")
            left_layout.addWidget(company_name_label)

            right_layout = QVBoxLayout()
            share_price_label = QLabel(f"{price_eur:.2f}€")
            share_price_label.setStyleSheet("font-size: 22px; font-weight: bold;")
            share_price_label.setAlignment(Qt.AlignRight)
            right_layout.addWidget(share_price_label)

            share_percentage_label = QLabel(f"{sign}{change:.2f}%")
            share_percentage_label.setAlignment(Qt.AlignRight)
            share_percentage_label.setStyleSheet(f"color: {color}; font-weight: bold;")
            right_layout.addWidget(share_percentage_label)

            box_layout.addLayout(left_layout)
            box_layout.addLayout(right_layout)

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
