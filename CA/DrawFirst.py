import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
import numpy as np
import Data


def drawPeople(allPeople):
    plt.clf()
    drawWallAndExit()
    p_x=[]
    p_y=[]
    for p in allPeople:
        if p.logo==Data.LOGO_PEOPLE:
            p_x.append(p.x)
            p_y.append(p.y)
    plt.subplot(1,1,1)
    plt.scatter(p_x,p_y,c='r')
    closeFig = plt.axes([0.8, 0.025, 0.1, 0.04])  # 关闭按钮
    closeFigbutton = Button(closeFig, 'close', hovercolor='0.5')  # 按钮样式
    closeFigbutton.on_clicked(closeFigure)  # 按钮按下去的动作
    plt.pause(1)

def closeFigure(event):
    plt.close()  # 将窗口关闭
    Data.flag = False  # 循环标记为Fasle
def drawWallAndExit():
    plt.plot([0,Data.ROOM_M],[0,0],c='b')
    plt.plot([0,8],[Data.ROOM_N,Data.ROOM_N],c='b')
    plt.plot([12,Data.ROOM_M],[Data.ROOM_N,Data.ROOM_N],c='b')
    # plt.plot([0,Data.ROOM_M],[Data.ROOM_N,Data.ROOM_N],c='b')
    plt.plot([0,0],[0,Data.ROOM_N],c='b')
    plt.plot([Data.ROOM_M,Data.ROOM_M],[0,Data.ROOM_N],c='b')

