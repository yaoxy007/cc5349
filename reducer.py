#!/usr/bin/python3

import sys

"""
input format:  key={category}, val={video ids in that category, [countries in that category]}
output format: key={category}, val={average number}
"""

def read_combiner_output(output):
    for line in output:
        yield line.strip().split("\\t")

def reducer():
    data = read_combiner_output(sys.stdin)
    current_category = ""
    c={}
  
    for category,ids_and_countries in data:
        ids = ids_and_countries.strip().split(",",1)[0]
        country=ids_and_countries.strip().split(",",1)[1]
        country=set(country)
        
        if not current_category:
            current_category=category
        elif category!=current_category:
            total_country = sum(map(lambda x:len(x),c.values()))
            total_ids = len(c)
            print("{},{}".format(category,total_country/total_ids))
            c.clear()
            current_category=category
        c[ids] = c.get(ids,set()) | country
    
    total_country = sum(map(lambda x:len(x),c.values()))
    total_ids = len(c)
    print("{},{}".format(category,total_country/total_ids))

    
if __name__ == "__main__":
    reducer()