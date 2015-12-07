
from grid_test import *

print
print "Unit Test"
main()
# Now do some testing
# left middle: row = 1:M-2, col = 0
#(1-(M-2))*N + (1-1)
print "From unit_test"
for i in range(1,M-1):
  print grid[i*N].get_ul()
  print grid[i*N].get_u()
  print grid[i*N].get_ur()
  print grid[i*N].get_r()
  print grid[i*N].get_br()
  print grid[i*N].get_b()
  print grid[i*N].get_bl()
  print grid[i*N].get_l()
  print grid[i*N].get_self()
  print
# end of left middle

print "test inner squares"
# inner squares: row = 1:M-2, col = 1:N-2
#(1-(M-2))*N + (1-(N-2))
for i in range(1,M-1):
  for j in range(1,N-1):
    print grid[i*N + j].get_ul()
    print grid[i*N + j].get_u()
    print grid[i*N + j].get_ur()
    print grid[i*N + j].get_r()
    print grid[i*N + j].get_br()
    print grid[i*N + j].get_b()
    print grid[i*N + j].get_bl()
    print grid[i*N + j].get_l()
    print grid[i*N + j].get_l_cost()
    print grid[i*N + j].get_ul_cost()
    print grid[i*N + j].get_self()
    print
# end of inner squares

print grid[2*N + 3].get_MN()
# calculate heuristic
START = (7,1)
END = (4,6)
a1 = abs(START[1] - END[1])
print "a1 =",a1
a2 = abs(START[0] - END[0])
print "a2 =",a2
b1 = 14*min(a1,a2)
print "b1 =",b1
b2 = 10*abs(a1-a2)
print "b2 =",b2
d = b1 + b2
print "d =",d


print "end of unit_tests"

# https://www.youtube.com/watch?v=KNXfSOx4eEE
# //========================================================
# // PSEUDO CODE BRO.
# //========================================================
# // 1: Declarations
# // 2: Initialize:
# //    1: Drop current node from openList
# //       Add current node to closedList
# //    2: Set current node as parent for each neighbor
# //       Add neighbors to openList
# //
# //    PART TWO
# //    3: Loop: (thru openList)
# //
# //       (openList should contain neighbors of closedList nodes here)
# //       (current node should be the node with the lowest F-cost from the last set of neighbors)
# //
# //    4: Loop (for each neighbor):
# //       0: Set neighbor w/ lowest F-cost from the openList as current node
# //          Add this new node to the closedList
# //       1: Add openlist'less neighbors to openList
# //          Set current node as parent for neighbor node
# //       2: If neighbor is already on the openList:
# //          1: Get G-cost of neighbor IF: neighbor's parent is current node's parent (default)
# //                                               IF: neighbor's parent is current node
# //          2: If the 2nd G-cost is less:
# //             1: set neighbor's parent to current node
# //             2: recalculate F and G costs (possibly you don't need this)
# //    5: Stop: IF: end node is in closedList or,
# //                IF: end node is not in closedList and openList is empty
# // 4: Save/Return Path
# // 5: Print Results: (if you wanna print)
# //    1: Fill grid with proper symbols
# //    2: Print grid?





















