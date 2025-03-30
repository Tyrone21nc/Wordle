"""
Author: Romain Donfack Dzeinse
Date: 1/20/24
Objective: Build a Wordscape type game
Inspiration: I play Wordscape on my phone and I like it
"""
import random

print("\t\t\t\t\tWelcome to WORDSCAPES")
print("Directions: ")
max_screen = 60  # The maximum length of a sentence across the screen can only be 60 characters
directions = "Win the game by guessing all the words with the associated letters"
print(directions)
# Below is to properly format the directions variable
# if len(directions) > max_screen:
#     print(directions[:max_screen-1] + "-")
#     print(directions[max_screen-1: (max_screen*2)-1])
print("Words used here are from www.wordunscrambler.net/")

all_words = {
    6: {
        "smoart": ["morats", "stroma", "stroam"],
        "rebato": ["Rebato", "boater", "borate"],
        "tchoir": ["rhotic", "thoric", "trochi"],
        "ghaire": ["hegari", "hegira", "hirage"],
        "bomsei": ["biomes", "mobies", "obeism"],
    },
    5: {
        # Will give two 2 letter hints
        # The print statement could look something like this
        # scrabble word: smoart   __o_s    m_r__    _t_o_   ...
        # Guess one of the words: atoms
        # atoms: correct a check mark or something
        # scrabble word: smoart   atoms    m_r__    _t_o_   ...
        # Guess one of the words: atoms
        # atoms already guessed
        # scrabble word: smoart   atoms    m_r__    _t_o_...
        # Guess one of the words:
        "smoart": ["atoms", "marts", "atmos", "amort", "morat", "smart", "storm", "romas", "roast", "trams"],
        "rebato": ["abore", "abort", "boart", "oater", "orate", "roate", "taber", "tabor"],
        "tchoir": ["chiro", "chirt", "choir", "crift", "ichor", "richt", "rotch", "torch", "toric"],
        "ghaire": ["gerah"],
        "bomsei": ["besom", "biome", "bisom", "bosie", "mebos", "mobes", "mobie"],
    },
    4: {
        # Will give two 2 letter hints
        "smoart": ["arms", "arts", "atom", "mars", "mart", "mast", "mats", "maot", "mort", "most",
                   "oars", "rams", "rats", "soma", "sort", "star", "taos", "tram", "tsar"],
        "rebato": ["aret", "bare", "bate", "bear", "beat", "beta", "boar", "boat", "boet", "bore", "bort", "brat",
                   "rate", "robe", "tear", "tore"],
        "tchoir": ["chit", "coth", "crit", "itch", "rich", "riot", "roch", "tich", "torc", "tori", "trio"],
        "ghaire": ["ager", "argh", "gair", "gare", "gari", "hair", "hare", "heir", "hire", "rage", "rhea"],
        "bomsei": ["bios", "bois", "emos", "mise", "mobe", "mobs", "mose", "obes", "obis", "semi", "some"],
    },
    3: {
        # Will give two 1 letter hints
        "smoart": ["arm", "art", "mas", "mat", "oar", "oat", "ors", "ram", "rat", "rom", "rot", "sat",
                   "tam", "tar", "tom"],
        "rebato": ["are", "art", "ate", "bar", "bat", "bet", "bot", "bra", "bro", "eat", "era", "oat",
                   "ora", "ore", "ort", "rat", "reo", "rob", "roe", "rot", "tab", "tar", "tea", "toe"],
        "tchoir": ["chi", "cot", "hit", "hot", "orc", "rot", "tic", "toc"],
        "ghaire": ["age", "air", "are", "ear", "era", "her", "ire", "rag", "rei", "rig"],
        "bomsei": ["bio", "boi", "emo", "ems", "ios", "ism", "mob", "obi", "obs", "sei", "sim", "sob"]
    }
}
print("\t\t\t\t\t", end="")
for i in all_words.keys():
    print(i, end="\t")
num_words = int(input("\nHow many words would you like: "))
all_words_keys = []
for i, element in enumerate(all_words):
    all_words_keys.append(element)
element = 6
while element > len(all_words_keys)-2 and element in all_words_keys:
    print(all_words[element].keys())
    element -= 1
print("cheese")
print("All keys of check board", all_words_keys)

if num_words in all_words.keys():
    print(all_words[num_words])
    # for j in range(0):
    #     print(all_words[num_words][j])
    #     # for element, value in enumerate(num_words):
    #     #     print(value, element, end="\t")








