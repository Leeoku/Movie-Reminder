# Custom movie parser for TheMovieChannel!

This is a unique problem for a unique individual. There are two solutions catalogued in this repo:

### docxcleaner.py
Built to return a (semi) clean list of movies from an originally hand-crafted, botique, docx. 

### main.py 
Built to grab the videos shown today via TMC.com for recording. The movies are then compared to the clean list of movies returning a final list of movies to record. This is hosted on Amazon AWS using CRON to run main.py daily and notifies the user via email.

## Quickstart

```
Ensure python 3 is installed
python3 -m virtualenv
pip install -r requirements.txt
python3 main.py
```

To get the list of cleaned movies from the docx:
Download the appropriate docx then:

```
python3 docxcleaner.py
```
This will be exported as ```cleanmovies.json``` and used in ```main.py```.
This repository does not include ```token.json``` and ```credentials.json``` from Gmail's SMTP authentication.

## Technologies
* <a href = 'https://www.crummy.com/software/BeautifulSoup/bs4/doc/'>Beautifulsoup4</a> - Webscraping
* <a href = 'https://python-docx.readthedocs.io/en/latest/'>Python-Docx</a> - Parsing the .doc file
* <a href = 'https://pypi.org/project/EZGmail/'>EZGmail</a> - Gmail SMTP

## Cloud
Amazon Debian Web Server

## Acknowledgements
Phil for mentoring and guiding me for my first large project.
