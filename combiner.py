#!/usr/bin/python3

import sys

"""
input format: category, video_id, country
output format: category, video ids in that category, countries in that category
"""

def read_map_output(map_output):
    for line in map_output:
        yield line.strip().split(",")

def combiner():
    data = read_map_output(sys.stdin)
    nums_of_category = {}
    ids_in_country = {}

    for category, vid, country in data:
        nums_of_category.setdefault(category,set()).add(vid)
        ids_in_country.setdefault(vid,set()).add(country)
    
    for cat,idset in nums_of_category.items():
        for ids,countries in ids_in_country.items():
            if ids in list(idset):
                print("{},{},{}".format(cat,ids,list(countries)))
            else:
                continue
    


if __name__ == "__main__":
    combiner()