import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import Label, Canvas, PhotoImage, Frame, Entry, Button

#keyboard functions
def clear_text():
    entry.delete(0, END)
def set_text_A(text):
    a = entry.get() + text
    entry.delete(0, len(entry.get()))
    entry.insert(0, a)
def set_text_B(text):
    a = entry.get() + text
    entry.delete(0, len(entry.get()))
    entry.insert(0, a)
def set_text_C(text):
    a = entry.get() + text
    entry.delete(0, len(entry.get()))
    entry.insert(0, a)
def set_text_D(text):
    a = entry.get() + text
    entry.delete(0, len(entry.get()))
    entry.insert(0, a)
def set_text_E(text):
    a = entry.get() + text
    entry.delete(0, len(entry.get()))
    entry.insert(0, a)
def set_text_F(text):
    a = entry.get() + text
    entry.delete(0, len(entry.get()))
    entry.insert(0, a)
def set_text_G(text):
    a = entry.get() + text
    entry.delete(0, len(entry.get()))
    entry.insert(0, a)
def set_text_H(text):
    a = entry.get() + text
    entry.delete(0, len(entry.get()))
    entry.insert(0, a)
def set_text_I(text):
    a = entry.get() + text
    entry.delete(0, len(entry.get()))
    entry.insert(0, a)
def set_text_J(text):
    a = entry.get() + text
    entry.delete(0, len(entry.get()))
    entry.insert(0, a)
def set_text_K(text):
    a = entry.get() + text
    entry.delete(0, len(entry.get()))
    entry.insert(0, a)
def set_text_L(text):
    a = entry.get() + text
    entry.delete(0, len(entry.get()))
    entry.insert(0, a)
def set_text_M(text):
    a = entry.get() + text
    entry.delete(0, len(entry.get()))
    entry.insert(0, a)
def set_text_N(text):
    a = entry.get() + text
    entry.delete(0, len(entry.get()))
    entry.insert(0, a)
def set_text_O(text):
    a = entry.get() + text
    entry.delete(0, len(entry.get()))
    entry.insert(0, a)
def set_text_P(text):
    a = entry.get() + text
    entry.delete(0, len(entry.get()))
    entry.insert(0, a)
def set_text_Q(text):
    a = entry.get() + text
    entry.delete(0, len(entry.get()))
    entry.insert(0, a)
def set_text_R(text):
    a = entry.get() + text
    entry.delete(0, len(entry.get()))
    entry.insert(0, a)
def set_text_S(text):
    a = entry.get() + text
    entry.delete(0, len(entry.get()))
    entry.insert(0, a)
def set_text_T(text):
    a = entry.get() + text
    entry.delete(0, len(entry.get()))
    entry.insert(0, a)
def set_text_U(text):
    a = entry.get() + text
    entry.delete(0, len(entry.get()))
    entry.insert(0, a)
def set_text_V(text):
    a = entry.get() + text
    entry.delete(0, len(entry.get()))
    entry.insert(0, a)
def set_text_W(text):
    a = entry.get() + text
    entry.delete(0, len(entry.get()))
    entry.insert(0, a)
def set_text_X(text):
    a = entry.get() + text
    entry.delete(0, len(entry.get()))
    entry.insert(0, a)
def set_text_Y(text):
    a = entry.get() + text
    entry.delete(0, len(entry.get()))
    entry.insert(0, a)
def set_text_Z(text):
    a = entry.get() + text
    entry.delete(0, len(entry.get()))
    entry.insert(0, a)

#main program
def instruction():
    tkinter.messagebox.showinfo('Welcome To the HANGMAN Game',
                                'You have 3 attempts to play this game ''\n'
                                'There are few images in this game ''\n'
                                'you have to guess them correctly''\n')
def image_start():
    first_image = Label(frame1, image=Image1)
    first_image.place( x=-350, y=20 ,relx=0.5, rely=0.15, relwidth=0.7, relheight=0.6, anchor='n')


def image_two():
    second_image = Label(frame1, image=Image2)
    second_image.place(x=-350, y=20 ,relx=0.5, rely=0.15, relwidth=0.7, relheight=0.6, anchor='n')


