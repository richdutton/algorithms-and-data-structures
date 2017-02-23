# pylint:disable=W0621

import pytest

from pkg.slist_cycles import Node, has_cycles


@pytest.fixture
def single():
    return Node(42, None)


@pytest.fixture
def single_cycles(single):
    single.next_ = single
    return single


@pytest.fixture
def double_no_cycles(single):
    single.next_ = Node(84, None)
    return single, single.next_


@pytest.fixture
def double_cycles_1_to_0(double_no_cycles):
    double_cycles = double_no_cycles
    double_cycles[1].next_ = double_cycles[0]
    return double_cycles[0]


@pytest.fixture
def double_cycles_1_to_1(double_no_cycles):
    double_cycles = double_no_cycles
    double_cycles[1].next_ = double_cycles[1]
    return double_cycles[0]


@pytest.fixture
def triple_no_cycles(double_no_cycles):
    triple_no_cycles = double_no_cycles
    triple_no_cycles[1].next_ = Node(168, None)
    return triple_no_cycles[0]


@pytest.fixture
def triple_cycles_from_2_to_0(triple_no_cycles):
    triple_cycles = triple_no_cycles
    triple_cycles.next_.next_.next_ = triple_cycles
    return triple_cycles


@pytest.fixture
def triple_cycles_from_2_to_1(triple_no_cycles):
    triple_cycles = triple_no_cycles
    triple_cycles.next_.next_.next_ = triple_cycles.next_
    return triple_cycles


@pytest.fixture
def triple_cycles_from_2_to_2(triple_no_cycles):
    triple_cycles = triple_no_cycles
    triple_cycles.next_.next_.next_ = triple_cycles.next_.next_
    return triple_cycles


def test_asserts_not_none():
    with pytest.raises(AssertionError):
        has_cycles(None)


def test_single_no_cycles(single):
    assert not has_cycles(single)


def test_single_cycles(single_cycles):
    assert has_cycles(single_cycles)


def test_double_no_cycles(double_no_cycles):
    assert not has_cycles(double_no_cycles[0])


def test_double_cycles_1_to_0(double_cycles_1_to_0):
    assert has_cycles(double_cycles_1_to_0)


def test_double_cycles_1_to_1(double_cycles_1_to_1):
    assert has_cycles(double_cycles_1_to_1)


def test_triple_no_cycles(triple_no_cycles):
    assert not has_cycles(triple_no_cycles)


def test_triple_cycles_2_to_0(triple_cycles_from_2_to_0):
    assert has_cycles(triple_cycles_from_2_to_0)


def test_triple_cycles_2_to_1(triple_cycles_from_2_to_1):
    assert has_cycles(triple_cycles_from_2_to_1)


def test_triple_cycles_2_to_2(triple_cycles_from_2_to_2):
    assert has_cycles(triple_cycles_from_2_to_2)


if __name__ == '__main__':
    pytest.main()
