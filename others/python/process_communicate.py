from multiprocessing import Process, Pipe, Queue

# One end send and another receive
conn1, conn2 = Pipe()
queue = Queue()

def f1():
	conn1.send('Hello Lin')
	queue.put('Hello Ping')

def f2():
	data = conn2.recv()
	data2 = queue.get()
	print(data, data2)

def main():
	Process(target=f1).start()
	Process(target=f2).start()

if __name__ == '__main__':
	main()

