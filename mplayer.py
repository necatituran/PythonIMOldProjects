import os   # import os
import pygame   # import pygame
import pygame.mixer
import tkinter as tkr   # import tkinter
# ask the user to select a directory
from tkinter.filedialog import askdirectory

musicplayer = tkr.Tk()  # create a window
musicplayer.title("Music Player")   # set the title of the window
musicplayer.geometry("450x350")  # set the size of the window
songlist = os.listdir()  # get the songs from the directory

playlist = tkr.Listbox(musicplayer, font="Helvetica 12 bold",   # create a playlist
                       bg="yellow", selectmode=tkr.SINGLE)  # create a playlist
for item in songlist:   # add the songs to the playlist
    pos = 0     # position of the song in the playlist
    # insert the song into the playlist
    playlist.insert(pos, item)
    pos = pos + 1                   # insert the song into the playlist

pygame.init()   # initialize pygame
pygame.mixer.init()  # initialize the mixer


def play():     # play the song
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))  # get the song title
    var.set(playlist.get(tkr.ACTIVE))   # get the song title
    pygame.mixer.music.play()  # play the song


def ExitMusicPlayer():  # exit the music player
    pygame.mixer.music.stop()   # stop the music


def Pause():    # pause the music
    pygame.mixer.music.pause()  # pause the music


def Unpause():  # unpause the music
    pygame.mixer.music.unpause()    # unpause the music


Button1 = tkr.Button(musicplayer, width=5, height=3, font="Helvetica 12 bold",
                     text="PLAY", command=play, bg="red", fg="white")  # create a button to play the song
# Button2 = tkr.Button(musicplayer, width=5, height=3, font="Helvetica 12 bold",
#                      text="STOP", command=stop, bg="red", fg="white")
# Button3 = tkr.Button(musicplayer, width=5, height=3, font="Helvetica 12 bold",
#                      text="PAUSE", command=pause, bg="purple", fg="white")
# Button4 = tkr.Button(musicplayer, width=5, height=3, font="Helvetica 12 bold",
#                      text="UNPAUSE", command=unpause, bg="orange", fg="white")
Button2 = tkr.Button(musicplayer, width=5, height=3, font="Helvetica 12 bold",
                     text="STOP", command=ExitMusicPlayer, bg="red", fg="white")
Button3 = tkr.Button(musicplayer, width=5, height=3, font="Helvetica 12 bold",
                     text="PAUSE", command=Pause, bg="purple", fg="white")
Button4 = tkr.Button(musicplayer, width=5, height=3, font="Helvetica 12 bold",
                     text="UNPAUSE", command=Unpause, bg="orange", fg="white")
Button5 = tkr.Button(musicplayer, width=5, height=3, font="Helvetica 12 bold",
                     text="Choose File", command=askdirectory, bg="green", fg="white")

var = tkr.StringVar()
song_title = tkr.Label(
    musicplayer, font="Helvetica 12 bold", textvariable=var)


song_title.pack()
Button1.pack(fill="x")
Button2.pack(fill="x")
Button3.pack(fill="x")
Button4.pack(fill="x")
Button5.pack(fill="x")
playlist.pack(fill="both", expand="yes")
musicplayer.mainloop()
