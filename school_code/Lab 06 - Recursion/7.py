def get_gcd(m,n):
    m1=n
    n1=m%n
    if n1 !=0:
        return get_gcd(m1,n1)
    else:
        return n