def BFS(m):
    start = (m.numRow, m.numCol)
    queue = [start]
    visited = [start]
    path = {}
    search = []
    while len(queue) > 0:
        # xóa phần tử ở vị trí đầu
        currCell = queue.pop(0)
        search.append(currCell)
        if currCell == m.goal:
            break
        for d in "NWSE":
            if m.mazeMap[currCell][d] == True:
                if d == "E":
                    currentCell = (currCell[0], currCell[1] + 1)
                elif d == "W":
                    currentCell = (currCell[0], currCell[1] - 1)
                elif d == "N":
                    currentCell = (currCell[0] - 1, currCell[1])
                elif d == "S":
                    currentCell = (currCell[0] + 1, currCell[1])
                if currentCell in visited:
                    continue
                queue.append(currentCell)
                visited.append(currentCell)
                path[currentCell] = currCell
    bfsPath = {}
    cell = m.goal;
    while cell != start:
        bfsPath[path[cell]] = cell
        cell = path[cell]
    return search, bfsPath
