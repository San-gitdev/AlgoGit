#python 3
#Task. Given two integers 𝑛 and 𝑚, output 𝐹𝑛 mod 𝑚 (that is, the remainder of 𝐹𝑛 when divided by 𝑚).
#Input Format. The input consists of two integers 𝑛 and 𝑚 given on the same line (separated by a space).
#Constraints. 1 ≤ 𝑛 ≤ 1018, 2 ≤ 𝑚 ≤ 103.
#Output Format. Output 𝐹𝑛 mod 𝑚.

#Below function is written to do following things:
#For a given m, find a repeating string, its length and store the pattern.
#For the given n, find remainder when divide dy m and derive the pisano number.
def pisano(n,m):
    i=0
    j=1
    s="01"
    if(n<7):
        loopcnt = 1000
    else:
        loopcnt = n*n*n
    for _ in range(2,loopcnt):
        i,j=j,i+j
        s = s+str(j%m)
        x=(s+s).find(s,1,-1)
        if(x!=-1):
            print(x)
            print(s[:x])
            pattern= s[:x]
            break
    print("Pattern identified for modulo ", m, " is: ", pattern, " with length ", x)
    k=n%x
    print(pattern[k])
    return
                        
    #print ("Fibonaci number ", n, " is ", j, " And relvant pisano number is ", j%m, end="\n")



    

if __name__=='__main__':
    a, b = map(int, input().split())
    if(a<3):
        print("1")
    pisano(a,b)



    
