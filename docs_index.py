from pathlib import Path

P = Path("NuMojo/docs/docs")

d = dict()

for i in P.rglob("*.md"):
    if i.name != "index.md":
        plist= str(i).split("/")[3:]
        if len(plist)==2:
            if plist[0] in d.keys():
                d[plist[0]]+=[plist[1]]
            else:
                d[plist[0]]=[plist[1]]
        if len(plist)==3:
            if plist[0] in d.keys():
                if plist[1] in d[plist[0]].keys():
                    d[plist[0]][plist[1]]+=[plist[2]]
                else:
                    d[plist[0]][plist[1]]=[plist[2]]
            else:
                d[plist[0]][plist[1]]=[plist[2]]
print(d)