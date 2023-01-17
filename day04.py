#tuple
a = 'harry',    #콤마(,)로 튜플생성
b = 'harry', 'ron'
c = ()          #()로 빈 튜플생성
d = ('harry',)  #(,)로 튜플 생성
f = ('hermione') # tuple x (string)

e = ('herry','ron') #packing
x,y = e # unpacking
g= x,y #packing

h= ('hermione',)
print(h,id(h))
h = h+e #concatenation
print(h,id(h))

print(x)
print(y)
print(g)
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
