from collections import defaultdict, deque
import random
import time
import unittest


def build_graph(courses, prerequisites):
    graph = defaultdict(list)

    for course in courses:
        graph[course]

    for course, prerequisite in prerequisites:
        graph[prerequisite].append(course)

    return graph


def course_order(graph):
    colors = {course: 0 for course in graph}
    order = deque()

    def dfs(course):
        colors[course] = 1

        for next_course in graph[course]:
            if colors[next_course] == 1:
                return False

            if colors[next_course] == 0:
                if not dfs(next_course):
                    return False

        colors[course] = 2
        order.appendleft(course)
        return True

    for course in graph:
        if colors[course] == 0:
            if not dfs(course):
                return None

    return list(order)


def is_valid_order(order, prerequisites):
    if order is None:
        return False

    positions = {course: index for index, course in enumerate(order)}
    return all(
        prerequisite in positions
        and course in positions
        and positions[prerequisite] < positions[course]
        for course, prerequisite in prerequisites
    )


def make_random_graph(size, edge_count):
    courses = [f"Course{i}" for i in range(size)]
    possible_edges = [
        (courses[j], courses[i])
        for i in range(size)
        for j in range(i)
    ]
    edges = random.sample(possible_edges, min(edge_count, len(possible_edges)))
    return courses, edges


def run_experiment():
    print("\nRuntime experiment")
    print("Courses | Edges | Time (seconds)")

    for size in [100, 200, 400, 800]:
        courses, prerequisites = make_random_graph(size, size * 2)
        graph = build_graph(courses, prerequisites)
        start = time.perf_counter()
        course_order(graph)
        elapsed = time.perf_counter() - start
        print(f"{size:7} | {len(prerequisites):5} | {elapsed:.6f}")


class CoursePlannerTests(unittest.TestCase):
    def test_empty_graph(self):
        self.assertEqual(course_order(build_graph([], [])), [])

    def test_one_course(self):
        graph = build_graph(["Prog101"], [])
        self.assertEqual(course_order(graph), ["Prog101"])

    def test_valid_order(self):
        courses = ["Prog101", "DataStruct", "Algo", "Math101", "Math201"]
        prerequisites = [
            ("DataStruct", "Prog101"),
            ("Algo", "DataStruct"),
            ("Math201", "Math101"),
            ("Algo", "Math201")
        ]
        graph = build_graph(courses, prerequisites)
        order = course_order(graph)
        self.assertTrue(is_valid_order(order, prerequisites))

    def test_cycle(self):
        courses = ["A", "B", "C"]
        prerequisites = [("B", "A"), ("C", "B"), ("A", "C")]
        graph = build_graph(courses, prerequisites)
        self.assertIsNone(course_order(graph))

    def test_multiple_prerequisites(self):
        courses = ["A", "B", "C"]
        prerequisites = [("C", "A"), ("C", "B")]
        graph = build_graph(courses, prerequisites)
        order = course_order(graph)
        self.assertTrue(is_valid_order(order, prerequisites))

    def test_large_graph(self):
        courses, prerequisites = make_random_graph(100, 150)
        graph = build_graph(courses, prerequisites)
        order = course_order(graph)
        self.assertTrue(is_valid_order(order, prerequisites))


if __name__ == "__main__":
    unittest.main(argv=["main.py"], exit=False)
    run_experiment()
