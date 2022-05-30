def chet(x):
   return x%2==0

def number(x,r=True,h=False):
    s=chet(x)
    if s:
        return r
    else:
        print(h)
print(chet(8))