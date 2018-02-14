"""Code to:

(1) Parse the named-entity-tagged characters in output.txt into a graph
(2) Encode the graph as an adjacency list
(3) Store the adjacency list in a file named ../step-2-module/input.txt"""

import json


# purely procedural text-processing piece of crap
if __name__ == '__main__':

    g = {}

    with open('output.txt', 'r+') as f:
        s = f.read().split(" ")

        s_split = []

        for index, token in enumerate(s):
            s[index] = token.split("/")

    count = 0

    for index, tokenlist in enumerate(s):

        if (len(tokenlist) == 2) and (tokenlist[1] == 'PERSON'):

            g[str(count)] = {'name' : tokenlist[0].lstrip("\n"), 'edges' : [], 'anti_edges' : []}

            count += 1

    with open('../step-2-module/input.json', 'w+') as f_inp:

        g_json = json.dumps(g)
        f_inp.write(g_json)







