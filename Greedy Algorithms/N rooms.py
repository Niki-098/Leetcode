def maxMeetings(start, end):
    n = len(start)
    meet = [(start[i], end[i]) for i in range(n)]
    meet = sorted(meet, key=lambda x: x[1])
    answer = []
    limit = meet[0][1]
    answer.append(1)
    for i in range(1, n):
        if meet[i][0] > limit:
            limit = meet[i][1]
            answer.append(i + 1)
    print("The order in which the meetings will be performed is:")
    for i in answer:
        print(i, end=" ")


if __name__ == "__main__":
    start = [1, 3, 0, 5, 8, 5]
    end = [2, 4, 5, 7, 9, 9]
    maxMeetings(start, end)
