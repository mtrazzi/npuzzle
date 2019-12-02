import tests.test_core as core

print("------------------- Snail TEST -------------------")
core.test_snail()

print("------------------- Row   TEST -------------------")
core.test_row()

print("------------------- A*    TEST -------------------")
core.test_AStar(3)

print("------------------- BFS   TEST -------------------")
core.test_BFS(3)

print("----------------- Euclidean TEST -----------------")
core.test_euclidean(3)

print("----------------- Manhattan TEST -----------------")
core.test_manhattan(3)

print("----------------- Tiles-out TEST -----------------")
core.test_tiles_out(3)

print("--------------- Uniform-cost TEST ----------------")
core.test_uniform_cost(3)

print("------------------ Size 4 TEST -------------------")
core.test_size4(3)

print("------------------ Size 5 TEST -------------------")
core.test_size5(1)

print("------------- Unsolvable Snail TEST --------------")
core.test_unsolvable_snail(5)

print("------------- Unsolvable  Row  TEST --------------")
core.test_unsolvable_row(5)
