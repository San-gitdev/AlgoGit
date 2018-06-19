# python3
#   Task. Given an integer 𝑛, find the last digit of the sum 𝐹0 + 𝐹1 + · · · + 𝐹𝑛.
# Input Format. The input consists of a single integer 𝑛.
#Constraints. 0 ≤ 𝑛 ≤ 1018.
#Output Format. Output the last digit of 𝐹0 + 𝐹1 + · · · + 𝐹𝑛.
# Remarks - Sum of first x number is equal to fibonacci number (x+2)

def LastDigitofsummingnFibos(n):
    i=0
    j=1
    sum=i+j
    for _ in range(2, n+2):
        i,j=j,i+j
        sum=i+j
        i,j,sum=i%10,j%10,sum%10
        if(sum==0):
            sum=10
        #print(i,j,sum-1)
       
    print("Last digit of Sum of first ", n, " Fibonacci numbers is: ",  sum-1)
    return


if __name__=='__main__':
    a = int(input())
    LastDigitofsummingnFibos(a)



    
