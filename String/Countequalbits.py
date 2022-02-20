str = "0100110101"
count0=count1=cnt=0
for i in str:
    if i=="0":
        count0+=1
    else:
        count1+=1
    if count0==count1:
        cnt+=1
if cnt<1:
    print(-1)
else:
    print(cnt)


