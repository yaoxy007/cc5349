#!/usr/bin/python3

import sys

"""
input format:  key={category}, val={video ids in that category, [countries in that category]}
output format: key={category}, val={average number}
"""

def read_combiner_output(output):
    for line in output:
        yield line.strip().split("\t")

def reducer():
    data = read_combiner_output(sys.stdin)

    current_category = ""
    c={}
    for i in range(100):
        for category,ids_and_countries in data:
            print(category+" "+ids_and_countries)
    # for category,ids_and_countries in data:
    #     ids = ids_and_countries.strip().split(":")[0]
    #     country=ids_and_countries.strip().split(":")[1].strip("[").strip("]")
    #     country_list = country.split(",")
    #     country=set(country_list)
    #     c[ids] = c.get(ids,set()) | country

    #     if current_category!=category:
    #         if current_category!="":
    #             total_country = sum(map(lambda x:len(x),c.values()))
    #             total_ids = len(c)
    #             print("{key}\t{val}".format(key=category,val=round(total_country/total_ids,2)))
    #         current_category=category
    #         c.clear()

    # if current_category!="":
    #     total_country = sum(map(lambda x:len(x),c.values()))
    #     total_ids = len(c)
    #     print("{key}\t{val}".format(key=category,val=round(total_country/total_ids,2)))

    
if __name__ == "__main__":
    reducer()