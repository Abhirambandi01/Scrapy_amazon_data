Title of the project:  Data Crawling from Quotes Store Website using Scrapy
Website link: http://quotes.toscrape.com

Data Contains Quote, Autor_name, Tags of the specific Quote.
Data From all the pages scraped and stored into :
1. csv formatted files (named as: items.csv)
2. json formatted files (named as: items.json)
3. xml formatted files (named as: items.xml)

Most Significantly, The data is crawled and stored in a SQLite3 database, which can be available for further processes for data insights.
It is stored as myquotes.db

Do install requirements.txt before starting the project:
pip install -r requirements.txt

Then you are good to go.

No need to worry about the format of the code, it is well formatted using "black".
Use below commands after completing the project, on project folder:
$ pip install black 
$ black .

