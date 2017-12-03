![doctoralia_logo](doctoralia_logo.png)
# Scraping doctoralia.com using scrapy
## Installing scrapy
This code is written on Python 3.6 and uses [scrapy 1.4.0](https://scrapy.org/).

You should install scrapy with pip:
```pip install --user scrapy```

**Note**: on my system, ```python``` points to ```python3.6``` and ```pip``` points to ```pip3```, you should check yours before running.

This spider starts from http://www.doctoralia.com.br/medicos, and goes to the next pages until reach 500 occurrences.

## Usage
To run this spider, open the terminal on this repository, then type:
```
cd doctoralia
scrapy crawl doctoralia
```

Your csv file with the scrapped data should be on doctoralia.com/doctoralia/doctoralia_data.csv

## Further observations
- This spider was designed for getting only the 500 first occurences, thus it will not scrap the entire web site;
- I have only attached instructions for running this spider localy but we could also use scrapinghub's cloud, which has excellent tools for debugging, and data checking;
- The csv structure should be: 
            ``` <Doctor's Name>, <Doctor's Speciality>,  <Doctor's Locations> ```
where fields are:

| Field | Content Type |
| ---  | --- |
| Doctor's Name | String |
| Doctor's Speciality | List of strings with all specialities |
| Doctor's Locations | List of strings with all locations |


![Scrapy-Logo](Scrapy-Logo-Horizontal.png)
