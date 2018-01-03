"""
	Created by Avinash on 2nd Jan, 2017
"""
from collections import namedtuple
from itertools import permutations

dimension = namedtuple("Dimension","height length width")

def create_rotation(given_dimensions):
	for current_dim in given_dimensions :
		for (height, length, width) in permutations((current_dim.height,current_dim.length,current_dim.width)) :
			if length >= width :
				yield dimension(height,length,width)

def sort_by_decreasing_area(rotations):
	return sorted(rotations, key = lambda dim : dim.length * dim.width, reverse = True)

def can_stack(box1,box2):
	return box1.length < box2.length and box1.width < box2.width

def boxstack(dimensions):
	boxes = sort_by_decreasing_area([rotation for rotation in create_rotation(dimensions)])
	num_boxes = len(boxes)
	T = [rotation.height for rotation in boxes]
	R = [id for id in range(num_boxes)]
	for i in range(1, num_boxes) :
		for j in range(0,i) :
			if can_stack(boxes[i],boxes[j]) :
				stacked_height = T[j] + boxes[i].height
				if stacked_height > T[i] : 
					T[i] = stacked_height
					R[i] = j
	max_height = max(T)
	start_index = T.index(max_height)
	while True :
		print(boxes[start_index])
		next_index = R[start_index]
		if next_index == start_index :
			break
		start_index = next_index
	return max_height

if __name__ == "__main__" :
	d1 = dimension(4,7,9)
	d2 = dimension(5,8,9)
	d3 = dimension(11,20,40)
	d4 = dimension(1,2,3)
	height = boxstack([d1,d2,d3,d4])
	print("Maximum height possible with the given dimension of boxes is %d"%height)

