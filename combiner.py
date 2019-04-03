import sys

"""
input format: category, video_id, country
output format: category, video ids in that category, countries in that category
"""

def read_map_output(map_output):
    for line in map_output:
        yield line.strip().split("\,")

def combiner():
    data = read_map_output(sys.stdin)
    nums_of_category = {}
    ids_in_country = {}
    output = ""

    for category, vid, country in data:
        nums_of_category.setdefault(category,set()).add(vid)
        ids_of_category=nums_of_category.values()
        ids_in_country.setdefault(ids_of_category,set()).add(country)
    
    for cat in nums_of_category:
        for ids in ids_in_country:
            if(ids in nums_of_category[cat]):
                output += "{}\,{}\,{}".format(cat,ids,ids_in_country[ids])
    print(output.strip())


if __name__ == "__main__":
    combiner()