import os
import csv                                                               # import csv
from pathlib import Path                                                 # path from pathlib
import sys                                                               # import sys
from Alloc import *                                                      # import Alloc


  
def main():                                                              # main function
    os.system("tasklist > Tasks-clu1.idd")                               # tasklist into Task-clu2.idd
    if getattr(sys,"frozen", False):                                     
        sci = os.path.dirname(sys.executable)                            # get path when app is executable
    else:
        sci = os.path.dirname(__file__)                                  # get path normaly app
    
    do = True
    
    taskstring = ""
    try:
        with open("Tasks-clu1.idd")as filetask:                          # read tasks file
            taskstring = filetask.read()
    except:
        print("\n+---------------------------------+\n| Cannot connect to the input data document\n+---------------------------------+\n")
    
    print("separating words to lines ...")                               
    lines = list(taskstring.split("K\n"))                                # split lines
    print("cleaning tasks ...")
    vm, task = lines[0].split("=\n")                                     # split tasks
    lines[0] = task
    print("call functions ...")

    lines1 = completeWord(lines)                                         # use complete-word
    lines2 = finderonespace(lines1)                                      # use finder-one-space

    lines3_1,lines3_2 = Division_into_Two_Part(lines2)                   # use divid-into-two-parts

    print("cleaning data lines4_1 ...")
    lines4_1 = []
    lines4_2 = []
    bull = False
    for line in lines3_1:                                                # left side tasks
        vidx = 0                                                       
        il = list(line)
        for let in line:
            
            if(let == " "):
                
                if(not bull):
                    il[vidx] = "--"
                    bull = True
                else:
                    il[vidx] = ""
            else:
                bull = False
                    
        
            vidx += 1
        line = "".join(il)
        lines4_1.append(line)
        bull = False

    print("cleaning data lines4_2 ...")
    bull = False 
    
    for line in lines3_2:                                                # right side tasks
        vidx = 0
        il = list(line)
        for let in line:
            
            if(let == " "):
                
                if(not bull):
                    il[vidx] = "--"
                    bull = True
                else:
                    il[vidx] = ""
            else:
                bull = False
                    
        
            vidx += 1
            
        line = "".join(il)
        lines4_2.append(line)
        bull = False
    
    
    lines4_1 = wordS(lines4_1)                                             # use word(s) function
    
    if(do): 
        print("fixing-1")
        Records = []
        print("fixing-2")
        Records2 = []
        print("fixing-3")
        
        
        print("fixing-4")
        
        os.remove("taskscsv.csv")
        #print(Records)
        for i,b in zip(lines4_1,lines4_2):
            name,pid = i.split("--")
            sessionName,sessionId,mem_usage = b[:-2].split("--")
            Records2.append(pid)
            with open("taskscsv.csv","a",newline="") as csvFile:             
                csv.writer(csvFile).writerow([name,pid,sessionName,sessionId,mem_usage]) # transfrom data to csvfile
        print("fixing-6")
        #print(Records2)
            
            
                        
                        
                
            
        
    
    
main()
    