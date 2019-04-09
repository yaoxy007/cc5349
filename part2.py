
import sys
from pyspark import SparkContext
import argparse
from datetime import datetime

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

def SeqOp(diffpair,inputpair):
    date1 = diffpair[0][0]
    diff1 = diffpair[0][1]
    date2 = diffpair[1][0]
    diff2 = diffpair[1][1]
    
    inputs = inputpair.split(":")
    dates = datetime.strptime(inputs[0],"%y.%d.%m")
    like = int(inputs[1])
    dislike = int(inputs[2])
    
    if(dates < date1): 
        date2 = date1
        diff2 = diff1
        date1 = dates
        diff1 = dislike - like
    elif(dates < date2):
        date2 = dates
        diff2 = dislike - like
    return [[date1,diff1],[date2,diff2]]

def CombOp(diffpair1, diffpair2):
    return diffpair1
    
MAX_DATE = datetime(9999,1,1)
def remap(diffpair):
    date1 = diffpair[0][0]
    diff1 = diffpair[0][1]
    date2 = diffpair[1][0]
    diff2 = diffpair[1][1]
    if(date1==MAX_DATE or date2==MAX_DATE):
        return 0
    else:
        return diff2-diff1

def order_items(line):
    
    rate = line[1]
    sub_parts = line[0].split(":")
    
    vid = sub_parts[0]
    category = sub_parts[1]
    country = sub_parts[2]
    
    key = vid
    value = str(rate)+", "+category+", "+country
    return key, value


if __name__ == "__main__":
    sc = SparkContext(appName="Top Dislike Growth")

    parser  =  argparse.ArgumentParser()
    parser.add_argument("--input",help="input path", default ='~/')
    parser.add_argument("--output",help="output path",default = '~/')
    args=parser.parse_args()
    input_path=args.input
    output_path=args.output

    videos = sc.textFile(input_path+"AllVideos_short.csv")

    header = videos.first()
    videos=videos.filter(lambda line:line!=header)

    first_mapped_rdd=videos.map(key_and_country)
    aggregated = first_mapped_rdd.aggregateByKey([[MAX_DATE,0],[MAX_DATE,0]],SeqOp,CombOp,1)

    aggregated_result = aggregated.mapValues(remap).sortBy(lambda a:a[1],0)
    result = aggregated_result.map(order_items)
    final = sc.parallelize(result.take(10))
    final.repartition(1).saveAsTextFile(output_path+"output_part2/")
    sc.stop()

