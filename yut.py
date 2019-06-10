import random

board = [["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"]]
outboard = [4,4,4,4]
done = [0,0,0,0]
onboard = [[],[],[],[]]
cur_yoot = []
yoot = ["\
    -----   -----   -----   -----\n\
   l     l l     l l     l l     l\n\
   l  X  l l  X  l l  X  l l  X  l\n\
   l     l l     l l     l l     l\n\
   l  X  l l  X  l l  X  l l  X  l\n\
   l     l l     l l     l l     l\n\
   l  X  l l  X  l l  X  l l  X  l\n\
   l     l l     l l     l l     l\n\
   l  X  l l  X  l l  X  l l  X  l\n\
   l     l l     l l     l l     l\n\
    -----   -----   -----   -----\n\
    모입니다!\n","\
    -----   -----   -----   -----\n\
   l     l l     l l     l l     l\n\
   l  X  l l  X  l l  X  l l     l\n\
   l     l l     l l     l l     l\n\
   l  X  l l  X  l l  X  l l     l\n\
   l     l l     l l     l l     l\n\
   l  X  l l  X  l l  X  l l     l\n\
   l     l l     l l     l l     l\n\
   l  X  l l  X  l l  X  l l     l\n\
   l     l l     l l     l l     l\n\
    -----   -----   -----   -----\n\
    도입니다!\n","\
    -----   -----   -----   -----\n\
   l     l l     l l     l l     l\n\
   l  X  l l  X  l l     l l  X  l\n\
   l     l l     l l     l l     l\n\
   l  X  l l  X  l l     l l  X  l\n\
   l     l l     l l     l l     l\n\
   l  X  l l  X  l l     l l  X  l\n\
   l     l l     l l     l l     l\n\
   l  X  l l  X  l l     l l  X  l\n\
   l     l l     l l     l l     l\n\
    -----   -----   -----   -----\n\
    도입니다!\n","\
    -----   -----   -----   -----\n\
   l     l l     l l     l l     l\n\
   l  X  l l  X  l l     l l     l\n\
   l     l l     l l     l l     l\n\
   l  X  l l  X  l l     l l     l\n\
   l     l l     l l     l l     l\n\
   l  X  l l  X  l l     l l     l\n\
   l     l l     l l     l l     l\n\
   l  X  l l  X  l l     l l     l\n\
   l     l l     l l     l l     l\n\
    -----   -----   -----   -----\n\
    개입니다!\n","\
    -----   -----   -----   -----\n\
   l     l l     l l     l l     l\n\
   l  X  l l     l l  X  l l  X  l\n\
   l     l l     l l     l l     l\n\
   l  X  l l     l l  X  l l  X  l\n\
   l     l l     l l     l l     l\n\
   l  X  l l     l l  X  l l  X  l\n\
   l     l l     l l     l l     l\n\
   l  X  l l     l l  X  l l  X  l\n\
   l     l l     l l     l l     l\n\
    -----   -----   -----   -----\n\
    도입니다!\n","\
    -----   -----   -----   -----\n\
   l     l l     l l     l l     l\n\
   l  X  l l     l l  X  l l     l\n\
   l     l l     l l     l l     l\n\
   l  X  l l     l l  X  l l     l\n\
   l     l l     l l     l l     l\n\
   l  X  l l     l l  X  l l     l\n\
   l     l l     l l     l l     l\n\
   l  X  l l     l l  X  l l     l\n\
   l     l l     l l     l l     l\n\
    -----   -----   -----   -----\n\
    개입니다!\n","\
    -----   -----   -----   -----\n\
   l     l l     l l     l l     l\n\
   l  X  l l     l l     l l  X  l\n\
   l     l l     l l     l l     l\n\
   l  X  l l     l l     l l  X  l\n\
   l     l l     l l     l l     l\n\
   l  X  l l     l l     l l  X  l\n\
   l     l l     l l     l l     l\n\
   l  X  l l     l l     l l  X  l\n\
   l     l l     l l     l l     l\n\
    -----   -----   -----   -----\n\
    개입니다!\n","\
    -----   -----   -----   -----\n\
   l     l l     l l     l l     l\n\
   l  X  l l     l l     l l     l\n\
   l     l l     l l     l l     l\n\
   l  X  l l     l l     l l     l\n\
   l     l l     l l     l l     l\n\
   l  X  l l     l l     l l     l\n\
   l     l l     l l     l l     l\n\
   l  X  l l     l l     l l     l\n\
   l     l l     l l     l l     l\n\
    -----   -----   -----   -----\n\
    걸입니다!\n","\
    -----   -----   -----   -----\n\
   l     l l     l l     l l     l\n\
   l     l l  X  l l  X  l l  X  l\n\
   l     l l     l l     l l     l\n\
   l     l l  X  l l  X  l l  X  l\n\
   l  /  l l     l l     l l     l\n\
   l     l l  X  l l  X  l l  X  l\n\
   l     l l     l l     l l     l\n\
   l     l l  X  l l  X  l l  X  l\n\
   l     l l     l l     l l     l\n\
    -----   -----   -----   -----\n\
    백도입니다!\n","\
    -----   -----   -----   -----\n\
   l     l l     l l     l l     l\n\
   l     l l  X  l l  X  l l     l\n\
   l     l l     l l     l l     l\n\
   l     l l  X  l l  X  l l     l\n\
   l  /  l l     l l     l l     l\n\
   l     l l  X  l l  X  l l     l\n\
   l     l l     l l     l l     l\n\
   l     l l  X  l l  X  l l     l\n\
   l     l l     l l     l l     l\n\
    -----   -----   -----   -----\n\
    개입니다!\n","\
    -----   -----   -----   -----\n\
   l     l l     l l     l l     l\n\
   l     l l  X  l l     l l  X  l\n\
   l     l l     l l     l l     l\n\
   l     l l  X  l l     l l  X  l\n\
   l  /  l l     l l     l l     l\n\
   l     l l  X  l l     l l  X  l\n\
   l     l l     l l     l l     l\n\
   l     l l  X  l l     l l  X  l\n\
   l     l l     l l     l l     l\n\
    -----   -----   -----   -----\n\
    개입니다!\n","\
    -----   -----   -----   -----\n\
   l     l l     l l     l l     l\n\
   l     l l  X  l l     l l     l\n\
   l     l l     l l     l l     l\n\
   l     l l  X  l l     l l     l\n\
   l  /  l l     l l     l l     l\n\
   l     l l  X  l l     l l     l\n\
   l     l l     l l     l l     l\n\
   l     l l  X  l l     l l     l\n\
   l     l l     l l     l l     l\n\
    -----   -----   -----   -----\n\
    걸입니다!\n","\
    -----   -----   -----   -----\n\
   l     l l     l l     l l     l\n\
   l     l l     l l  X  l l  X  l\n\
   l     l l     l l     l l     l\n\
   l     l l     l l  X  l l  X  l\n\
   l  /  l l     l l     l l     l\n\
   l     l l     l l  X  l l  X  l\n\
   l     l l     l l     l l     l\n\
   l     l l     l l  X  l l  X  l\n\
   l     l l     l l     l l     l\n\
    -----   -----   -----   -----\n\
    개입니다!\n","\
    -----   -----   -----   -----\n\
   l     l l     l l     l l     l\n\
   l     l l     l l  X  l l     l\n\
   l     l l     l l     l l     l\n\
   l     l l     l l  X  l l     l\n\
   l  /  l l     l l     l l     l\n\
   l     l l     l l  X  l l     l\n\
   l     l l     l l     l l     l\n\
   l     l l     l l  X  l l     l\n\
   l     l l     l l     l l     l\n\
    -----   -----   -----   -----\n\
    걸입니다!\n","\
    -----   -----   -----   -----\n\
   l     l l     l l     l l     l\n\
   l     l l     l l     l l  X  l\n\
   l     l l     l l     l l     l\n\
   l     l l     l l     l l  X  l\n\
   l  /  l l     l l     l l     l\n\
   l     l l     l l     l l  X  l\n\
   l     l l     l l     l l     l\n\
   l     l l     l l     l l  X  l\n\
   l     l l     l l     l l     l\n\
    -----   -----   -----   -----\n\
    걸입니다!\n","\
    -----   -----   -----   -----\n\
   l     l l     l l     l l     l\n\
   l     l l     l l     l l     l\n\
   l     l l     l l     l l     l\n\
   l     l l     l l     l l     l\n\
   l  /  l l     l l     l l     l\n\
   l     l l     l l     l l     l\n\
   l     l l     l l     l l     l\n\
   l     l l     l l     l l     l\n\
   l     l l     l l     l l     l\n\
    -----   -----   -----   -----\n\
    윷입니다!\n"]

