# [cite_start]Task 3: Web Scraper for News Headlines [cite: 3]

[cite_start]This project is a submission for Task 3 of the Elevate Labs Python Developer Internship[cite: 1, 2].

## 🎯 Objective
[cite_start]The objective of this task is to create a Python script that scrapes the top headlines from a news website and saves them to a text file[cite: 4, 6]. [cite_start]This task demonstrates the ability to automate data collection from a public website[cite: 11].

## 🛠️ Tools Used
* [cite_start]**Python** 
* [cite_start]**requests**: For making HTTP GET requests to fetch the website's HTML[cite: 5, 8].
* [cite_start]**BeautifulSoup**: For parsing the HTML and extracting the required data[cite: 5, 9].

## 🚀 How It Works
1.  The script `scrape_headlines.py` sends an HTTP GET request to a news website (e.g., BBC News).
2.  [cite_start]It uses `BeautifulSoup` to parse the returned HTML content[cite: 9].
3.  [cite_start]It searches for all `<h3>` tags (a common tag for headlines) using `soup.find_all()`.
4.  [cite_start]It extracts the text content from each tag using `.text`  and removes any leading/trailing whitespace.
5.  [cite_start]Finally, it writes each headline to the `headlines.txt` file.

## 📂 Deliverables
1.  **`scrape_headlines.py`**: The Python script used for scraping.
2.  [cite_start]**`headlines.txt`**: The output file containing the scraped headlines.
