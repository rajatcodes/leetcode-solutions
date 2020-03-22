# https://leetcode.com/problems/multiply-strings/

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        temp = ''
        a = []
        if(num1==0) or (num2==0):
            return '0'
        if(num1==1):
            return num2
        if(num2==1):
            return num1
        if(len(num2)<len(num1)):
            temp = num1
            num1 = num2
            num2 = temp
        n1 = len(num1)
        n2 = len(num2)
        max_len = 0
        for i in reversed(range(n1)):
            b = [0]*((n1-1)-i)
            x = int(num1[i])
            carryover = 0
            for j in reversed(range(n2)):
                y = int(num2[j])*x + carryover
                carryover = y // 10
                y = y % 10
                b.append(y)
            if carryover!=0:
                b.append(carryover)
            if(max_len<len(b)):
                max_len = len(b)
            a.append(b)
        c = []
        print(a)
        for row in a:
            if(len(row)<max_len):
                row.extend([0]*(max_len-len(row)))
            c.append(row)
        carryover = 0
        prod = ''
        flag=True
        for i in range(max_len):
            temp=carryover
            for j in range(len(c)):
                temp=temp+c[j][i]
            temp = int(temp)
            carryover = temp // 10
            temp = temp % 10
            if(temp!=0) & (flag):
                flag=False
            prod = str(temp)+prod
        if carryover!=0:
            prod = str(carryover)+prod
        if(flag):
            prod ='0'
        return prod
        
