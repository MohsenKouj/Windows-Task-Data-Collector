def create_cpath(path):
    with open("current_path.idd","w") as cpath:
        cpath.write(path)
def finderonespace(lines):
    print(".... ....>> finderOneSpace :: processing words")
    
    newLines = []
    for item in lines:
        for vidx in range(len(item)):
            if item[vidx] == " " and vidx > 0 and vidx < len(item)-1:
                #print(item[vidx-1], item[vidx], item[vidx+1],"\n")
                if(item[vidx-1] != " " and item[vidx+1] != " "):
                    il = list(item)
                    il[vidx] = "%"
                    item = "".join(il)
                    
        newLines.append(item)
    print(".... ....>> finderOneSpace :: complete")
    return newLines

print("....>> define completeword function")
def completeWord(lines):
    print(".... ....>> completeword :: processing words")
    end = 0
    newLines = []
    
    for item in lines:
        for vidx in range(len(item)):
            if item[vidx] == " " and vidx > 0 and vidx < len(item)-1:
                if item[vidx+1] == " ":
                    break
                else:
                    il = list(item)
                    il[vidx] = "!"
                    item = "".join(il)
                
        newLines.append(item)
    print(".... ....>> completeword :: complete")
    return newLines

print("....>> define split function")
def split(lines):
    print(".... ....>> split :: processing lines")
    
    first = []
    second = []
    for i in lines[:-3]:
        print(i)
        a,b = i.split("%")
        first.append(a)
        second.append(b)
        print(a)
        
    print(".... ....>> split :: complete")
    return first, second

print("....>> define hover_spaces function")
def Hover_spaces(lines):
    print(".... ....>> hover_spaces :: processing words")
    
    bul = False
    lis = []
    for line in lines:
        for let in line:
            let_idx = line.index(let)
            if let == " " and let_idx > 0 and let_idx < len(line):
                if line[let_idx-1] == ' ' and line[let_idx+1] == ' ':
                    if not bul:
                        il = list(line)
                        il[let_idx] = "&"
                        line = "".join(il)
                        bul = True
                else:
                    bul = False
        lis.append(line)
    print(".... ....>> hover_spaces :: complete")
    return lis
print("....>> define division_into_Two_Part function")   
def Division_into_Two_Part(lines2):
    print(".... ....>> division_into_Two_Part :: processing lists")
    newList1 = []
    newList2 = []
    i = 0
    for line in lines2:
        try:
            #print(line)
            #input()
            l1,l2 = line.split("%")
            
            newList1.append(l1)
            newList2.append(l2)
        except:
            print("Amplitude:"+str(i))
            i += 1
    print(".... ....>> division_into_Two_Part :: complete")
    return newList1, newList2

def wordS(lines):
        newLines = []
        for line in lines:
            vidx = 0
            for let in line:
                if let == "!":
                    il = list(line)
                    il[vidx] = " "
                    line = "".join(il)
                vidx += 1
            newLines.append(line)
        return newLines
  