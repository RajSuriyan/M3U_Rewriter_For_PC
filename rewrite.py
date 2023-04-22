import re
import os


def modify(filename):
    
    with open(filename,'r',encoding="utf-8") as f:
        s=f.readlines()

        top="#EXTM3U\n"
        s=s[1:]
        lines=[]
        for i in s:
            match=re.findall(r"/Music.*",i)
            for j,a in enumerate(match):
                match[j]=".."+match[j]+"\n"        
            lines.extend(match)
        lines.insert(0,top)
    with open(filename,"w",encoding="utf-8") as f:
        f.writelines(lines)
        
l=os.listdir()
for i in l:
    if ".txt" in i:
        modify(i)

