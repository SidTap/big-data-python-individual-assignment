def build_tallest_stack(disks):
    n = len(disks)
    disks.sort(key=lambda x: x[0]) # sort disks based on width
    max_heights = [disk[2] for disk in disks] # initialize max_heights

    for j in range(1, n):
        for i in range(j):
            if disks[j][0] > disks[i][0] and disks[j][1] > disks[i][1] and disks[j][2] > disks[i][2]:
                max_heights[j] = max(max_heights[j], max_heights[i] + disks[j][2])

    max_height = max(max_heights)
    stack = []
    for i in range(n-1, -1, -1):
        if max_heights[i] == max_height:
            stack.append(disks[i])
            max_height -= disks[i][2]
    
    return stack[::-1]

disks = [[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [1, 3, 1], [4, 4, 5]]
print(build_tallest_stack(disks))
# prints [[4, 4, 5], [3, 2, 3], [2, 1, 2]]


# Time complexity: O(n^2) because there is a loop with iterated through the entire list(n = items in disks)
# Space complexity: O(n) because a new list is created with all entries of height(n = items in disks)