#!/bin/bash

spark-submit \
    --master local[4] \
    part2.py \
    --input file:///home/hadoop/comp5349/cc5349/a1/ \
    --output file:///home/hadoop/comp5349/cc5349/cc5349/
	 

    