"""
def check(a,b,board):
    if board[a][b] == 0:
        return "□"
    else:
        return str(board[a][b])
def show_board():
    global board

    print("\n 10 "+check(0,10,board)+board[1][10]+"    9 "+ board[0][9]+board[1][9]+"    8 "+board[0][8]+board[1][8]+"    7 "+board[0][7]+board[1][7]+"    6 "+board[0][6]+board[1][6]+"    5 "+board[0][5]+board[1][5])
    print(" 10 "+board[2][10]+board[3][10]+"    9 "+ board[2][9]+board[3][9]+"    8 "+board[2][8]+board[3][8]+"    7 "+board[2][7]+board[3][7]+"    6 "+board[2][6]+board[3][6]+"    5 "+board[2][5]+board[3][5]+"\n\n")
    print(" 11 "+board[0][11]+board[1][11]+"   25 "+ board[0][25]+board[1][25]+"      "+"        "+"     21 "+board[0][20]+board[1][20]+"    4 "+board[0][4]+board[1][4])
    print(" 11 "+board[2][11]+board[3][11]+"   25 "+ board[2][25]+board[3][25]+"      "+"        "+"     21 "+board[2][20]+board[3][20]+"    4 "+board[2][4]+board[3][4]+"\n\n")
    print(" 12 "+board[0][12]+board[1][12]+"      "+"   26 "+board[0][26]+board[1][26]+"       21 "+board[0][21]+board[1][21]+"          3 "+board[0][3]+board[1][3])
    print(" 12 "+board[2][12]+board[3][12]+"      "+"   26 "+board[2][26]+board[3][26]+"       21 "+board[2][21]+board[3][21]+"          3 "+board[2][3]+board[3][3])
    print("                     22 "+board[0][22]+board[1][22]+"                     ")
    print("                     22 "+board[2][22]+board[3][22]+"                     ")
    print(" 13 "+board[0][13]+board[1][13]+"      "+"   23 "+board[0][23]+board[1][23]+"       27 "+board[0][27]+board[1][27]+"          2 "+board[0][2]+board[1][2])
    print(" 13 "+board[2][13]+board[3][13]+"      "+"   23 "+board[2][23]+board[3][23]+"       27 "+board[2][27]+board[3][27]+"          2 "+board[2][2]+board[3][2]+"\n\n")
    print(" 14 "+board[0][14]+board[1][14]+"   24 "+ board[0][24]+board[1][24]+"      "+"        "+"     28 "+board[0][28]+board[1][28]+"    1 "+board[0][1]+board[1][1])
    print(" 14 "+board[2][14]+board[3][14]+"   24 "+ board[2][24]+board[3][24]+"      "+"        "+"     28 "+board[2][28]+board[3][28]+"    1 "+board[2][1]+board[3][1]+"\n\n")
    print(" 15 "+board[0][15]+board[1][15]+"   16 "+ board[0][16]+board[1][16]+"   17 "+board[0][17]+board[1][17]+"   18 "+board[0][18]+board[1][18]+"   19 "+board[0][19]+board[1][19]+"    0 "+board[0][0]+board[1][0])
    print(" 15 "+board[2][15]+board[3][15]+"   16 "+ board[2][16]+board[3][16]+"   17 "+board[2][17]+board[3][17]+"   18 "+board[2][18]+board[3][18]+"   19 "+board[2][19]+board[3][19]+"    0 "+board[2][0]+board[3][0]+"↑start\n\n")


"""


