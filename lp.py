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
obj=[1.0]*106
lhs_eq=[]
rhs_eq=[]
for i in range (100,106):
    x=[0.0]*106
    x[i]=1;
    lhs_eq.append(x.copy())
    rhs_eq.append(i)
lhs_ineq=[]
rhs_ineq=[]
for i in range (0,100):
    x=[0.0]*106
    x[i]=-1
    lhs_ineq.append(x.copy())
    rhs_ineq.append(-i)
for i in range (1,100):
    x=[0.0]*106
    x[i]=-6
    x[0]=3
    x[i+3]=1
    x[i+5]=1
    x[i+6]=1
    lhs_ineq.append(x.copy())
    rhs_ineq.append(0)
bnd =[(0,float("inf"))]*106
x=[0.0]*106
x[0]=-3
x[3]=1
x[5]=1
x[6]=1
lhs_ineq.append(x.copy())
rhs_ineq.append(0)
opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,    A_eq=lhs_eq, b_eq=rhs_eq, bounds=bnd, method="revised simplex")
print(opt.x)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

