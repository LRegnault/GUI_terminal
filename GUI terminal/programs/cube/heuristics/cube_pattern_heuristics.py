from heuristics.pattern_database import patternDatabaseHeuristic, generateDatabase
from programs.cube.cubes.cube2x2 import Cube2x2
from programs.cube.cubes.cube3x3 import Cube3x3

from typing import Dict
import threading

def cube3x3PatternHeuristic(state: Cube3x3):
	return cube3x3CornerPatternHeuristic(state)

def cube3x3CornerPatternHeuristic(state: Cube3x3):
	state_repr = state.represent()
	state_2x2_repr = [
		0 * 2 ** 11 + 0 * 2 ** 8 + 0 * 2 ** 5 + state_repr[0] % 2 ** 5,
		0 * 2 ** 11 + 0 * 2 ** 8 + 1 * 2 ** 5 + state_repr[2] % 2 ** 5,
		0 * 2 ** 11 + 1 * 2 ** 8 + 0 * 2 ** 5 + state_repr[5] % 2 ** 5,
		0 * 2 ** 11 + 1 * 2 ** 8 + 1 * 2 ** 5 + state_repr[7] % 2 ** 5,
		1 * 2 ** 11 + 0 * 2 ** 8 + 0 * 2 ** 5 + state_repr[13] % 2 ** 5,
		1 * 2 ** 11 + 0 * 2 ** 8 + 1 * 2 ** 5 + state_repr[15] % 2 ** 5,
		1 * 2 ** 11 + 1 * 2 ** 8 + 0 * 2 ** 5 + state_repr[18] % 2 ** 5,
		1 * 2 ** 11 + 1 * 2 ** 8 + 1 * 2 ** 5 + state_repr[20] % 2 ** 5
		]

	state_2x2 = Cube2x2()
	state_2x2.fromRepresentation(state_2x2_repr)

	actions_2x2 = ["U", "U'", "U2", "F", "F'", "F2", "R", "R'", "R2"]
	actions_3x3 = ["U", "U'", "U2", "F", "F'", "F2", "R", "R'", "R2", "D", "D'", "D2", "B", "B'", "B2", "L", "L'", "L2"]
	action_restrictions = {
		"U" : ["U", "U'", "U2"],
		"U'" : ["U", "U'", "U2"],
		"U2" : ["U", "U'", "U2"],
		"F" : ["F", "F'", "F2"],
		"F'" : ["F", "F'", "F2"],
		"F2" : ["F", "F'", "F2"],
		"R" : ["R", "R'", "R2"],
		"R'" : ["R", "R'", "R2"],
		"R2" : ["R", "R'", "R2"],
		"D" : ["U", "U'", "U2", "D", "D'", "D2"],
		"D'" : ["U", "U'", "U2", "D", "D'", "D2"],
		"D2" : ["U", "U'", "U2", "D", "D'", "D2"],
		"B" : ["F", "F'", "F2", "B", "B'", "B2"],
		"B'" : ["F", "F'", "F2", "B", "B'", "B2"],
		"B2" : ["F", "F'", "F2", "B", "B'", "B2"],
		"L" : ["R", "R'", "R2", "L", "L'", "L2"],
		"L'" : ["R", "R'", "R2", "L", "L'", "L2"],
		"L2" : ["R", "R'", "R2", "L", "L'", "L2"],
		None : []
	}

	edge_subset_1 = [(1, 0, 0), (1, 0, 2), (0, 1, 2), (2, 1, 0), (0, 2, 1), (2, 2, 1)]
	edge_subset_2 = [(0, 0, 1), (2, 0, 1), (0, 1, 0), (2, 1, 2), (1, 2, 0), (1, 2, 2)]

	corners_ptr = []
	edges_1_ptr = []
	edges_2_ptr = []

	# corners_thread = threading.Thread(target=lambda ptr, arg1, arg2: ptr.append(patternDatabaseHeuristic(arg1, arg2)), args=(corners_ptr, ".cube2x2", (state_2x2, actions_2x2, action_restrictions, Cube2x2(), isEquivalent2x2, {})))
	# edges_1_thread = threading.Thread(target=lambda ptr, arg1, arg2: ptr.append(patternDatabaseHeuristic(arg1, arg2)), args=(edges_1_ptr, ".edges1", (state, actions_3x3, action_restrictions, Cube3x3(), isEquivalent3x3EdgeSubset, {"edge_subset" : edge_subset_1})))
	# edges_2_thread = threading.Thread(target=lambda ptr, arg1, arg2: ptr.append(patternDatabaseHeuristic(arg1, arg2)), args=(edges_2_ptr, ".edges2", (state, actions_3x3, action_restrictions, Cube3x3(), isEquivalent3x3EdgeSubset, {"edge_subset" : edge_subset_2})))

	corners_thread = threading.Thread(target=lambda ptr, arg1, arg2, arg3, arg4, arg5, arg6: ptr.append(generateDatabase(arg1, arg2, arg3, arg4, arg5, arg6)), args=(corners_ptr, ".cube2x2", Cube2x2(), actions_2x2, action_restrictions, isEquivalent2x2, {}), daemon=True)
	edges_1_thread = threading.Thread(target=lambda ptr, arg1, arg2, arg3, arg4, arg5, arg6: ptr.append(generateDatabase(arg1, arg2, arg3, arg4, arg5, arg6)), args=(edges_1_ptr, ".edges1", Cube3x3(), actions_3x3, action_restrictions, isEquivalent3x3EdgeSubset, {"edge_subset" : edge_subset_1}), daemon=True)
	edges_2_thread = threading.Thread(target=lambda ptr, arg1, arg2, arg3, arg4, arg5, arg6: ptr.append(generateDatabase(arg1, arg2, arg3, arg4, arg5, arg6)), args=(edges_2_ptr, ".edges2", Cube3x3(), actions_3x3, action_restrictions, isEquivalent3x3EdgeSubset, {"edge_subset" : edge_subset_2}), daemon=True)

	corners_thread.start()
	edges_1_thread.start()
	edges_2_thread.start()

	corners_thread.join()
	edges_1_thread.join()
	edges_2_thread.join()

	# return max(corners_ptr[0], max(edges_1_ptr[0], edges_2_ptr[0]))

