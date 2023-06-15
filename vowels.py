sentence = input("Enter a sentence: ")
modified_sentence = ""

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

for char in sentence:
    if char in vowels:
        continue
    modified_sentence += char

print("Modified sentence:", modified_sentence)
