# pylint:disable=W0621

import pytest

from pkg.trie import Trie

_FIRST_WORD = 'trie'
_UNLINKED_WORD = 'word'
_LINKED_WORD = 'trie node'
_LINKED_WORD_2 = 'trie trie'


@pytest.fixture
def empty_trie():
    return Trie()


@pytest.fixture
def single_word_trie(empty_trie):
    single_word_trie = empty_trie
    single_word_trie.add(_FIRST_WORD)
    return single_word_trie


def test_empty_trie(empty_trie):
    assert len(empty_trie) == 0
    assert _FIRST_WORD not in empty_trie


def test_add_none_asserts(empty_trie):
    with pytest.raises(AssertionError):
        empty_trie.add(None)


def test_add_empty_string_asserts(empty_trie):
    with pytest.raises(AssertionError):
        empty_trie.add('')


def test_single_word_tree(single_word_trie):
    assert len(single_word_trie) == len(_FIRST_WORD)
    assert _FIRST_WORD in single_word_trie
    assert _UNLINKED_WORD not in single_word_trie
    assert _LINKED_WORD not in single_word_trie


def test_add_unlinked_word(single_word_trie):
    multi_word_tree = single_word_trie
    multi_word_tree.add(_UNLINKED_WORD)

    assert len(single_word_trie) == len(_FIRST_WORD) + len(_UNLINKED_WORD)
    assert _FIRST_WORD in multi_word_tree
    assert _UNLINKED_WORD in multi_word_tree
    assert _LINKED_WORD not in multi_word_tree


def test_add_linked_word(single_word_trie):
    multi_word_tree = single_word_trie
    multi_word_tree.add(_LINKED_WORD)

    assert len(multi_word_tree) == len(_LINKED_WORD)
    assert _FIRST_WORD in multi_word_tree
    assert _LINKED_WORD in multi_word_tree
    assert _UNLINKED_WORD not in multi_word_tree


def test_add_linked_words(single_word_trie):
    multi_word_tree = single_word_trie
    multi_word_tree.add(_LINKED_WORD)
    multi_word_tree.add(_LINKED_WORD_2)

    common_substring_length = len(_FIRST_WORD) + 1
    assert len(multi_word_tree) == len(_LINKED_WORD) + len(_LINKED_WORD_2) - common_substring_length
    assert _FIRST_WORD in multi_word_tree
    assert _LINKED_WORD in multi_word_tree
    assert _UNLINKED_WORD not in multi_word_tree


def test_add_twice(single_word_trie):
    single_word_trie.add(_FIRST_WORD)
    assert len(single_word_trie) == len(_FIRST_WORD)
