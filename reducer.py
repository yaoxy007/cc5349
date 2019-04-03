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
    for category,ids,countries in data:
        print(category+" "+ids+" "+countries)
    
    # current_category = ""
    # id_count = 0
    # country_count = 0
    # output = ""
    # c={}
    # for category,ids,countries in data:
    #     country=countries.strip().split(",")
    #     # country=set(country)
    #     if not current_category:
    #         current_category=category
    #     elif category!=current_category:
    #         # total_country = sum(map(lambda x:len(x),c.values()))
    #         # total_ids = len(c)
    #         print("{},{}".format(category,country_count/id_count))
    #         # c.clear()
    #         current_category=category
    #     # c[ids] = c.get(ids,set()) | country
    #     id_count +=1
    #     country_count+=len(country)
    
    # # total_country = sum(map(lambda x:len(x),c.values()))
    # # total_ids = len(c)
    # print("{},{}".format(category,country_count/id_count))

    
if __name__ == "__main__":
    reducer()