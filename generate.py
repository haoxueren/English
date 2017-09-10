import os

input=open('C:/Users/Haoxueren/Desktop/WordBank/README.MD','w')
for file in os.listdir('C:/Users/Haoxueren/Desktop/WordBank/Words'):
    word=file[:-4]
    word_md='[%s](https://github.com/%s) | '%(word,word)
    input.write(word_md)
input.close()
print('Generate Completed...')
