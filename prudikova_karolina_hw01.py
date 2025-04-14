import json

with open("alice.txt", mode="r", encoding="utf-8") as file:
    text = file.read()

text = text.lower()

frequency = dict()

for character in text:
    if character not in (' ', '\n'):
        if character in frequency:
            frequency[character] += 1
        else:
            frequency[character] = 1

frequency = dict(sorted(frequency.items()))

with open("hw01_output.json", mode="w", encoding="utf-8") as output:
    json.dump(frequency, output, ensure_ascii=False, indent=4)