import copy
import threading
import math

class ThreadSafeList:
    def __init__(self):
        self._list = list()
        self._lock = threading.Lock()
    
    def __repr__(self):
        with self._lock:
            return self.list.__repr__()
    
    def append(self, value):
        with self._lock:
            self._list.append(value)

    def pop(self):
        with self._lock:
            return self._list.pop()
    
    def get(self, index):
        with self._lock:
            return self._list[index]
    
    def size(self):
        with self._lock:
            return len(self._list)

class OrientedGraph:
	class Node:
		def __init__(self, id, value):
			self.id = id
			self.value = value
		
		def __repr__(self):
			return str(self.value)
	
	def __init__(self):
		self.next_node_id = 0

		self.nodes = []
		self.connections = []
	
	def __repr__(self):
		return str(self.nodes) + "\n" + str(self.connections)

	def createNode(self, node_value):
		node = self.Node(self.next_node_id, node_value)
		self.next_node_id += 1
		return node

	def addNode(self, node):
		self.nodes.append(node)
	
	def removeNode(self, node):
		for connection in self.connections:
			if connection[0] == node or connection[1] == node:
				self.removeConnection(connection)
		self.nodes.remove(node)
	
	def connectNodes(self, source_node, destination_node, label=""):
		self.connections.append((source_node, destination_node, label))
	
	def removeConnection(self, connection):
		self.connections.remove(connection)
	
	def isConnected(self, source_node, destination_node):
		return self.path(source_node, destination_node) is not None
	
	def size(self):
		return len(self.nodes)
	
	def path(self, source_node, destination_node):
		queued = []
		queue = Queue()
		queue.push((source_node, []))
		while not queue.isEmpty():
			current, path = queue.pop()
			queued.append(current)
			if current.value == destination_node.value:
				return path
			else:
				for connection in self.connections:
					if connection[0] == current:
						if connection[1] not in queued:
							tmp = copy.deepcopy(path)
							tmp.append(connection)
							queue.push((connection[1], tmp))
							queued.append(connection[1])
		return None

class Tree:
	class Node:
		def __init__(self, value):
			self.value = value
			self.childs = []
	
	def __init__(self):
		self.root = None
		self.nodes = []
	
	def getParent(self, node):
		for n in self.nodes:
			if node in n.childs:
				return n
	
	def addNode(self, node, parent):
		parent.childs.append(node)
		self.nodes.append(node)
	
	def removeNode(self, node):
		if len(node.childs) > 0:
			raise RuntimeError("Tree.removeNode: tried to remove non-leaf node")
		
		parent = self.getParent(node)
		return parent.childs.pop(parent.childs.index(node))

class Stack:
	def __init__(self):
		self.stack = []
	
	def size(self):
		return len(self.stack)
	
	def isEmpty(self):
		return self.size() == 0
	
	def push(self, item):
		self.stack.append(item)
	
	def pop(self):
		if self.isEmpty():
			raise RuntimeError("Stack.pop(): stack is empty")
		return self.stack.pop()

class Queue:
	def __init__(self):
		self.input_stack = Stack()
		self.output_stack = Stack()
	
	def size(self):
		return self.input_stack.size() + self.output_stack.size()
	
	def isEmpty(self):
		return self.size() == 0
	
	def push(self, item):
		self.input_stack.push(item)
	
	def pop(self):
		if self.isEmpty():
			raise RuntimeError("Queue.pop(): queue is empty")
		if self.output_stack.isEmpty():
			n = self.input_stack.size()
			for i in range(n):
				self.output_stack.push(self.input_stack.pop())
		return self.output_stack.pop()
	
	def toList(self):
		output = self.output_stack.stack
		output.reverse()
		return output + self.input_stack.stack

class Heap:
	def __init__(self, comparison_function, low_root=True):
		self.compare = comparison_function # checks if param1 is >= to param2
		self.low_root = low_root
		self.heap = []
	
	def size(self):
		return len(self.heap)
	
	def isEmpty(self):
		return self.size() == 0
	
	def height(self):
		return math.floor(math.log2(self.size()))
	
	def trickle(self, i):
		k = i + 1
		v = self.heap[k - 1]
		is_heap = False
		while not is_heap and 2 * k <= self.size():
			j = 2 * k
			if j < self.size():
				if not self.compare(self.heap[j - 1], self.heap[j]):
					j += 1
				if self.compare(v, self.heap[j - 1]):
					is_heap = True
				else:
					self.heap[k - 1] = self.heap[j - 1]
					k = j
		self.heap[k - 1] = v
	
	def sift(self, i):
		v = self.heap[i]
		while i > 0 and not self.compare(self.heap[math.floor(i / 2)], v):
			self.heap[i] = self.heap[math.floor(i / 2)]
			i = math.floor(i / 2)
		self.heap[i] = v
	
	def addLeaf(self, item):
		self.heap.append(item)
		self.sift(self.size() - 1)
	
	def RemoveRoot(self):
		root = self.heap[0]
		self.heap[0] = self.heap[-1]
		if self.size() <= 1:
			self.heap = []
		else:
			self.heap[:-1]
			self.trickle(0)
		return root
	
	def toList(self):
		return self.heap
	
	def fromList(self, l):
		self.heap = []
		for item in l:
			self.addLeaf(item)

class PriorityQueue:
	def __init__(self, comparison_function):
		self.heap = Heap(comparison_function)
	
	def size(self):
		return self.heap.size()
	
	def isEmpty(self):
		return self.heap.isEmpty()
	
	def push(self, item):
		self.heap.addLeaf(item)
	
	def pop(self):
		return self.heap.RemoveRoot()
	
	def toList(self):
		return self.heap.toList()
	
	def fromList(self, l):
		self.heap.fromList(l)

class State:
	def __init__(self):
		pass

	def represent(self):
		pass
	
	def fromRepresentation(self, representation):
		pass

	def reverse(self, action):
		pass

	def apply(self, action):
		pass