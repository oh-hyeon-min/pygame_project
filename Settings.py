import os

# 게임 세팅 - 시험해보기 주석

# 화면 사이즈
import pygame

horizontal_margin = 200
vertical_margin = 100
screen_width = 1056 + horizontal_margin * 2
screen_height = 576 + vertical_margin * 2

bgm_vol = 100
effect_vol = 100
vol_ratio = 0.25

# 색
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
# 프레임
FPS = 60
# 타일 사이즈
tile_width_size = 48
tile_height_size = 48
# 이미지 경로
current_path = os.path.dirname(__file__)
images_path = os.path.join(current_path, "Images\\TestPix")
# 맵 -> 적들이 길 위에서만 움직이게 변경
map = [[["C2","W1","W1","W1","W1","W1","W1","W1","W1","W1","W1","F","W1","W1","W1","W1","W1","W1","W1","W1","W1","C1"],
       ["W2",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","W4"],
       ["W2",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","W4"],
       ["W2",".",".",".",".",".",".",".",".",".","O",".",".",".",".",".",".","R","R","R",".","W4"],
       ["W2",".","R","R","R",".",".",".",".",".",".","O",".",".",".",".",".","R","M","R",".","W4"],
       ["W2",".","R","JM","R",".",".",".",".",".",".",".","O",".",".",".",".","R","R","R",".","W4"],
       ["W2",".","R","R","R",".",".",".",".",".",".",".",".","O",".",".",".",".",".",".",".","W4"],
       ["W2",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","W4"],
       ["W2",".",".",".",".","R","R",".",".","O",".",".",".",".",".",".",".",".","M","R",".","W4"],
       ["W2",".",".",".",".","R","I",".",".",".",".",".",".",".",".",".",".",".","R","R",".","W4"],
       ["W2","P",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","W4"],
       ["C3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","C4"]],
       
       [["C2","W1","W1","W1","W1","W1","W1","W1","W1","W1","W1","F","W1","W1","W1","W1","W1","W1","W1","W1","W1","C1"],
       ["W2",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","W4"],
       ["W2",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","W4"],
       ["W2",".",".","O",".",".",".",".",".",".","O",".",".",".",".",".",".","M","R",".",".","W4"],
       ["W2",".","R","R","R","O",".",".",".",".",".","O",".",".",".",".",".","R","R",".",".","W4"],
       ["W2",".","R","M","R","O",".",".",".",".",".",".",".",".",".",".",".","R","R",".",".","W4"],
       ["W2",".","R","R","R","O",".",".",".",".",".",".",".","O",".",".",".",".",".",".",".","W4"],
       ["W2",".",".","O",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","W4"],
       ["W2",".",".",".",".",".",".",".",".","O",".",".",".",".",".",".",".",".","M","R",".","W4"],
       ["W2",".",".",".",".",".",".",".",".",".",".",".",".","M",".","O",".",".","R","R",".","W4"],
       ["W2","P",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","W4"],
       ["C3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","C4"]],
       
       [["C2","W1","W1","W1g","W1","W1","W1g","W1","W1","W1","W1","F","W1","W1","W1","W1","W1","W1","W1","W1","W1","C1"],
       ["W2",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","W4"],
       ["W2",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","W4"],
       ["W2",".",".",".",".",".",".",".",".",".","O",".",".",".",".",".",".","R","R","R",".","W4"],
       ["W2",".","M",".",".",".",".",".",".","O",".","O",".",".",".",".",".","R","M","R",".","W4"],
       ["W2",".","R",".",".",".",".",".","O",".",".",".","O",".",".",".",".","R","R","R",".","W4"],
       ["W2",".",".",".",".",".",".",".",".",".",".",".",".","O",".",".",".",".",".",".",".","W4"],
       ["W2",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","W4"],
       ["W2",".",".",".",".",".",".",".",".","O","O","O",".",".",".",".",".",".","M","R",".","W4"],
       ["W2",".",".",".",".",".",".",".","O",".",".","O",".",".",".",".",".",".","R","R",".","W4"],
       ["W2","P",".",".",".",".",".",".","O",".",".",".",".",".",".",".",".",".",".",".",".","W4"],
       ["C3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","C4"]],
       [["C2","W1","W1","W1","W1","W1","W1","W1","W1","W1","F","W1","W1","W1","W1","W1","W1","W1","W1","W1","W1","C1"], #스테이지4 이벤트맵
       ["W2",".",".",".",".",".",".",".",".",".","R",".",".",".",".",".",".",".",".",".",".","W4"],
       ["W2",".",".",".",".",".",".",".",".",".","R",".",".",".",".",".",".",".",".",".",".","W4"],
       ["W2",".",".",".",".",".",".",".",".",".","R",".",".",".",".",".",".",".",".",".",".","W4"],
       ["W2",".",".",".",".",".",".",".",".",".","R",".",".",".",".",".",".",".",".",".",".","W4"],
       ["W2",".",".",".",".",".",".",".",".",".","R",".",".",".",".",".",".",".",".",".",".","W4"],
       ["W2",".",".","R",".",".",".",".",".",".","R",".",".",".",".",".",".",".","R",".",".","W4"],
       ["W2",".",".","R",".",".",".",".",".",".","R",".",".",".",".",".",".",".","R",".",".","W4"],
       ["W2",".",".","R",".",".",".",".",".",".","R",".",".",".",".",".",".",".","R",".",".","W4"],
       ["W2",".",".","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R",".",".","W4"],
       ["W2",".",".",".",".",".",".",".",".",".","P",".",".",".",".",".",".",".",".",".",".","W4"],
       ["C3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","C4"]],
       [["C2","W1","W1","W1g","W1","W1","W1g","W1","W1","W1","W1","F","W1","W1","W1","W1","W1","W1","W1","W1","W1","C1"],
       ["W2",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","W4"],
       ["W2",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","W4"],
       ["W2",".",".",".",".",".",".",".",".",".","O",".",".",".",".",".",".","R","R","R",".","W4"],
       ["W2",".","M",".",".",".",".",".",".","O",".","O",".",".",".",".",".","R","M","R",".","W4"],
       ["W2",".","R",".",".",".",".",".","O",".",".",".","O",".",".",".",".","R","R","R",".","W4"],
       ["W2",".",".",".",".",".",".",".",".",".",".",".",".","O",".",".",".",".",".",".",".","W4"],
       ["W2",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","W4"],
       ["W2",".",".",".",".",".",".",".",".","O","O","O",".",".",".",".",".",".","M","R",".","W4"],
       ["W2",".",".",".",".",".",".",".","O",".",".","O",".",".",".",".",".",".","R","R",".","W4"],
       ["W2","P",".",".",".",".",".",".","O",".",".",".",".",".",".",".",".",".",".",".",".","W4"],
       ["C3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","C4"]],
       [["C2","W1","W1","W1g","W1","W1","W1g","W1","W1","W1","W1","F","W1","W1","W1","W1","W1","W1","W1","W1","W1","C1"],
       ["W2",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","W4"],
       ["W2",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","W4"],
       ["W2",".",".",".",".",".",".",".",".",".","O",".",".",".",".",".",".","R","R","R",".","W4"],
       ["W2",".","M",".",".",".",".",".",".","O",".","O",".",".",".",".",".","R","M","R",".","W4"],
       ["W2",".","R",".",".",".",".",".","O",".",".",".","O",".",".",".",".","R","R","R",".","W4"],
       ["W2",".",".",".",".",".",".",".",".",".",".",".",".","O",".",".",".",".",".",".",".","W4"],
       ["W2",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","W4"],
       ["W2",".",".",".",".",".",".",".",".","O","O","O",".",".",".",".",".",".","M","R",".","W4"],
       ["W2",".",".",".",".",".",".",".","O",".",".","O",".",".",".",".",".",".","R","R",".","W4"],
       ["W2","P",".",".",".",".",".",".","O",".",".",".",".",".",".",".",".",".",".",".",".","W4"],
       ["C3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","C4"]],
       [["C2","W1","W1","W1g","W1","W1","W1g","W1","W1","W1","W1","F","W1","W1","W1","W1","W1","W1","W1","W1","W1","C1"],
       ["W2",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","W4"],
       ["W2",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","W4"],
       ["W2",".",".",".",".",".",".",".",".",".","O",".",".",".",".",".",".","R","R","R",".","W4"],
       ["W2",".","M",".",".",".",".",".",".","O",".","O",".",".",".",".",".","R","M","R",".","W4"],
       ["W2",".","R",".",".",".",".",".","O",".",".",".","O",".",".",".",".","R","R","R",".","W4"],
       ["W2",".",".",".",".",".",".",".",".",".",".",".",".","O",".",".",".",".",".",".",".","W4"],
       ["W2",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","W4"],
       ["W2",".",".",".",".",".",".",".",".","O","O","O",".",".",".",".",".",".","M","R",".","W4"],
       ["W2",".",".",".",".",".",".",".","O",".",".","O",".",".",".",".",".",".","R","R",".","W4"],
       ["W2","P",".",".",".",".",".",".","O",".",".",".",".",".",".",".",".",".",".",".",".","W4"],
       ["C3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","C4"]],
       [["C2","W1","W1","W1","W1","W1","W1","W1","W1","W1","W1","F","W1","W1","W1","W1","W1","W1","W1","W1","W1","C1"], #스테이지8 이벤트맵
       ["W2",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","W4"],
       ["W2",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","W4"],
       ["W2",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","W4"],
       ["W2",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","W4"],
       ["W2",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","W4"],
       ["W2",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","W4"],
       ["W2",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","W4"],
       ["W2",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","W4"],
       ["W2",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","W4"],
       ["W2","P",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","W4"],
       ["C3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","C4"]],
       [["C2","W1","W1","W1g","W1","W1","W1g","W1","W1","W1","W1","F","W1","W1","W1","W1","W1","W1","W1","W1","W1","C1"],
       ["W2",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","W4"],
       ["W2",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","W4"],
       ["W2",".",".",".",".",".",".",".",".",".","O",".",".",".",".",".",".","R","R","R",".","W4"],
       ["W2",".","M",".",".",".",".",".",".","O",".","O",".",".",".",".",".","R","M","R",".","W4"],
       ["W2",".","R",".",".",".",".",".","O",".",".",".","O",".",".",".",".","R","R","R",".","W4"],
       ["W2",".",".",".",".",".",".",".",".",".",".",".",".","O",".",".",".",".",".",".",".","W4"],
       ["W2",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","W4"],
       ["W2",".",".",".",".",".",".",".",".","O","O","O",".",".",".",".",".",".","M","R",".","W4"],
       ["W2",".",".",".",".",".",".",".","O",".",".","O",".",".",".",".",".",".","R","R",".","W4"],
       ["W2","P",".",".",".",".",".",".","O",".",".",".",".",".",".",".",".",".",".",".",".","W4"],
       ["C3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","C4"]],
       [["C2","W1","W1","W1","W1","W1","W1","W1","W1","W1","W1","F","W1","W1","W1","W1","W1","W1","W1","W1","W1","C1"],
       ["W2",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","W4"],
       ["W2",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","W4"],
       ["W2",".",".",".",".",".",".",".",".",".","O",".",".",".",".",".",".","R","R","R",".","W4"],
       ["W2",".","R","R","R",".",".",".",".",".",".","O",".",".",".",".",".","R","M","R",".","W4"],
       ["W2",".","R","JM","R",".",".",".",".",".",".",".","O",".",".",".",".","R","R","R",".","W4"],
       ["W2",".","R","R","R",".",".",".",".",".",".",".",".","O",".",".",".",".",".",".",".","W4"],
       ["W2",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","W4"],
       ["W2",".",".",".",".",".",".",".",".","O",".",".",".",".",".",".",".",".","M","R",".","W4"],
       ["W2",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","R","R",".","W4"],
       ["W2","P",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","W4"],
       ["C3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","W3","C4"]]]