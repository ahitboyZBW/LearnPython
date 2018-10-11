# _*_ coding: utf-8 _*_ 
import curses
from random import randrange, choice
from collections import defaultdict

# 用户的六种行为，上、下、左、右、游戏重置，退出
actions = ['Up','Left','Down','Right','Restart','Exit']
letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']
print(letter_codes)
actions_dict = dict(zip(letter_codes,actions * 2))

# 初始化棋盘的参数，可以指定期盼的高宽以及胜利的条件，默认是经典的4*4 ~2048
class GameField(object):
    def __init__(self, height = 4, width = 4, win = 2048):
        self.height = height
        self.width = width
        self.win_value = 2048
        self.score = 0             #当前得分
        self.highscore = 0         #最高分
        self.reset()               #棋盘重置
    # 随机位置产生生成2和4
    def spawn(self):
        new_element = 4 if randrange(100) > 89 else 2
        (i,j) = choice([i,j] for i in range(self.width) for j in range(self.height) if self.field([i][j])==0)
        self.field([i][j]) = new_element

    def reset(self):
        if self.score > self.highscore:
            slef.highscore = self.score
        self.score = 0
        self.field = [[0 for i in range(self.width)] for j in range(self.height)]
        self.spawn()
        self.spawn()


def move_row_left(row):
    def tighten(row): # 把零散的非零元素挤到一起
        new_row = [i for i in row if i != 0]
        new_row += [0 for i in range(len(row)-len(new_row))]
        return new_row
    def merge(row):# 对临近元素进行合并
        pair = False
        new_row = []
        for i in range(len(row)):
            if pair:
                new_row.append(2*row[i])
                self.score += 2*row[i]
                pair = False
            else:
                if 
def main(stdscr):
    def init():
        #重置游戏棋盘
        return 'Game' # 状态改为进行游戏
    
    def not_game(state):
        # 画出 GameOver 或者Win 的界面
        # 读取用户输入得到的action，判断是重启游戏还是结束
        responses= defaultdict(lambda:state) 
        # 默认是当前状态，没有行为就会一直在当前界面循环
        responses['Restart'], responses['Exit'] = 'Init','Exit' # 不同行为转换到不同的状态
        return response[actions]
    def game():
        # 画出当前棋盘的状态
        # 读取用户输入得到action
        if action == 'Restart':
            return 'Init'
        if action == 'Exit':
            return 'Exit'
        #if 成功移动了一步
        #    if 游戏胜利了:
        #        return 'Win'
        #    if 游戏失败了:
        #        return 'Gameover'
        return 'Game'

    #获取用户输入
    def get_user_action(keyboard):
        char = "N"
        while char not in actions_dict:
            char = keyboard.getch()
        return actions_dict[char]
    #矩阵转至和矩阵逆转
    def transpose(field):
        return [list(row) for row in zip(*field)]

    #矩阵逆转
    def invert(field):
        return [row[::-1] for row in field]
    
    state_actions = {
        'Init' : init,
        'Win' : lambda:not_game('Win'),
        'Gameover':lambda:not_game('Gameover'),
        'Game':game
    }

    state = 'Init'

    #状态机开始循环
    while state != 'Exit':
        state=state_actions[state]()
