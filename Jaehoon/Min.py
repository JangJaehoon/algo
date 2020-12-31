def inputArray():
    	for _ in range(2):
		grid = list(map(int, input().split()))
		return grid

def MinInput(grid):
	print(min(grid))				 
				 
if __name__ == "__main__":
	MinInput(inputArray)