import json

content_output = open("train_contents.txt",'w',encoding='utf-8')
label_output = open("train_labels.txt",'w',encoding='utf-8')


data = open('news.txt',encoding='utf-8')

for line in data:
    s = json.loads(line)
    category = str(s["category"])
    content = str(s["content"])
    label_output.write(category + '\n')
    content_output.write(content + '\n')

label_output.close()
content_output.close()
