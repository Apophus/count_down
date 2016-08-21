import time
def countdown(p,q):
    i=p
    j=q
    k=0
    while True:
        if(j==-1):
            j=59
            i -=1
        if(j > 9):  
            print "\r"+str(k)+str(i)+":"+str(j),
        else:
            print "\r"+str(k)+str(i)+":"+str(k)+str(j),
        time.sleep(1)
        j -= 1
        if(i==0 and j==-1):
            break
    if(i==0 and j==-1):
        print "\rGoodbye!"
        time.sleep(1)
countdown(1,5) #countdown(min,sec)