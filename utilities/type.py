x = [0, 0, 0]
x.append([2, 5])

for i in range(len(x)):
    if isinstance(x[i], list):
        for j in range(len(x[i])):
            print(x[i][j], end=' ')
    else:
        print(x[i], end=' ')