import re
with open('sample-input.txt', 'r') as f:
    n = int(f.readline())
    for i in xrange(n):
        f.readline()
        flights = int(f.readline())
        
        graph = {}
        
        for j in xrange(flights):
            flights_data = [re.sub(r'(:\d+)|(\.\d+)', '', x) for x in f.readline().split()]
            print flights_data