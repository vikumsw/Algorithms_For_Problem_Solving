'''
On a infinite plane, a robot initially stands at (0,0) and faces north. The robot can recieve one of three insructions:
    'G': go straight 1 unit
    'L': turn 90 degrees to the left
    'R': turn 90 degrees to the right
    The robot performs the instructions given in order, and repeats them forever.
    return true if there exists a circle, in the plane such that the robot never leaves the circle.
    
    Input: "GGLLGG"
    Ouput: true
'''

def isLooping(step):
    # if robot does not return after 4 steps, it never returns
    pos=[0,0]
    direction=0 # north 0, west 1, south 2, east 3
    
    for i in range(4):
        for c in step:
            if   c=='G':
                if   direction==0:
                    pos[1]+=1
                elif direction==1:
                    pos[0]+=1
                elif direction==2:
                    pos[1]+=-1
                else:
                    pos[0]+=-1
            elif c=='L':
                direction-=1
            elif c=='R':
                direction+=1
            else:
                return False;
                
            direction = direction%4
            
        print('pos:{} , dir:{}'.format(pos,direction))
    
    if pos == [0,0]:
        return True
    else:
        return False
        

print(isLooping('GGLLGG'))
print(isLooping('GGGLGLL'))

