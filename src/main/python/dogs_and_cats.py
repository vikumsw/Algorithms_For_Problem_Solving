# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most problems.
t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
    
    n, d, c, m = [int(s) for s in input().split(" ")] # read a list of integers, 2 in this case
    s = input()
    
    #print(n, d, c, m,s)

    def solve(n, d, c, m,s):
        if s.count('D') == 0:
            print("Case #{}: {}".format(i, "YES"))
            return

        checkDog = False
        for ch in s:
            if checkDog and ch == 'D':
                print("Case #{}: {}".format(i, "NO"))
                return
            else:
                if ch == 'D':
                    d -= 1
                    c += m
                else:
                    c-=1
                
                if d==-1:
                    print("Case #{}: {}".format(i, "NO"))
                    return

                if c==-1:
                    checkDog=True

        print("Case #{}: {}".format(i, "YES"))
    
    solve(n, d, c, m,s)