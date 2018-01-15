import numpy as np
import pprint

print('---------------')
STATIC_FIELD = np.zeros((40, 40))
for b in range(35, 39):
        for jj in range(0, 19):                 # 左部门口边界
                STATIC_FIELD[jj][39] = -1000
                STATIC_FIELD[jj][b] = 4.5
        for kk in range(22, 39):                # 右部门口边界
                STATIC_FIELD[kk][39] = -1000
                STATIC_FIELD[kk][b] = 4.5
        for e in range(19, 22):
                STATIC_FIELD[e][b] = 5          # 教室上部  含出口
                STATIC_FIELD[e][39]=1000
for ii in range(0, 39):
        STATIC_FIELD[0][ii] = -1000
        STATIC_FIELD[ii][0] = -1000
        STATIC_FIELD[39][ii] = -1000
        STATIC_FIELD[39][39] = -1000  # 教室边界
for l in range(6, 38, 2):
        for m in range(6, 19):  # 教室课桌之间
                STATIC_FIELD[l][m] = 3
        for n in range(22, 35):
                STATIC_FIELD[l][n] = 2
for o in range(5,37,2):
        for oo in range(6, 19):
                STATIC_FIELD[o,oo]=-1000
        for ooo in range(22,35):
                STATIC_FIELD[o,ooo]=-1000
for j in range(1, 6):
        for i in range(1, 39):  # 教室下部
                STATIC_FIELD[i][j] = 1
for z in range(19,22):
        for zz in range(6,35):
                STATIC_FIELD[zz][z]=3.5
for cc in range(5, 37):
        for c in range(1, 6):
                STATIC_FIELD[c][cc] = 4
        for ccc in range(35, 39):
                STATIC_FIELD[ccc][cc] = 4
# print(STATIC_FIELD)
pprint.pprint(STATIC_FIELD)
print('----------------------')

