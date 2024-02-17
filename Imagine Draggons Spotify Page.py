"""
Name: Romain Donfack Dzeinse
Date: 2/17/24
Objective: Attempt to Duplicate my Imagine Dragons Spotify Page
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

print("\033[1;32m▶\033[0m",end="")
# print("\u001b[42m     \033[0m")
# print("\u001b[42m \033[0;32m\u001b[40m|\\\u001b[42m   \033[0m")
# print("\u001b[42m \033[0;32m\u001b[40m| \\\u001b[42m   \033[0m     \033[0;32m\u001b[40m-→\033[0m    \033[0;32m\u001b[40m———\033[0m")
# print("\u001b[42m \033[0;32m\u001b[40m|  |\u001b[42m   \033[0m    \033[0;32m\u001b[40m←-\033[0m    \033[0;32m\u001b[40m|↓|\033[0m")
# print("\u001b[42m \033[0;32m\u001b[40m| /\u001b[42m   \033[0m           \033[0;32m\u001b[40m———\033[0m")
# print("\u001b[42m \033[0;32m\u001b[40m|/\u001b[42m   \033[0m")
# print("\u001b[42m     \033[0m")
print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t🔍\033[0;37mSEARCH\033[0m")
print()
print()
# print(len("Title                    "))
my_max = 25
print("\033[0;31m#\033[0m \033[0;34mTitle\033[0m                      \033[1;32mAlbum\033[0m                    \033[1;35mDate added\033[0m                    🕘")
for i in range(len(song_playlist_dict)):
    print(f"\033[0;31m{i+1}\033[0m ", end="")
    for j in range(len(song_playlist_dict[i])):
        artist_or_song = "Artist"
        if j == 0:
            remainder = my_max - len(artist_or_song) - len(song_playlist_dict[i][j])
            total = len(artist_or_song) + len(song_playlist_dict[i][j])
            if total <= my_max:
                print(f"\033[0;34m{artist_or_song}: {song_playlist_dict[i][j]}\033[0m" + str(" " * remainder) + "\033[1;32mEmpty\033[0m" + "\t\t\t\t\t\033[1;35mJune 30, 2023\033[0m" + "\t\t\t\t\t\033[1;36m4:02\033[0m")
            else:
                word = song_playlist_dict[i][j]
                first = len(song_playlist_dict[i][j])
                total = my_max - first
                print(f"\033[0;34m{artist_or_song}: {word[0:total-15]}...\033[0m" + str(" " * 6) + "\033[1;32mEmpty\033[0m" + "\t\t\t\t\t\033[1;35mJune 30, 2023\033[0m" + "\t\t\t\t\t\033[1;36m3:48\033[0m")
        else:
            artist_or_song = "Song"
            # print(f"  {artist_or_song}: " + song_playlist_dict[i][j], end="")
            remainder = my_max - len(artist_or_song) - len(song_playlist_dict[i][j])
            total = len(artist_or_song) + len(song_playlist_dict[i][j])
            if total <= my_max:
                print(f"  \033[0;34m{artist_or_song}: {song_playlist_dict[i][j]}\033[0m" + str(" " * remainder))
            else:
                word = song_playlist_dict[i][j]
                first = len(song_playlist_dict[i][j])
                total = my_max - first
                print(f"  \033[0;34m{artist_or_song}: {word[0:total-12]}...\033[0m")
    print()
