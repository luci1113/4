from mrjob.job import MRJob #MapReduce jobs #mrjob is currently an active Framework for MapReduce programming
import sys

#With mrjob, we can write code for Mapper and Reducer in a single class. In case we don’t have Hadoop installed then also we can test the mrjob program in our local system environment
class CharacterCount(MRJob):
    #MapReduce is a way of writing programs designed for processing vast amounts of data
    
    '''The below mapper() function defines the mapper for MapReduce and takes  
    key value argument and generates the output in tuple format .  
    The mapper below is splitting the line and generating a word with its own  
    count i.e. 1'''
    def mapper(self, _, line): 
        # Emit each character with count 1
        for char in line:
            yield char, 1
    '''The below reducer() is aggregating the result according to their key and 
    producing the output in a key-value format with its total count'''
    def reducer(self, key, values):
        # Sum up the counts for each character
        yield key, sum(values)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python character_count.py <input_file>")
        sys.exit(1)
    CharacterCount.run()