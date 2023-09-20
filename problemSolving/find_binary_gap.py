def solution(N):

    bits = bin(N)[2:]

    current_gap = 0
    longest_gap = 0

    for bit in bits:
        if bit == "1":
            longest_gap = max(longest_gap, current_gap)
            current_gap = 0
        else:
            current_gap += 1

    return longest_gap


print(solution(512))
