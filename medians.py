def medians(a):
    a.sort()
    midlle = len(a) // 2
    return (a[midlle] + a[~midlle]) / 2

n=int(input("enter limit"))

a = [int(x) for x in input().split()]

print(medians(a))
