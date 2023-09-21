############ My Original & ChatGPT's Better solutions with timing ##########
# Problem link https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/
import time

# MY original solution
def original_solution(A, K):
    if len(A) != 0:
        for _ in range(1, K+1):
            last = A.pop(-1)
            A.insert(0, last)
    return A

# The alternative solution
def efficient_solution(A, K):
    if len(A) == 0:
        return A
    N = len(A)
    K %= N
    rotated_part = A[N - K:]
    A[N - K:] = A[:N - K]
    A[:N - K] = rotated_part
    return A

# Generate a sample array and rotation value for testing
A = list(range(1, 10001))  # Replace with your actual array
K = 1000  # Replace with your desired rotation value

# Time the execution of the original solution
start_time = time.time()
original_solution(A.copy(), K)
end_time = time.time()
print(f"Original solution took {end_time - start_time} seconds")

# Time the execution of the efficient solution
start_time = time.time()
efficient_solution(A.copy(), K)
end_time = time.time()
print(f"Efficient solution took {end_time - start_time} seconds")
