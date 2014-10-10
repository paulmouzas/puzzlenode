import re
from collections import deque
from pprint import pprint

def hours_to_minutes(time):
    """
    Converts time from the format HH:MM to an the amount of minutes
    Returns as an integer instead of a string
    """
    hours, minutes = time.split(':')
    return int(hours) * 60 + int(minutes)

with open('sample-input.txt', 'r') as f:
    n = int(f.readline())
    for i in xrange(n):
        f.readline()
        flights = int(f.readline())
        
        graph = {}
        
        for j in xrange(flights):
            flights_data = deque([re.sub(r'(\.\d+)', '', x) for x in f.readline().split()])

            from_node = flights_data.popleft()
            if not graph.get(from_node):
                graph[from_node] = []
            to = flights_data.popleft()
            depart = hours_to_minutes(flights_data.popleft())
            arrive = hours_to_minutes(flights_data.popleft())
            cost = flights_data.popleft()
            
            graph[from_node] += {(to, depart, arrive, cost)}
        pprint(graph)
        

    