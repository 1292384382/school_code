def collatz(n):
    if n==1:
        print(n)
        pass
    elif n%2==0:
        print(n)
        collatz(int(n/2))
    elif n%2==1:
        print(n)
        collatz(n*3+1)