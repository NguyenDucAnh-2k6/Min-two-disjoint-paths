import sys
from ortools.sat.python import cp_model
def Input():
    f=sys.stdin
    [n,m]=[int(x) for x in f.readline().split()]
    E=[]
    InA=[[] for _ in range(n+1)]
    OutA=[[] for _ in range(n+1)]
    for i in range(m):
        [u,v,w]=[int(x) for x in f.readline().split()]
        E.append([u,v,w])
        OutA[u].append([v,w])
        InA[v].append([u,w])
    return n,m,E,InA, OutA
def inputfile(filename):
    with open(filename, 'r') as f:
        [n,m]=[int(x) for x in f.readline().split()]
        E=[]
        InA=[[] for _ in range(n+1)]
        OutA=[[] for _ in range(n+1)]
        for i in range(m):
            [u,v,w]=[int(x) for x in f.readline().split()]
            E.append([u,v,w])
            OutA[u].append([v,w])
            InA[v].append([u,w])
    return n,m,E,InA, OutA
#n,m,E,InA,OutA=Input()
n,m,E,InA,OutA=inputfile('Min disjoint paths data.txt')
model=cp_model.CpModel()
#define decision variables
x={}
y={}
for [i,j,w] in E:
    x[i,j]=model.NewIntVar(0,1,'x('+ str(i)+','+ str(j)+')')
    y[i,j]=model.NewIntVar(0,1,'x('+ str(i)+','+ str(j)+')')
MAX=0
#Set upper bound for objective func
for [i,j,w] in E:
    MAX+=w
obj=model.NewIntVar(0,MAX,'obj')
s=1
t=n
for i in range(1,n+1):
    if i!=s and i!=t:
        model.Add(sum(x[j,i] for [j,w] in InA[i]) == sum(x[i,j] for [j,w] in OutA[i]))
        model.Add(sum(x[j,i] for [j,w] in InA[i])<=1)
        model.Add(sum(y[j,i] for [j,w] in InA[i]) == sum(y[i,j] for [j,w] in OutA[i]))
        model.Add(sum(y[j,i] for [j,w] in InA[i])<=1)
    model.Add(sum(x[1,j] for [j,w] in OutA[1])==1)
    model.Add(sum(x[j,n] for [j,w] in InA[n])==1)
    model.Add(sum(y[1,j] for [j,w] in OutA[1])==1)
    model.Add(sum(y[j,n] for [j,w] in InA[n])==1)
for [i,j,w] in E:
    model.Add(x[i,j]+y[i,j]<=1)
obj=0
#Expression for obj
for [i,j,w] in E:
    obj+=(x[i,j]+y[i,j])*w
model.Minimize(obj)
solver=cp_model.CpSolver()
solver.parameters.max_time_in_seconds=10.00
status=solver.Solve(model)
if status==cp_model.OPTIMAL or status==cp_model.FEASIBLE:
    print(solver.Value(obj))
    print('x path: ')
    for [i,j,w] in E:
        if solver.Value(x[i,j])>0:
            print(i, end='->')
    print(t)
    print('y path: ')
    for [i,j,w] in E:
        if solver.Value(y[i,j])>0:
            print(i, end='->')
    print(t)
else:
    print("NOT_FEASIBLE")
