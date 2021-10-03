import datetime
def time_in_range(start, end, x):
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end

n=int(input())
c1,c2,c3=0,0,0 

while n>0:
    a,b=map(int,input().split())
    x=True
    bus_start = datetime.time(7, 0, 0)
    bus_end = datetime.time(7, 30, 0)
    case1=time_in_range(bus_start,bus_end, datetime.time(a, b, 0))

    friend_start = datetime.time(7, 31, 0)
    friend_end = datetime.time(8, 30, 0)
    case2=time_in_range(friend_start,friend_end, datetime.time(a, b, 0))

    auto_start = datetime.time(8, 31, 0)
    auto_end = datetime.time(4, 30, 0)
    case3=time_in_range(auto_start, auto_end, datetime.time(a, b, 0))
    
    if case1==x:
        c1+=1
    if case2==x:
        c2+=1  
    if case3==x:
        c3+=1
    
    n-=1
if c1>c2 and c1>c3:
    print("I went mostly on college bus this week")
if c2>c1 and c2>c3:
    print("I went mostly with my friend on bike this week")
if c3>c1 and c3>c2:
    print("I went mostly on auto this week")
