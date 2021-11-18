# MapReduce-in-Python
A simple implementation of map and reduce functions to Python with HDFS as data storage. 

The file used in this small project is a file full of names of different shapes. 

The MapReduce program was then run on using Hadoop Streaming. 

You can exacute Hadoop streming by: 

hadoop jar usr/lib/hadoop-mapreduce/hadoop-streaming.jar -files mapper.py, reducer.py - input shapes_data.txt (put your own input file) -output shapes_counter -mapper mapper.py -reducer.py
