import string
text = "!INF( w (!J!"
word = ""
"""for ch in text:
    for letter in string.ascii_letters:
        if ch == letter:
            word = word + ch
        elif ch == "":
        	word = word + ch"""
for ch in text:
        for letter in string.punctuation:
            if ch != letter:
                word = word + ch
print(word)
 
input()