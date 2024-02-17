"""
Name: Romain Donfack Dzeinse
Date: 2/16/24
Objective: Recommend a song from a spotify playlist
"""
import random
# Note to self
"""
Characters that look like this \u001b[40m are called ANSI escape codes and they originate from the colors you see when 
coding on terminal or the gl server

Change word color:
    black = "\u001b[30m"
    red = "\u001b[31m"
    green = "\u001b[32m"
    yellow = "\u001b[33m"
    blue = "\u001b[34m"
    magenta = "\u001b[35m"
    cyan = "\u001b[36m"

Change word highlighting:
    black = "\u001b[40m"
    red = "\u001b[41m"
    green = "\u001b[42m"
    yellow = "\u001b[43m"
    blue = "\u001b[44m"
    magenta = "\u001b[45m"
    cyan = "\u001b[46m"
    white = "\u001b[47m"
Back to original:
    Make sure to put this after every text 
    color change and background color change
    - \033[0m
"""
song_playlist_dict = [
    ["Imagine Dragons", "On top of the World"],
    ["Coldplay", "Viva La Vida"],
    ["Imagine Dragons", "Bones"],
    ["Coldplay and Chainsmokers", "Somthing just like this"],
    ["Imagine Dragons", "Enemy"],
    ["Coldplay", "Yellow"],
    ["Imagine Dragons", "Follow You"],
    ["Coldplay", "Fix You"],
    ["OneRepublic", "Counting Stars"],
    ["Twenty One Pilots", "Stressed Out"],
    ["Adam Levine and R. City", "Locked Away"],
    ["Twenty One Pilots", "Ride"],
    ["OneRepublic", "I Ain't Worried"],
    ["Fall Out Boy", "Centuries"],
    ["Jason Goodman", "Pompeii"],
]
print("\tYour Spotify Imagine Dragging These Nuts Playlist")
print()
# Just printing the songs and the artist in a boring way
# for i in range(len(song_playlist_dict)):
#     print("|", end="")
#     for j in range(len(song_playlist_dict[i])):
#         artist_or_song = "Artist"
#         if j == 0:
#             print(f"{artist_or_song}: " + song_playlist_dict[i][j], end="\t")
#         else:
#             artist_or_song = "Song"
#             print(f"{artist_or_song}: " + song_playlist_dict[i][j], end="")
#
#     print("|")
# print()
# print()
# print()
# Much more formatted playlist
my_max = 60
spaces = " "
for i in range(len(song_playlist_dict)):
    a, s = "\033[94mArtist\033[0m", "\033[92mSong\033[0m"
    for j in range(len(song_playlist_dict)):
        if j < 1:
            remainder = my_max - len(song_playlist_dict[i][j]) - len(song_playlist_dict[i][j+1])
            if remainder <= my_max:
                print(f"\033[1m{song_playlist_dict[i][j]}{spaces * (remainder-1)}{song_playlist_dict[i][j + 1]}")
            else:
                word = song_playlist_dict[i][j + 1]
                first = len(song_playlist_dict[i][j])
                total = my_max - first
                print(f"{song_playlist_dict[i][j]} {word[0:total]}")
            print(f"⬛{a}⬛\t\t\t\t\t\t\t\t\t\t\t⬛{s}⬛")
    print()

random_songs = []
for i in range(len(song_playlist_dict)):
    random_songs.append(song_playlist_dict[i][1])
shuffle = random.choice(random_songs)
for i, element in enumerate(random_songs):
    if shuffle == element:
        indices = i
print(f"\u001b[40mYour recommended song is \033[94m{song_playlist_dict[indices][1]}\033[0m\u001b[40m by"
      f" \033[92m{song_playlist_dict[indices][0]}\033[0m")



