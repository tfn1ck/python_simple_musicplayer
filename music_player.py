import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os


class Musicplayer:

    def __init__(self):
        self.music_player = tkr.Tk()
        self.music_player.title("Python_Music_Player")
        self.music_player.geometry("480x380")
        self.directory = askdirectory()
        os.chdir(self.directory)
        self.song_list = os.listdir(self.directory)

    def play(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(self.song_list[self.play_list.curselection()[0]])
        self.var.set(self.song_list[self.play_list.curselection()[0]])
        pygame.mixer.music.play()

    def stop(self):
        pygame.mixer.music.stop()

    def pause(self):
        pygame.mixer.music.pause()

    def unpause(self):
        pygame.mixer.music.unpause()

    def button(self):
        self.Button1 = tkr.Button(self.music_player, width=5, height=3, font="Helvetica 12 bold", text="PLAY",
                                  command=self.play, bg="blue", fg="white")
        self.Button2 = tkr.Button(self.music_player, width=5, height=3, font="Helvetica 12 bold", text="STOP",
                                  command=self.stop, bg="red", fg="white")
        self.Button3 = tkr.Button(self.music_player, width=5, height=3, font="Helvetica 12 bold", text="PAUSE",
                                  command=self.pause, bg="purple", fg="white")
        self.Button4 = tkr.Button(self.music_player, width=5, height=3, font="Helvetica 12 bold", text="UNPAUSE",
                                  command=self.unpause, bg="orange", fg="white")

    def run(self):
        self.var = tkr.StringVar()
        song_title = tkr.Label(self.music_player, font="Helvetica 12 bold", textvariable=self.var)
        song_title.pack()
        self.button()
        self.Button1.pack(fill="x")
        self.Button2.pack(fill="x")
        self.Button3.pack(fill="x")
        self.Button4.pack(fill="x")
        self.play_list = tkr.Listbox(self.music_player, font="helvetica 12 bold", bg="black", selectmode=tkr.SINGLE)
        for item in self.song_list:
            self.play_list.insert(tkr.END, item)
        self.play_list.pack(fill="both", expand="yes")

        self.music_player.mainloop()


if __name__ == "__main__":
    mp = Musicplayer()
    mp.run()
