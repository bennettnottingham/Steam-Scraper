## Steam Scraper: Extract Top Selling Games Details

A Python-based web scraper that navigates through the Steam Store, focusing on top-selling games, and extracts pertinent details about each game. It utilizes `Selenium` for browser automation and `BeautifulSoup` for parsing and extracting the required data.

### Features:

1. **Automated Scrolling**: Automated full-page scrolling using Selenium to ensure that all the top-selling games are loaded.
2. **Data Extraction**: Extracts the following details:
   - Game Name
   - Release Date
   - Price (Including sale status and the final price)
   - Direct Link to the Game on Steam Store
   - Review Summary
   - Number of Reviews
   - Sale Status (Whether the game is currently on sale)
3. **Output**: Outputs the scraped data to a CSV file named `steam_games.csv`. The CSV contains 9,206 rows, each corresponding to a distinct video game's data.

### Usage:

1. Ensure all required packages (`selenium`, `beautifulsoup4`, `pandas`) are installed.
2. Run the script.

### What's Next?

After successfully scraping the data:

1. **Data Cleaning**: There might be instances where the data extracted is not in its cleanest form. Some potential cleaning steps might involve:
   - Parsing and converting the number of reviews from string format to integers.
   - Standardizing date formats.
   - Handling missing values.
   
2. **Exploratory Data Analysis (EDA)**: Dive deep into the data to identify patterns, trends, or anomalies. Some potential avenues for EDA might be:
   - Visualizing the distribution of game prices.
   - Analyzing the trend of review counts for games over time.
   - Exploring the correlation between review sentiments and game prices.
   
3. **Deep Dive into Reviews**: Instead of just scraping the review summary, we can scrape detailed reviews and perform:
   - **Sentiment Analysis**: Understand the sentiment behind reviews - whether they are positive, negative, or neutral. It could be a proxy to gauge the success or reception of games.
   - **Word Clouds**: Identify frequent words or terms used in the reviews to understand what players are talking about.

---

This project offers a foundational step into understanding the dynamics of the gaming market on the Steam platform. By building upon it, one can drive more insights, inform business decisions, or simply satisfy one's curiosity about the gaming landscape.
