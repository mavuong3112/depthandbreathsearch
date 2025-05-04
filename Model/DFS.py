def DFS(m):
    start = (m.numRow, m.numCol)
    visited = [start]
    stack = [start]
    path = {}
    search = []
    while len(stack) > 0:
        # xóa phần tử ở vị trí cuối
        currCell = stack.pop()
        search.append(currCell)
        if currCell == m.goal:
            break
        for d in "WNSE":
            if m.mazeMap[currCell][d] == True:
                if d == "E":
                    neighbourCell = (currCell[0], currCell[1] + 1)
                elif d == "W":
                    neighbourCell = (currCell[0], currCell[1] - 1)
                elif d == "S":
                    neighbourCell = (currCell[0] + 1, currCell[1])
                elif d == "N":
                    neighbourCell = (currCell[0] - 1, currCell[1])
                if neighbourCell in visited:
                    continue
                visited.append(neighbourCell)
                stack.append(neighbourCell)
                path[neighbourCell] = currCell
    dfsPath = {}
    cell = m.goal
    while cell != start:
        dfsPath[path[cell]] = cell
        cell = path[cell]
    return search, dfsPath
