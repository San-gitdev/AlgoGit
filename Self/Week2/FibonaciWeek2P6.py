# python3
#   Task. Given an integer 𝑛, find the last digit of the sum 𝐹0 + 𝐹1 + · · · + 𝐹𝑛.
# Input Format. The input consists of a single integer 𝑛.
#Constraints. 0 ≤ 𝑛 ≤ 1018.
#Output Format. Output the last digit of 𝐹0 + 𝐹1 + · · · + 𝐹𝑛.

def LastDigitofsummingnFibos(n):
    i=0
    j=1
    sum=i+j
    for cnt in range(2, n+1):
        i,j=j,i+j
        sum=sum+j
        print("Fibonacci number ", cnt, " is ", j," and its sum is " , sum)
    return


if __name__=='__main__':
    a = int(input())
    LastDigitofsummingnFibos(a)



    
