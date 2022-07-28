a=[]
print(a,type(a))

p=["ameerpet",55]
print(p,type(p))
print(p[0],type(p[0]))
print(p[1],type(p[1]))


a=None
print(type(a))


b=[2,7.9,"hi",None,True]
print(b[0],type(b[0]))
print(b[1],type(b[1]))                       #2
print(b[2]),type(b[2])                       #7.9
print(b[5],type(b[5]))                       #indexerror: list index out of range


r=[4,3.1,"python"]
r[0]=89.23                                    #[89.23,3.1,'python]
r[-1]='GT'
print(r)                                       #[89.23,3.1,'GT']



n=[1,3.7,"hello",[10,11]]
print(n,type(n))
print(n[0],type(n[0]))
print(n[1],type(n[1]))
print(n[3][0],type(n[3][0]))                    #10 int
print(n[3][1],type(n[3][1]))                    #11 int


n=[1,3.4,"hello",[10,11]]
n.append('josh')
print(n)                                         #1,3.4,'hello',[10,11],'josh'


n=[1,3.4,"hello",[10,11]]
n.clear()
print(n)                                          #[]


n=[5,10,'hello',10,'']
print(n.count(''))
print(n.count(10))                                  #2
print(n.count(5))                                   #1


a=[5,10,15]
b=[1,2,5,7]
a.extend(b)                                         #[5,10,15,1,2,5,7]
b.extend(a)
print(b)                                       


n=[2,3,4,'hello',4.5,[56]]
print(n.index(14.5))                                   #index not found
print(n.index(4.5))                                    #4
print(n.index([56]))                                   #6
print(n.rindex[2])                                       #attributeerror: list object has no attribute rindex