# Min-two-disjoint-paths modeling
Roads can be modeled as edges and stations are modeled as vertices in G = (V, E) <br />
Given a network which is a directed graph G = (V,E). Each directed edge (i,j) has length c(i,j).  <br />
Find two edge-disjoint paths from 1 to n (two paths that do not have common edges) such that the sum of lengths of the two paths is minimal.  <br />

# Input  <br />
Line 1: contains 2 positive integers n and m (1 <= n,m <= 30)  <br />
Line i+1 (i = 1, 2, . . ., m): contains 3 positive integers u, v, c in which w is the length of the directed edge(u,v)  <br />

# Output  <br />
Write the sum of lengths of thw two edge-disjoint paths found, or write NOT_FEASIBLE if no solution found.  <br />

# Example  <br />
Input  <br />
10 18  <br />
1 2 2  <br />
1 3 3  <br />
1 4 6  <br />
2 4 8  <br />
2 5 5  <br />
3 4 1  <br />
3 6 7 <br />
4 5 9 <br />
4 6 3 <br />
5 8 9 <br />
5 9 1 <br />
6 7 4 <br />
6 8 4 <br />
7 8 8 <br />
7 10 4 <br />
8 9 5 <br />
8 10 5 <br />
9 10 3 <br />


Output <br />
26 

