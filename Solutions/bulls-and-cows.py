"""
Link: https://leetcode.com/problems/bulls-and-cows/
"""


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret_hash = {}
        for secret_index in range(len(secret)):
            if secret_hash.get(secret[secret_index]) is None:
                default = set()
            else:
                default = secret_hash.get(secret[secret_index])
            default.add(secret_index)
            secret_hash[secret[secret_index]] = default
        bull_sets = set()
        for guess_index in range(len(guess)):
            char = guess[guess_index]
            if char in secret_hash:
                locations = secret_hash[char]
                if guess_index in locations:
                    bull_sets.add(guess_index)

        cow_sets = set()
        for guess_index in range(len(guess)):
            if guess_index in bull_sets:
                continue
            char = guess[guess_index]
            if char in secret_hash:
                locations = secret_hash[char]
                for location in locations:
                    if location not in cow_sets and location not in bull_sets:
                        cow_sets.add(location)
                        break

        return str(len(bull_sets)) + "A" + str(len(cow_sets)) + "B"