import sys
import os
infile=""
outfile=""
cmdlist=[]
header=False
for i in range(len(sys.argv)):
    if (sys.argv[i]=="/out"):
        if sys.argv[i+1].find("/lib")!=-1:
            outfile=sys.argv[i+2]
            header=True
        else:
            outfile=sys.argv[i+1]
    elif (sys.argv[i]=="/in"): 
        infile=sys.argv[i+1]
with open(infile,"r") as f:
    cmdlist=f.readlines()
    for i in range(len(cmdlist)):
        cmdlist[i]=cmdlist[i].split("\n")[0]
if cmdlist[0]!="동작 그만" or cmdlist[-1]!="밑장빼기냐!!!":
    print("당신은 타짜입니다.")
    exit(1)
line=0
numfunc=0
command_c="#include<stdio.h>\n"
if header:
    command_c="#ifndef infile\n#define infile\n#include<stdio.h>\n"
arglist="abcdefghijklmnopqrstuvwxyzABCDEFGHIJHKLMNOPQRSTUVWXYZ"
isvoid=False
ismain=False
lib=""
infunc=False
scope=0
while line<len(cmdlist):
    used=0
    cmd=cmdlist[line]
    if isvoid or cmd.find("/")!=-1:
        infunc=False
    if cmd.startswith("이")and cmd.endswith("는 이제 제 겁니다."):
        for i in cmd:
            if i=="는":
                break
            elif i!="이" and i!=" ":
                lib+=i
        command_c+="#include\""+lib+"\"\n"
    if(cmd.find("hold")!=-1 and cmd.find("to pay respect")!=-1):
        scope+=1
        if(cmd.find("X")!=-1):
            command_c+="int "
            isvoid=False
            ismain=False
            infunc=True
            numfunc+=1
            command_c+="f"+str(numfunc)+"("
        elif(cmd.find("Y")!=-1):
            command_c+="void "
            isvoid=True
            ismain=False
            numfunc+=1
            command_c+="f"+str(numfunc)+"("
        elif(cmd.find("Z")!=-1):
            command_c+="int main(){\n"
            ismain=True
            infunc=False
        if not (isvoid or ismain):
            infunc=True
            for i in range(len(cmd)):
                if cmd[i]=="[":
                    command_c+="int "+arglist[used]
                    used+=1
                elif cmd[i]==",":
                    command_c+=",int "+arglist[used]
                elif cmd[i]=="]" or i>=len(cmd)-1:
                    command_c+="){\n"
        elif isvoid and not ismain:
            command_c+="){\n"
    elif cmd.find("펄")!=-1 and cmd.find("럭")!=-1 and cmd.find("무야호")==-1:
        pointer=cmd.count("~")
        num=0
        if cmd.find("곱창")!=-1:
            num1=[]
            for i in cmd:
                if i=="곱":
                    num1.append(num)
                    num=0
                elif i=="창":
                    continue
                elif i=="!":
                    num+=1
                elif i=="i":
                    num-=1
            for j in num1:
                num*=j
        else:
            num=cmd.count("!")-cmd.count("i")
        if cmd.find("몰")!=-1 and cmd.find("루")!=-1:
            pointer2=cmd.count("?")
            if infunc:
                if num==0:  
                    command_c+="int "+str(arglist[pointer])+"="+str(arglist[pointer2])+";\n"
                elif num>0:
                    command_c+="int "+str(arglist[pointer])+"="+str(arglist[pointer2])+"-"+str(num)+";\n"
                else:
                    command_c+="int "+str(arglist[pointer])+"="+str(arglist[pointer2])+"+"+str(abs(num))+";\n"
            else:  
                command_c+="int a"+str(pointer)+"=a"+str(pointer2)+";\n"
        elif cmd.find("아")!=-1 and cmd.find("루")!=-1:
            pointer2=cmd.count("?")
            if infunc:  
                command_c+="int "+str(arglist[pointer])+"=a"+str(pointer2)+";\n"
            else:  
                command_c+="int a"+str(pointer)+"=a"+str(pointer2)+";\n"
        else:
            if infunc:  
                command_c+=str(arglist[pointer])+"="+str(num)+";\n"
            else:  
                command_c+="int a"+str(pointer)+"="+str(num)+";\n"
    elif cmd.find("루")!=-1 and infunc:
        num=cmd.count("!")-cmd.count("i")
        if cmd.find("몰")!=-1:
            pointer=cmd.count("?")
            command_c+=str(arglist[pointer])+"-="+str(num)+";\n"
        if cmd.find("아")!=-1:
            pointer=cmd.count("?")
            command_c+="a"+str(arglist[pointer])+"+="+str(num)+";\n"
    elif cmd.find("루")!=-1 and not infunc:
        num=cmd.count("!")-cmd.count("i")
        if cmd.find("몰")!=-1:
            pointer=cmd.count("?")
            command_c+="a"+str(pointer)+"-="+str(num)+";\n"
        if cmd.find("아")!=-1:
            pointer=cmd.count("?")
            command_c+="a"+str(pointer)+"+="+str(num)+";\n"
    elif cmd.find("폭력 멈춰")!=-1:
        scope-=1
        command_c+="\n}\n"
    elif cmd.find("멈춰")!=-1 and( not ismain and (not isvoid) ):
        num=cmd.count("!")-cmd.count("i")
        scope-=1
        if num==0:
            pointer=cmd.count("?")
            command_c+="return "+str(arglist[pointer])+";\n"
        else:
            command_c+="return "+str(num)+";\n"
        if cmd.find("/")!=-1:
            command_c+="\n}\n"
            if scope==0:
                infunc=False
    elif  cmd.find("멈춰")!=-1 and ismain :
        scope-=1
        num=cmd.count("!")-cmd.count("i")
        if num==0:
            pointer=cmd.count("?")
            command_c+="return a"+str(pointer)+";\n"
        else:
            command_c+="return "+str(num)+";\n"
        if cmd.find("/")!=-1:
            command_c+="\n}\n"
            if scope==0:
                infunc=False
    elif cmd.find("멈춰")!=-1 and (isvoid ):
        command_c+="return;\n}\n"
        if cmd.find("/")!=-1:
            if scope==0:
                infunc=False
    elif (cmd.find("이 왜")!=-1 or cmd.find("가 왜")!=-1) and (cmd.find("에서 나와?")!=-1 or cmd.find("서 나와?")!=-1):
        op=""
        if not (ismain or isvoid):
            scope+=1
            infunc=True
        if cmd.find("형")!=-1 or cmd.find("누나")!=-1:
            op="==0"
        elif cmd.find("동생")!=-1 or cmd.find("아우")!=-1:
            op="!=0"
        pointer=0
        num=0
        for i in cmd:
            if(i=="!"):
                pointer+=1
        if infunc:
            command_c+="if("+str(arglist[pointer])+op+"){\n"
        else:
            command_c+="if(a"+str(pointer)+op+"){\n"
    if cmd.find("무야호")!=-1 and cmd.find("어 나가")==-1:
        num=cmd.count("!")-cmd.count("i")
        if cmd.find("[")!=-1 and cmd.find("]")!=-1:
            command_c+="f"+str(num)+"("
            pointer=0
            for i in cmd: 
                if i==",":
                    command_c+=","
                elif i=="~":
                    pointer+=1
                elif i=="럭":
                    if ismain:
                        command_c+="a"+str(pointer)
                    else:
                        command_c+=str(arglist[pointer])
                elif i=="펄": 
                    pointer=0
                elif i=="]":
                    command_c+=");\n"
    if cmd.find("어 나가")!=-1:
        num=cmd.count("!")-cmd.count("i")
        pointer=0
        if cmd.find("무야호")!=-1:
            command_c+='printf(\"%d\",f'+str(num)+"("
            for i in cmd:
                if i!="[" and i!="]":
                    if i==",":
                        command_c+=","
                    elif i=="~":
                        pointer+=1
                    elif i=="럭":
                        if ismain:
                            command_c+="a"+str(pointer)
                        else:
                            command_c+=arglist[pointer]
                    elif i=="펄":
                        pointer=0
                elif i=="]":
                    command_c+="));\n"
                    break
        elif num==0 and cmd.find("/")!=-1:
            command_c+='printf(\"\\n\");\n'
        else:
            command_c+='printf(\"%d\",a'+str(num)+');\n'
    if cmd.find("다 나가")!=-1:
        num=cmd.count("!")-cmd.count("i")
        if num==0 and cmd.find("/")!=-1:
            command_c+='printf(\"\\n\");\n'
        else:
            command_c+='printf(\"%c\",a'+str(num)+');\n'
    if cmd.find("입력 해야쥬?")!=-1:
        num=cmd.count("!")-cmd.count("i")
        command_c+='scanf(\"%d\",&a'+str(num)+');\n'
    line+=1
if not header:
    with open("tmp.c","w") as t:
        t.write(command_c)
    if outfile!="":
        with open(outfile,"w") as ff:
            os.system("gcc -Wall tmp.c -o "+outfile)
    else:
        os.system("gcc -Wall tmp.c -o ./a.out")
    #os.system("rm tmp.c")
else:
    with open(outfile,"w") as o:
        o.write(command_c+"\n#endif")
