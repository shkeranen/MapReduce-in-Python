#!/usr/bin/env python

import sys

#initialize varibles
current_word = None
current_count = 0
word = None

#input comes from STDIN (standard input)
for line in sys.stdin:
  
  #remove trailing spaces at the end of each line
  line = line.strip()
  
  #parse the input we got from mapper.py and store as word and count variables
  word, count = line.split('\t', 1)
  
  #convert count (currently a string) to int
  try:
    count = int(count)
  except ValueError:
    #count was not a number
    continue
    
  #this IF switch works due to Hadoop's sorting which the map output is sorted by key (here the key is word) before it is passed to the reducer
  if current_word == word:
    current_count += count
  else:
    if current_word:
      #write result to STDOUT
      print '%s\t%s' % (current_word, current_count)
      
    current_count = count
    current_word = word
  
#do not fortget to output the last word
if current_word == word:
  print '%s\t%s' % (current_word, current_count)
    