"""
def show_board():
    global board

    print("\n    "+board[0][10]+board[1][10]+"      "+ board[0][9]+board[1][9]+"      "+board[0][8]+board[1][8]+"      "+board[0][7]+board[1][7]+"      "+board[0][6]+board[1][6]+"      "+board[0][5]+board[1][5])
    print("    "+board[2][10]+board[3][10]+"      "+ board[2][9]+board[3][9]+"      "+board[2][8]+board[3][8]+"      "+board[2][7]+board[3][7]+"      "+board[2][6]+board[3][6]+"      "+board[2][5]+board[3][5]+"\n\n")
    print("    "+board[0][11]+board[1][11]+"      "+ board[0][20]+board[1][20]+"      "+"      "+"        "+"      "+board[0][21]+board[1][21]+"      "+board[0][4]+board[1][4])
    print("    "+board[2][11]+board[3][11]+"      "+ board[2][20]+board[3][20]+"      "+"      "+"        "+"      "+board[2][21]+board[3][21]+"      "+board[2][4]+board[3][4]+"\n\n")
    print("    "+board[0][12]+board[1][12]+"      "+"     "+"     "+board[0][22]+board[1][22]+"      "+board[0][23]+board[1][23]+"                "+board[0][3]+board[1][3])
    print("    "+board[2][12]+board[3][12]+"      "+"     "+"     "+board[2][22]+board[3][22]+"      "+board[2][23]+board[3][23]+"                "+board[2][3]+board[3][3])
    print("                             "+board[0][24]+board[1][24]+"                     ")
    print("                             "+board[2][24]+board[3][24]+"                     ")
    print("    "+board[0][13]+board[1][13]+"      "+"     "+"     "+board[0][25]+board[1][25]+"      "+board[0][26]+board[1][26]+"                "+board[0][2]+board[1][2])
    print("    "+board[2][13]+board[3][13]+"      "+"     "+"     "+board[2][25]+board[3][25]+"      "+board[2][26]+board[3][26]+"                "+board[2][2]+board[3][2]+"\n\n")
    print("    "+board[0][14]+board[1][14]+"      "+ board[0][27]+board[1][27]+"      "+"      "+"        "+"      "+board[0][28]+board[1][28]+"      "+board[0][1]+board[1][1])
    print("    "+board[2][14]+board[3][14]+"      "+ board[2][27]+board[3][27]+"      "+"      "+"        "+"      "+board[2][28]+board[3][28]+"      "+board[2][1]+board[3][1]+"\n\n")
    print("    "+board[0][15]+board[1][15]+"      "+ board[0][16]+board[1][16]+"      "+board[0][17]+board[1][17]+"      "+board[0][18]+board[1][18]+"      "+board[0][19]+board[1][19]+"      "+board[0][0]+board[1][0])
    print("    "+board[2][15]+board[3][15]+"      "+ board[2][16]+board[3][16]+"      "+board[2][17]+board[3][17]+"      "+board[2][18]+board[3][18]+"      "+board[2][19]+board[3][19]+"      "+board[2][0]+board[3][0]+"↑start\n\n")
 """
