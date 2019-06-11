import random

board = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
outboard = [4,4,4,4]
done = [0,0,0,0]
#onboard = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
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
get_stat = 0

def check(a,b):
    global board
    if board[a][b] == 0:
        return "□"
    else:
        return str(board[a][b])

def show_board():
    global board,outboard,done

    print("\n 10 "+check(0,10)+check(1,10)+"    9 "+ check(0,9)+check(1,9)+"    8 "+check(0,8)+check(1,8)+"    7 "+check(0,7)+check(1,7)+"    6 "+check(0,6)+check(1,6)+"    5 "+check(0,5)+check(1,5))
    print("    "+check(2,10)+check(3,10)+"      "+ check(2,9)+check(3,9)+"      "+check(2,8)+check(3,8)+"      "+check(2,7)+check(3,7)+"      "+check(2,6)+check(3,6)+"      "+check(2,5)+check(3,5)+"\n\n")
    print(" 11 "+check(0,11)+check(1,11)+"   25 "+ check(0,25)+check(1,25)+"                   20 "+check(0,20)+check(1,20)+"    4 "+check(0,4)+check(1,4))
    print("    "+check(2,11)+check(3,11)+"      "+ check(2,25)+check(3,25)+"                      "+check(2,20)+check(3,20)+"      "+check(2,4)+check(3,4)+"\n\n")
    print(" 12 "+check(0,12)+check(1,12)+"         26 "+check(0,26)+check(1,26)+"       21 "+check(0,21)+check(1,21)+"          3 "+check(0,3)+check(1,3))
    print("    "+check(2,12)+check(3,12)+"            "+check(2,26)+check(3,26)+"          "+check(2,21)+check(3,21)+"            "+check(2,3)+check(3,3))
    print("                     22 "+check(0,22)+check(1,22)+"                     ")
    print("                        "+check(2,22)+check(3,22)+"                     ")
    print(" 13 "+check(0,13)+check(1,13)+"         23 "+check(0,23)+check(1,23)+"       27 "+check(0,27)+check(1,27)+"          2 "+check(0,2)+check(1,2))
    print("    "+check(2,13)+check(3,13)+"            "+check(2,23)+check(3,23)+"          "+check(2,27)+check(3,27)+"            "+check(2,2)+check(3,2)+"\n\n")
    print(" 14 "+check(0,14)+check(1,14)+"   24 "+ check(0,24)+check(1,24)+"                   28 "+check(0,28)+check(1,28)+"    1 "+check(0,1)+check(1,1))
    print("    "+check(2,14)+check(3,14)+"      "+ check(2,24)+check(3,24)+"                      "+check(2,28)+check(3,28)+"      "+check(2,1)+check(3,1)+"\n\n")
    print(" 15 "+check(0,15)+check(1,15)+"   16 "+ check(0,16)+check(1,16)+"   17 "+check(0,17)+check(1,17)+"   18 "+check(0,18)+check(1,18)+"   19 "+check(0,19)+check(1,19)+"    0 "+check(0,0)+check(1,0))
    print("    "+check(2,15)+check(3,15)+"      "+ check(2,16)+check(3,16)+"      "+check(2,17)+check(3,17)+"      "+check(2,18)+check(3,18)+"      "+check(2,19)+check(3,19)+"      "+check(2,0)+check(3,0)+"↑start\n\n")
    print("outboard : "+str(outboard)+"      done : "+str(done))

def move_next(player,mov,start,cur_loc):
    global board
    #print(str(player)+" "+str(mov)+" "+str(start)+" "+str(cur_loc))
    if mov == 0:
        global onboard
        """말을 업지 않을 경우 아래 코드처럼 분기를 나누고 그걸 판별하는 코드를 추가로 작성해야함
        if board[player][cur_loc] == 0:
            board[player][cur_loc] = board[player][start]
        else:
            board[player][cur_loc] += board[player][start]
        """
        board[player][cur_loc] += board[player][start] #말을 업음
        board[player][start] = 0
        #onboard[player][start] = 0
        #onboard[player][cur_loc] = 1
        for i in range(4):
            if i != player and board[i][cur_loc] != 0:
                global outboard
                outboard[i] += board[i][cur_loc]
                board[i][cur_loc] = 0
                #onboard[i][cur_loc] = 0
                global get_stat
                get_stat = 1
        #print("get stat : ",str(get_stat))
        #return get_stat
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
            done[player] += board[player][start]
            board[player][start] = 0
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

def show_state(player,cur_yoot):
    yootlen = len(cur_yoot)
    print("you have ",end=' ')
    for i in range(len(board[player])):
        if board[player][i] != 0:
            print("["+str(i)+" : "+str(board[player][i])+"]",end=' ')
    print("onboard")
    print("and you have ",end='')
    print(str(cur_yoot),end=' ') 
    print("chance to move")

def get_move(player):
    global cur_yoot,outboard,board,get_stat
    while(len(cur_yoot)>0):
        show_state(player,cur_yoot)
        print("input [onboard_index] (new : -1)")
        onidx = int(input())
        print("input [yoot_index]")
        yoot = int(input())
        yoot = cur_yoot.pop(yoot)
        mix_stat = 0
        if(onidx == -1):
            outboard[player] -= 1
            if(board[player][0] != 0):
                mix_stat = board[player][0]
            board[player][0] = 1
            onidx = 0
        #print(yoot)
        move_next(player,yoot,onidx,onidx)
        if mix_stat != 0:
            board[player][0] = mix_stat
        show_board()
        if(get_stat == 1):
            print("got pieces! roll more")
            roll_yoot()
            get_stat = 0
    
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
