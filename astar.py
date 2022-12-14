import csv
import math
import numpy as np
import matplotlib.pyplot as plt

# start = (0, 3)
# end = (19, 20)
matrix = np.matrix([[1.,1.,1.,0.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.],
  [1.,0.,0.,0.,1.,0.,0.,0.,0.,0.,1.,0.,0.,0.,1.,0.,1.,0.,0.,0.,1.],
  [1.,0.,1.,0.,1.,1.,1.,0.,1.,1.,1.,0.,1.,0.,1.,0.,1.,0.,1.,0.,1.],
  [1.,0.,1.,0.,0.,0.,0.,0.,1.,0.,1.,0.,1.,0.,1.,0.,1.,0.,1.,0.,1.],
  [1.,0.,1.,1.,1.,0.,1.,1.,1.,0.,1.,0.,1.,1.,1.,0.,1.,0.,1.,0.,1.],
  [1.,0.,0.,0.,1.,0.,1.,0.,1.,0.,1.,0.,0.,0.,1.,0.,0.,0.,1.,0.,1.],
  [1.,1.,1.,0.,1.,1.,1.,0.,1.,0.,1.,1.,1.,0.,1.,1.,1.,1.,1.,0.,1.],
  [1.,0.,1.,0.,0.,0.,0.,0.,1.,0.,0.,0.,1.,0.,0.,0.,1.,0.,0.,0.,1.],
  [1.,0.,1.,1.,1.,0.,1.,1.,1.,1.,1.,0.,1.,1.,1.,0.,1.,1.,1.,0.,1.],
  [1.,0.,0.,0.,0.,0.,0.,0.,1.,0.,0.,0.,1.,0.,1.,0.,1.,0.,0.,0.,1.],
  [1.,0.,1.,1.,1.,1.,1.,0.,1.,0.,1.,1.,1.,0.,1.,0.,1.,1.,1.,0.,1.],
  [1.,0.,1.,0.,1.,0.,1.,0.,0.,0.,1.,0.,1.,0.,1.,0.,0.,0.,0.,0.,1.],
  [1.,1.,1.,0.,1.,0.,1.,1.,1.,0.,1.,0.,1.,0.,1.,0.,1.,0.,1.,1.,1.],
  [1.,0.,1.,0.,0.,0.,0.,0.,0.,0.,1.,0.,0.,0.,1.,0.,1.,0.,1.,0.,1.],
  [1.,0.,1.,1.,1.,1.,1.,1.,1.,0.,1.,1.,1.,0.,1.,1.,1.,0.,1.,0.,1.],
  [1.,0.,1.,0.,1.,0.,0.,0.,0.,0.,0.,0.,1.,0.,0.,0.,0.,0.,0.,0.,1.],
  [1.,0.,1.,0.,1.,1.,1.,0.,1.,0.,1.,1.,1.,0.,1.,1.,1.,0.,1.,0.,1.],
  [1.,0.,1.,0.,0.,0.,0.,0.,1.,0.,0.,0.,0.,0.,0.,0.,1.,0.,1.,0.,1.],
  [1.,0.,1.,0.,1.,0.,1.,0.,1.,1.,1.,1.,1.,1.,1.,0.,1.,0.,1.,1.,1.],
  [1.,0.,0.,0.,1.,0.,1.,0.,0.,0.,0.,0.,0.,0.,1.,0.,1.,0.,0.,0.,0.],
  [1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.]])

matrix = np.matrix([[0., 0., 0., 0., 0.], [0., 0., 1., 0., 0.], [0., 1., 1., 0., 0.], [0., 0., 1., 0., 0.], [0., 0., 0., 0., 0.]])


def astar(maze, start, end):
    ## TODO: Implement A start algorithm
    return [(0, 2),(0, 1), (1, 1), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (4, 3)]

def verify(maze, start, end, path):
    if path[0][0]!=start[0] or path[0][1]!=start[1] or path[-1][0]!=end[0] or path[-1][1]!=end[1]:
        print('Start or end incorrect')
        return False
    last = None
    for pos in path:
        if maze[pos] == 1:
            print('Path cross a wall')
            return False
        if last==None:
            last = pos
            continue
        diffX = abs(pos[0] - last[0])
        diffY = abs(pos[1] - last[1])
        if diffX > 1 or diffY > 1 or diffX + diffY > 1:
            print('Path not consecutive')
            return False
        last = pos
    print('Correct path')
    return True


def displayMatrix(mat):
    plt.matshow(mat)
    plt.show()

def displayPath(mat, path):
    if path != None:
        for (y, x) in path:
            mat[x, y] = math.inf
    plt.matshow(mat)
    plt.show()

displayMatrix(matrix)
maze = np.asarray(matrix)
start = (0, 2)
end = (4, 3)

path = astar(maze, start, end)
displayPath(matrix, path)
print(verify(maze, start, end, path))
