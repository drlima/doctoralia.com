![](doctoralia_logo.png)
# Scrappying data from doctoralia.com using scrapy framework

This code is written using Python 3.6 and uses [scrapy 1.4.0.](https://scrapy.org/).

You should install scrapy with pip:
```pip install --user scrapy```

Note: on my system, python points to python3.6 and pip points to pip3.

This spider starts from http://www.doctoralia.com.br/medicos, and goes to the next pages until reach 500 occurrences. Each page displays 20 doctors, hence we scrap the 25 first pages.

# Usage
To run this spider, open the terminal on this repository, then type:
```
cd doctoralia
scrapy crawl doctoralia
```

Your csv file with the scrapped data should be on doctoralia.com/doctoralia/doctoralia_data.csv

![](Scrapy-Logo-Horizontal.png)
