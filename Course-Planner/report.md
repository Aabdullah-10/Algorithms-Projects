# Course Planner - Project Report

## 1. Problem Description

The Course Planner helps students arrange their courses according to their prerequisites. A course must be completed before a course that depends on it. The program prints a valid study order. If the prerequisites contain a cycle, the program reports that no valid order exists.

## 2. Graph Model

The problem is represented by a directed graph. Each course is a vertex. Each prerequisite relationship is a directed edge from the prerequisite course to the course that depends on it. An adjacency list stores the graph.

For example, if Prog101 is required before DataStruct, and DataStruct is required before Algo, the edges are Prog101 to DataStruct and DataStruct to Algo.

## 3. Algorithm

The program uses Depth-First Search (DFS) to perform topological sorting. Each vertex has one of three states: unvisited, visiting, or finished. When DFS visits a course, it marks it as visiting and explores its dependent courses. When all its dependent courses are finished, it marks the course as finished and adds it to the front of the result.

If DFS reaches a course that is already being visited, it has found a back edge. This means the graph contains a cycle, so the program returns no study order. Otherwise, the resulting list is a valid topological order.

## 4. Complexity Analysis

Every course is visited once, and every prerequisite edge is checked once. Therefore, the time complexity is Θ(V + E), where V is the number of courses and E is the number of prerequisite relationships. The adjacency list and DFS state use Θ(V + E) space, including the graph representation.

## 5. Experiments and Tests

The program includes unit tests for an empty graph, one course, a valid prerequisite order, a cycle, multiple prerequisites, and a larger generated graph. It also generates larger directed acyclic graphs and measures the runtime for different numbers of courses and edges. The experiment prints the course count, edge count, and measured time when the program runs.

The tests check both that a valid order is returned and that every prerequisite appears before the course that depends on it. The cycle test checks that no order is returned when a cycle exists.

## 6. Conclusion

DFS topological sorting provides a simple way to arrange courses while respecting prerequisites. The cycle check prevents the program from displaying an invalid order. The algorithm runs in Θ(V + E) time, so it can handle larger graphs efficiently.

## 7. Reflection

One interesting point is that a cycle makes course planning impossible, even if most courses have no problem. In the future, the project could be extended to group courses by semester and limit each semester to three courses.
