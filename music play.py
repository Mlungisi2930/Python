from tkinter import *
import pygame
import os
import time 
from tkinter import filedialog
from pygame import mixer
pygame.mixer.init()
window = Tk()
window.config(bg="white")
window.title ("Mlungisi media player")
window.geometry("500x300")


song_listbox=Listbox(window,bg="blue",fg="green",width=60)
song_listbox.pack(pady=20)

def add_songs():
    song =filedialog.askopenfilename(initialdir="Playlist/",title="choose a song",filetypes=(("mp3 files","*.mp3"),))
    song_listbox.insert(END,song)
    song = song.replace("C:/Users/MORNING SESSION SDL5/Desktop/music_play/Playlist","r")
    song = song.replace(".mp3","")

def play_song():
    song= song_listbox.get(ACTIVE)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()
    

def stop():
    pygame.mixer.music.stop()
    

global paused
paused=False

def pause_song():
    if pause_btn["text"]  =="pause":
        mixer.music.pause()
        pause_btn["text"] = "play"
    else:
        mixer.music.unpause()
        pause_btn["text"] ="pause"
        
def pre_btn():
    previous- song_listbox.curselction()
    previous= previous [0] -1
    song=song_listbox.get(previous)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()
    song_listbox.selection_clear(0,END)
    song_listbox.activate(previous)
    song_listbox.selection_set(previous)

def next_btn():
    next= song_listbox.curselction()
    next= next [0] -1
    song=song_listbox.get(next)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()
    song_listbox.selection_clear(0,END)
    song_listbox.activate(next)
    song_listbox.selection_set(next)

def mute_music():
    global muted
    if muted:
        mixer.music.set-volume(0.7)
        volumebtn.configure()
        scale.set(70)
        muted=FALSE

    else:
        mixer.music.set_volume(0.7)
        volumebtn.configure()
        scale.set(0)
        muted=TRUE


play_btn_img=PhotoImage(file=r"C:/images/play.png")

next_btn_img=PhotoImage(file=r"C:/images/next.png")

pre_btn_img=PhotoImage(file=r"C:/images/pre.png")

pause_btn_img=PhotoImage(file=r"C:/images/pause.png")

stop_btn_img=PhotoImage(file=r"C:/images/stop.png")

Controls_frame = Frame(window)
Controls_frame.pack()

#button
play_btn=Button(Controls_frame,image=play_btn_img,borderwidth=0,padx=10,pady=10,command=play_song)
play_btn.grid(column=0,row=0)             
next_btn=Button(Controls_frame,image=next_btn_img,borderwidth=0,padx=10,pady=10, command=next_btn)
next_btn.grid(column=1,row=0,padx=10)
pre_btn=Button(Controls_frame,image=pre_btn_img,borderwidth=0,padx=10, command=pre_btn)
pre_btn.grid(column=2,row=0,padx=10)                
pause_btn=Button(Controls_frame,image=pause_btn_img,borderwidth=0,padx=10,pady=10, command=pause_song)
pause_btn.grid(column=3,row=0,padx=10)              
stop_btn=Button(Controls_frame,image=stop_btn_img,borderwidth=0,padx=10,pady=10, command=stop)
stop_btn.grid(column=4,row=0,pady=10)



my_menu=Menu(window)
window.config(menu= my_menu)

add_songs_menu=Menu(my_menu)
my_menu.add_cascade(label="add songs",menu= add_songs_menu)
add_songs_menu.add_command(label="add 1 song to playlist",command=add_songs)

scale = Scale(window, from_ =0, to =100, orient =HORIZONTAL, bg="green",width=5,length =360,)
scale.set(0)
scale.pack()

window.mainloop()




