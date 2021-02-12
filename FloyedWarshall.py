
import sys
import string
#Driver Code 
#sys.stdout.write("Maximal item set with total value " + str(totalvalue) + " and weight " + str(W)+":")
        
# Python Program for Floyd Warshall Algorithm
 
# Number of vertices in the graph
V = 4
 
# Define infinity as the large 
# enough value. This value will be
# used for vertices not connected to each other

INF = 99999

filename = ""
filename = sys.argv[1]


with open(filename, "r") as f:
    i=0
    FWGraph = [[]]
    wt = []
    val = []
    weight = []
    score = f.read() # Read all file in case values are not on a single line
    score_ints = [ int(x) for x in score.split() ]# Convert strings to ints
    #print(score_ints)

for i in range(2 ,len(score_ints),3):
    weight.append(score_ints[i])
    score_ints[i] = 0
max_size = max(score_ints)
#print(max_size)
#print(weight)
#print(score_ints)

# Using above second method to create a  
# 2D array 
rows, cols = (max_size, max_size) 
arr = [[INF for i in range(cols)] for j in range(rows)] 
#print(arr) 

for j in range (max_size):
    for i in range(max_size):
        if(j == i):
            arr[i][j] = 0
#print(arr)

def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]

score_ints = remove_values_from_list(score_ints, 0)

#print(score_ints)

n = 2
out = [score_ints[k:k+n] for k in range(0, len(score_ints), n)] 

#print(out)




listofzeros = [0] * (max_size)
#print(listofzeros)
#arr.insert(0,listofzeros)

# for i in range (len(arr)):
#     for j in range(i):
#         print( "III"+str(i),"JJJ" + str(j))
#         arr[out[rows]][out[cols]] = weight[rows]

# print(arr)
# while j>0:
#     arr[score_ints[i]][score_ints[i+1]] = weight[i]

j = len(out)
#print(len(weight))
#print(len(out))
#print(len(arr))
# print(out[4][0],out[4][1])
# print(arr[out[4][0]][out[4][1]])
#print(weight[4])


j=0
for i in range(len(weight)):
    #print(len(score_ints))
    #print("VALUE OF I", i)
    #print(out[i][0],out[i][1])
    #print("ASSIGN WEIGHT", weight[i])
    arr[out[i][0]-1][out[i][1]-1] = weight[i]
    #print(arr)
        
#print(arr)

        

# Solves all pair shortest path 
# via Floyd Warshall Algorithm
 
def floydWarshall(graph):
   
    """ dist[][] will be the output 
       matrix that will finally
        have the shortest distances 
        between every pair of vertices """
    """ initializing the solution matrix 
    same as input graph matrix
    OR we can say that the initial 
    values of shortest distances
    are based on shortest paths considering no 
    intermediate vertices """
    iteration = 0
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
 
    """ Add all vertices one by one 
    to the set of intermediate
     vertices.
     ---> Before start of an iteration, 
     we have shortest distances
     between all pairs of vertices 
     such that the shortest
     distances consider only the 
     vertices in the set 
    {0, 1, 2, .. k-1} as intermediate vertices.
      ----> After the end of a 
      iteration, vertex no. k is
     added to the set of intermediate 
     vertices and the 
    set becomes {0, 1, 2, .. k}
    """
    for k in range(V):
 
        # pick all vertices as source one by one
        for i in range(V):
 
            # Pick all vertices as destination for the
            # above picked source
            for j in range(V):
 
                # If vertex k is on the shortest path from
                # i to j, then update the value of dist[i][j]
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j] )
                if(i == 0 and j == 0 and k == 0 and V == 4):
                    printSolution(dist,iteration)
                    iteration = iteration + 1
        printSolution(dist,iteration)
        iteration = iteration + 1
 
 
# A utility function to print the solution
def printSolution(dist,i):
    print "Iteration " + str(i)
    for i in range(V):
        for j in range(V):
            if(dist[i][j] == INF or dist[i][j] == INF - 2):
                print "%7s" % ("-"),
            else:
                print "%7d\t" % (dist[i][j]),
            if j == V-1:
                print ""
 
 
# Driver program to test the above program
# Let us create the following weighted graph
"""
            10
       (0)------->(3)
        |         /|\
      5 |          |
        |          | 1
       \|/         |
       (1)------->(2)
            3           """
graph = [[0, 5, INF, 10],
         [INF, 0, 3, INF],
         [INF, INF, 0,   1],
         [INF, INF, INF, 0]
         ]
# Print the solution
floydWarshall(arr)
# This code is contributed by Mythri J L