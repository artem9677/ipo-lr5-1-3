string  = open('text.txt','r',encoding='utf-8')
out = open('output.txt','w',encoding='utf-8')

i = 1

for line in string:
    out.write(str(i) + " ")
    out.write(line)
    i+=1

string.close()
out.close()
