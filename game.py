import os

grid = [['      ','       ','       ','       ','       ','       ','       ','       '],
        ['      ',
         ' \\  /  ',
         '  \\/   ',
         '  /\\   ',
         ' /  \\  ',
         '       '],
        [' ___  ',
         ' |   | ',
         ' |   | ',
         ' |   | ',
         ' |___| ',
         '       ']]

def drawGrid(state):
    
    for row in range(3):
        for entry in range(6):
            if entry == 0:
                print(str(row*3+1)+grid[state[row][0]][entry]+'|'+str(row*3+2)+grid[state[row][1]][entry]+'|'+str(row*3+3)+grid[state[row][2]][entry])
            else:
                print(grid[state[row][0]][entry]+'|'+grid[state[row][1]][entry]+'|'+grid[state[row][2]][entry])

        if row !=2:
            print("-------|-------|-------")
    
state = [[0,0,0],[0,0,0],[0,0,0]]

def run():
    print(("-"*20))
    print("Welcome to TIC TAC TOE".center(20,' '))
    print("Press 1 to play")
    print("Press 2 to quit")
    x = int(input("Enter choice:"))
    try:
        if x==1:
            game(1,0,False)
        elif x==2:
            exit()
        else:
            raise TypeError
    except TypeError:
        print("!!!Wrong Input!!!")
        input("Press Enter key to continue...")
        clearscrn()
        run()

def game(value,count,flag):
    drawGrid(state)
    if flag:
        winner(value*-1)
    else:
        print("\n" * 5)
        
        if count == 9:
            winner(0)
            return ""
        user = "X" if value == 1 else "O"

        n = input(f"{user} marks in location: ")
        print("Dummy")
        try:
            n = int(n)
            if 1 <= n <= 9:
                row = (n - 1) // 3
                col = (n - 1) % 3
                print("Dummy")
                if state[row][col] == 0:
                    state[row][col] = value
                    

                    print("checking")
                    ans = result(state,value)
                    print("checked")
                    if ans != 0:
                        flag = True

                    clearscrn()
                    value *= -1
                    game(value,count+1,flag)

                else:
                    print("!!!Cell already taken!!!")
                    input("Press Enter key to continue...")
                    clearscrn()
                    game(value,count,flag)
            else:
                raise ValueError
        except ValueError:
            print("!!!Wrong Value!!!")
            input("Press Enter key to continue...")
            clearscrn()
            game(value,count,flag)

def winner(value):
    if value == 1:
        print("Winner is X")
    elif value == -1:
        print("Winner is O")
    else:
        print("DRAW")

def result(state,value):

    for i in range(3):
        if state[i][0] == state[i][1] == state[i][2] == value:
            return value
        if state[0][i] == state[1][i] == state[2][i] == value:
            return value
        
    if state[0][0] == state[1][1] == state[2][2] == value:
            return value
    if state[0][2] == state[1][1] == state[2][0] == value:
            return value
    return False

def clearscrn():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Linux and macOS
        os.system('clear')


if __name__ == "__main__":
    run()


