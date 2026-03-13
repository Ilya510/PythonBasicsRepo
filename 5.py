n, m = map(int, input().split())
matrix = []

for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Транспонирование матрицы
transposed = [[matrix[i][j] for i in range(n)] for j in range(m)]

# Вывод результата
for row in transposed:
    print(*(row))