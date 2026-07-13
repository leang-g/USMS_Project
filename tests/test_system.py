"""Basic tests for USMS data structures and seed data."""

from data_structures.hash_table import HashTable
from data_structures.stack import Stack
from data_structures.graph import Graph  # (from graph)
from database import courses_db as courses, students_db as students, teachers_db as teachers, prereq_graph, build_prereq_graph  # (from graph)
from utils.data_generator import seed_database  # (from graph)


def test_seed_database():
    seed_database()

    assert len(students) >= 10
    assert len(teachers) >= 1
    assert len(courses) >= 1


def test_hash_table_insert_search_delete():
    table = HashTable()

    table.insert("S001", "Student One")

    assert table.search("S001") == "Student One"
    assert table.delete("S001") is True
    assert table.search("S001") is None


def test_stack_push_pop():
    stack = Stack()

    stack.push("add_student")

    assert stack.peek() == "add_student"
    assert stack.pop() == "add_student"
    assert stack.is_empty() is True


def test_graph_topological_sort_and_cycle():  # (from graph)
    g = Graph()  # (from graph)
    g.add_edge("CS101", "CS102")
    g.add_edge("CS102", "CS201")

    assert g.is_reachable("CS101", "CS201") is True
    assert g.is_reachable("CS201", "CS101") is False
    assert g.has_cycle() is False  # (from graph)

    order = g.topological_sort()  # (from graph)
    assert order is not None
    assert order.index("CS101") < order.index("CS102") < order.index("CS201")

    g.add_edge("CS201", "CS101")
    assert g.has_cycle() is True  # (from graph)
    assert g.topological_sort() is None  # (from graph)


def test_prereq_graph_built_from_seed():  # (from graph)
    seed_database()
    build_prereq_graph()  # (from graph)

    assert prereq_graph.has_edge("CS101", "CS102")  # (from graph)
    assert prereq_graph.has_cycle() is False  # (from graph)
    assert prereq_graph.topological_sort() is not None  # (from graph)
