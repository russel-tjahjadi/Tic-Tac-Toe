from tkinter import *
import tkinter.messagebox
import random
w=Tk()
w.title("Tic Tac Toe")
##2 players
def click2():
    global w
    global turn
    playerbutton2.pack()
    for button in w.winfo_children():
        button.destroy()
    w.title("Tic tac toe")
    turn="O"
    tkinter.messagebox.showinfo("Game description:", "The objective of Tic Tac Toe is to get three in a row. You play on a three by three game board. The first player is known as X and the second is O. Players alternate placing Xs and Os on the game board until either oppent has three in a row or all nine squares are filled, so it's like the sign X must be placed in a position to get three in a row horizontally, vertically or diagonally. The same goes to O  X always goes first, and in the event that no one has three in a row, the statemate is called a cat game.")
    tkinter.messagebox.showinfo("PLAYERS:", "PLAYER 1:X , PLAYER 2:O")
    tkinter.messagebox.showinfo("Rules:", "player 1 goes first, player 2 goes second")
    def winorloseordraw():
        global turn
        ##for the O
        if (b1["text"]=="O" and b2["text"]=="O" and b3["text"]=="O") or (b1["text"]=="O" and b4["text"]=="O" and b7["text"]=="O") or (b1["text"]=="O" and b5["text"]=="O" and b9["text"]=="O"):
            tkinter.messagebox.showinfo("winner" , "O wins" )
            turn="END"
        elif (b2["text"]=="O" and b5["text"]=="O" and b8["text"]=="O"):
            tkinter.messagebox.showinfo("winner", "O wins")
            turn="END"
        elif (b3["text"]=="O" and b6["text"]=="O" and b9["text"]=="O"):
            tkinter.messagebox.showinfo("winner", "O wins")
            turn="END"
        elif (b3["text"]=="O" and b5["text"]=="O" and b7["text"]=="O"):
            tkinter.messagebox.showinfo("winner", "O wins")
            turn="END"
        elif (b4["text"]=="O" and b5["text"]=="O" and b6["text"]=="O"):
            tkinter.messagebox.showinfo("winner", "O wins")
            turn="END"
        elif (b5["text"]=="O" and b2["text"]=="O" and b8["text"]=="O"):
            tkinter.meessagebox.showinfo("winner", "O wins")
            turn="END"
        elif (b7["text"]=="O" and b8["text"]=="O" and b9["text"]=="O"):
            tkinter.messagebox.showinfo("winner", "O wins")
            turn="END"
        #for the X
        elif (b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X") or (b1["text"]=="X" and b4["text"]=="X" and b7["text"]=="X") or (b1["text"]=="X" and b5["text"]=="X" and b9["text"]=="X"):
            tkinter.messagebox.showinfo("winner", "X wins")
            turn="END"
        elif (b2["text"]=="X" and b5["text"]=="X" and b8["text"]=="X"):
            tkinter.messagebox.showinfo("winner", "X wins")
            turn="END"
        elif (b3["text"]=="X" and b6["text"]=="X" and b9["text"]=="X"):
            tkinter.messagebox.showinfo("winner", "X wins")
            turn="END"
        elif (b3["text"]=="X" and b5["text"]=="X" and b7["text"]=="X"):
            tkinter.messagebox.showinfo("winner", "X wins")
            turn="END"
        elif (b4["text"]=="X" and b5["text"]=="X" and b6["text"]=="X"):
            tkinter.messagebox.showinfo("winner", "X wins")
            turn="END"
        elif (b5["text"]=="X" and b2["text"]=="X" and b8["text"]=="X"):
            tkinter.meessagebox.showinfo("winner", "X wins")
            turn="END"
        elif (b7["text"]=="X" and b8["text"]=="X" and b9["text"]=="X"):
            tkinter.messagebox.showinfo("winner", "X wins")
            turn="END"
        #for the draw
        elif (b1["text"]!="" and b2["text"]!="" and b3["text"]!="" and b4["text"]!="" and b5["text"]!="" and b6["text"]!="" and b7["text"]!="" and b8["text"]!="" and b9["text"]!=""):
            tkinter.messagebox.showinfo("", "DRAW")
            turn="END"


    def click1():
        global turn
        if b1["text"]=="" and turn!="END":
            if turn=="X":
                turn="O"
            else:
                turn="X"
            b1["text"]=turn
        winorloseordraw()   

    def click2():
        global turn
        if b2["text"]=="" and turn!="END":
            if turn=="X":
                turn="O"
            else:
                turn="X"
            b2["text"]=turn
        winorloseordraw()
    def click3():
        global turn
        if b3["text"]=="" and turn!="END":
            if turn=="X":
                turn="O"
            else:
                turn="X"
            b3["text"]=turn
        winorloseordraw()
    def click4():
        global turn
        if b4["text"]=="" and turn!="END":
            if turn=="X":
                turn="O"
            else:
                turn="X"
            b4["text"]=turn
        winorloseordraw()
    def click5():
        global turn
        if b5["text"]=="" and turn!="END":
            if turn=="X":
                turn="O"
            else:
                turn="X"
            b5["text"]=turn
        winorloseordraw()


    def click6():
        global turn
        if b6["text"]=="" and turn!="END":
            if turn=="X":
                turn="O"
            else:
                turn="X"
            b6["text"]=turn
        winorloseordraw()

    def click7():
        global turn
        if b7["text"]=="" and turn!="END":
            if turn=="X":
                turn="O"
            else:
                turn="X"
            b7["text"]=turn
        winorloseordraw()
    def click8():
        global turn
        if b8["text"]=="" and turn!="END":
            if turn=="X":
                turn="O"
            else:
                turn="X"
            b8["text"]=turn
        winorloseordraw()

        
    def click9():
        global turn
        if b9["text"]=="" and turn!="END":
            if turn=="X":
                turn="O"
            else:
                turn="X"
            b9["text"]=turn
        winorloseordraw()
    def restart():
        global turn
        turn="X"
        b1["text"]=""
        b2["text"]=""
        b3["text"]=""
        b4["text"]=""
        b5["text"]=""
        b6["text"]=""
        b7["text"]=""
        b8["text"]=""
        b9["text"]=""
    b1=Button(w, text="", command=click1, width=8, height=4)
    b1.grid(column=1, row=0)
    b2=Button(w, text="", command=click2,width=8, height=4)
    b2.grid(column=2, row=0)
    b3=Button(w, text="", command=click3,width=8, height=4)
    b3.grid(column=3, row=0)
    b4=Button(w,text="", command=click4,width=8, height=4)
    b4.grid(column=1, row=1)
    b5=Button(w, text="", command=click5,width=8, height=4)
    b5.grid(column=2, row=1)
    b6=Button(w, text="", command=click6,width=8, height=4)
    b6.grid(column=3, row=1)
    b7=Button(w, text="", command=click7,width=8, height=4)
    b7.grid(column=1, row=2)
    b8=Button(w, text="", command=click8,width=8, height=4)
    b8.grid(column=2, row=2)
    b9=Button(w, text="", command=click9,width=8, height=4)
    b9.grid(column=3, row=2)
    restart=Button(w, text="Restart", command=restart, width=8, height=4)
    restart.grid(column=2, row=3)
        
def click():
    global w
    global turn
    playerbutton1.pack()
    for button in w.winfo_children():
        button.destroy()
    w.title("Tic tac toe")
    turn="X"
    tkinter.messagebox.showinfo("Game description:", "The objective of Tic Tac Toe is to get three in a row. You play on a three by three game board. The first player is known as X and the second is O. Players alternate placing Xs and Os on the game board until either oppent has three in a row or all nine squares are filled, so it's like the sign X must be placed in a position to get three in a row horizontally, vertically or diagonally. The same goes to O  X always goes first, and in the event that no one has three in a row, the statemate is called a cat game.")
    tkinter.messagebox.showinfo("PLAYER 1:", "X")
    tkinter.messagebox.showinfo("PLAYER 2:", "O")

    def winorloseordraw():
        global turn
        #for the X
        if (b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X") or (b1["text"]=="X" and b4["text"]=="X" and b7["text"]=="X") or (b1["text"]=="X" and b5["text"]=="X" and b9["text"]=="X"):
            tkinter.messagebox.showinfo("winner", "X wins")
            turn="END"
        elif (b2["text"]=="X" and b5["text"]=="X" and b8["text"]=="X"):
            tkinter.messagebox.showinfo("winner", "X wins")
            turn="END"
        elif (b3["text"]=="X" and b6["text"]=="X" and b9["text"]=="X"):
            tkinter.messagebox.showinfo("winner", "X wins")
            turn="END"
        elif (b3["text"]=="X" and b5["text"]=="X" and b7["text"]=="X"):
            tkinter.messagebox.showinfo("winner", "X wins")
            turn="END"
        elif (b4["text"]=="X" and b5["text"]=="X" and b6["text"]=="X"):
            tkinter.messagebox.showinfo("winner", "X wins")
            turn="END"
        elif (b5["text"]=="X" and b2["text"]=="X" and b8["text"]=="X"):
            tkinter.meessagebox.showinfo("winner", "X wins")
            turn="END"
        elif (b7["text"]=="X" and b8["text"]=="X" and b9["text"]=="X"):
            tkinter.messagebox.showinfo("winner", "X wins")
            turn="END"
        #for the robot
        elif (b1["text"]=="O" and b2["text"]=="O" and b3["text"]=="O") or (b1["text"]=="O" and b4["text"]=="O" and b7["text"]=="O") or (b1["text"]=="O" and b5["text"]=="O" and b9["text"]=="O"):
            tkinter.messagebox.showinfo("" , "You lost" )
            turn="END"
        elif (b2["text"]=="O" and b5["text"]=="O" and b8["text"]=="O"):
            tkinter.messagebox.showinfo("", "You lost")
            turn="END"
        elif (b3["text"]=="O" and b6["text"]=="O" and b9["text"]=="O"):
            tkinter.messagebox.showinfo("", "You lost")
            turn="END"
        elif (b3["text"]=="O" and b5["text"]=="O" and b7["text"]=="O"):
            tkinter.messagebox.showinfo("", "You lost")
            turn="END"
        elif (b4["text"]=="O" and b5["text"]=="O" and b6["text"]=="O"):
            tkinter.messagebox.showinfo("", "You lost")
            turn="END"
        elif (b5["text"]=="O" and b2["text"]=="O" and b8["text"]=="O"):
            tkinter.meessagebox.showinfo("", "You lost")
            turn="END"
        elif (b7["text"]=="O" and b8["text"]=="O" and b9["text"]=="O"):
            tkinter.messagebox.showinfo("", "You lost")
            turn="END"
        
        #for the draw
        elif (b1["text"]!="" and b2["text"]!="" and b3["text"]!="" and b4["text"]!="" and b5["text"]!="" and b6["text"]!="" and b7["text"]!="" and b8["text"]!="" and b9["text"]!=""):
            tkinter.messagebox.showinfo("", "DRAW")
            turn="END"


    def defense():
        notyetplace=True
        #Strategical defense
        ##strategical defense
        if b6["text"]==b8["text"]=="X" and b9["text"]=="":
            b9["text"]="O"
            notyetplace=False
        ##strategical defense
        elif b1["text"]==b8["text"]=="X" and b4["text"]=="" :
            b4["text"]="O"
            notyetplace=False
        ##1st strategical defense
        elif b1["text"]==b9["text"]=="X" and b4["text"]=="":
            b4["text"]="O"
            notyetplace=False
        ##2nd strategical defense 
        elif b5["text"]==b9["text"]=="X" and b3["text"]=="":
            b3["text"]="O"
            notyetplace=False
        ## diagonal defense (part of strategical defense)
        elif b3["text"]==b5["text"]=="X" and b7["text"]=="":
            b7["text"]="O"
            notyetplace=False
        ## 3rd strategical defense
        elif (b3["text"]==b7["text"]=="X" and b6["text"]=="") or (b3["text"]==b8["text"]=="X" and b6["text"]==""):
            b6["text"]="O"
            notyetplace=False
        #ROWS:
        #1st row:
        elif b1["text"]==b2["text"]=="X" and b3["text"]=="":
            b3["text"]="O"
            notyetplace=False
        elif b1["text"]==b3["text"]=="X" and b2["text"]=="":
            b2["text"]="O"
            notyetplace=False
        elif b2["text"]==b3["text"]=="X" and b1["text"]=="":
            b1["text"]="O"
            notyetplace=False

        #2nd row:
        elif b4["text"]==b5["text"]=="X" and b6["text"]=="":
            b6["text"]="O"
            notyetplace=False
        elif b4["text"]==b6["text"]=="X" and b5["text"]=="":
            b5["text"]="O"
            notyetplace=False
        elif b5["text"]==b6["text"]=="X" and b4["text"]=="":
            b4["text"]="O"
            notyetplace=False

        #3rd row:
        elif b7["text"]==b8["text"]=="X" and b9["text"]=="":
            b9["text"]="O"
            notyetplace=False
        elif b7["text"]==b9["text"]=="X" and b8["text"]=="":
            b8["text"]="O"
            notyetplace=False
        elif b8["text"]==b9["text"]=="X" and b7["text"]=="":
            b7["text"]="O"
            notyetplace=False

        #COLUMNS:
        #1st column:
        elif b1["text"]==b4["text"]=="X" and b7["text"]=="":
            b7["text"]="O"
            notyetplace=False
        elif b1["text"]==b7["text"]=="X" and b4["text"]=="":
            b4["text"]="O"
            notyetplace=False
        elif b4["text"]==b7["text"]=="X" and b1["text"]=="":
            b1["text"]="O"
            notyetplace=False

        #2nd column:
        elif b2["text"]==b5["text"]=="X" and b8["text"]=="":
            b8["text"]="O"
            notyetplace=False
        elif b2["text"]==b8["text"]=="X" and b5["text"]=="":
            b5["text"]="O"
            notyetplace=False
        elif b5["text"]==b8["text"]=="X" and b2["text"]=="":
            b2["text"]="O"
            notyetplace=False
        #3rd column:
        elif b3["text"]==b6["text"]=="X" and b9["text"]=="":
            b9["text"]="O"
            notyetplace=False
        elif b3["text"]==b9["text"]=="X" and b6["text"]=="":
            b6["text"]="O"
            notyetplace=False
        elif b6["text"]==b9["text"]=="X" and b3["text"]=="":
            b3["text"]="O"
            notyetplace=False

        #DIAGONALS:
        #1st diagonal:
        elif b1["text"]==b5["text"]=="X" and b9["text"]=="":
            b9["text"]="O"
            notyetplace=False
        elif b1["text"]==b9["text"]=="X" and b5["text"]=="":
            b5["text"]="O"
            notyetplace=False
        elif b5["text"]==b9["text"]=="X" and b1["text"]=="":
            b1["text"]="O"
            notyetplace=False
        
        #2nd diagonal:
        elif b3["text"]==b5["text"]=="X" and b7["text"]=="":
            b7["text"]="O"
            notyetplace=False
        elif b3["text"]==b7["text"]=="X" and b5["text"]=="":
            b5["text"]="O"
            notyetplace=False
        elif b5["text"]==b7["text"]=="X" and b3["text"]=="":
            b3["text"]="O"
            notyetplace=False
        return notyetplace
     
        
    def win():
        #ROWS:
        #1st row:
        if b1["text"]==b2["text"]=="O" and b3["text"]=="":
            b3["text"]="O"
            notyetplace=False
        elif b1["text"]==b3["text"]=="O" and b2["text"]=="":
            b2["text"]="O"
            notyetplace=False
        elif b2["text"]==b3["text"]=="O" and b1["text"]=="":
            b1["text"]="O"
            notyetplace=False

        #2nd row:
        elif b4["text"]==b5["text"]=="O" and b6["text"]=="":
            b6["text"]="O"
            notyetplace=False
        elif b4["text"]==b6["text"]=="O" and b5["text"]=="":
            b5["text"]="O"
            notyetplace=False
        elif b5["text"]==b6["text"]=="O" and b4["text"]=="":
            b4["text"]="O"
            notyetplace=False

        #3rd row:
        elif b7["text"]==b8["text"]=="O" and b9["text"]=="":
            b9["text"]="O"
            notyetplace=False
        elif b7["text"]==b9["text"]=="O" and b8["text"]=="":
            b8["text"]="O"
            notyetplace=False
        elif b8["text"]==b9["text"]=="O" and b7["text"]=="":
            b7["text"]="O"
            notyetplace=False

        #COLUMNS:
        #1st column:
        elif b1["text"]==b4["text"]=="O" and b7["text"]=="":
            b7["text"]="O"
            notyetplace=False
        elif b1["text"]==b7["text"]=="O" and b4["text"]=="":
            b4["text"]="O"
            notyetplace=False
        elif b4["text"]==b7["text"]=="O" and b1["text"]=="":
            b1["text"]="O"
            notyetplace=False

        #2nd column:
        elif b2["text"]==b5["text"]=="O" and b8["text"]=="":
            b8["text"]="O"
            notyetplace=False
        elif b2["text"]==b8["text"]=="O" and b5["text"]=="":
            b5["text"]="O"
            notyetplace=False
        elif b5["text"]==b8["text"]=="O" and b2["text"]=="":
            b2["text"]="O"
            notyetplace=False
        #3rd column:
        elif b3["text"]==b6["text"]=="O" and b9["text"]=="":
            b9["text"]="O"
            notyetplace=False
        elif b3["text"]==b9["text"]=="O" and b6["text"]=="":
            b6["text"]="O"
            notyetplace=False
        elif b6["text"]==b9["text"]=="O" and b3["text"]=="":
            b3["text"]="O"
            notyetplace=False

        #DIAGONALS:
        #1st diagonal:
        elif b1["text"]==b5["text"]=="O" and b9["text"]=="":
            b9["text"]="O"
            notyetplace=False
        elif b1["text"]==b9["text"]=="O" and b5["text"]=="":
            b5["text"]="O"
            notyetplace=False
        elif b5["text"]==b9["text"]=="O" and b1["text"]=="":
            b1["text"]="O"
            notyetplace=False
        
        #2nd diagonal:
        elif b3["text"]==b5["text"]=="O" and b7["text"]=="":
            b7["text"]="O"
            notyetplace=False
        elif b3["text"]==b7["text"]=="O" and b5["text"]=="":
            b5["text"]="O"
            notyetplace=False
        elif b5["text"]==b7["text"]=="O" and b3["text"]=="":
            b3["text"]="O"
            notyetplace=False
        else:
            notyetplace=True
        return notyetplace

    
    def strategy():
        notyetplace=True
        ##1st strategy middle spot
        if b5["text"]=="":
            b5["text"]="O"
            notyetplace=False
        elif (b5["text"]=="O") or (b5["text"]=="") or (b5["text"]=="X"):
            if b1["text"]=="":
                b1["text"]="O"
                notyetplace=False
            elif b3["text"]=="":
                b3["text"]="O"
                notyetplace=False
            elif b7["text"]=="":
                b7["text"]="O"
                notyetplace=False
            elif b9["text"]=="":
                b9["text"]="O"
                notyetplace=False
        ##2nd strategy 236
        elif b2["text"]=="":
            b2["text"]="O"
            notyetplace=False
        elif (b2["text"]=="") or (b2["text"]=="O"):
            if b3["text"]=="":
                b3["text"]="O"
                notyetplace=False
            elif b6["text"]=="":
                b6["text"]="O"
                notyetplace=False
        ##4th strategy 124
        elif b1["text"]=="":
            b1["text"]="O"
            notyetplace=False
        elif b1["text"]=="" or b1["text"]=="O":
            if b2["text"]=="":
                b2["text"]="O"
                notyetplace=False
            elif b4["text"]=="":
                b4["Text"]="O"
                notyetplace=False
        ##5th strategy 478
        elif b7["text"]=="":
            b7["text"]="O"
            notyetplace=False
        elif b7["text"]=="" or b7["text"]=="O":
            if b8["text"]=="":
                b8["text"]="O"
                notyetplace=False
            elif b4["text"]=="":
                b4["Text"]="O"
                notyetplace=False
        ##6th strategy 986
        elif b9["text"]=="":
            b9["text"]="O"
            notyetplace=False
        elif b9["text"]=="" or b9["text"]=="O":
            if b6["text"]=="":
                b6["text"]=="O"
                notyetplace=False
            elif b8["text"]=="":
                b8["text"]="O"
                notyetplace=False
        ##7th strategy 179
        elif b1["text"]=="":
            b1["text"]="O"
            notyetplace=False
        elif b1["text"]=="" or b1["text"]=="O":
            if b7["text"]=="":
                b7["text"]="O"
                notyetplace=False
            elif b9["text"]=="":
                b9["text"]="O"
                notyetplace=False
        ##8th strategy 397
        elif b3["text"]=="":
            b3["text"]="O"
            notyetplace=False
        elif b3["text"]=="" or b3["text"]=="O":
            if b7["text"]=="":
                b7["text"]="O"
                notyetplace=False
            elif b9["text"]=="":
                b9["text"]="O"
                notyetplace=False
        #just to tell the strategy status
        return notyetplace
    def computer():
        z=win()
        if z==True:
            x=defense()
            if x==True:
                y=strategy()
                if y==True:
                    notyetplace=True
                    grn=[]
                    while notyetplace!=False and len(grn)<9:
                        buttonnumber=random.randint(1,9)
                        if buttonnumber not in grn:
                            grn.append(buttonnumber)
                            if buttonnumber==1 and notyetplace==True:
                               if b1["text"]=="":
                                   b1["text"]="O"
                                   notyetplace=False
                               else:
                                   notyetplace=True
                            elif buttonnumber==2 and notyetplace==True:
                               if b2["text"]=="":
                                   b2["text"]="O"
                                   notyetplace=False
                               else:
                                   notyetplace=True
                            elif buttonnumber==3 and notyetplace==True:
                               if b3["text"]=="":
                                   b3["text"]="O"
                                   notyetplace=False
                               else:
                                   notyetplace=True
                            elif buttonnumber==4 and notyetplace==True:
                               if b4["text"]=="":
                                   b4["text"]="O"
                                   notyetplace=False
                               else:
                                   notyetplace=True
                            elif buttonnumber==5 and notyetplace==True:
                               if b5["text"]=="":
                                   b5["text"]="O"
                                   notyetplace=False
                               else:
                                   notyetplace=True
                            elif buttonnumber==6 and notyetplace==True:
                               if b6["text"]=="":
                                   b6["text"]="O"
                                   notyetplace=False
                               else:
                                   notyetplace=True
                            elif buttonnumber==7 and notyetplace==True:
                               if b7["text"]=="":
                                   b7["text"]="O"
                                   notyetplace=False
                               else:
                                   notyetplace=True
                            elif buttonnumber==8 and notyetplace==True:
                               if b8["text"]=="":
                                   b8["text"]="O"
                                   notyetplace=False
                               else:
                                   notyetplace=True
                            elif buttonnumber==9 and notyetplace==True:
                               if b9["text"]=="":
                                   b9["text"]="O"
                                   notyetplace=False
                               else:
                                   notyetplace=True
    ##for all the clicks, make sure to follow the def click1()
    def click1():
        #make a global turn because its for every function that has a click on it
        global turn
        if b1["text"]=="" and turn!="END":
            if turn=="X":
                b1["text"]="X"
            computer()
        winorloseordraw()   

    def click2():
        global turn
        if b2["text"]=="" and turn!="END":
            if turn=="X":
                b2["text"]="X"
            computer()
        winorloseordraw()
    def click3():
        global turn
        if b3["text"]=="" and turn!="END":
            if turn=="X":
                b3["text"]="X"
            computer()
        winorloseordraw()
    def click4():
        global turn
        if b4["text"]=="" and turn!="END":
            if turn=="X":
               b4["text"]="X"
            computer()
        winorloseordraw()
    def click5():
        global turn
        if b5["text"]=="" and turn!="END":
            if turn=="X":
                b5["text"]="X"
            computer()
        winorloseordraw()
    def click6():
        global turn
        if b6["text"]=="" and turn!="END":
            if turn=="X":
               b6["text"]="X"
            computer()
        winorloseordraw()

    def click7():
        global turn
        if b7["text"]=="" and turn!="END":
            if turn=="X":
                b7["text"]="X"
            computer()
        winorloseordraw()
    def click8():
        global turn
        if b8["text"]=="" and turn!="END":
            if turn=="X":
                b8["text"]="X"
            computer()
        winorloseordraw()

        
    def click9():
        global turn
        if b9["text"]=="" and turn!="END":
            if turn=="X":
               b9["text"]="X"
            computer()
        winorloseordraw()
    def restart():
        global turn
        turn="X"
        b1["text"]=""
        b2["text"]=""
        b3["text"]=""
        b4["text"]=""
        b5["text"]=""
        b6["text"]=""
        b7["text"]=""
        b8["text"]=""
        b9["text"]=""

    b1=Button(w, text="", command=click1, width=8, height=4)
    b1.grid(column=1, row=0)
    b2=Button(w, text="", command=click2,width=8, height=4)
    b2.grid(column=2, row=0)
    b3=Button(w, text="", command=click3,width=8, height=4)
    b3.grid(column=3, row=0)
    b4=Button(w,text="", command=click4,width=8, height=4)
    b4.grid(column=1, row=1)
    b5=Button(w, text="", command=click5,width=8, height=4)
    b5.grid(column=2, row=1)
    b6=Button(w, text="", command=click6,width=8, height=4)
    b6.grid(column=3, row=1)
    b7=Button(w, text="", command=click7,width=8, height=4)
    b7.grid(column=1, row=2)
    b8=Button(w, text="", command=click8,width=8, height=4)
    b8.grid(column=2, row=2)
    b9=Button(w, text="", command=click9,width=8, height=4)
    b9.grid(column=3, row=2)
    restar=Button(w, text="Restart", command=restart, width=8, height=4)
    restar.grid(column=2, row=3)

playerbutton1=Button(w, text="1 player mode", command=click)
playerbutton2=Button(w, text="2 player mode", command=click2)
playerbutton1.pack()
playerbutton2.pack()
w.mainloop()

'''
what the board will look like:
1 2 3
4 5 6
7 8 9
'''
