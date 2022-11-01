output = 0
X = int(input())
same = []
for i in range(X):
    a = input().split(" ")
    same.append(a[0])
    same.append(a[1])
Y = int(input())
different = []
for i in range(Y):
    a = input().split(" ")
    different.append(a[0])
    different.append(a[1])
G = int(input())
groups = []
for i in range(G):
    a = input().split(" ")
    groups.append(a[0])
    groups.append(a[1])
    groups.append(a[2])
for i in range(0, X*2, 2):
    index = groups.index(same[i])
    if index % 3 == 0:
        if groups[index+1] == same[i+1] or groups[index+2] == same[i+1]:
            pass
        else:
            output += 1
    elif index % 3 == 1:
        if groups[index+1] == same[i+1] or groups[index-1] == same[i+1]:
            pass
        else:
            output += 1
    else:
        if groups[index-2] == same[i+1] or groups[index-1] == same[i+1]:
            pass
        else:
            output += 1
for i in range(0, Y*2, 2):
    index = groups.index(different[i])
    if index % 3 == 0:
        if groups[index+1] == different[i+1] or groups[index+2] == different[i+1]:
            output += 1
    elif index % 3 == 1:
        if groups[index+1] == different[i+1] or groups[index-1] == different[i+1]:
            output += 1
    else:
        if groups[index-2] == different[i+1] or groups[index-1] == different[i+1]:
            output += 1
# for i in range(G):
#     groups.append(input().split(" "))
# for i in range(0, X*2, 2):
#     for j in range(G):
#         if same[i] in groups[j]:
#             if same[i+1] in groups[j]:
#                 pass
#             else:
#                 output += 1
# for i in range(0, Y*2, 2):
#     for j in range(G):
#         if different[i] in groups[j]:
#             if different[i+1] in groups[j]:
#                 output += 1
print(output)
