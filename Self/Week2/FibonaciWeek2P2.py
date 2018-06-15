# python3
#   Task. Given an integer 𝑛, find the last digit of the 𝑛th Fibonacci number 𝐹𝑛 (that is, 𝐹𝑛 mod 10).
#   Input Format. The input consists of a single integer 𝑛.
#   Constraints. 0 ≤ 𝑛 ≤ 107.
#   Output Format. Output the last digit of 𝐹𝑛.


import array

def RecFn(n):
    i=0
    j=1
    for _ in range(2,n+1):
        i,j=j%10,(i+j)%10
    print(j%10)
    return
if __name__ == '__main__':
    a = int(input())
    if(a==0 or a==1):
        print(a)
    else:
        RecFn(a)
