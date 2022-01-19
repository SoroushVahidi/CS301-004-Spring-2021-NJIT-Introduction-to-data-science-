# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
 #   print_hi('PyCharm')
v=[0.0]*125

for i in range (100,125):
    v[i]+=i

#print(a)
t=0
while(1):
    t=t+1
    x=v[:]
    #print(x)
    if(t>1024000):
        break
    for i in range (0,100):
        v[i]=max(i,(4*x[i+4]+2*x[i+9]+x[i+16]+9*x[0])/16)
  #  print(x)
   # print(v)
    di=numpy.subtract(v,x)
   # print(abs(di))
   # print(sum(abs(di)))
  #  if((sum(abs(di))<0.000001) ):
   #     break
   # print(di)
    #if(dif<1):
     #   break
    #print(v)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
print(t)
print(v)
