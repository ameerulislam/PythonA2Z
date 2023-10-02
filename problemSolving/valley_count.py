def countingValleys(steps, path):
    # Write your code here
    valley = 0
    sea_level = 0

    for i in path:
        if i == "U":
            if sea_level == -1:
                sea_level += 1
                valley += 1
            else:
                sea_level += 1
        else:
            sea_level -= 1
    
    return print(valley)


countingValleys(8, "DDUUUUDD")
