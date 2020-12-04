import string
alphabet=string.ascii_letters
sentence=input("enter a sentence:")
count_letters={}
for letter in sentence:
    if letter in count_letters:
        count_letters[letter]+=1
    else:
        count_letters[letter]=1
print(len(count_letters))
if(len(count_letters)>=26):
    print("pangram")
else:
    print("not a pangram")
