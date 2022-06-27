import random
import time
f=open("note.txt","r")
words=[]
for line in f:
   w=line.split('\n')
   words.append(w[0])
score=0
start = time.time()
while time.time() - start < 60:
#while True:
        r=random.choice(words)
        print(r)
        inp=input()
        if(inp==r):
           score=score+1
        else:
           continue
print(score)
f.close()