def image_three():
    second_image = Label(frame1, image=Image3)
    second_image.place(x=-350, y=20 ,relx=0.5, rely=0.15, relwidth=0.7, relheight=0.6, anchor='n')


def image_forth():
    second_image = Label(frame1, image=Image4)
    second_image.place(x=-350, y=20 ,relx=0.5, rely=0.15, relwidth=0.7, relheight=0.6, anchor='n')


def image_fifth():
    second_image = Label(frame1, image=Image5)
    second_image.place(x=-350, y=20 ,relx=0.5, rely=0.15, relwidth=0.7, relheight=0.6, anchor='n')


def image_sixth():
    second_image = Label(frame1, image=Image6)
    second_image.place(x=-350, y=20 ,relx=0.5, rely=0.15, relwidth=0.7, relheight=0.6, anchor='n')
turns = 3
def check(entry):
        global turns
        if (entry == "DOG"):
            tkinter.messagebox.showinfo('Answer', 'Congratulation, you got it!')
            image_two()

        elif (entry == "SQUIRREL"):
                tkinter.messagebox.showinfo('Answer', 'Congratulation, you got it!')
                image_three()

        elif (entry == 'HORSE'):
                    tkinter.messagebox.showinfo('Answer', 'Congratulation, you got it!')
                    image_forth()
        elif (entry == 'WOLF'):
                        tkinter.messagebox.showinfo('Answer', 'Congratulation, you got it!')
                        image_fifth()

        elif (entry == 'ROOSTER'):
                            tkinter.messagebox.showinfo('Answer', 'Congratulation, you got it!')
                            image_sixth()

        elif (entry == 'FROG'):
                                tkinter.messagebox.showinfo('Answer', 'Congratulation, you got it!')


        elif (turns == 0):
            tkinter.messagebox.showinfo('REMAINING GUESSES', 'YOU ARE OUT OF GUESSES')

        else:
            tkinter.messagebox.showinfo('Answer', 'You are wrong \n \n YOU HAVE LOST 1 GUESS IN 3')
            turns = turns - 1

