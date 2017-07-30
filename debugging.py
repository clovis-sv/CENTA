 import pdb

def transform(x,y): 
 z=x+y
 x *=2
 z= x+y
 return z

z=5
x=50
y=60
n=1000
pdb.set_trace()
transform(5,10)
print('z='+str(z))
n=transform(2,3)
print('n = ' + str(n))
