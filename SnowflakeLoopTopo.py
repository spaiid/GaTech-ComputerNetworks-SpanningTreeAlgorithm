# submitted by Bob Walters, OMSCS Fall 2018
# # Snowflake - loops within loops
#                              1
#                             / \
#                            /   \
#                           2     3
#                            \   /
#                             \ /
#                     11       4      15
#                    /  \    / | \   /  \
#                   /    \  /  |  \ /    \
#                  12-----10---5---14----16
#                   \    /  \  |  / \    /
#                    \  /    \ | /   \  /
#                     13       6      17
#                             / \
#                            /   \
#                           7     8
#                            \   /
#                             \ /
#                              9

topo = { 1 : [2, 3],
         2 : [1, 4],
         3 : [1, 4],
         4 : [2, 3, 5, 10, 14], 
         5 : [4, 6, 10, 14],
         6 : [5, 10, 14, 7, 8],
         7 : [6, 9],
         8 : [6, 9],
         9 : [7, 8],
         10: [4, 5, 6, 11, 12, 13],
         11: [10, 12],
         12: [10, 11, 13],
         13: [10, 12],
         14: [4, 5, 6, 15, 16, 17],
         15: [14, 16],
         16: [14, 15, 17],
         17: [14, 16] }