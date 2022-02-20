def printallsubsequence(n,res):
    if len(n)==0:
        print(res,end=" ")
        return
    printallsubsequence(n[1:],res+n[0])
    printallsubsequence(n[1:],res)

subseq=""
str="kishan"
printallsubsequence(str,subseq)
