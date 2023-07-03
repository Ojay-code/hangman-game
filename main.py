from tkinter import *
import customtkinter as ctk
from tkinter import messagebox

from string import ascii_uppercase
import random
# from PIL import Image,ImageTk

window = ctk.CTk()
window.resizable(False,False)
window.geometry('500x400')
window.title('OjayHangman Game')
word_list= ['OTILOR', 'INDENT','RESIZABLE','OCCUPY', 'COMPUTER', 'COMPANY', 'UNIVERSITY', 'PYTHON'
            ]

photos = [PhotoImage(file="hang0.png"), PhotoImage(file="hang1.png"), PhotoImage(file="hang2.png"),
PhotoImage(file="hang3.png"), PhotoImage(file="hang4.png"), PhotoImage(file="hang5.png"),
PhotoImage(file="hang6.png"), PhotoImage(file="hang7.png"), PhotoImage(file="hang8.png"),
PhotoImage(file="hang9.png"), PhotoImage(file="hang10.png"), PhotoImage(file="hang11.png")]






def newGame():
    global the_word_withSpaces
    global numberOfGuesses
    numberOfGuesses =0

    the_word=random.choice(word_list)
    the_word_withSpaces = " ".join(the_word)
    lblWord.set(' '.join("_"*len(the_word)))

def guess(letter):
	global numberOfGuesses
	if numberOfGuesses<11:	
		txt = list(the_word_withSpaces)
		guessed = list(lblWord.get())
		if the_word_withSpaces.count(letter)>0:
			for c in range(len(txt)):
				if txt[c]==letter:
					guessed[c]=letter
				lblWord.set("".join(guessed))
				if lblWord.get()==the_word_withSpaces:
					messagebox.showinfo("Hangman","You Won!")
		else:
			numberOfGuesses += 1
			imgLabel.config(image=photos[numberOfGuesses])
			if numberOfGuesses==11:
					messagebox.showwarning("Hangman","Game Over")


imgLabel=Label(window)
imgLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=40)



lblWord = StringVar()
Label(window, textvariable  =lblWord,font=('consolas 24 bold')).grid(row=0, column=3 ,columnspan=7,padx=20)

n=0
for c in ascii_uppercase:
    butt=ctk.CTkButton(window, text=c, command=lambda c=c: guess(c), width= 10, border_width= 3, border_spacing=20).grid(row=1+n//9,column=n%9)
    n+=1

but1= ctk.CTkButton(window, text="New\nGame", command=lambda:newGame(),width= 6,border_spacing=10).grid(row=3, column=8)

newGame()
window.mainloop()
