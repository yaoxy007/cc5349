import sys


"""
input format: video_id,               trending_date,            category_id,
              category,               publish_time,             views,
              likes,                  dislikes,                 comment_count,
              ratings_disabled,       video_error_or_removed,   country
"""

def mapper():
    
    for line in sys.stdin:
        line = line.strip()
        parts = line.split("\,")
        
        if(len(parts)!=12):
            continue
        
        video_id = parts[0]
        category = parts[3]
        country = parts[11]

        print("{}\,{}\,{}".format(video_id,category,country))

if __name__ == "__main__":
    mapper()
