
s1="ABCCCCBB"
counts={}
for x in s1:
    counts[x]=counts.get(x,0)+1
lst=list(counts.items())
lst.sort(key=lambda x:x[1],reverse=True)
for i in range(len(lst)):
    print("{}出现{}次".format(lst[i][0],lst[i][1]))