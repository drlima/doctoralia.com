# -*- coding: utf-8 -*-

import csv
from doctoralia import settings


def write_to_csv(item):
    try:
        with open(settings.csv_file_path) as csvfile:
            rows = len(list(csv.reader(csvfile)))
    except:
        rows = 0
    if rows < 500:
        writer = csv.writer(open(settings.csv_file_path, 'a'), lineterminator='\n')
        writer.writerow([item[key] for key in item.keys()])

class WriteToCsv(object):
    def process_item(self, item, spider):
        write_to_csv(item)
        return item

