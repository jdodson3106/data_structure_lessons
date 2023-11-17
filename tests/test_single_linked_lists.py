import pytest

from src.single_linked_list import Node, LinkedList


def test_create_empty_list():
    ls = LinkedList()
    assert ls is not None
    assert len(ls) == 0

def test_len():
    ls = LinkedList()
    assert len(ls) == 0

    ls.append(Node(data=1))
    assert len(ls) == 1


def test_append():
    ls = LinkedList()
    assert len(ls) == 0

    n1, n2, n3 = Node(data=1), Node(data=2), Node(data=3)
    r1 = ls.append(n1)
    r2 = ls.append(n2)
    r3 = ls.append(n3)

    assert r1 == 1
    assert r2 == 2
    assert r3 == 3
    assert len(ls) == 3


def test_get():
    ls = LinkedList()
    assert len(ls) == 0

    n1, n2, n3 = Node(data=1), Node(data=2), Node(data=3)
    ls.append(n1)
    ls.append(n2)
    ls.append(n3)

    found, idx = ls.get(3)
    assert found == 3
    assert idx == 2

    found2, idx2 = ls.get(100)
    assert found2 is None
    assert idx2 is None


def test_get_at():
    ls = LinkedList()
    assert len(ls) == 0

    n1, n2, n3 = Node(data=1), Node(data=2), Node(data=3)
    ls.append(n1)
    ls.append(n2)
    ls.append(n3)

    r1 = ls.get_at(0)
    r2 = ls.get_at(1)
    r3 = ls.get_at(2)

    assert r1 == 1
    assert r2 == 2
    assert r3 == 3
    assert len(ls) == 3

    with pytest.raises(IndexError) as e:
        ls.get_at(1000)


def test_delete():
    ls = LinkedList()
    assert len(ls) == 0

    d, idx = ls.delete(0)
    assert d is None
    assert idx is None

    n1, n2, n3 = Node(data=1), Node(data=2), Node(data=3)
    ls.append(n1)
    ls.append(n2)
    ls.append(n3)

    deleted, at = ls.delete(2)
    assert deleted == 2
    assert at == 1
    assert len(ls) == 2
    assert ls.get_at(1) == 3

def test_delete_at():
    ls = LinkedList()
    assert len(ls) == 0

    n1, n2, n3 = Node(data=1), Node(data=2), Node(data=3)
    ls.append(n1)
    ls.append(n2)
    ls.append(n3)

    deleted, idx = ls.delete_at(1)
    assert deleted == 2
    assert idx == 1
    assert len(ls) == 2
    assert ls.get_at(1) == 3

    with pytest.raises(IndexError):
        ls.delete_at(1000)


def test_is_empty():
    ls = LinkedList()
    assert ls.is_empty()
    ls.append(Node(data=1))
    assert not ls.is_empty()
