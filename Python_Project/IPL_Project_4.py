import random
status=True
while status:
    print("---------------------IPL GAME:2025-----------------------\n")
    team_list=["CSK","RCB","KKR","MI","KXIP","LSG","RR","SRH","GT","DC"]
    print(team_list)
    print()
    team=input("Enter Your Team Name:- ")
    team=team.upper()
    if team not in team_list:
        print("You Enter Invalid Team")
    else:   
        opp1=random.choice(team_list)
        while team == opp1:
            opp1=random.choice(team_list)
        print(f"Your Opponent Team Name is:- {opp1}\n")
        print(f">>>>>>>>>>>>>>>> {team} VS {opp1} <<<<<<<<<<<<<<<\n")
        print("---------------------TOSS TIME-------------------------")
        toss_list=['H','T']
        toss=input("\nDo You Want Tail or Head Enter That(H/T):- ")
        toss=toss.upper()
        print(f"Your Enter Choice is:- {toss}")
        if toss not in toss_list:
            print("You Enter Invalid Choice")
        else:
            opp=random.choice(toss_list)
            print(f"Toss Result:- {opp}")
            if toss == opp:
                print("You Won The Toss")
                choice=input("Enter Your Choice Batting or Balling:- ")
                print(f"Your Choice is:- {choice}\n")
            else:
                print("You Loss The Toss")
                choice_list=["Batting","Balling"]
                opp=random.choice(choice_list)
                print(f"Your Oppenent Team Choose A :- {opp}\n")
            print("----------------------SCORE BOARD--------------------")
            ran=random.randint(100,200)
            wic=random.randint(1,10)
            print(f"Score Of {team}:-{ran}/{wic}")
            ran1=random.randint(100,200)
            wic1=random.randint(1,10)
            print(f"Score Of {opp1}:-{ran1}/{wic1}\n")
            if ran > ran1:
                print(f"{team} is a Winner Team")
            else:
                print(f"{opp1} is a Winner Team")
    choice=input("\nDo You Want To Continue This Game(y/n):- ")
    if choice == 'Y' or choice == 'y':
        status=True
    else:
        status=False



   
    
