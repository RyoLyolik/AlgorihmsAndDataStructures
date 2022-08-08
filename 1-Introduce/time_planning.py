# INPUTS

n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]

times.sort(key=lambda x:x[-1])
events = [times[0]]
for event in range(n):
    if events[-1][1] <= times[event][0]:
        events.append(times[event])

print(events)
