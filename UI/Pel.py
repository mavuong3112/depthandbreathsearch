from tkinter import *
from collections import *
from Color import COLOR
from Maze import *


# khởi tạo điểm màu
class pel:
    def __init__(self, parentMaze, x=None, y=None, color: COLOR = COLOR.pink):

        self._parentMaze = parentMaze
        self.color = color
        if x is None:
            x = parentMaze.numRow
        if y is None:
            y = parentMaze.numCol
        self.x = x
        self.y = y
        self._parentMaze._pels.append(self)
        self.goal = self._parentMaze.goal
        self._body = []
        self.position = (self.x, self.y)

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, newX):
        self._x = newX

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, newY):
        self._y = newY
        w = self._parentMaze._cell_width
        x = self.x * w - w + self._parentMaze._LabWidth
        y = self.y * w - w + self._parentMaze._LabWidth
        self._coord = (y, x, y + w, x + w)

        if hasattr(self, "_head"):
            # đặt màu sắc cho đường đi
            self._parentMaze._canvas.itemconfig(self._head, fill=self.color.value[1], outline="")
            # đặt màu sắc cho điểm bắt đầu
            self._parentMaze._canvas.tag_raise(self._head)
        # chỉnh màu cho điểm đầu
        self._head = self._parentMaze._canvas.create_rectangle(*self._coord, fill=self.color.value[0], outline="")
        # Hiện đường của cạnh
        self._parentMaze._redrawCell(self.x, self.y, theme=self._parentMaze.theme)
