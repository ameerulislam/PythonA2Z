def Solve (N, A):
    # Write your code here
    if 0 in A:
        return 0
    positives = float('inf')
    negatives = float('-inf')
    for i in A:
        if i>0 and i < positives:
            positives = i
        elif i<0 and i > negatives:
            negatives = i
    if abs(positives)  > abs(negatives):
        return negatives
    else:
        return positives

    
N = input()
A = list(map(int, input().split()))
out_ = Solve(N, A)
print (out_)
