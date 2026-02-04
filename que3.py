filename = "abc.txt"
with open(filename, "r") as file:
    text = file.read()
    words = text.split()
    word_count = len(words)
print("Total number of words:", word_count)
