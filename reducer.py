#!/usr/bin/python3

import sys

"""
input format: category, video ids in that category, countries in that category
output format: category, average number
"""

def read_combiner_output(output):
    for line in output:
        yield line.strip().split(",")

def reducer():
    data = read_combiner_output(sys.stdin)
    current_category = ""
    id_count = 0
    country_count = 0
    output = ""
    for category,ids,countries in data:
        current_category = category
        country_count += len(countries)
        id_count += 1
        output += "{}\,{}".format(current_category,country_count/id_count)
        if current_category!=category:
            country_count = 0
            id_count = 0
    print(output.strip())



if __name__ == "__main__":
    reducer()