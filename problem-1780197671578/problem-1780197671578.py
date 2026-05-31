# Last updated: 5/30/2026, 8:21:11 PM
1class Solution:
2    def passwordStrength(self, password: str) -> int:
3        password = set(list(password))
4        strength = 0
5        for char in password:
6            if char.isalpha():
7                if char.islower():
8                    strength += 1
9                else:
10                    strength += 2
11            elif char.isnumeric():
12                strength += 3
13            elif char in ["!", "@", "#", "$"]:
14                strength += 5
15        
16        return strength