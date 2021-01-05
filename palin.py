word = list(input())
word_reverse = list(reversed(word))
print(word)
print(word_reverse)      
if word == word_reverse:
    print("Palindrome")
else:
    print("Not palindrome")