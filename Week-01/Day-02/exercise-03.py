word = input("Enter a word: ")

a = word[0]
b = word[-1]
c = word[:3]
d = word[-3:]
length= len(word)

print(f"First letter: {a}")
print(f"Last letter: {b}")
print(f"First three letters: {c}")
print(f"Last three letters: {d}")
print(f"Total length: {length}")