import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("500x400")

        # Initialize Pygame mixer
        pygame.mixer.init()

        # Track variables
        self.playlist = []
        self.current_track = 0
        self.playing = False  # Track whether music is currently playing or paused

        # Create GUI components
        self.create_gui()

    def create_gui(self):
        # Playlist box
        self.playlistbox = tk.Listbox(self.root, selectmode=tk.SINGLE, bg="lightgray", selectbackground="darkgray")
        self.playlistbox.pack(pady=10)

        # Buttons
        btn_load = tk.Button(self.root, text="Load", command=self.load_music, width=10, bg="#4CAF50", fg="white")
        btn_load.pack(pady=5)

        self.btn_play_pause = tk.Button(self.root, text="Play", command=self.toggle_play_pause, width=10, bg="#2196F3", fg="white")
        self.btn_play_pause.pack(pady=5)

        btn_stop = tk.Button(self.root, text="Stop", command=self.stop_music, width=10, bg="#F44336", fg="white")
        btn_stop.pack(pady=5)

        btn_prev = tk.Button(self.root, text="Previous", command=self.prev_track, width=10, bg="#FFC107", fg="white")
        btn_prev.pack(pady=5)

        btn_next = tk.Button(self.root, text="Next", command=self.next_track, width=10, bg="#FF9800", fg="white")
        btn_next.pack(pady=5)

    def load_music(self):
        file_path = filedialog.askopenfilename(defaultextension=".mp3", filetypes=[("Music Files", "*.mp3")])
        if file_path:
            self.playlist.append(file_path)
            self.playlistbox.insert(tk.END, file_path)

    def toggle_play_pause(self):
        if self.playlist:
            if not self.playing:
                pygame.mixer.music.load(self.playlist[self.current_track])
                pygame.mixer.music.play()
                self.btn_play_pause.config(text="Pause", bg="#CDB79E")
            else:
                pygame.mixer.music.pause()
                self.btn_play_pause.config(text="Play", bg="#2196F3")
            self.playing = not self.playing

    def stop_music(self):
        pygame.mixer.music.stop()
        self.playing = False
        self.btn_play_pause.config(text="Play", bg="#2196F3")

    def prev_track(self):
        if len(self.playlist) > 1:
            self.current_track = (self.current_track - 1) % len(self.playlist)
            pygame.mixer.music.load(self.playlist[self.current_track])
            pygame.mixer.music.play()

    def next_track(self):
        if len(self.playlist) > 1:
            self.current_track = (self.current_track + 1) % len(self.playlist)
            pygame.mixer.music.load(self.playlist[self.current_track])
            pygame.mixer.music.play()

if __name__ == "__main__":
    root = tk.Tk()
    music_player = MusicPlayer(root)
    root.mainloop()
