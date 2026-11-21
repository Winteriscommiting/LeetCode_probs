class Solution:
    def robotSim(self, commands, obstacles):
        blocked=set()
        for o in obstacles:
            blocked.add((o[0], o[1]))
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        x,y=0,0
        dirs=0
        maxDist=0
        for cmd in commands:
            if cmd==-1:
                dirs=(dirs+1)%4
            elif cmd == -2:
                dirs=(dirs+3)%4
            else:
                while cmd>0:
                    nx=x+directions[dirs][0]
                    ny=y+directions[dirs][1]
                    if (nx,ny) in blocked:
                        break
                    x=nx
                    y=ny
                    maxDist=max(maxDist,x*x+y*y)
                    cmd-=1
        return maxDist