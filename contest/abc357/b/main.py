s = input()

upperCase = 0
lowerCase = 0

for letter in s:
    if letter.isupper():
        upperCase += 1
    else:
        lowerCase += 1

if upperCase > lowerCase:
    print(s.upper())
else:
    print(s.lower())