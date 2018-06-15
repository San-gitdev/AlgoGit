# python3
#   Task. Given an integer 𝑛, find the 𝑛th Fibonacci number 𝐹𝑛.
#   Input Format. The input consists of a single integer 𝑛.
#   Constraints. 0 ≤ 𝑛 ≤ 45.
#   Output Format. Output 𝐹𝑛.



import array

def RecFn(n):
    i=0
    j=1
    for _ in range(2,n+1):
        i,j=j,i+j
    print (j, end="\n")
    return
if __name__ == '__main__':
    a = int(input())
    if(a==0 or a==1):
        print(a)
    else:
        RecFn(a)
