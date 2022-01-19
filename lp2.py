# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy

import scipy

from scipy.optimize import linprog

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
 #   print_hi('PyCharm')
obj=[1.0]*125
lhs_eq=[]
rhs_eq=[]
for i in range (100,125):
    x=[0.0]*125
    x[i]=1;
    lhs_eq.append(x.copy())
    rhs_eq.append(i)
lhs_ineq=[]
rhs_ineq=[]
for i in range (0,100):
    x=[0.0]*125
    x[i]=-1
    lhs_ineq.append(x.copy())
    rhs_ineq.append(-i)
for i in range (1,100):
    x=[0.0]*125
    x[i]=-16
    x[0]=9
    x[i+4]=4
    x[i+9]=2
    x[i+16]=1
    lhs_ineq.append(x.copy())
    rhs_ineq.append(0)
bnd =[(0,float("inf"))]*125
x=[0.0]*125
x[0]=-7
x[4]=4
x[9]=2
x[16]=1
lhs_ineq.append(x.copy())
rhs_ineq.append(0)
opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,    A_eq=lhs_eq, b_eq=rhs_eq, bounds=bnd, method="revised simplex")
print(opt.x)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

