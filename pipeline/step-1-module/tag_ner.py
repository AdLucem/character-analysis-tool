"""Code to:

(1) Parse the named-entity-tagged characters in output.txt into a graph
(2) Encode the graph as an adjacency list
(3) Store the adjacency list in a file named ../step-2-module/input.txt"""

import json
import os


# purely procedural text-processing piece of crap
if __name__ == '__main__':

    raw_data_filepath = get_raw_data_location(
        '../../data/pride_and_prejudice.filepath')

    with open(raw_data_filepath, 'r+') as f:

        raw_data = f.read()

        # attach start and end offsets to each token
        # in the raw text file
        data_with_offsets = attach_offsets(raw_data)

        # run the NER tagger on the raw text file
        







