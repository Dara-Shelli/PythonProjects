from collections import deque

dasha = 'Dasha'
bart = 'Bart'
alex = 'Alex'
jamie = 'Jamie'

waiting_queue = deque([])

waiting_queue.append(dasha)
waiting_queue.append(bart)
waiting_queue.append(alex)
waiting_queue.append(jamie)

print(f"waiting line: {waiting_queue}")

for person in range(len(waiting_queue)):
    print(f'Served: {waiting_queue.popleft()}', '\n')
    print(f'Waiting line:{waiting_queue}','\n')
else:
    print("All done for the day")

