a=input('请输入加密内容：')
for b in a:
    if'a'<=b<='z':
        print(chr(ord("a")+(ord(b)-ord("a")+3)%26),end="")
    elif "A"<=b<="Z":
        print(chr(ord("A")+(ord(b)-ord("A")+3)%26),end="")
    else:
        print(b,end="")