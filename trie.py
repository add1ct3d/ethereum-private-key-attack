"""
Simple implementation of a trie-like data structure to store target
ETH addresses.
"""

class EthereumAddressTrie(object):
    """Convert a list of target addresses into a trie.

    Encoding the the target addresses as the prefixes in the trie allows
    use to quickly find how close the guess is to any of the target addresses.

    Each node in the trie corresponds to a prefix in one of the possible
    target addresses.  If there is no path from a node, then there is
    no matching target addresss.

    For example; given the targets [ abcde, abbcd, abcdf, acdef ], the
    resulting trie would look like:

    a -> b -> b -> c -> d
          \-> c -> d -> e
                    \-> f
         c -> d -> e -> f
    """
    def __init__(self, list_of_addresses):
        self._value = {}
        for target in list_of_addresses:
            ptr = self._value
            for digit in target:
                if digit not in ptr:
                    ptr[digit] = {}
                ptr = ptr[digit]

    def Find(self, address):
        """Traverse the trie, matching as far as we can.

        Args: a potential ETH address

        Returns: a tuple of (count, sub_address), where `count` is the
            number of of leading hex digits that match a target address
            and `sub_address` is the first `count` hex digits in the
            address in question.
        """
        trie = self._value
        for count, char in enumerate(address):
            if char not in trie:
                break
            trie = trie[char]
        return count, address[:count]
