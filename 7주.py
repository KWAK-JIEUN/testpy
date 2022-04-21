f=open('mbox.txt')
fw=open(f'words.txt', 'w')


for line in f:
    line=line.strip()
    if line.startswith('From '):
        t=line.split()
        tt=t[1]+','+t[-1]
        print(tt)
        fw.write(tt)
        fw.write('\n')
        
fw.close()
f.close()
