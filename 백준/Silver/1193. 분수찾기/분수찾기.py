idx=int(input())

degree=0
degree_sum=0

while(degree_sum<idx):
    degree+=1
    degree_sum+=degree

gap = degree_sum - idx

if(degree%2==1):
    denom = degree - gap
    numer= degree+1 - denom
else:
    numer = degree - gap
    denom = degree+1 - numer
    
print("{}/{}".format(numer,denom))