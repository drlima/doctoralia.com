#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
from doctoralia import settings


def write_to_csv(item):
    writer = csv.writer(open(settings.csv_file_path, 'a'), lineterminator='\n')
    writer.writerow([item[key] for key in item.keys()])

class WriteToCsv(object):
    def process_item(self, item, spider):
        write_to_csv(item)
        return item
