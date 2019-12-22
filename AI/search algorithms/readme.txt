Note: Make sure that all the files are in the same directory.

There are 5 files in total:
1) ucs.py
2) Node.py
3) input1.txt
4) astar.py
5) h_kassel.txt

ucs.py:

This file contains the following methods:
1) read_file(file_name): 
This method takes a file as input and reads it and returns the data in the file.

2) adj_node(frng, routes, vst_node): 
This method returns all the adjacent nodes connected to a node.
It has parameters like frng (Contains the set of nodes that will be used to find a path currently), routes (contains the routes in the map which helps us to find all the nodes), vst_node (contains all the nodes which have already been visited). This method will return nothing.

3) get_fringe(routes, source, dest_city):
This method sorts the fringe based on the least cost. This method will not return anything.

4) path_retrace(dest_node):
This method helps in retracing the path from destination node to source node. This method will not return anything.

5)ucs(routes, source, dest):
This method implements Uninformed cost search on the routes from source to destination. This method will not return anything.

6)main():
The code starts from this method
are
astar.py:

This file contains the following methods:
1) Priority Queue - Storing each node being processed and assessing costs for each node.


How to run the code:

The command to run the code is:
	python ucs.py <input_file.ext> <source> <destination>
Example:
	python ucs.py input1.txt luebeck kassel
