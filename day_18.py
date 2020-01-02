# https://adventofcode.com/2019/day/18

import copy
import re   # regular expression
from collections import deque
from lab_vis import LabVis
import time

inputFile = 'input/18_input'


def getInputData():
    '''Reads the input file end returns the data in a list of int'''
    data = []
    with open(inputFile) as input:
        for line in input:
            data.append([line.strip()])
    return data

def getAnwer(x):
    return(x*x-x-1)



def mazeStrFile2MazeMatrix(input):
    print(input)
    mazeMatrix = []
    for line in input:
        mazeMatrix.append([(bool(re.match('[@.a-zA-Z]',ch)), ch) for ch in str(line).strip()])
    return mazeMatrix

def maze2graph(maze):
    print(maze)
    height = len(maze)
    width = len(maze[0]) if height else 0
    graph = {}
    print(height,width)
    graph = {(i, j): [] for j in range(width) for i in range(height) if maze[i][j][0]}
  
    for row, col in graph.keys():
        #graph[(row, col)].append(maze[row][col][1]) # add information of keys doors
        if row < height - 1 and maze[row + 1][col][0]:
            graph[(row, col)].append(("S", (row + 1, col)))
            graph[(row + 1, col)].append(("N", (row, col)))
        if col < width - 1 and maze[row][col + 1][0]:
            graph[(row, col)].append(("E", (row, col + 1)))
            graph[(row, col + 1)].append(("W", (row, col)))
    return graph

def BFS_path(graph, start, goal): #labytinthDisplay):
    # start = (37, 39)
    # goal = (x,y)
    queue = deque([("", start)])
    visited = set()
    while queue:
        path, current = queue.popleft()
        if current == goal:
            return path
        if current in visited:
            continue
        
        visited.add(current)
        labytinthDisplay.drawOxygen(current[0], current[1])
        #labytinthDisplay.draw_text(str(maxPath))
        labytinthDisplay.drawStart(start[0], start[1])
        labytinthDisplay.screen_update()
        #time.sleep(0.05)
        for direction, neighbour in graph[current]:
            queue.append((path + direction, neighbour))
    return "Did not finw a way"

def day18PartOne():
    answer = "unknown"
    print(f'Solution Day 18, Part one:\nAnswer: {answer} \n\n')


def day18PartTwo():
    answer = "unknown"
    print(f'Solution Day 18, Part two:\nAnswer: {answer} \n\n')


if __name__ == "__main__":
    #day18PartOne()
    #day18PartTwo()

    #### Just testing

    file = getInputData()
    maze = mazeStrFile2MazeMatrix(file)
    print(maze)

    # re.match('[.][^.][.]'

    maze1 = ['############',
            '#b.A.@.a...#',
            '############']

    maze2 = ['########################',
            '#f.D.E.e.C.b.A.@.a.B.c.#',
            '######################.#',
            '#d.....................#',
            '########################']

    maze3 = ['########################',
            '#...............b.C.D.f#',
            '#.######################',
            '#.....@.a.B.c.d.A.e.F.g#',
            '########################']

    labytinthDisplay = LabVis(81,81,10)
    #maze = mazeStrFile2MazeMatrix(maze3)
    # print(maze)

    graph = maze2graph(maze)
    print(graph)
    labytinthDisplay.drawLabytinth2(graph)
    labytinthDisplay.drawStart(40, 42)
    labytinthDisplay.screen_update()
    #input()
    minpath = BFS_path(graph, (40,42), (-1,-1))
    print(minpath)
    input()
    

# Run from terminal:
# $ python day_18.py
