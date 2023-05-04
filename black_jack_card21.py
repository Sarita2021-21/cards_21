import random
from arts_2 import logo 
print(logo)
list_of_cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
global cards_total
computers_choice=random.randint(2,11)
# print(computers_choice)
def comparing_values():
    if cards_total>computer_cards_total and cards_total<=21:
        print("You won")
    elif cards_total<computer_cards_total and computer_cards_total<=21:
        print("Computer won")
    elif cards_total==computer_cards_total:
        print("It's a draw")


def computers_choice_1():
    global computer_cards_total
    computer_cards_total=0
    if computers_choice<21:
        # print("computer choose another card")
        computers_choice_2=random.randint(2,11)
        computer_cards_total=computers_choice+computers_choice_2
        # print(f"Computers card total is {computer_cards_total}")
        if computer_cards_total<16:
            # print("Computer have to pick another card as computer card total is less then 16")
            computers_choice_2=random.randint(2,11)
            computer_cards_total+=computers_choice_2
            print(f"Computers card total is {computer_cards_total}")
            # if computer_cards_total>21 and cards_total<21:
            #     print("Computer Lose.You won")
            # return cards_total
        # user_choice_2=input("Do you want to show your card. If yes then type 'y'").lower()
        # if cards_total>16 and user_choice_2=="y":
        #     print(f"your card total is {cards_total}")
        #     return cards_total
        
        
        

def cards_choice():
    global cards_total
    cards_total=0
    if user_choice_1<21:
        print("Pick another card")
        user_choice_2=int(input())
        cards_total=user_choice_1+user_choice_2
        print(f"your card total is {cards_total}")
        while cards_total<16:
            print("you have to pick another card as your card total is less then 16")
            user_choice_2=int(input())
            cards_total+=user_choice_2
            print(f"your card total is {cards_total}")
            # return cards_total
        user_choice_2=input("Do you want to show your card. If yes then type 'y' otherwise type 'n'").lower()
        while cards_total>16 and user_choice_2=="y" and computer_cards_total<cards_total:
            print(f"your card total is {cards_total}")
            print(f"Computers card total is {computer_cards_total}")
            break
            
        if user_choice_2=="n":
            print("Pick another card")
            user_choice_3=int(input())
            cards_total+=user_choice_3
            print(f"your card total is {cards_total}")
            if cards_total>21:
                print("Sorry You lose. Computer Won")
            
            
user_choice=(input(" Do you want to play card 21 or a blackjack game? If 'Yes' the type'y' else type 'n'")).lower()
if user_choice=='y':
    # cards_choice()
    user_choice_1=int(input(f"Enter a number of your choice given in the card list {list_of_cards}"))
    while user_choice_1>=12:
        print("Wrong card selection please choose different card")
        break
        cards_choice()
        computers_choice_1()
        comparing_values()
    else:
        computers_choice_1()
        cards_choice()
        comparing_values()
        
elif user_choice=="n":
    print("no issue come again when you want to play blackjack")
    pass
else:
    print("you made a wrong choice")

        # else:
            

        
    


# if cards_total>16 and cards_total==21:
#     user_accept=input("do you want to show the cards.If 'Yes' then type 'y' else type 'n'").lower()
#     if user_accept=="y":
#         print(f"users cards total is {cards_total}")        
#             # if cards_total<16:
#         #     print("you have to pick another card as your card total is less then 16")
#         #     user_choice_2=int(input())
#         #     cards_total=user_choice_1+user_choice_2
#         # # user_choice
        
        

