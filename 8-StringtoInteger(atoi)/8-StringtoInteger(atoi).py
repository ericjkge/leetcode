# Last updated: 6/4/2025, 11:23:50 AM
class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        result = 0
        index = 0
        n = len(s)
        MAX = 2 ** 31 - 1
        MIN = -(2 ** 31)

        # Step 1: whitespace

        while index < n and s[index] == " ":
            index += 1

        # Step 2: signedness

        if index < n and s[index] == "+":
            index += 1
        elif index < n and s[index] == "-":
            sign = -1
            index += 1
        
        # Step 3: conversion
        while index < n and s[index] == "0":
            index += 1

        while index < n and s[index].isdigit():
            result = result * 10 + int(s[index])
            index += 1
        
        # Step 4: rounding
        result *= sign

        if result > MAX:
            return MAX
        if result < MIN:
            return MIN

        return result
        

        
        
        
