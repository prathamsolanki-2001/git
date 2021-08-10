import random
import tkinter

window = tkinter.Tk()
def bot(userChoice):
    choices = ['R','P','S']
    opponenetChoice = random.choice(choices)
    pc = tkinter.Label(window, text = "Bot Choice :")
    pc.place( x = 40, y = 90)
    pc1 = tkinter.Label(window, text = opponenetChoice)
    pc1.place( x = 120, y = 90)
    comments = ['Bot Wins']
    if opponenetChoice == str.upper(userChoice):
        r1 = tkinter.Label(window, text = "  Tie!             ")
        r1.place( x = 40, y = 150)
    elif opponenetChoice == 'R' and userChoice.upper() == 'S':  
        p = random.choice(comments)    
        r1 = tkinter.Label(window, text = p)
        r1.place( x = 40, y = 150)
    elif opponenetChoice == 'S' and userChoice.upper() == 'P':      
        p = random.choice(comments)    
        r1 = tkinter.Label(window, text = p)
        r1.place( x = 40, y = 150)
    elif opponenetChoice == 'P' and userChoice.upper() == 'R':      
        p = random.choice(comments)    
        r1 = tkinter.Label(window, text = p)
        r1.place( x = 40, y = 150)
    else:       
        r1 = tkinter.Label(window, text = "You win")
        r1.place( x = 40, y = 150)

def main(): 
    numlbl = tkinter.Label(window, text = "Choose your best weapon : [R]ock, [P]aper And [S]cissors ")
    numlbl.place( x = 40, y = 40)
    numtxt = tkinter.Entry(window, width=20)
    numtxt.place( x = 45, y= 65)

    dis = tkinter.Button(window, bg = 'red', text = "Battle!!", width = 75, height = 5, command =lambda: bot(numtxt.get()))
    dis.place( x = 40, y = 250)

    window.title("Rock, Paper And Scissor")
    window.geometry("600x400")
    window.mainloop()

if __name__ == "__main__":
    main()


