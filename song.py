import time
import sys

def type_lyrics(line, char_delay=0.085):
    for char in line:
        print(char, end="", flush=True)
        time.sleep(char_delay)
    print()  

def print_lyrics():
    lyrics = [
        "Wherever you go, that's where I'll follow",
        "Nobody's promised tomorrow",
        "So I'ma love you every night like it's the last night",
        "Like it's the last night",
        "If the world was ending, I'd wanna be next to you",
        "If the party was over and our time on Earth was through",
        "I'd wanna hold you just for a while and die with a smile",
        "If the world was ending, I'd wanna be next to you"
    ]


    delays = [1.8, 1.7, 2.0, 2.3, 2.4, 2.2, 2.5, 3.0]

    print("Now playing: If The World Was Ending\n")
    time.sleep(1.8)

    for i, line in enumerate(lyrics):
        type_lyrics(line)
        if i < len(delays):
            time.sleep(delays[i])

print_lyrics()
