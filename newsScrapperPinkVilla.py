from newspaper import Article

def scrape_news(url):
    """
    Scrapes the content of a news article from a given URL.

    Args:
        url (str): The URL of the news article.

    Returns:
        dict: A dictionary containing the title, author, and text of the article,
              or None if an error occurs.
    """
    try:
        article = Article(url)
        article.download()
        article.parse()

        return {
            "title": article.title,
            "author": article.authors,
            "text": article.text
        }
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    news_url = "https://timesofindia.indiatimes.com/entertainment/hindi/bollywood/news"
    news_data = scrape_news(news_url)

    if news_data:
        print(news_data)
        print("Title:", news_data["title"])
        print("Author:", news_data["author"])
        print("Text:", news_data["text"][:500], "...") # Print only first 500 characters
    else:
        print("Failed to scrape news from the URL.")