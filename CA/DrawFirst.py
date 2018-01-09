import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
import numpy as np
import Data


def drawPeople(allPeople,allTable):
    plt.clf()
    # drawBar()

    drawWallAndExit()
    p_x=[]
    p_y=[]
    t_x=[]
    t_y=[]
    c_x=[]
    c_y=[]
    for p in allPeople:
        if p.logo==Data.LOGO_PEOPLE:
            if p.isCrowded:
                p_x.append(p.x)
                p_y.append(p.y)
            else:
                c_x.append(p.x)
                c_y.append(p.y)
    for t in allTable:
        t_x.append(t.x)
        t_y.append(t.y)



    plt.subplot(1,1,1)
    plt.scatter(c_x, c_y, c='b')
    plt.scatter(p_x, p_y, c='r')
    plt.scatter(t_x, t_y, marker='s',c='darkorange')
    closeFig = plt.axes([0.8, 0.025, 0.1, 0.04])  # 关闭按钮
    closeFigbutton = Button(closeFig, 'close', hovercolor='0.5')  # 按钮样式
    closeFigbutton.on_clicked(closeFigure)  # 按钮按下去的动作
    plt.pause(0.1)


def closeFigure(event):
    plt.close()  # 将窗口关闭
    Data.flag = False  # 循环标记为Fasle
def drawWallAndExit():
    plt.plot([0,Data.ROOM_M],[0,0],marker='s',c='black')                         #下方的线
    plt.plot([0,18],[Data.ROOM_N,Data.ROOM_N],marker='s',c='black')              #上方的线  左部分
    plt.plot([22,Data.ROOM_M],[Data.ROOM_N,Data.ROOM_N],marker='s',c='black')    #上方的线  右部分
    plt.plot([0,0],[0,Data.ROOM_N],marker='s',c='black')                         #左方的线
    plt.plot([Data.ROOM_M,Data.ROOM_M],[0,Data.ROOM_N],marker='s',c='black')     #右方的线
# def drawBar():
#
#     plt.plot([range(5,37,2),range(5,37,2)],[5,18],marker='s',c='b')
#     plt.plot([range(5,37,2),range(5,37,2)],[22,36],marker='s',c='b')



