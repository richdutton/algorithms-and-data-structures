class _TrieNode:
    @staticmethod
    def _split_fragment(fragment):
        assert len(fragment)
        return fragment[0], (fragment[1:] if len(fragment) > 1 else None)

    def __init__(self, char=None, fragment=None):
        self._char = char
        self._children = []

        if fragment:
            self._children.append(_TrieNode(*self._split_fragment(fragment)))

    @property
    def char(self):
        return self._char

    def add_fragment(self, fragment):
        first_char, remaining_fragment = self._split_fragment(fragment)
        for child in self._children:
            assert child.char
            if remaining_fragment and child.char == first_char:
                child.add_fragment(remaining_fragment)
                return

        self._children.append(_TrieNode(first_char, remaining_fragment))

    def fragment_exists(self, fragment):
        first_char, remaining_fragment = self._split_fragment(fragment)
        # todo: does it make sense
        for child in self._children:
            if child.char == first_char:
                return child.fragment_exists(remaining_fragment)

        return False


class Trie:
    def __init__(self):
        self._root = _TrieNode()

    def add_word(self, word):
        assert word
        self._root.add_fragment(word)

    def word_exists(self, word):
        assert word
        self._root.fragment_exists(word)
