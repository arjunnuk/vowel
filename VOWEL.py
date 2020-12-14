dict={'vowels':0,'letters':0,'pervowels':0}
word=input("enter a word")
for x in word:
    dict['letters']+=1
    if x in 'aeiou' or x in 'AEIOU':
        dict['vowels']+=1
dict['pervowels']=(dict['vowels']*100//dict['letters'])
print("the number of vowels=",dict['vowels'])
print("the number of letters=",dict['letters'])
print("percentage of vowels=",dict['pervowels'])
print("arjun uk")
