# This Script Convert Python to Java (source-to-source) using Regular Expression
# Author: Ansari Shahid (mrpascal) <ansarishahid640@gmail.com>
# Just a hobby, Not a big language translater 
# Highly Exprimental release

import os
import sys
import re

pyFile = open("source.py", "r") #Python File to read
jFile = open("source.java", "w") #To create Java file


#Function to write to the file
def writeline(string):
    jFile.write(string + "\n")

previousCount = 0
for line in pyFile.readlines():
    #detect blank lines
    test_line = line.strip()
    if len(test_line) == 0:
        pass
        
    else:
    
        currentCount = 0
        for char in line:
            if char == " ":
                currentCount += 1
            else:
                break
        
        if currentCount == len(line):
            # empty line, do nothing
            break
                
        if previousCount > currentCount:
            # we stepped out a block
            
            # NOTE - if we went from 12 indents to 4, we should add two closing brackets, one at 12 and one at 4
            # FIXME ERROR
            count = (previousCount - currentCount) // 4
            while count != 0:
                writeline(" " * count * 4 + "}")
                count -= 1
            pass
            
        if previousCount < currentCount:
            # we stepped in a block. should write open paren
            writeline(" " * previousCount + "{")

        # now run regex suite on the line
        # might cause error if none
        
        line = re.sub(r"False",r"false", line)
        line = re.sub(r"@property",r"", line)
        line = re.sub(r"self",r"this", line)
        line = re.sub(r"\(this,",r"(", line)
        line = re.sub(r"\(this\)",r"()", line)
        line = re.sub(r"True",r"true", line)
        line = re.sub(r"print\(",r"System.out.println(", line)
        line = re.sub(r"and",r"&", line)
        line = re.sub(r"not",r"!", line)
        line = re.sub(r"#",r"//", line)
        #line = re.sub("r'(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])():' ", "r'(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(){'", line)
        line = re.sub(r"def",r"public void", line)
        
        # handle if elses - add parenthesis
        p = re.compile(r'(?<=if)(.+)(?=\:)')
        if p.search(line) != None:
            string = p.search(line).group(0)
            string = "( " + string + " ) "
            line = "if " + string + "NOEND"
        
        # finish regex
        line = re.sub(r":",r" ", line) #since brackets already handled
       	
  
        # HANDLE """ xxx """ --> /* xxx */ (can do by hand if need be)
        r = re.compile('(?<=\"\"\")(.+)(?=\"\"\")')
        if r.search(line) != None:
            string = r.search(line).group(0)
            string = "/* " + string + " */ "
            
        # add ;
        line = line.rstrip()
        
        
        if len(line) != 0 and line[len(line)-5:len(line)] == "NOEND":
            line = line[:len(line)-5]
        
        else:
            if len(line) != 0 and line[len(line)-1] not in ("(" , "{", "}"):
                line = line + ";"
        
        
        # remove extra ; in method declarations
        z = re.compile("public void")
        if z.search(line) != None:
            line = line[:len(line)-1]

        # remove extra ; in class declarations
        cl = re.compile("class")
        if cl.search(line) != None:
            if len(line) != 0 and line[len(line)-1] not in ("{"):
                line = line[:len(line)-1 ] + ""
            else:
                line = line[:len(line)-1 ]
        
        # remove extra ; from else part
        el = re.compile("else")
        if el.search(line) != None:
            line = line[:len(line)-1]

                
        # update counts
        previousCount = currentCount
        writeline(line)


pyFile.close()
jFile.close()