def show_board():
    global board

    print("\n 10 "+board[0][10]+board[1][10]+"    9 "+ board[0][9]+board[1][9]+"    8 "+board[0][8]+board[1][8]+"    7 "+board[0][7]+board[1][7]+"    6 "+board[0][6]+board[1][6]+"    5 "+board[0][5]+board[1][5])
    print(" 10 "+board[2][10]+board[3][10]+"    9 "+ board[2][9]+board[3][9]+"    8 "+board[2][8]+board[3][8]+"    7 "+board[2][7]+board[3][7]+"    6 "+board[2][6]+board[3][6]+"    5 "+board[2][5]+board[3][5]+"\n\n")
    print(" 11 "+board[0][11]+board[1][11]+"   25 "+ board[0][25]+board[1][25]+"      "+"        "+"     21 "+board[0][20]+board[1][20]+"    4 "+board[0][4]+board[1][4])
    print(" 11 "+board[2][11]+board[3][11]+"   25 "+ board[2][25]+board[3][25]+"      "+"        "+"     21 "+board[2][20]+board[3][20]+"    4 "+board[2][4]+board[3][4]+"\n\n")
    print(" 12 "+board[0][12]+board[1][12]+"      "+"   26 "+board[0][26]+board[1][26]+"       21 "+board[0][21]+board[1][21]+"          3 "+board[0][3]+board[1][3])
    print(" 12 "+board[2][12]+board[3][12]+"      "+"   26 "+board[2][26]+board[3][26]+"       21 "+board[2][21]+board[3][21]+"          3 "+board[2][3]+board[3][3])
    print("                     22 "+board[0][22]+board[1][22]+"                     ")
    print("                     22 "+board[2][22]+board[3][22]+"                     ")
    print(" 13 "+board[0][13]+board[1][13]+"      "+"   23 "+board[0][23]+board[1][23]+"       27 "+board[0][27]+board[1][27]+"          2 "+board[0][2]+board[1][2])
    print(" 13 "+board[2][13]+board[3][13]+"      "+"   23 "+board[2][23]+board[3][23]+"       27 "+board[2][27]+board[3][27]+"          2 "+board[2][2]+board[3][2]+"\n\n")
    print(" 14 "+board[0][14]+board[1][14]+"   24 "+ board[0][24]+board[1][24]+"      "+"        "+"     28 "+board[0][28]+board[1][28]+"    1 "+board[0][1]+board[1][1])
    print(" 14 "+board[2][14]+board[3][14]+"   24 "+ board[2][24]+board[3][24]+"      "+"        "+"     28 "+board[2][28]+board[3][28]+"    1 "+board[2][1]+board[3][1]+"\n\n")
    print(" 15 "+board[0][15]+board[1][15]+"   16 "+ board[0][16]+board[1][16]+"   17 "+board[0][17]+board[1][17]+"   18 "+board[0][18]+board[1][18]+"   19 "+board[0][19]+board[1][19]+"    0 "+board[0][0]+board[1][0])
    print(" 15 "+board[2][15]+board[3][15]+"   16 "+ board[2][16]+board[3][16]+"   17 "+board[2][17]+board[3][17]+"   18 "+board[2][18]+board[3][18]+"   19 "+board[2][19]+board[3][19]+"    0 "+board[2][0]+board[3][0]+"↑start\n\n")

