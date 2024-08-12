from tkinter import *
from tkinter import messagebox
import random

players = ["X", "O"]
papan = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
turn = None
player = None

def play():
    global window
    global player
    global papan
    global turn
    window_width = 500
    window_height = 600
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))
    window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))
    window.resizable(False, False)
    judul.destroy()
    play_btn.destroy()
    quit_btn.destroy()

    player = random.choice(players)

    turn = Label(window, font=("Consolas", 25, "bold"), text="GILIRAN: "+player, fg="white", bg="#1c4766")
    turn.pack(side=TOP, pady=15)

    frame = Frame(window)
    frame.pack()

    for row in range(3):
        for column in range(3):
            papan[row][column] = Button(frame, text="", font=("Arial", 25, "bold"), width=7, height=3,
                                        command=lambda row=row, column=column: next_turn(row, column))
            papan[row][column].grid(row=row, column=column)

    restart_btn = Button(window, font=("Arial", 20, "bold"), text="RESTART", fg="#1c4766", activeforeground="#1c4766", command=new_game)
    restart_btn.pack(side=BOTTOM, pady=15)

def next_turn(row, column):
    global player
    global papan
    global turn
    if papan[row][column]['text'] == "" and check_winner() is False:
        if player == players[0]:
            papan[row][column]['text'] = player
            papan[row][column].config(fg="red")
            if check_winner() is False:
                player = players[1]
                turn.config(text=("GILIRAN: "+player))
                
            elif check_winner() is True:
                turn.config(text=(player+" MENANG"), fg="#00ff40")
                
            elif check_winner() == "SERI":
                turn.config(text="SERI", fg="yellow")
        else:
            papan[row][column]['text'] = player
            papan[row][column].config(fg="#103e75")
            if check_winner() is False:
                player = players[0]
                turn.config(text=("GILIRAN: "+player))
                
            elif check_winner() is True:
                turn.config(text=(player+" MENANG"), fg="#00ff40")
                
            elif check_winner() == "SERI":
                turn.config(text="SERI", fg="yellow")

def check_winner():
    global player
    global papan
    global turn
    for row in range(3):
        if papan[row][0]['text'] == papan[row][1]['text'] == papan[row][2]['text'] != "":
            papan[row][0].config(bg="#00ff40")
            papan[row][1].config(bg="#00ff40")
            papan[row][2].config(bg="#00ff40")
            return True

    for column in range(3):
        if papan[0][column]['text'] == papan[1][column]['text'] == papan[2][column]['text'] != "":
            papan[0][column].config(bg="#00ff40")
            papan[1][column].config(bg="#00ff40")
            papan[2][column].config(bg="#00ff40")
            return True
        
    if papan[0][0]['text'] == papan[1][1]['text'] == papan[2][2]['text'] != "":
        papan[0][0].config(bg="#00ff40")
        papan[1][1].config(bg="#00ff40")
        papan[2][2].config(bg="#00ff40")
        return True
    
    if papan[0][2]['text'] == papan[1][1]['text'] == papan[2][0]['text'] != "":
        papan[0][2].config(bg="#00ff40")
        papan[1][1].config(bg="#00ff40")
        papan[2][0].config(bg="#00ff40")
        return True
    
    elif empty_space() is False:
        for row in range(3):
            for column in range(3):
                papan[row][column].config(bg="yellow")
        return "SERI"
    
    else:
        return False
    
def empty_space():
    global player
    global papan
    global turn
    spaces = 9
    for row in range(3):
        for column in range(3):
            if papan[row][column]['text'] != "":
                spaces-=1
                
    if spaces == 0:
        return False
    else:
        return True
         
def new_game():
    global player
    global papan
    global turn
    global player
    player = random.choice(players)
    
    turn.config(text=("GILIRAN: "+player), fg="white")
    for row in range(3):
        for column in range(3):
            papan[row][column].config(text="", bg="white")

def quit():
    if messagebox.askyesno(title="KONFIRMASI", message="Apakah anda yakin ingin keluar?"):
        window.destroy()

window = Tk()
window.title("Tic Tac Toe")

icon_window = PhotoImage(file="Gambar\\x.png")
window.iconphoto(True, icon_window)
window.config(background="#1c4766")

window_width = 600
window_height = 400
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))
window.resizable(False, False)

title_menu = "████████╗██╗ ██████╗    ████████╗ █████╗  ██████╗    ████████╗ ██████╗ ███████╗\n╚══██╔══╝██║██╔════╝    ╚══██╔══╝██╔══██╗██╔════╝    ╚══██╔══╝██╔═══██╗██╔════╝\n ██║   ██║██║            ██║   ███████║██║            ██║   ██║   ██║█████╗\n   ██║   ██║██║            ██║   ██╔══██║██║            ██║   ██║   ██║██╔══╝  \n   ██║   ██║╚██████╗       ██║   ██║  ██║╚██████╗       ██║   ╚██████╔╝███████╗\n   ╚═╝   ╚═╝ ╚═════╝       ╚═╝   ╚═╝  ╚═╝ ╚═════╝       ╚═╝    ╚═════╝ ╚══════╝"

judul = Label(window, font=("Consolas", 10), text=title_menu, fg="white", bg="#1c4766")
judul.pack(pady=35)

play_btn = Button(window, text="PLAY", command=play, font=("Arial", 25, "bold"), width=9, fg="#1c4766", activeforeground="#1c4766")
play_btn.pack(pady=20)

quit_btn = Button(window, text="QUIT", command=quit, font=("Arial", 25, "bold"), width=9, fg="#1c4766", activeforeground="#1c4766")
quit_btn.pack(pady=20)

window.mainloop()