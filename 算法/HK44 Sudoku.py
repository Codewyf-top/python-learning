# -*- coding: utf-8 -*-
"""
@Time ： 2021/8/11 7:15 下午
@Auth ： Codewyf
@File ：HK44 Sudoku.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Hesitating

"""
def myprint(matrix):
    for i in range(9):
        print(" ".join(list(map(str,matrix[i]))))

def find_zeros(matrix):
    result = []
    for i in range(9):
        for j in range(9):
            if matrix[i][j] == 0:
                result.append([i,j])
    return result

def isend(matrix):
    for l in matrix:
        if 0 in l:
            return False
    return True

def find_neighbors(matrix,i,j):
    result = []
    result.append(matrix[i])
    result.append([matrix[k][j] for k in range(9)])
    result.append([matrix[k][l] for k in range((i//3)*3,(i//3)*3+3) \
        for l in range((j//3)*3,(j//3)*3+3)])
    return result

def dfs(matrix, zeros):
    if not zeros:
        myprint(matrix)
        return -1
    n, now = len(zeros), zeros[0]
    neibor = find_neighbors(matrix,now[0],now[1])
    for i in range(1,10):
        if i not in neibor[0] and i not in neibor[1] and i not in neibor[2]:
            matrix[now[0]][now[1]] = i
            y = dfs(matrix, zeros[1:n])
            if y == 0:
                matrix[now[0]][now[1]] = 0
                continue
    return 0


matrix = []
for i in range(9):
    s = list(map(int,input().split()))
    matrix.append(s)

dfs(matrix, find_zeros(matrix))