def move_next(player,mov,start,cur_loc):
    global board
    if mov == 0:
        global onboard
        if board[player][cur_loc] == "□":
            board[player][cur_loc] = board[player][start]
        else:
            board[player][cur_loc] = str(int(board[player][cur_loc])+int(board[player][start]))
        board[player][start] = "□"
        for i in range(len(onboard[player])):
            if onboard[player][i] == start:
                onboard[player][i] = cur_loc
        for i in range(4):
            if i != player and board[i][cur_loc] != "□":
                for j in range(len(onboard[i])):
                    if j == cur_loc:
                        global outboard
                        outboard[i] += int(board[i][cur_loc])
                        onboard[i].pop[j]
                board[i][cur_loc] = "□"
                return 1
        return 0
    elif mov == -1:
        if cur_loc == 0:
            print("19 or 28?")
            a = input()
            if a == "19":
                move_next(player,0,start,19)
            else:
                move_next(player,0,start,28)
        elif cur_loc == 20:
            move_next(player,0,start,5)
        elif cur_loc == 25:
            move_next(player,0,start,10)
        elif cur_loc == 22:
            print("21 or 26?")
            a = input()
            if a == "21":
                move_next(player,0,start,21)
            else:
                move_next(player,0,start,26)
        elif cur_loc == 15:
            print("14 or 24?")
            a = input()
            if a == "14":
                move_next(player,0,start,14)
            else:
                move_next(player,0,start,24)
        elif cur_loc == 27:
            move_next(player,0,start,22)
        else:
            move_next(player,0,start,cur_loc-1)
    else:
        if cur_loc == 19 or cur_loc == 28:
            global done
            done[player] += int(board[player][start])
            board[player][start] = "□"
            for i in range(len(onboard[player])):
                if onboard[player][i] == start:
                    onboard[player].pop(i)
            return 0
        elif cur_loc == 26:
            if mov == 1:
                move_next(player,mov-1,start,22)
            else:
                move_next(player,mov-2,start,27)
        elif cur_loc == start and (start == 5 or start == 22 or start == 10):
            print("Would you like to take a shortcut? [y/n]")
            ans = input()
            if ans == "y":
                if start == 5:
                    a = 20
                elif start == 22:
                    a = 27
                else:
                    a = 25
                move_next(player,mov-1,start,a)
            else:
                move_next(player,mov-1,start,cur_loc+1)
        elif cur_loc == 24:
            move_next(player,mov-1,start,15)
        else:
            move_next(player,mov-1,start,cur_loc+1)

