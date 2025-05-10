class Solution:
    def romanToInt(self, s: str) -> int:
        num=0
        s = s[::-1]
        t = 0
        for i in s:
            if i == "M":
                if t <= 1000:
                    num = num + 1000
                else:
                    num = num - 1000
                t = 1000
            if i == "D":
                if t <= 500:
                    num = num + 500
                else:
                    num = num - 500
                t = 500
            if i == "C":
                if t <= 100:
                    num = num + 100
                else:
                    num = num - 100
                t = 100
            if i == "L":
                if t <= 50:
                    num = num + 50
                else:
                    num = num - 50
                t = 50
            if i == "X":
                if t <= 10:
                    num = num + 10
                else:
                    num = num - 10
                t = 10
            if i == "V":
                if t <= 5:
                    num = num + 5
                else:
                    num = num - 5
                t = 5
            if i == "I":
                if t <= 1:
                    num = num + 1
                else:
                    num = num - 1
                t = 1
        return num