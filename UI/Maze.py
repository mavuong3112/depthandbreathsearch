import random
from tkinter import *
from collections import deque
from Pel import *
from Color import *
from TextLabel import *


class maze: 
    # hàm chính của class maze
    def __init__(self,numRow=100,numCol=100):
        self.numRow=numRow
        self.numCol=numCol
        self.mazeMap={}
        self.maze=[]
        self.path={} 
        self._cell_width=50  
        self._win=None 
        self._canvas=None
        self._pels=[]

    @property
    def maze(self):
        return self._maze
    @maze.setter        
    def maze(self,n):
        self._maze=[]
        y=0
        for n in range(self.numCol):
            x = 1
            y = 1+y
            for m in range(self.numRow):
                self.maze.append((x,y))
                self.mazeMap[x,y]={'E':0,'W':0,'N':0,'S':0}
                x = x + 1 
    def openEast(self,x, y):
        # Xóa tường bên phải
        self.mazeMap[x,y]['E']=1
        if y+1<=self.numCol:
            self.mazeMap[x,y+1]['W']=1
    def openWest(self,x, y):
        # Xóa tường bên trái
        self.mazeMap[x,y]['W']=1
        if y-1>0:
            self.mazeMap[x,y-1]['E']=1
    def openNorth(self,x, y):
        # Xóa tường bên tren
        self.mazeMap[x,y]['N']=1
        if x-1>0:
            self.mazeMap[x-1,y]['S']=1
    def openSouth(self,x, y):
        # Xóa tường bên duoi
        self.mazeMap[x,y]['S']=1
        if x+1<=self.numRow:
            self.mazeMap[x+1,y]['N']=1
    
    def createMaze(self, difficulty=0,theme:COLOR=COLOR.dark):
        _stack=[]
        _closed=[]
        self.theme=theme
        # Ngẫu nhiên vị trí của goal
        while (TRUE):
            x = random.randint(1,self.numRow)
            y = random.randint(1,self.numCol)
            if x!= self.numRow or y!= self.numCol: break
        
        self.goal=(x,y)
        def blockedNeighbours(cell):
            n=[]
            for compass in self.mazeMap[cell].keys():
                if self.mazeMap[cell][compass]==0:
                    if compass=='E' and (cell[0],cell[1]+1) in self.maze:
                        n.append((cell[0],cell[1]+1))
                    elif compass=='W' and (cell[0],cell[1]-1) in self.maze:
                        n.append((cell[0],cell[1]-1))
                    elif compass=='N' and (cell[0]-1,cell[1]) in self.maze:
                        n.append((cell[0]-1,cell[1]))
                    elif compass=='S' and (cell[0]+1,cell[1]) in self.maze:
                        n.append((cell[0]+1,cell[1]))
            return n
        def removeWallinBetween(cellST,cellND):
            # xóa tường ở giữa 2 ô
            if cellST[0]==cellND[0]:
                if cellST[1]==cellND[1]+1:
                    self.mazeMap[cellST]['W']=1
                    self.mazeMap[cellND]['E']=1
                else:
                    self.mazeMap[cellST]['E']=1
                    self.mazeMap[cellND]['W']=1
            else:
                if cellST[0]==cellND[0]+1:
                    self.mazeMap[cellST]['N']=1
                    self.mazeMap[cellND]['S']=1
                else:
                    self.mazeMap[cellST]['S']=1
                    self.mazeMap[cellND]['N']=1
        def isCyclic(cellST,cellND):
            ans=False
            if cellST[0]==cellND[0]:
                if cellST[1]>cellND[1]: cellST,cellND=cellND,cellST
                if self.mazeMap[cellST]['S']==1 and self.mazeMap[cellND]['S']==1:
                    if (cellST[0]+1,cellST[1]) in self.maze and self.mazeMap[(cellST[0]+1,cellST[1])]['E']==1:
                        ans= True
                if self.mazeMap[cellST]['N']==1 and self.mazeMap[cellND]['N']==1:
                    if (cellST[0]-1,cellST[1]) in self.maze and self.mazeMap[(cellST[0]-1,cellST[1])]['E']==1:
                        ans= True
            else:
                if cellST[0]>cellND[0]: cellST,cellND=cellND,cellST
                if self.mazeMap[cellST]['E']==1 and self.mazeMap[cellND]['E']==1:
                    if (cellST[0],cellST[1]+1) in self.maze and self.mazeMap[(cellST[0],cellST[1]+1)]['S']==1:
                        ans= True
                if self.mazeMap[cellST]['W']==1 and self.mazeMap[cellND]['W']==1:
                    if (cellST[0],cellST[1]-1) in self.maze and self.mazeMap[(cellST[0],cellST[1]-1)]['S']==1:
                        ans= True
            return ans
       
        _stack.append((x,y))
        _closed.append((x,y))

        while len(_stack) > 0:
            cell = []
            if(x , y +1) not in _closed and (x , y+1) in self.maze:
                cell.append("E")
            if (x , y-1) not in _closed and (x , y-1) in self.maze:
                cell.append("W")
            if (x+1, y ) not in _closed and (x+1 , y ) in self.maze:
                cell.append("S")
            if (x-1, y ) not in _closed and (x-1 , y) in self.maze:
                cell.append("N") 
            if len(cell) > 0:    
                currentCell = (random.choice(cell))
                if currentCell == "E":
                    self.openEast(x,y)
                    self.path[x, y+1] = x, y
                    y = y + 1
                    _closed.append((x, y))
                    _stack.append((x, y))

                elif currentCell == "W":
                    self.openWest(x, y)
                    self.path[x , y-1] = x, y
                    y = y - 1
                    _closed.append((x, y))
                    _stack.append((x, y))

                elif currentCell == "N":
                    self.openNorth(x, y)
                    self.path[(x-1 , y)] = x, y
                    x = x - 1
                    _closed.append((x, y))
                    _stack.append((x, y))

                elif currentCell == "S":
                    self.openSouth(x, y)
                    self.path[(x+1 , y)] = x, y
                    x = x + 1
                    _closed.append((x, y))
                    _stack.append((x, y))

            else:
                x, y = _stack.pop()

        # lặp để tạo nhiều đường dẫn
        if  difficulty!=0:
            
            x,y=self.numRow,self.numCol
            pathCells=[(x,y)]
            while x!=self.numRow or y!=self.numCol:
                x,y=self.path[(x,y)]
                pathCells.append((x,y))
            notPathCells=[i for i in self.maze if i not in pathCells]
            random.shuffle(pathCells)
            random.shuffle(notPathCells)
            pathLength=len(pathCells)
            notPathLength=len(notPathCells)
            countST,countND=pathLength/3* difficulty/100,notPathLength/3* difficulty/100
            
            # Xóa các khối từ đường dẫn ngắn nhất
            count=0
            i=0
            while count<countST: 
                if len(blockedNeighbours(pathCells[i]))>0:
                    cell=random.choice(blockedNeighbours(pathCells[i]))
                    if not isCyclic(cell,pathCells[i]):
                        removeWallinBetween(cell,pathCells[i])
                        count+=1
                    i+=1
                        
                else:
                    i+=1
                if i==len(pathCells):
                    break
            
            if len(notPathCells)>0:
                count=0
                i=0
                while count<countND: 
                    if len(blockedNeighbours(notPathCells[i]))>0:
                        cell=random.choice(blockedNeighbours(notPathCells[i]))
                        if not isCyclic(cell,notPathCells[i]):
                            removeWallinBetween(cell,notPathCells[i])
                            count+=1
                        i+=1
                            
                    else:
                        i+=1
                    if i==len(notPathCells):
                        break
        self._drawMaze(self.theme)
        pel(self,*self.goal,color=COLOR.red)
      
    def _drawMaze(self,theme):
        # Tao Tkinter 
        
        self._LabWidth= 40
        self._win=Tk()
        self._win.title('Nhóm đề tài 2')
        scr_width=self._win.winfo_screenheight()
        scr_height=self._win.winfo_screenheight() 
        self._win.geometry(f"{scr_width}x{scr_height}+0+0")
        self._canvas = Canvas(width=scr_width-10, height=scr_height-10, bg=theme.value[0]) 
        self._canvas.pack(expand=YES, fill=BOTH) 
        # Tính chiều rộng của mê cung
        k=3.25
        if self.numRow>=95 and self.numCol>=95:
            k=0
        elif self.numRow>=80 and self.numCol>=80:
            k=1
        elif self.numRow>=70 and self.numCol>=70:
            k=1.5
        elif self.numRow>=50 and self.numCol>=50:
            k=2
        elif self.numRow>=35 and self.numCol>=35:
            k=2.5 
        elif self.numRow>=22 and self.numCol>=22:
            k=3
        self._cell_width=round(min(((scr_height+25-self.numRow-k*self._LabWidth)/(self.numRow)),((scr_width+20-self.numCol-k*self._LabWidth)/(self.numCol)),90),3)
        
        # Tạo dòng cho mê cung
        if self._win is not None:
            if self.maze is not None:
                for cell in self.maze:
                    x,y=cell
                    w=self._cell_width
                    x=x*w-w+self._LabWidth
                    y=y*w-w+self._LabWidth
                    if self.mazeMap[cell]['E']==False:
                        l=self._canvas.create_line(y + w, x, y + w, x + w,width=2,fill=theme.value[1],tag='line')
                    if self.mazeMap[cell]['W']==False:
                        l=self._canvas.create_line(y, x, y, x + w,width=2,fill=theme.value[1],tag='line')
                    if self.mazeMap[cell]['N']==False:
                        l=self._canvas.create_line(y, x, y + w, x,width=2,fill=theme.value[1],tag='line')
                    if self.mazeMap[cell]['S']==False:
                        l=self._canvas.create_line(y, x + w, y + w, x + w,width=2,fill=theme.value[1],tag='line')
    # Tạo cột cho mê cung
    def _redrawCell(self,x,y,theme):
        w=self._cell_width
        cell=(x,y)
        x=x*w-w+self._LabWidth
        y=y*w-w+self._LabWidth
        if self.mazeMap[cell]['E']==False:
            self._canvas.create_line(y + w, x, y + w, x + w,width=2,fill=theme.value[1])
        if self.mazeMap[cell]['W']==False:
            self._canvas.create_line(y, x, y, x + w,width=2,fill=theme.value[1])
        if self.mazeMap[cell]['N']==False:
            self._canvas.create_line(y, x, y + w, x,width=2,fill=theme.value[1])
        if self.mazeMap[cell]['S']==False:
            self._canvas.create_line(y, x + w, y + w, x + w,width=2,fill=theme.value[1])

    _tracePathList=[]
    def _tracePathSingle(self,a,p,delay):
       
        if (a.x,a.y)==(a.goal):
            del maze._tracePathList[0][0][a]
            if maze._tracePathList[0][0]=={}:
                del maze._tracePathList[0]
                if len(maze._tracePathList)>0:
                    self.tracePath(maze._tracePathList[0][0])
                 
            return
        # Dành cho đường đi ngắn nhất
        if(type(p)==dict):
            if(len(p)==0):
                del maze._tracePathList[0][0][a]
                return
            a.x,a.y=p[(a.x,a.y)]
        # Danh cho đường đi tìm
        if (type(p)==list):
            if(len(p)==0):
                del maze._tracePathList[0][0][a]
                if maze._tracePathList[0][0]=={}:
                    del maze._tracePathList[0]
                    if len(maze._tracePathList)>0:
                        self.tracePath(maze._tracePathList[0][0]) 
                return
            a.x,a.y=p[0]
            del p[0]

        self._win.after(delay, self._tracePathSingle,a,p,delay)    

    def tracePath(self,compass, delay=50):
        self._tracePathList.append((compass,delay))
        if maze._tracePathList[0][0]==compass: 
            for a,p in compass.items():
                if a.goal!=(a.x,a.y) and len(p)!=0:
                    self._tracePathSingle(a,p,delay)
    def run(self):
        self._win.mainloop()
# m = maze()
# m.createMaze()
# m.run()