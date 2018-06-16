#python 3
#Naive algorithm to find Pisano period for a F(n)

#Below function is a naive function to determine Reminder of Fibonacci number n when using modulo m
def pisano(n,m):
    i=0
    j=1
    for _ in range(2,n+1):
        i,j=j,i+j
    print (j%m, end="\n")
    return

if __name__=='__main__':
    a, b = map(int, input().split())
    pisano(a,b)



    
