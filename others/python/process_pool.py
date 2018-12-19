from multiprocessing import Pool

def f(i):
	print(i, end=' ')

def main():
	pool = Pool(processes=3)
	for i in range(30):
		pool.apply(f, (i,))

if __name__ == '__main__':
	main()

