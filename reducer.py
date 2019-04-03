#!/usr/bin/python3

import sys

"""
input format: category, video ids in that category, countries in that category
output format: category, average number
"""

def read_combiner_output(output):
    for line in output:
        yield line.strip().split(",",2)

def reducer():
    data = read_combiner_output(sys.stdin)
    current_category = ""
    id_count = 0
    country_count = 0
    output = ""
    for category,ids,countries in data:
        country=countries.strip().split(",")
        if current_category != category:
            if current_category!="":
                output = "{},{}".format(current_category,country_count/id_count)
                print(output.strip())
            current_category=category
        country_count += len(country)
        id_count += 1

    if current_category!="":
        output = "{},{}".format(current_category,country_count/id_count)
        print(output.strip())
    
if __name__ == "__main__":
    reducer()