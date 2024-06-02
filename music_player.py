import os
import random
import simpleaudio as sa
import tkinter as tk
import keyboard
import threading

def play_song(song_name):
    song = sa.WaveObject.from_wave_file(song_name)
    play_song = song.play()

def start_playing():
    selected_song = song_listbox.get(tk.ACTIVE)
    threading.Thread(target=play_song, args=(selected_song,)).start()

def stop_playing():
    sa.stop_all()

def play_random_song():
    random_song = random.choice(songs)
    threading.Thread(target=play_song, args=(random_song,)).start()

songs = []

window = tk.Tk()
window.title("Naoise's totally bitchin music player")
window.geometry("600x400")
window.configure(bg='green')
window.eval('tk::PlaceWindow . center')

Label = tk.Label(window, text = "Hello Naoise")
Label.pack()


# listbox to display the songs
song_listbox = tk.Listbox(window, bg='white', fg='black', font=('Arial', 12))
song_listbox.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

# scrollbar
scrollbar = tk.Scrollbar(song_listbox)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
song_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=song_listbox.yview)

# loop through wav files in dir and add them to the song list
for song in os.listdir():
    if song.endswith('.wav'):
        songs.append(song)
        song_listbox.insert(tk.END, song)

# play selected song
play_button = tk.Button(window, text="Play Song", command=lambda: [stop_playing(), start_playing()], bg='blue', fg='white', font=('Arial', 12))
play_button.pack(pady=10)

# stop selected song
stop_button = tk.Button(window, text="Stop Song", command=stop_playing, bg='red', fg='white', font=('Arial', 12))
stop_button.pack(pady=10)

# play a random song
random_button = tk.Button(window, text="Play Random Song", command=lambda: [stop_playing(), play_random_song()], bg='orange', fg='white', font=('Arial', 12))
random_button.pack(pady=10)



window.mainloop()