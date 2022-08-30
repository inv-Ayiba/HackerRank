#sequenceOfnumberAndg for each array inside sf(array[1])=array[0] and g(array[0])=array[1]
sequenceOfnumberAndg = [[1, 1], [2, 2], [3, 5], [4, 15], [5, 25], [6, 3], [7, 13], [8, 23], [9, 6], [10, 16], [11, 26], [12, 44], [13, 144], [14, 256], [15, 36], [16, 136], [17, 236], [18, 67], [19, 167], [20, 267], [21, 349], [22, 1349], [23, 2349], [24, 49], [25, 149], [26, 249], [27, 9], [28, 19], [29, 29], [30, 129], [31, 229], [32, 1229], [33, 39], [34, 139], [35, 239], [36, 1239],[37, 13339],[38 , 23599],[39 , 44679],[40 , 44079]]
sequenceOfnumberAndSg= [[1, 1], [2, 2], [3, 5], [4, 6], [5, 7], [6, 3], [7, 4], [8, 5], [9, 6], [10, 7], [11, 8], [12, 8], [13, 9], [14, 13], [15, 9], [16, 10], [17, 11], [18, 13], [19, 14], [20, 15], [21, 16], [22, 17], [23, 18], [24, 13], [25, 14], [26, 15], [27, 9], [28, 10], [29, 11], [30, 12], [31, 13], [32, 14], [33, 12], [34, 13], [35, 14], [36, 15],[37, 19],[38 , 28],[39 , 30],[40 , 24]]
# Python code for the above approach
class Node:
	def __init__(self, d):
		self.data = d
		self.next = None

# initialize a new head for the linked list
head = None

# detect if there is a loop
# in the linked list
def detectLoop(head):
	slowPointer = head
	fastPointer = head

	while (slowPointer != None
		and fastPointer != None
		and fastPointer.next != None):
		slowPointer = slowPointer.next
		fastPointer = fastPointer.next.next
		if (slowPointer == fastPointer):
			return 1

	return 0

# inserting new values
target=sequenceOfnumberAndSg


head=Node(target[0][1])
print(target[0],head.data)
rat= head.next=Node(target[1][1])
print(target[1],rat.data)

for i in range(2,len(target)):
    poop=rat.next=Node(target[i][1]);print(target[i],poop.data)
	

# # head = Node(10)
# # head.next = Node(20)
# # head.next.next = Node(30)
# # head.next.next.next = Node(40)
# # head.next.next.next.next = Node(50)

# adding a loop for the sake
# of this example
temp = head
while (temp.next != None):
	temp = temp.next

temp.next = head


# loop added;
if (detectLoop(head)):
	print("Loop exists in the Linked List")
else:
	print("Loop does not exists in the Linked List")



