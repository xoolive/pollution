# a solution :
# minimisation problem
tprob = pulp.LpProblem("Test",pulp.LpMinimize)

# constants
p1min=0
p1max=100
c1=50
p2min=10
p2max=400
c2=100

# variables

## production
p1=[pulp.LpVariable(f"p1_{t}",0,p1max) for t in range(0,24)]
p2=[pulp.LpVariable(f"p2_{t}",0,p2max) for t in range(0,24)]

## on/off
on1=[pulp.LpVariable(f"on1_{t}",cat=pulp.LpBinary) for t in range(0,24)]
on2=[pulp.LpVariable(f"on2_{t}",cat=pulp.LpBinary) for t in range(0,24)]


# constraints
for t in range(0,24):
    tprob+=p1[t]>=p1min*on1[t] # if 'on' produce at least min
    tprob+=p1[t]<=p1max*on1[t] # if 'on' produce at most max, if 'off' produce 0 
    tprob+=p2[t]>=p2min*on2[t]
    tprob+=p2[t]<=p2max*on2[t]
    
    tprob+=p1[t]+p2[t]>=demand[t]
    
# objective
tprob+=sum([p1[t]*c1 + p2[t]*c2 for t in range(0,24)])


# display
assert pulp.LpStatus[tprob.solve()] == 'Optimal'
p1res=[pulp.value(p1[t]) for t in range(0,24)]
p2res=[pulp.value(p2[t]) for t in range(0,24)]

plt.plot(demand,'b')
plt.plot(p1res,'g')
plt.plot(p2res,'r')