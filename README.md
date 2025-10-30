# Oregon Pathfinder

A pathfinding program with Dijkstra's Algorithm, Greedy Best-First Search, and A* using the provided Oregon highway data

## How to use

### Running the Program

Navigate to the project

   cd oregon_pathfinder

Run project

   python3 main.py
   
Enter 1-4 to continue

### Example Runs (3)

base) Chromebook:oregon_pathfinder connoreveretts$ conda activate base
p(base) Chromebook:oregon_pathfinder connoreveretts$ python3 main.py

==================================================
Oregon Pathfinder
==================================================

Select pathfinding algorithm:
1. Dijkstra's Algorithm
2. Greedy Best-First Search
3. A* Algorithm
4. Exit

Enter choice (1-4): 1
Enter start city: Salem
Enter destination city: Roseburg

Running Dijkstra's Algorithm...

Path found: Salem → Eugene → Roseburg
Total distance: 134.0 miles
Vertices explored: 8
Edges evaluated: 24
Execution time: 0.000151 seconds

==================================================
Oregon Pathfinder
==================================================

Select pathfinding algorithm:
1. Dijkstra's Algorithm
2. Greedy Best-First Search
3. A* Algorithm
4. Exit

Enter choice (1-4): 2     
Enter start city: Newport
Enter destination city: Bend

Running Greedy Best-First Search...

Path found: Newport → Corvallis → Eugene → Bend
Total distance: 224.0 miles
Vertices explored: 4
Edges evaluated: 12
Execution time: 0.002571 seconds

==================================================
Oregon Pathfinder
==================================================

Select pathfinding algorithm:
1. Dijkstra's Algorithm
2. Greedy Best-First Search
3. A* Algorithm
4. Exit

Enter choice (1-4): 3
Enter start city: Pendleton
Enter destination city: Medford

Running A* Algorithm...

Path found: Pendleton → The_Dalles → Hood_River → Portland → Salem → Eugene → Roseburg → Medford
Total distance: 476.0 miles
Vertices explored: 13
Edges evaluated: 33
Execution time: 0.000426 seconds


### Required Test Cases

#### Test Case 1: Short Distance - Portland → Salem

Dijkstra's Algorithm found Portland → Salem at 47.0 miles.
Explores 2 vertices and 4 edges in 0.000263 seconds. 
Greedy Best-First Search found Portland → Salem at 47.0 miles, explores 2 vertices and 4 edges in 0.000154 seconds. 
A* Algorithm found Portland → Salem at 47.0 miles, explores 2 vertices and 4 edges in 0.000072 seconds.

#### Test Case 2: Medium Distance - Portland → Eugene
Dijkstra's Algorithm found Portland → Salem → Eugene at 111.0 miles, explores 7 vertices and 17 edges in 0.000135 seconds. 
Greedy Best-First Search found Portland → Salem → Eugene at 111.0 miles, explores 3 vertices and 7 edges in 0.000113 seconds. 
A* Algorithm found Portland → Salem → Eugene at 111.0 miles, explores 3 vertices and 7 edges in 0.000368 seconds.

#### Test Case 3: Long Distance - Portland → Ashland
Dijkstra's Algorithm found Portland → Salem → Eugene → Roseburg → Medford → Ashland at 283.0 miles, and explores 20 vertices and 51 edges in 0.000271 seconds. 
Greedy Best-First Search found Portland → Newport → Florence → Coos_Bay → Roseburg → Medford → Ashland at 412.0 miles, and explores 7 vertices and 18 edges in 0.000176 seconds. 
A* Algorithm found Portland → Salem → Eugene → Roseburg → Medford → Ashland at 283.0 miles, and explores 8 vertices and 23 edges in 0.000164 seconds.

#### Test Case 4: Diagonal Route - Portland → Burns
Dijkstra's Algorithm found Portland → Hood_River → The_Dalles → Madras → Redmond → Bend → Burns at 351.0 miles, and explores 22 vertices and 53 edges in 0.000199 seconds. 
Greedy Best-First Search found Portland → Hood_River → The_Dalles → Madras → Redmond → Bend → Burns at 351.0 miles, and explores 7 vertices and 16 edges in 0.000142 seconds. 
A* Algorithm found Portland → Hood_River → The_Dalles → Madras → Redmond → Bend → Burns at 351.0 miles, and explores 10 vertices and 27 edges in 0.000502 seconds.

