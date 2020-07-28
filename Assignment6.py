l1=[1,2,3,4,5,7,8]
l2=["a","b","c","d","e"]
res = {l1[i]: l2[i] for i in range(min(len(l1),len(l2)))}
print(res)


