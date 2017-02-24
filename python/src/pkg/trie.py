# pylint:disable=C0103
# pylint:disable=W0212


class _TrieNode:
    @staticmethod
    def _split_fragment(fragment):
        assert fragment
        return fragment[0], (fragment[1:] if len(fragment) > 1 else None)

    def __init__(self, char=None, fragment=None):
        self._char = char
        self._children = []

        if fragment:
            self._children.append(_TrieNode(*self._split_fragment(fragment)))

    def add_fragment(self, fragment):
        first_char, remaining_fragment = self._split_fragment(fragment)
        assert first_char

        for child in self._children:
            assert child._char

            if child._char == first_char:
                if remaining_fragment:
                    child.add_fragment(remaining_fragment)
                return

        # did not find first_char in children
        self._children.append(_TrieNode(first_char, remaining_fragment))

    def fragment_exists(self, fragment):
        first_char, remaining_fragment = self._split_fragment(fragment)

        for child in self._children:
            if child._char == first_char:
                return True if not remaining_fragment else child.fragment_exists(remaining_fragment)

        return False

    def __str__(self):
        return '{} -> ({})'.format(self._char, ', '.join([str(child) for child in self._children]))

    def __len__(self):
        return sum([len(child) for child in self._children]) + 1


class Trie:
    def __init__(self):
        self._root = _TrieNode()

    def add(self, word):
        assert word
        self._root.add_fragment(word)

    def __contains__(self, word):
        assert word
        return self._root.fragment_exists(word)

    def __str__(self):
        return str(self._root)

    def __len__(self):
        ''' Calculate and return number of nodes in Trie, not including root.  Note: value is not pre-calculated or cached'''
        return len(self._root) - 1
