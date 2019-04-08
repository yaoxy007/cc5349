#!/bin/bash

spark-submit \
    --master local[4] \
    part2.py \
    --input file:///home/hadoop/comp5349/cc5349/lab_commons/a1_data/ \
    --output file:///home/hadoop/comp5349/cc5349/cc5349/
	 

    
