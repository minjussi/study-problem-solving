def solution(people, limit):
    boat = 0
    people.sort(reverse=True)
    left = 0
    right = len(people)-1
    while left <= right:
        if people[left] + people[right] > limit:
            boat += 1
            left += 1
        elif people[left] + people[right] <= limit:
            boat += 1
            left += 1
            right -= 1
    return boat
