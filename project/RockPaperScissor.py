print("Lets play Rock Paper Scissor")

player1 = str(input("Enter the Object you Have to Select - r , p , s[Rock , Paper , Scissor]\n"))
player2 = str(input("Enter the Object you Have to Select - r , p , s[Rock, Paper ,Sscissor]\n "))

#Rock Condition
if (player1 == 'r') and (player2 == 'r'):
    print("Player1 choose {option} and player2 choose {option2}".format(option = player1 , option2 = player2))
    print("Thats a Tie")

elif (player1 == 'r') and (player2 == 'p'):
    print("player1 choose {option} and player2 choose {option2}".format(option = player1, option2 = player2))
    print("Player2 Wins because Paper is choosen")


elif (player1 == 'r') and (player2 == 's'):
    print("player1 choose {option} and player2 choose {option2}".format(option = player1 , option2 = player2))
    print("player1 Wins Because Rock is Choosen")



#Paper Condition
if (player1 == 'p') and (player2 == 'r'):
    print("player1 choose {option} and player2 choose {option2}".format(option =player1, option2 =player2))
    print("Player1 wins Because Paper is choosen")

elif (player1 == 'p') and (player2 =='p'):
    print("player1 choose {option} and player2 choose {option2}".format(option = player1, option2 = player2))
    print("Thats A Tie ")


elif (player1 == 'p') and (player2 =='s'):
    print("player1 choose {option} and player2 choose {option2}".format(option = player1, option2 = player2))
    print("Player2 Wins")


#Scissor 
if (player1 == 's') and (player2 == 'p'):
    print("player1 choose {option} and player2 choose {option2}".format(option = player1 ,option2 = player2))
    print("Player1 wins")

elif (player1 == 's') and (player2 == 'r'):
    print("player choose {option} and player2 choose {option2} ".format(option = player1 , option2 = player2))
    print("Player2 wins")

elif (player1 == 's') and (player2 == 's'):
    print("player1 choose {option} and player2 choose {option}".format(option = player1 , option2 = player2))
    print("Tie")


else:
     print("Error :choose correct option")