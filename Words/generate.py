import os

for file in os.listdir('C:/Users/Haoxueren/Desktop/WordBank/Words'):
    word=file[:-4]
    word_md='[%s](https://github.com/%s)'%(word,word)
    file=open('')
    print(word_md)
