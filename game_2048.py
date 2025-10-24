import random

matrix_x = 4
matrix_y = 4

matrix = []
for i_x in range(matrix_x):
    matrix_row = []
    for i_y in range(matrix_y):
        matrix_row.append(random.randrange(0, 6, 2))
    matrix.append(matrix_row)

    print("Пропишите stop что бы завершить игрую")

while True:
    
    for row in matrix:
        print(' '.join(str(val) if val != 0 else '.' for val in row))
        
    input_keybord = input("Ход (w/a/s/d): ").lower()

    if input_keybord == "w":
        for y in range(4):
            for x in range(1, 4):
                if matrix[x][y] != 0:
                    for k in range(x - 1, -1, -1):
                        if matrix[k][y] == 0:
                            matrix[k][y] = matrix[x][y]
                            matrix[x][y] = 0
                            x = k
                        elif matrix[k][y] == matrix[x][y]:
                            matrix[k][y] *= 2
                            matrix[x][y] = 0
                            break
                        else:
                            break

    elif input_keybord == "s":
        for y in range(4):
            for x in range(2, -1, -1):
                if matrix[x][y] != 0:
                    for k in range(x + 1, 4):
                        if matrix[k][y] == 0:
                            matrix[k][y] = matrix[x][y]
                            matrix[x][y] = 0
                            x = k
                        elif matrix[k][y] == matrix[x][y]:
                            matrix[k][y] *= 2
                            matrix[x][y] = 0
                            break
                        else:
                            break

    elif input_keybord == "a":
        for x in range(4):
            for y in range(1, 4):
                if matrix[x][y] != 0:
                    for k in range(y - 1, -1, -1):
                        if matrix[x][k] == 0:
                            matrix[x][k] = matrix[x][y]
                            matrix[x][y] = 0
                            y = k
                        elif matrix[x][k] == matrix[x][y]:
                            matrix[x][k] *= 2
                            matrix[x][y] = 0
                            break
                        else:
                            break

    elif input_keybord == "d":
        for x in range(4):
            for y in range(2, -1, -1):
                if matrix[x][y] != 0:
                    for k in range(y + 1, 4):
                        if matrix[x][k] == 0:
                            matrix[x][k] = matrix[x][y]
                            matrix[x][y] = 0
                            y = k
                        elif matrix[x][k] == matrix[x][y]:
                            matrix[x][k] *= 2
                            matrix[x][y] = 0
                            break
                        else:
                            break
    elif input_keybord == "stop":
        print("Игра приостановленна")
        break
    
    empty = [(x, y) for x in range(4) for y in range(4) if matrix[x][y] == 0]
    if empty:
        x, y = random.choice(empty)
        matrix[x][y] = random.choice([2, 4])
