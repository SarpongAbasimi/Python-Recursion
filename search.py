#Fuction takes two argument, a word and a letter if
#the letter is in the word , it will print the letter


def find(word,letter):
    loop=0
    while loop < len(word):
        for i in word[loop]:
            print i
            loop += 1
            if i == letter:
                print ('The letter Yu asked me to find was letter {}'.format(i))



find('name','a')