#gui creation
window=Tk()
window.title("HANGMAN")
window.geometry('1080x720')
newword=Button(window,text='NEW WORD',activeforeground='RED',activebackground='BLACK')
newword.place(x=200,y=20)
Image1 = PhotoImage(file="F:\\CODES\\PYTHON\\HANGMAN\\ani images\\animated-dog-image-0240.gif")
Image2 = PhotoImage(file="F:\\CODES\\PYTHON\\HANGMAN\\ani images\\squirrel.gif")
Image3 = PhotoImage(file="F:\\CODES\\PYTHON\\HANGMAN\\ani images\\horse.gif")
Image4 = PhotoImage(file="F:\\CODES\\PYTHON\\HANGMAN\\ani images\\wolf.gif")
Image5 = PhotoImage(file="F:\\CODES\\PYTHON\\HANGMAN\\ani images\\rooster.gif")
Image6 = PhotoImage(file="F:\\CODES\\PYTHON\\HANGMAN\\ani images\\frog.gif")
canvas = Canvas(window, height=0, width=0)
canvas.pack()
background = PhotoImage(file="F:\\CODES\\PYTHON\\HANGMAN\\ani images\\white.gif")
label_background = Label(window, image=background)
label_background.place(relwidth=1, relheight=1)
frame1 = Frame(window, bg='#0a202b', bd=10)
frame1.place(relx=0.5, rely=0.05, relwidth=0.85, relheight=0.7, anchor='n')
label = Label(frame1)
label.place(relwidth=1, relheight=1)
frame2 = Frame(window, bg='#0a202b', bd=10)
frame2.place(relx=0.5, rely=0.8, relwidth=0.85, relheight=0.15, anchor='n')
entry = Entry(frame2, font=40)
entry.place(relwidth=0.6, relheight=1)
button = Button(frame2, text="OK", font=12, bg='grey', command=lambda: check(entry.get()))
button.place(relx=0.65, relwidth=0.35, relheight=1)
image_start()
title = Label(window, text="Welcome To the HANGMAN Game", font=120, bg='white')
title.place(relx=0.5, rely=0.1, relwidth=0.6, relheight=0.05, anchor='n')
info = Button(window, text="Click here for instruction", font=100, bg='grey', command=instruction)
info.place( x=-200, y=0, relx=0.5, rely=0.65, relwidth=0.2, relheight=0.05, anchor='n')
newword = Button(window, text="NEWWORD", font=100, bg='grey', command=image_three)
newword.place( x=200, y=0, relx=0.5, rely=0.65, relwidth=0.2, relheight=0.05, anchor='n')
#keyboard
A = Button(window, text="A", font=100, bg='grey', command=lambda: set_text_A('A'))
A.place( x=900, y=200)
B = Button(window, text="B", font=100, bg='grey', command=lambda: set_text_B('B'))
B.place( x=940, y=200)
C = Button(window, text="C", font=100, bg='grey', command=lambda: set_text_C('C'))
C.place( x=980, y=200)
D = Button(window, text="D", font=100, bg='grey', command=lambda: set_text_D('D'))
D.place( x=1020, y=200)
E = Button(window, text="E", font=100, bg='grey', command=lambda: set_text_E('E'))
E.place( x=1060, y=200)
F = Button(window, text="F", font=100, bg='grey', command=lambda: set_text_F('F'))
F.place( x=1100, y=200)
G = Button(window, text="G", font=100, bg='grey', command=lambda: set_text_G('G'))
G.place( x=1140, y=200)
H = Button(window, text="H", font=100, bg='grey', command=lambda: set_text_H('H'))
H.place( x=1180, y=200)
I = Button(window, text="I", font=100, bg='grey', command=lambda: set_text_I('I'))
I.place( x=1220, y=200)
J = Button(window, text="J", font=100, bg='grey', command=lambda: set_text_J('J'))
J.place( x=1260, y=200)
K = Button(window, text="K", font=100, bg='grey', command=lambda: set_text_K('K'))
K.place( x=1300, y=200)
L = Button(window, text="L", font=100, bg='grey', command=lambda: set_text_L('L'))
L.place( x=940, y=260)
M = Button(window, text="M", font=100, bg='grey', command=lambda: set_text_M('M'))
M.place( x=980, y=260)
N = Button(window, text="N", font=100, bg='grey', command=lambda: set_text_N('N'))
N.place( x=1020, y=260)
O = Button(window, text="O", font=100, bg='grey', command=lambda: set_text_O('O'))
O.place( x=1060, y=260)
P = Button(window, text="P", font=100, bg='grey', command=lambda: set_text_P('P'))
P.place( x=1100, y=260)
Q = Button(window, text="Q", font=100, bg='grey', command=lambda: set_text_Q('Q'))
Q.place( x=1140, y=260)
R = Button(window, text="R", font=100, bg='grey', command=lambda: set_text_R('R'))
R.place( x=1180, y=260)
S = Button(window, text="S", font=100, bg='grey', command=lambda: set_text_S('S'))
S.place( x=1220, y=260)
T = Button(window, text="T", font=100, bg='grey', command=lambda: set_text_T('T'))
T.place( x=1260, y=260)
U = Button(window, text="U", font=100, bg='grey', command=lambda: set_text_U('U'))
U.place( x=1000, y=320)
V = Button(window, text="V", font=100, bg='grey', command=lambda: set_text_V('V'))
V.place( x=1040, y=320)
W = Button(window, text="W", font=100, bg='grey', command=lambda: set_text_W('W'))
W.place( x=1080, y=320)
X = Button(window, text="X", font=100, bg='grey', command=lambda: set_text_X('X'))
X.place( x=1120, y=320)
Y = Button(window, text="Y", font=100, bg='grey', command=lambda: set_text_Y('Y'))
Y.place( x=1160, y=320)
Z = Button(window, text="Z", font=100, bg='grey', command=lambda: set_text_Z('Z'))
Z.place( x=1200, y=320)
clear_button = Button(window, text="Clear", font=12, bg='grey', command=clear_text)
clear_button.place(x=1085, y=380)


window.mainloop()
