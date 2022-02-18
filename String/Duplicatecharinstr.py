s="test string"
#hashing
_dic={}
for i in s:
    if i not in _dic:
        _dic[i]=1
    else:
        _dic[i]+=1
for i,j in _dic.items():
    if j>1:
        print("{} has {} repeatation.".format(i,j))
