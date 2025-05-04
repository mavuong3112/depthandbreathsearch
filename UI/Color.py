from tkinter import *
from enum import Enum

# class chứ tất cả các màu sử dụng trong twinker


class COLOR(Enum):
    # Màu của maze
    dark = ("#000000", "#ECF0F1")  # Nền tối (xám đen) viền sáng (trắng nhạt)
    light = ("#ECF0F1", "#2C3E50")  # Nền sáng (trắng nhạt) viền tối (xám đen)

# Màu của goal
    red = ("#E74C3C", "#C0392B")  # Màu đỏ tươi cho mục tiêu 

# Màu của đường đi
    pink = ("#F1C40F", "#F39C12")  
    blue = ("#00509E", "#00C0FF")  