def isEquivalent2x2(state_repr_1, state_repr_2, argv: Dict):
	translation_table = {
		"DBL" : [],
		"BLD" : ["x", "y"],
		"LDB" : ["z'", "y'"],
		"RBD" : ["z"],
		"DRB" : ["y'"],
		"BDR" : ["x", "y2"],
		"FDL" : ["x'"],
		"DLF" : ["y"],
		"LFD" : ["z'", "y2"],
		"FRD" : ["x'", "y'"],
		"RDF" : ["z", "y"],
		"DFR" : ["y2"],
		"ULB" : ["x2", "y"],
		"BUL" : ["x"],
		"LBU" : ["z'"],
		"UBR" : ["z2"],
		"RUB" : ["z", "y'"],
		"BRU" : ["x", "y'"],
		"UFL" : ["x2"],
		"FLU" : ["x'", "y"],
		"LUF" : ["z'", "y"],
		"URF" : ["x2", "y'"],
		"FUR" : ["x'", "y2"],
		"RFU" : ["z", "y2"]
	}

	state_1 = Cube2x2()
	state_2 = Cube2x2()
	state_1.fromRepresentation(state_repr_1)
	state_2.fromRepresentation(state_repr_2)

	if state_1.cube_array[0][0][0].sides["U"] == "y" and state_1.cube_array[0][0][0].sides["L"] == "b" and state_1.cube_array[0][0][0].sides["B"] == "o":
		state_1_orientation_key = "ULB"
	elif state_1.cube_array[0][0][0].sides["B"] == "y" and state_1.cube_array[0][0][0].sides["U"] == "b" and state_1.cube_array[0][0][0].sides["L"] == "o":
		state_1_orientation_key = "BUL"
	elif state_1.cube_array[0][0][0].sides["L"] == "y" and state_1.cube_array[0][0][0].sides["B"] == "b" and state_1.cube_array[0][0][0].sides["U"] == "o":
		state_1_orientation_key = "LBU"
	elif state_1.cube_array[0][0][1].sides["U"] == "y" and state_1.cube_array[0][0][1].sides["F"] == "b" and state_1.cube_array[0][0][1].sides["L"] == "o":
		state_1_orientation_key = "UFL"
	elif state_1.cube_array[0][0][1].sides["F"] == "y" and state_1.cube_array[0][0][1].sides["L"] == "b" and state_1.cube_array[0][0][1].sides["U"] == "o":
		state_1_orientation_key = "FLU"
	elif state_1.cube_array[0][0][1].sides["L"] == "y" and state_1.cube_array[0][0][1].sides["U"] == "b" and state_1.cube_array[0][0][1].sides["F"] == "o":
		state_1_orientation_key = "LUF"
	elif state_1.cube_array[0][1][0].sides["D"] == "y" and state_1.cube_array[0][1][0].sides["B"] == "b" and state_1.cube_array[0][1][0].sides["L"] == "o":
		state_1_orientation_key = "DBL"
	elif state_1.cube_array[0][1][0].sides["B"] == "y" and state_1.cube_array[0][1][0].sides["L"] == "b" and state_1.cube_array[0][1][0].sides["D"] == "o":
		state_1_orientation_key = "BLD"
	elif state_1.cube_array[0][1][0].sides["L"] == "y" and state_1.cube_array[0][1][0].sides["D"] == "b" and state_1.cube_array[0][1][0].sides["B"] == "o":
		state_1_orientation_key = "LDB"
	elif state_1.cube_array[0][1][1].sides["F"] == "y" and state_1.cube_array[0][1][1].sides["D"] == "b" and state_1.cube_array[0][1][1].sides["L"] == "o":
		state_1_orientation_key = "FDL"
	elif state_1.cube_array[0][1][1].sides["D"] == "y" and state_1.cube_array[0][1][1].sides["L"] == "b" and state_1.cube_array[0][1][1].sides["F"] == "o":
		state_1_orientation_key = "DLF"
	elif state_1.cube_array[0][1][1].sides["L"] == "y" and state_1.cube_array[0][1][1].sides["F"] == "b" and state_1.cube_array[0][1][1].sides["D"] == "o":
		state_1_orientation_key = "LFD"
	elif state_1.cube_array[1][0][0].sides["U"] == "y" and state_1.cube_array[1][0][0].sides["B"] == "b" and state_1.cube_array[1][0][0].sides["R"] == "o":
		state_1_orientation_key = "UBR"
	elif state_1.cube_array[1][0][0].sides["R"] == "y" and state_1.cube_array[1][0][0].sides["U"] == "b" and state_1.cube_array[1][0][0].sides["B"] == "o":
		state_1_orientation_key = "RUB"
	elif state_1.cube_array[1][0][0].sides["B"] == "y" and state_1.cube_array[1][0][0].sides["R"] == "b" and state_1.cube_array[1][0][0].sides["U"] == "o":
		state_1_orientation_key = "BRU"
	elif state_1.cube_array[1][0][1].sides["U"] == "y" and state_1.cube_array[1][0][1].sides["R"] == "b" and state_1.cube_array[1][0][1].sides["F"] == "o":
		state_1_orientation_key = "URF"
	elif state_1.cube_array[1][0][1].sides["F"] == "y" and state_1.cube_array[1][0][1].sides["U"] == "b" and state_1.cube_array[1][0][1].sides["R"] == "o":
		state_1_orientation_key = "FUR"
	elif state_1.cube_array[1][0][1].sides["R"] == "y" and state_1.cube_array[1][0][1].sides["F"] == "b" and state_1.cube_array[1][0][1].sides["U"] == "o":
		state_1_orientation_key = "RFU"
	elif state_1.cube_array[1][1][0].sides["R"] == "y" and state_1.cube_array[1][1][0].sides["B"] == "b" and state_1.cube_array[1][1][0].sides["D"] == "o":
		state_1_orientation_key = "RBD"
	elif state_1.cube_array[1][1][0].sides["D"] == "y" and state_1.cube_array[1][1][0].sides["R"] == "b" and state_1.cube_array[1][1][0].sides["B"] == "o":
		state_1_orientation_key = "DRB"
	elif state_1.cube_array[1][1][0].sides["B"] == "y" and state_1.cube_array[1][1][0].sides["D"] == "b" and state_1.cube_array[1][1][0].sides["R"] == "o":
		state_1_orientation_key = "BDR"
	elif state_1.cube_array[1][1][1].sides["F"] == "y" and state_1.cube_array[1][1][1].sides["R"] == "b" and state_1.cube_array[1][1][1].sides["D"] == "o":
		state_1_orientation_key = "FRD"
	elif state_1.cube_array[1][1][1].sides["R"] == "y" and state_1.cube_array[1][1][1].sides["D"] == "b" and state_1.cube_array[1][1][1].sides["F"] == "o":
		state_1_orientation_key = "RDF"
	elif state_1.cube_array[1][1][1].sides["D"] == "y" and state_1.cube_array[1][1][1].sides["F"] == "b" and state_1.cube_array[1][1][1].sides["R"] == "o":
		state_1_orientation_key = "DFR"
	
	if state_2.cube_array[0][0][0].sides["U"] == "y" and state_2.cube_array[0][0][0].sides["L"] == "b" and state_2.cube_array[0][0][0].sides["B"] == "o":
		state_2_orientation_key = "ULB"
	elif state_2.cube_array[0][0][0].sides["B"] == "y" and state_2.cube_array[0][0][0].sides["U"] == "b" and state_2.cube_array[0][0][0].sides["L"] == "o":
		state_2_orientation_key = "BUL"
	elif state_2.cube_array[0][0][0].sides["L"] == "y" and state_2.cube_array[0][0][0].sides["B"] == "b" and state_2.cube_array[0][0][0].sides["U"] == "o":
		state_2_orientation_key = "LBU"
	elif state_2.cube_array[0][0][1].sides["U"] == "y" and state_2.cube_array[0][0][1].sides["F"] == "b" and state_2.cube_array[0][0][1].sides["L"] == "o":
		state_2_orientation_key = "UFL"
	elif state_2.cube_array[0][0][1].sides["F"] == "y" and state_2.cube_array[0][0][1].sides["L"] == "b" and state_2.cube_array[0][0][1].sides["U"] == "o":
		state_2_orientation_key = "FLU"
	elif state_2.cube_array[0][0][1].sides["L"] == "y" and state_2.cube_array[0][0][1].sides["U"] == "b" and state_2.cube_array[0][0][1].sides["F"] == "o":
		state_2_orientation_key = "LUF"
	elif state_2.cube_array[0][1][0].sides["D"] == "y" and state_2.cube_array[0][1][0].sides["B"] == "b" and state_2.cube_array[0][1][0].sides["L"] == "o":
		state_2_orientation_key = "DBL"
	elif state_2.cube_array[0][1][0].sides["B"] == "y" and state_2.cube_array[0][1][0].sides["L"] == "b" and state_2.cube_array[0][1][0].sides["D"] == "o":
		state_2_orientation_key = "BLD"
	elif state_2.cube_array[0][1][0].sides["L"] == "y" and state_2.cube_array[0][1][0].sides["D"] == "b" and state_2.cube_array[0][1][0].sides["B"] == "o":
		state_2_orientation_key = "LDB"
	elif state_2.cube_array[0][1][1].sides["F"] == "y" and state_2.cube_array[0][1][1].sides["D"] == "b" and state_2.cube_array[0][1][1].sides["L"] == "o":
		state_2_orientation_key = "FDL"
	elif state_2.cube_array[0][1][1].sides["D"] == "y" and state_2.cube_array[0][1][1].sides["L"] == "b" and state_2.cube_array[0][1][1].sides["F"] == "o":
		state_2_orientation_key = "DLF"
	elif state_2.cube_array[0][1][1].sides["L"] == "y" and state_2.cube_array[0][1][1].sides["F"] == "b" and state_2.cube_array[0][1][1].sides["D"] == "o":
		state_2_orientation_key = "LFD"
	elif state_2.cube_array[1][0][0].sides["U"] == "y" and state_2.cube_array[1][0][0].sides["B"] == "b" and state_2.cube_array[1][0][0].sides["R"] == "o":
		state_2_orientation_key = "UBR"
	elif state_2.cube_array[1][0][0].sides["R"] == "y" and state_2.cube_array[1][0][0].sides["U"] == "b" and state_2.cube_array[1][0][0].sides["B"] == "o":
		state_2_orientation_key = "RUB"
	elif state_2.cube_array[1][0][0].sides["B"] == "y" and state_2.cube_array[1][0][0].sides["R"] == "b" and state_2.cube_array[1][0][0].sides["U"] == "o":
		state_2_orientation_key = "BRU"
	elif state_2.cube_array[1][0][1].sides["U"] == "y" and state_2.cube_array[1][0][1].sides["R"] == "b" and state_2.cube_array[1][0][1].sides["F"] == "o":
		state_2_orientation_key = "URF"
	elif state_2.cube_array[1][0][1].sides["F"] == "y" and state_2.cube_array[1][0][1].sides["U"] == "b" and state_2.cube_array[1][0][1].sides["R"] == "o":
		state_2_orientation_key = "FUR"
	elif state_2.cube_array[1][0][1].sides["R"] == "y" and state_2.cube_array[1][0][1].sides["F"] == "b" and state_2.cube_array[1][0][1].sides["U"] == "o":
		state_2_orientation_key = "RFU"
	elif state_2.cube_array[1][1][0].sides["R"] == "y" and state_2.cube_array[1][1][0].sides["B"] == "b" and state_2.cube_array[1][1][0].sides["D"] == "o":
		state_2_orientation_key = "RBD"
	elif state_2.cube_array[1][1][0].sides["D"] == "y" and state_2.cube_array[1][1][0].sides["R"] == "b" and state_2.cube_array[1][1][0].sides["B"] == "o":
		state_2_orientation_key = "DRB"
	elif state_2.cube_array[1][1][0].sides["B"] == "y" and state_2.cube_array[1][1][0].sides["D"] == "b" and state_2.cube_array[1][1][0].sides["R"] == "o":
		state_2_orientation_key = "BDR"
	elif state_2.cube_array[1][1][1].sides["F"] == "y" and state_2.cube_array[1][1][1].sides["R"] == "b" and state_2.cube_array[1][1][1].sides["D"] == "o":
		state_2_orientation_key = "FRD"
	elif state_2.cube_array[1][1][1].sides["R"] == "y" and state_2.cube_array[1][1][1].sides["D"] == "b" and state_2.cube_array[1][1][1].sides["F"] == "o":
		state_2_orientation_key = "RDF"
	elif state_2.cube_array[1][1][1].sides["D"] == "y" and state_2.cube_array[1][1][1].sides["F"] == "b" and state_2.cube_array[1][1][1].sides["R"] == "o":
		state_2_orientation_key = "DFR"
	
	for action in translation_table[state_1_orientation_key]:
		state_1.apply(action)
	
	for action in translation_table[state_2_orientation_key]:
		state_2.apply(action)
	
	return state_1.represent() == state_2.represent()