#### Test Case 5: Coastal vs. Inland - Portland → Medford
Dijkstra's Algorithm found Portland → Salem → Eugene → Roseburg → Medford at 268.0 miles, and explores 19 vertices and 48 edges in 0.003464 seconds.
Greedy Best-First Search found Portland → Newport → Florence → Coos_Bay → Roseburg → Medford at 397.0 miles, and explores 6 vertices and 15 edges in 0.001211 seconds. 
A* Algorithm found Portland → Salem → Eugene → Roseburg → Medford at 268.0 miles, and explores 6 vertices and explores 18 edges in 0.000140 seconds.

## Reflection


I tested all three of the pathfinding algorithms using all of the test cases and compared their performance and behavior. The results show a clear difference in quality and speed.


Dijkstra's algorithm always found the best path in all five of the test cases, but it also explored the most vertices in every scenario. Which makes sense as it finds every possible route and compares from there. While this did give us the right answer, it uses significantly more computational power and time than the other algorithms.


Greedy Best First Search was the most efficient in terms of verties explored, it examined the least amount of vertices, but it did affect the optimality. The two main examples were test cases (Portland to Ashland and Portland to Medford). It found suboptimal paths that were about 129 miles longer than the optimal route. The algorithm assumed by straight line distance and using coastal routes through Newport that it would be closer to the southern destination, but it was actually longer. Greedy only found optional paths when the heuristic happened to align with the actual road geometry, as in the Portland to BURNS route. But the executions were faster.


The A* algorithm did the best overall, which isn't shocking, but it found the most optimal in each test case and explored way fewer vertices than Dijkstra. It was considerably less, being around 60% less, while still always finding the most optimal oath. For example, A* explored only 6 vertices compared to Dijkstra's 19, yet both found the 268-mile optimal path.


Each algorithm has a time when it excels. Dijkstra's Algorithm is best when you need to guarantee shortest paths and don't have any reliable heuristic function, and is useful when computing the shortest path from one source to all other destinations. But point for ot point it would be very inefficient.


Greedy Best First should only be used when speed is most critical and the output is okay to be wrong sometimes. It's an average algorithm, but I can't think of a justification to use this over something else.


A* is clearly the best choice as it's most practical and combines the optimality guarantee with high efficiency. The test data shows it always finds optimal paths while exploring a fraction of the vertices of Dijkstra. This makes this the best choice for GPS and many more applications.


It seems all three algorithms have the same worst-case time complexity of O((V+E)log V), where V is the vertices and E is the edges. The log V is from the priority queue operations for the binary leaps. But their average case performances do differ a lot based on the prior choice of vertex exploration.


Dijkstra explores vertices in the strict order of actual distance from the source, going in all directions, and we see this in the test data, as even when there are 5-7 cities, it goes 19-22 vertices for longer routes. This is evidence of every vertex being explored in the directions.


A* uses f(n) = g(n) + h(n) to prioritize vertices where g(n) is the cost from the start and h(n) is the cost to the goal or the expected cost. The tests all show that its search reduces exploration. For example, for Portland-Medford, A* explored only 6 vertices compared to Dijkstra's 19, a 68% reduction.


Greedy just uses only h(n) for prioritization, achieving more focused exploration, but at the cost of optimization. The data shows it only goes 6-7 vertices for long routes, but at the cost of missing optimal paths.


The Haversine formula, from my understanding, is the calculation of great circle distance between latitude/longitude coordinates to represent the shortest path possible on Earth's surface. This is admissible for A* because straight line distance will never overestimate the actual road distance, which is needed for A *'s optimal guarantee.


But the test results showed the limitations of the Haversine heuristic in Oregon geography. For the Portland Medford route, Newport is geographically closer to Medford than Salem in straight-line distance. This is what caused greedy best first to choose the coastal route, which is 129 miles longer since there are winding roads and mountains.


The heuristic did well for the Portland Burns route, where the train is straight and less options to choose from. All three did good and found the right path. This is an example of how heuristic effectiveness varies with geography and roads. For A*, the heuristic guarantees optimality while giving guidance. For Greedy, even straight line distances can be way too misleading and break the optimal route.