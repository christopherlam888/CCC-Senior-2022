N = int(input())
A = N
output = 0
if N % 4 == 0:
    output += 1
if N % 5 == 0:
    output += 1
x = N//4 - 1
for i in range(x):
    A -= 4
    if A % 5 == 0:
        output += 1
print(output)
