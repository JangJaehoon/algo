# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
a = int(input())
print(a)
def inputArray():
	for _ in range(a):
		grid = list(map(int, input().split()))
		print(grid)

def bubbleSort(grid):
	for i in range(len(grid)-1):
		for j in range(len(grid)-i-1):
			if grid[j] > grid[j+1]:
				grid[j], grid[j+1] = grid[j+1], grid[j]
				print(grid)

if __name__ == "__main__":
	inputArray()
	bubbleSort()