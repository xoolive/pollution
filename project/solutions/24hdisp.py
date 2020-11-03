
# a solution
p1res=[pulp.value(p1[t]) for t in range(0,24)]
p2res=[pulp.value(p2[t]) for t in range(0,24)]

plt.plot(demand,'b')
plt.plot(p1res,'g')
plt.plot(p2res,'r')