from utils.data_structures import Queue, OrientedGraph, State, ThreadSafeList, PriorityQueue

import json
import pickle
from typing import List, Dict, Tuple
import types

db_path = "./heuristics/databases/"
database_pointer_list = ThreadSafeList()
graph_pointer_list = ThreadSafeList()

def getDatabase(database_name):
	for i in range(database_pointer_list.size()):
		if database_name == database_pointer_list.get(i)[0]:
			return database_pointer_list.get(i)[1]
	try:
		with open(db_path + database_name + ".pickle", "rb") as f:
			database = (database_name, [pickle.load(f)])
	except FileNotFoundError:
		database = (database_name, [{"entries" : [], "generation_queue" : [], "complete" : False}])
	database_pointer_list.append(database)

	return database[1]

def getGraph(database_name):
	for i in range(graph_pointer_list.size()):
		if database_name == graph_pointer_list.get(i)[0]:
			return graph_pointer_list.get(i)[1]
	graph_pointer = [OrientedGraph()]
	graph_pointer_list.append((database_name, graph_pointer))
	return graph_pointer

def saveDatabase(database_name):
	for i in range(database_pointer_list.size()):
		if database_name == database_pointer_list.get(i)[0]:
			with open(db_path + database_name + ".pickle", "wb") as f:
				pickle.dump(database_pointer_list.get(i)[1][0], f, protocol=pickle.HIGHEST_PROTOCOL)

def evaluate(database_name: str, state_data: Tuple[State, List[str], Dict, State, types.FunctionType, Dict]):
	state = state_data[0]
	actions = state_data[1]
	action_constraints = state_data[2]
	goal = state_data[3]
	compareStates = state_data[4]
	argv = state_data[5]
	obj_type = type(state)

	graph_pointer = getGraph(database_name)
	state_node = None
	goal_node = None
	for node in graph_pointer[0].nodes:
		if node.value == state.represent():
			state_node = node
		if node.value == goal.represent():
			goal_node = node
	
	if goal_node is None:
		goal_node = graph_pointer[0].createNode(goal.represent())
		graph_pointer[0].addNode(goal_node)
	if state_node is None:
		state_node = graph_pointer[0].createNode(state.represent())
		graph_pointer[0].addNode(state_node)
	
	queued = [state_node]
	queue = Queue()
	queue.push((state_node, None))
	goal_reached = False
	while not (goal_reached or queue.isEmpty()):
		current, last_action = queue.pop()
		if compareStates(current.value, goal_node.value, argv):
			goal_reached = True
			continue
		obj = obj_type()
		obj.fromRepresentation(current.value)
		for action in actions:
			if action in action_constraints[last_action]:
				continue
			obj.apply(action)
			obj_repr = obj.represent()
			obj.apply(obj.reverse(action))

			if obj_repr in [item.value for item in queued]:
				continue

			node = None
			for n in graph_pointer[0].nodes:
				if compareStates(n.value, obj_repr, argv):
					node = n
					break
			if node is None:
				node = graph_pointer[0].createNode(obj_repr)
				graph_pointer[0].addNode(node)
			if (current, node, action) not in graph_pointer[0].connections:
				graph_pointer[0].connectNodes(current, node, action)
			queue.push((node, action))
			queued.append(node)
	
	path = graph_pointer[0].path(state_node, goal_node)
	if path is not None:
		path_queue = Queue()
		for step in path:
			path_queue.push(step)
		db_pointer = getDatabase(database_name)
		if compareStates(state_node.value, goal_node.value, argv):
			db_pointer[0]["states"].append(state_node.value)
			db_pointer[0]["values"].append(0)
		while not path_queue.isEmpty():
			current = path_queue.pop()
			if current[0].value in db_pointer[0]["states"]:
				break
			db_pointer[0]["states"].append(current[0].value)
			db_pointer[0]["values"].append(path_queue.size() + 1)
		saveDatabase(database_name)

def patternDatabaseHeuristic(database_name, state_data: Tuple[State, List[str], Dict, State, types.FunctionType, Dict]):
	database_pointer = getDatabase(database_name)
	for i in range(len(database_pointer[0]["entries"])):
		if state_data[4](state_data[0].represent(), database_pointer[0]["entries"][i][0], state_data[5]):
			return database_pointer[0]["entries"][1]
	evaluate(database_name, state_data)
	return database_pointer[0]["entries"][1]

def generateDatabase(database_name, goal: State, actions: List[str], action_restrictions: Dict, compareFunction: types.FunctionType, compare_args: Dict):
	def compare(item1, item2):
		return item1[1] <= item2[1]
	print(f"Starting generation of database '{database_name}'")
	database_pointer = getDatabase(database_name)
	if database_pointer[0]["complete"]:
		print(f"Database '{database_name}' already complete")
		return
	obj_type = type(goal)
	goal_repr = goal.represent()
	queue = PriorityQueue(compare)
	if len(database_pointer[0]["generation_queue"]) == 0:
		database_pointer[0]["entries"].append((goal_repr, 0))
		queue.push((goal_repr, 0, None))
	else:
		queue.fromList(database_pointer[0]["generation_queue"])

	processed_states = 0
	max_depth = -1
	while not queue.isEmpty():
		current, depth, last_action = queue.pop()
		if depth > max_depth:
			max_depth = depth
			print(f"Reached depth of \x1b[38;2;0;128;255m{depth}\x1b[39m for database '\x1b[38;2;0;255;255m{database_name}\x1b[39m'")
		obj = obj_type()
		obj.fromRepresentation(current)
		for action in actions:
			if action in action_restrictions[last_action]:
				continue
			obj.apply(action)
			obj_repr = obj.represent()
			obj.apply(obj.reverse(action))

			in_database = False
			for i in range(len(database_pointer[0]["entries"])):
				if compareFunction(obj_repr, database_pointer[0]["entries"][i][0], compare_args):
					in_database = True
					break
			if in_database:
				continue
			database_pointer[0]["entries"].append((obj_repr, depth + 1))
			processed_states += 1
			queue.push((obj_repr, depth + 1, action))
		
		if processed_states >= 100:
			database_pointer[0]["generation_queue"] = queue.toList()
			saveDatabase(database_name)
			processed_states = 0
	
	database_pointer[0]["complete"] = True
	database_pointer[0]["generation_queue"] = queue.toList()
	saveDatabase(database_name)
	print(f"Database '{database_name}' generated")