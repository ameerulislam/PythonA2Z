def solution(A):
    # Implement your solution here
    n = len(A)+1
    result = (n*(n+1)//2) - sum(A)
    return result
