# Course Planner

A simple Python project that finds a valid order for taking courses based on their prerequisites.

## How it works

- Each course is a vertex in a directed graph.
- An edge goes from a prerequisite to the course that depends on it.
- DFS is used to create a topological order.
- If DFS finds a cycle, no valid order is returned.

## Run

```bash
python main.py
```

The program runs the unit tests and then prints a small runtime experiment.

## Complexity

The graph is processed in `O(V + E)` time, where `V` is the number of courses and `E` is the number of prerequisite relationships.
