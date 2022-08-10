import random
print("WELCOME TO COW_BULL GAME :")
print("IF GUESS NUMBER AND POSITION ARE RIGHT SO,BULL")
print("IF GUESS NUMBER ARE RIGHT BUT POSITION NOT SO,COW")
print("YOU HAVE ONLY 5 CHANCE")
name=input("ENTER YOUR NAME :")
print("WELCOME",name)
def game():
    number=random.sample([0,1,2,3,4,5,6,7,8,9],4)
    print(number)
    print("BEST OF LUCK :")
    cow=[]
    bull=[]
    for i in range(5):
        if bull==number:
            print("YOU ARE WINNER ")
            play=input("DO YOU WANT TO PLAY AGAIN 'Y' OR 'N'")
            if play=='y':
                game()
            if play=='N':
                print("THANKS FOR PLAY THIS GAME")
                break
        guess_number=int(input("ENTER YOUR GUESS NUMBER :"))
        guess_position=int(input("ENTER YOUR GUESS POSITION :"))
        for i in number:
            if guess_number in number:
                if guess_number in number and number.index(guess_number)==guess_position:
                    bull.insert(guess_position,guess_number)
                    print("Bull:",bull)
                    break
                else:
                    cow.insert(guess_position,guess_number)
                    print("Cow:",cow)
                    break
            else:
                print("YOUR NUMBER NOT EXISTS IN LIST :")
                break
        else:
            print("SORRY YOUR CHANCE IS FINISHED :")
game()
