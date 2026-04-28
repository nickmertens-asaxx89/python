import datetime

read1 = input('Hit enter to start:')
start = datetime.datetime.now()
print(f'Starting time: {start}\n')

read2 = input('Hit enter to stop:')
stop = datetime.datetime.now()
print(f'Stopping time: {stop}\n')

print(f'Time elapsed: {stop-start}')