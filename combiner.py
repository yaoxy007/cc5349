#!/usr/bin/python3

import sys

"""
input format: key = {category}   val={video_id, country}
output format: key={category}, val={video ids in that category, [countries in that category]}
"""

def read_map_output(map_output):
    for line in map_output:
        yield line.strip().split("\t")

def combiner():
    data = read_map_output(sys.stdin)
    nums_of_category = {}
    ids_in_country = {}

    for category, vid_and_country in data:
        vid = vid_and_country.split(",")[0]
        country=vid_and_country.split(",")[1]
        nums_of_category.setdefault(category,set()).add(vid)
        ids_in_country.setdefault(vid,set()).add(country)
    
    for cat,idset in nums_of_category.items():
        for ids,countries in ids_in_country.items():
            if ids in list(idset):
                print("{key}\t{val}".format(key=cat,val="%s:%s" % (ids,list(countries.strip()))))
            else:
                continue
    


if __name__ == "__main__":
    combiner()