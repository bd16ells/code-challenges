class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        for i in range(2**k):
            binary = bin(i)[2:]
            binary = '0'*(k - len(binary)) + binary
            if binary not in s:
                return False
        return True