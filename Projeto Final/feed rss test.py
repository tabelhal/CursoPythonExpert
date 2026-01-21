import feedparser
from datetime import datetime

# List of active Portuguese news RSS feeds
RSS_FEEDS = [
    "https://www.rtp.pt/noticias/rss",  # RTP Últimas notícias
]


def fetch_all_news():
    all_entries = []

    for url in RSS_FEEDS:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            # Safely extract attributes
            title = getattr(entry, "title", "Sem título")
            link = getattr(entry, "link", "Sem link")
            description = getattr(entry, "summary", "Sem descrição")
            author = getattr(entry, "author", "Sem autor")
            published = getattr(entry, "published", "Sem data")

            # Convert date to readable format if possible
            try:
                if hasattr(entry, "published_parsed"):
                    published = datetime(*entry.published_parsed[:6]).strftime("%Y-%m-%d %H:%M")
            except Exception:
                pass

            # Extract topics/categories
            categories = []
            if hasattr(entry, "tags"):
                categories = [tag.term for tag in entry.tags]
            categories_str = ", ".join(categories) if categories else "Sem tópicos"

            all_entries.append({
                "title": title,
                "description": description,
                "published": published,
                "topics": categories_str
            })

    # Sort by published date descending if possible
    all_entries.sort(key=lambda x: x["published"], reverse=True)

    print(f"Total news fetched: {len(all_entries)}\n")

    # Print first 20 articles
    for i, entry in enumerate(all_entries[:10], 1):
        print(f"{i}. {entry['title']}")
        print(f"   Published: {entry['published']}")
        print(f"   Topics: {entry['topics']}")
        print(f"   Description: {entry['description']}\n")
        print("-" * 150)


if __name__ == "__main__":
    fetch_all_news()
