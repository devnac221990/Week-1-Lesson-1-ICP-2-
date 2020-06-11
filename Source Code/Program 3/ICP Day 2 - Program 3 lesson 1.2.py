def capitalize(word):
    if word.isalpha():
        word=word.lower()
        word=word[0].upper() + word[1:]
    return word
wordcount=dict()
file = open('D:\python100.txt','r')
lines = file.readlines()
file.close()
filteredtext=''
for line in lines:
    if line!='\n':
        filteredtext+=(line.replace('\n',''))

print(filteredtext)

filteredtext = filteredtext.split(' ')
for word in filteredtext:
    capitalized=capitalize(word)
    if capitalized in wordcount:
        wordcount[capitalized]+=1
    else:
        wordcount[capitalized]=1

print(wordcount)

writefile = open('writefile.txt', 'w')
for keys in wordcount:
    writefile.write("{}:{}".format(keys,wordcount[keys]))
writefile.close()