def isEquivalent3x3EdgeSubset(state_repr_1, state_repr_2, argv: Dict):
	translation_table = {
		"UF" : [],
		"UR" : ["y"],
		"UB" : ["y2"],
		"UL" : ["y'"],
		"FU" : ["x", "y2"],
		"FR" : ["x", "y"],
		"FD" : ["x"],
		"FL" : ["x", "y'"],
		"RU" : ["z'", "y'"],
		"RF" : ["z'"],
		"RD" : ["z'", "y"],
		"RB" : ["z'", "y2"],
		"DF" : ["z2"],
		"DR" : ["x2", "y"],
		"DB" : ["x2"],
		"DL" : ["z2", "y"],
		"BU" : ["x'"],
		"BR" : ["x'", "y"],
		"BD" : ["x'", "y2"],
		"BL" : ["x'", "y'"],
		"LU" : ["z", "y"],
		"LF" : ["z"],
		"LD" : ["z", "y'"],
		"LB" : ["z", "y2"]
	}

	state_1 = Cube3x3()
	state_2 = Cube3x3()
	state_1.fromRepresentation(state_repr_1)
	state_2.fromRepresentation(state_repr_2)

	w_state_1 = ""
	g_state_1 = ""
	for side in state_1.cube:
		if state_1.cube[side][1][1] == "w":
			w_state_1 = side
		elif state_1.cube[side][1][1] == "g":
			g_state_1 = side
		if w_state_1 != "" and g_state_1 != "":
			break
	state_1_orientation_key = w_state_1 + g_state_1

	w_state_2 = ""
	g_state_2 = ""
	for side in state_1.cube:
		if state_2.cube[side][1][1] == "w":
			w_state_2 = side
		elif state_2.cube[side][1][1] == "g":
			g_state_2 = side
		if w_state_2 != "" and g_state_2 != "":
			break
	state_2_orientation_key = w_state_2 + g_state_2

	for action in translation_table[state_1_orientation_key]:
		state_1.apply(action)
	
	for action in translation_table[state_2_orientation_key]:
		state_2.apply(action)
	
	edge_subset = argv["edge_subset"]
	for x, y, z in edge_subset:
		for side in state_1.cube_array[x][y][z].sides:
			if state_1.cube_array[x][y][z].sides[side] != state_2.cube_array[x][y][z].sides[side]:
				return False
	return True