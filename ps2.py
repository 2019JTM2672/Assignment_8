#!/usr/bin/python3.6
from itertools import chain 
print("Welcome to the Game!")

mat=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(0,3):
    for j in range(0,3):
        print(mat[i][j], end="  ")  
    print()
def player1():
    # global m1
    # global mat
    a,b=input("position and number to be entered: ").split()
    m1= list(chain.from_iterable(mat))             # printing flatten_list 
    m1[int(a)-1]=int(b)
    print(m1)
print("player 1 chance")
player1()    
def player2():
    # global m1
    # global m2
    c,d=input("position and number to be entered: ").split()
    m2= list(chain.from_iterable(m1))             # printing flatten_list 
    m2[int(c)-1]=int(d)
    print(m2)
print("player 2 chance")
player2()

def check1 ():
    if m1[0]+m1[1]+m1[2]>=15:
        print("player 1 win")
    elif m1[3]+m1[4]+m1[5]>=15:
        print("player 1 win")    
    elif m1[6]+m1[7]+m1[8]>=15:
        print("player 1 win")
    elif m1[0]+m1[3]+m1[6]>=15:
        print("player 1 win")
    elif m1[1]+m1[4]+m1[7]>=15:
        print("player 1 win")
    elif m1[2]+m1[5]+m1[8]>=15:
        print("player 1 win")
    elif m1[0]+m1[4]+m1[8]>=15:
        print("player 1 win")
    elif m1[2]+m1[4]+m1[6]>=15:
        print("player 1 win")
def check2():
    if m1[0]+m1[1]+m1[2]>=15:
        print("player 2 win")
    elif m1[3]+m1[4]+m1[5]>=15:
        print("player 2 win")    
    elif m1[6]+m1[7]+m1[8]>=15:
        print("player 2 win")
    elif m1[0]+m1[3]+m1[6]>=15:
        print("player 2 win")
    elif m1[1]+m1[4]+m1[7]>=15:
        print("player 2 win")
    elif m1[2]+m1[5]+m1[8]>=15:
        print("player 2 win")
    elif m1[0]+m1[4]+m1[8]>=15:
        print("player 2 win")
    elif m1[2]+m1[4]+m1[6]>=15:
        print("player 2 win")

    

    while(1):    
    x=int(input("press 1 for work : press 2 for exit"))
    if x==1:
        switch()
    elif x==2:
        exit()    
    else:
        print("invalid input")