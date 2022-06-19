"""
Link: https://leetcode.com/problems/search-suggestions-system
"""


class Node:
    def __init__(self):
        self.children = {}
        self.words = []


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        pt = self.root
        for character in word:
            if character not in pt.children:
                pt.children[character] = Node()
            pt = pt.children[character]
            pt.words.append(word)

    def start_with(self, word):
        pt = self.root
        results = []
        for character in word:
            if character not in pt.children:
                return []
            pt = pt.children[character]
        results = pt.words
        results.sort()
        return results[:3]


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        product = Trie()
        for item in products:
            product.insert(item)
        results = []
        prefix = ""
        for character in searchWord:
            results.append(product.start_with(prefix + character))
            prefix += character
        return results