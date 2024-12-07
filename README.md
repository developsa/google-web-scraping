# Google Web Scraping with BeautifulSoup

 This project is a simple application that performs web scraping on Google search results using Python. Based on the word or sentence entered by the user, a Google search is conducted and the results are processed using the BeautifulSoup library. This project serves as an introductory tool for those looking to dive into data collection and processing

## Features
- Takes a word from the user and turns it into a Google search query.
- Fetches the search results using BeautifulSoup.
- Prints each result's link and title to the screen.
- Secures user information using environment variables.

## Libraries Used

- `requests`: Used to send HTTP requests.
- `BeautifulSoup`: Used to parse HTML data and structure the search results.
- `python-dotenv`: Used to load environment variables.

## Installation

1. Ensure Python 3 and pip are installed.
2. Install the necessary libraries by running the following command in the project directory:
   ```bash
   pip install -r requirements.txt
3. Create a .env file and set the USER_AGENT variable:
    ```bash
    USER_AGENT Info = Your Web Browser => F12 => Network => Request Headers => User-Agent
   
4.  Run the project with the following command:
   ```bash
    python main.py