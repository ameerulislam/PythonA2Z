# https://app.codility.com/programmers/lessons/4-counting_elements/perm_check/
#my solution (my one is without any loop so I believe it's better than chatgpt)
def solution(A):
    # Implement your solution here
    N = len(A)
    # Unique test
    if len(set(A)) != len(A):
        return 0
    # Sum should match the natural number formula
    if sum(A) == N*(N+1)/2:
        return 1
    else:
        return 0


# chatgpt solution
def solution(A):
    n = len(A)
    seen = set()

    for element in A:
        if element in seen or element > n:
            return 0
        seen.add(element)

    return 1 if len(seen) == n else 0
