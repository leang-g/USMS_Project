"""Basic tests for USMS data structures and seed data."""

from data_structures.hash_table import HashTable
from data_structures.stack import Stack
from database import courses, seed_database, students, teachers


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