def roll_yoot():
    global yoot,cur_yoot
    a = random.randint(0,15)
    print(yoot[a])
    a = check_yoot(a)
    cur_yoot.append(a)
    return a

def check_yoot(num):   
    a = [5,1,1,2,1,2,2,3,-1,2,2,3,2,3,3,4,0]
    return a[num]

def show_state(player,cur_yoot,onboard):

    yootlen = len(cur_yoot)
    boardlen = len(onboard[player])
    print("you have ",end=' ') 
    print(str(onboard[player]),end=' ')
    """
    for i in range(boardlen):
        print(str(i)+" : "+str(onboard[player][i]),end=' ')
    """
    print("onboard")
    print("and you have ",end='')
    print(str(cur_yoot),end=' ') 
    """
    for i in range(yootlen):
        print(str(i)+" : "+str(cur_yoot[i]),end=' ')
    """
    print("chance to move")

def get_move(player):
    global cur_yoot,onboard,outboard,board
    get_stat = 0
    while(len(cur_yoot)>0):
        if(get_stat):
            roll_yoot()
            get_stat = 0
        show_state(player,cur_yoot,onboard)
        print("input [onboard_index] (new : -1)")
        onidx = int(input())
        print("input [yoot_index]")
        yoot = int(input())
        yoot = cur_yoot.pop(yoot)
        mix_stat = 0
        if(onidx == -1):
            onboard[player].append(0)
            outboard[player] -= 1
            if(board[player][0] != "□"):
                mix_stat = int(board[player][0])
            board[player][0] = "1"
        
        get_stat = move_next(player,yoot,onboard[player][onidx],onboard[player][onidx])

        if mix_stat != 0:
            board[player][0] = str(mix_stat)
        show_board()
    


"""
show_board()
board[0][0]="1"
show_board()
move_next(0,5,0,0)
show_board()
move_next(0,3,5,5)
show_board()
"""
def roll(roll_more): 
    while roll_more > 0:
        a = roll_yoot()
        roll_more -= 1
        if a == 5 or a == 4:
            roll_more += 1

def turn(player):
    print("player "+str(player)+"\'s turn!")
    roll(1)
    get_move(player)

    

show_board()


playeridx = 0
while True:
    turn(playeridx)
    if done[playeridx] == 4:
        print("player "+str(playeridx)+"won!")
        break
    playeridx = (playeridx + 1) % 4
