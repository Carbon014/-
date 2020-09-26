c=input('请输入解密内容：')
for d in c:
    if'a'<=d<='z':
        print(chr(ord("a")+(ord(d)-ord("a")-3)%26),end="")
    elif "A"<=d<="Z":
        print(chr(ord("A")+(ord(d)-ord("A")-3)%26),end="")
    else:
        print(d,end="")