#!/usr/bin/python3

import sys

"""
input format:  key={category}, val={video ids in that category, [countries in that category]}
output format: key={category}, val={average number}
"""

# def read_combiner_output(output):
#     for line in output:
#         yield line.strip().split("\t")

# def reducer():
#     data = read_combiner_output(sys.stdin)
#     current_category = ""
#     c={}

#     for category,ids_and_countries in data:
#         ids = ids_and_countries.strip().split(":")[0]
#         country=ids_and_countries.strip().split(":")[1].strip("[").strip("]")
#         country_list = country.split(",")
#         country=set(country_list)
#         if current_category == "":
#             current_category = category
#         if current_category != category:
#                 total_country = sum(map(lambda x:len(x),c.values()))
#                 total_ids = len(c)
#                 print("{key}, {val}".format(key=category,val=round(total_country/total_ids,2)))
#                 c.clear()
#                 current_category=category
#         c[ids] = c.get(ids,set()) | country
        
#         # if(current_category == category):
#         #     c[ids] = c.get(ids,set()) | country

#         # if current_category!=category:
#         #     if current_category=="":
#         #         c[ids] = c.get(ids,set()) | country
#         #     if current_category!="":
#         #         total_country = sum(map(lambda x:len(x),c.values()))
#         #         total_ids = len(c)
#         #         print("{key}, {val}".format(key=category,val=round(total_country/total_ids,2)))
#         #     current_category=category
#         #     c.clear()

#     # if current_category!="":
#     total_country = sum(map(lambda x:len(x),c.values()))
#     total_ids = len(c)
#     print("{key}\t{val}".format(key=category,val=round(total_country/total_ids,2)))

import sys


def read_combiner_output(line):
    category, parts = line.strip().split('\t')
    parts = parts.split(':')
    video_id = parts[0]
    country=parts[1].strip("[").strip("]")
    country_list = country.split(",")
    country=set(country_list)
    return category, video_id, country


def output(category, country_dict):
    total = sum(map(lambda x: len(x), country_dict.values()))
    num_of_videos = len(country_dict)
    print('%s: %s' % (category, total / num_of_videos))


def reducer():
    """
    Input: category    video_id,country_1,country_2,...,country_n
    Output: category: 1.4
    """
    current_category = ''
    trending_countries = {}
    for line in sys.stdin:
        category, video_id, country_set = read_combiner_output(line)
        if not current_category:
            current_category = category
        elif category != current_category:
            # receiving data with new category means last category finished
            output(current_category, trending_countries)
            trending_countries.clear()
            current_category = category
        # get previous country list if exists and add new countries in it
        trending_countries[video_id] = trending_countries.get(video_id, set()) | country_set
    output(current_category, trending_countries)
    
if __name__ == "__main__":
    reducer()