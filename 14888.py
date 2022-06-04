from itertools import permutations
import sys

input = sys.stdin.readline

n = int(input())

a = list(map(int,input().split()))

data = list(map(int,input().split()))

operators = []

for i in range(4):
    for j in range(data[i]):
        if i == 0:
            operators.append('+')
        elif i == 1:
            operators.append('-')
        elif i == 2:
            operators.append('*')
        else:
            operators.append('/')

operators = list(permutations(operators,n-1))

max = 0
min = 1e9

for temp_operators in operators:
    result = a[0]
    for i in range(n-1):
        if temp_operators[i] == '+':
            result = result + a[i+1]
        elif temp_operators[i] == '-':
            result = result - a[i+1]
        elif temp_operators[i] == '*':
            result = result * a[i+1]
        else:
            if result < 0 or a[i+1] < 0:
                result = result / a[i+1]
                result = -result
            else:
                result = result / a[i+1]

    if result > max:
        max = result

    if result < min:
        min = result

print(max)
print(min) 

n = int(input())
data = list(map(int,input().split()))
add,sub,mul,div = map(int,input().split())

min_value = 1e9
max_value = -1e9

def dfs(i,now):
    global min_value, max_value, add, sub, mul, div

    if i == n:
        min_value = min(min_value,now)
        max_value = max(max_value,now)

    else:
        if add > 0:
            add -= 1
            dfs(i+1,now + data[i])
            add += 1
        
        if sub > 0:
            sub -= 1
            dfs(i+1,now - data[i])
            sub += 1

        if mul > 0:
            mul -= 1
            dfs(i+1,now * data[i])
            mul += 1

        if div > 0:
            div -= 1
            dfs(i+1,int(now / data[i]))
            div += 1

dfs(1,data[0])

