import findspark
findspark.init()
import sys
from pyspark import SparkContext

sc = SparkContext(appName="Top Dislike Growth")
output_path = "topDislikes"

videos = sc.textFile("AllVideos_short.csv")

def key_and_country(line):
    line = line.strip()
    parts = line.split(",")
    video_id = parts[0].strip()
    category = parts[3].strip()
    country = parts[11].strip()
    trending_date = parts[1].strip()
    likes = parts[6].strip()
    dislikes = parts[7].strip()
    key = video_id+":"+category+":"+country
    value = trending_date+":"+likes+":"+dislikes
    return key,value

def get_growth_rate(input):
    line = [i for i in input]
    diff=[0,0]
    if len(line)>1:
        for i in range(2):
            like = line[i].split(":")[1]
            dislike = line[i].split(":")[2]
            diff[i] = int(like) - int(dislike)
        growth_rate = diff[0]-diff[1]
        return growth_rate
    else:
        return 0

def order_items(line):
    
    rate = line[1]
    sub_parts = line[0].split(":")
    
    vid = sub_parts[0]
    category = sub_parts[1]
    country = sub_parts[2]
    
    key = vid
    value = str(rate)+", "+category+", "+country
    return key, value

header = videos.first()
videos=videos.filter(lambda line:line!=header)

vv=videos.map(key_and_country)
rdd=vv.groupByKey().mapValues(get_growth_rate)
aggregated_result = rdd.sortBy(lambda a:a[1],0)
result = aggregated_result.map(order_items)
final = sc.parallelize(result.take(10))
final.repartition(1).saveAsTextFile("Output")
sc.stop()

