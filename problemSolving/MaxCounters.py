# My solution, times out on big values
def solution(N, A):
    # Implement your solution here
    list_N = [0] * N
    for X in A:
        if X == N+1:
           list_N = [max(list_N)]*N
        else:
            list_N[X-1] += 1
    return list_N

# chatgpt solution finally got it right and it's pretty crazy how it works! I assume my max(list_N) was getting screwed for long list

def solution(N, A):
    counters = [0] * N
    max_counter = 0
    current_max = 0
    
    for operation in A:
        if 1 <= operation <= N:
            # Increase the counter at the specified position
            counters[operation - 1] = max(counters[operation - 1], current_max) + 1
            # Update the max_counter if necessary
            max_counter = max(max_counter, counters[operation - 1])
        elif operation == N + 1:
            # Set the current_max to the max_counter for the next "increase" operation
            current_max = max_counter

    # Update any remaining counters that haven't been updated to the current_max
    counters = [max(counter, current_max) for counter in counters]

    return counters
