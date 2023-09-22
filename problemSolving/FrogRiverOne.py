# https://app.codility.com/programmers/lessons/4-counting_elements/
# Solution from chatgpt
def solution(X, A):
    # Implement your solution here
    positions = set()
    for second, leaf_position in enumerate(A):
        positions.add(leaf_position)
        if len(positions) == X:
            return second
    return -1
