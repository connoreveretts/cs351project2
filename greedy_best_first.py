import heapq
import time
from algorithm_result import AlgorithmResult

# Greedy Best First Search Algorithm
class GreedyBestFirstSearch:
    def find_path(self, graph, start_vertex_name, destination_vertex_name):
        start_time = time.time()
        vertices_explored = 0
        edges_evaluated = 0
        
        # Check if start and end place exist
        if not graph.has_vertex(start_vertex_name) or not graph.has_vertex(destination_vertex_name):
            execution_time = time.time() - start_time
            return AlgorithmResult("", 0.0, vertices_explored, edges_evaluated, execution_time, False)
        
        # Setting up priority queue
        heuristic = graph.haversine_distance(start_vertex_name, destination_vertex_name)
        priority_queue = [(heuristic, start_vertex_name)]
        previous_vertices = {}
        visited = set()
        actual_distances = {start_vertex_name: 0}
        
        # Main loop
        while priority_queue:
            current_heuristic, current_vertex = heapq.heappop(priority_queue)
            
            # Skip if already visited
            if current_vertex in visited:
                continue
            visited.add(current_vertex)
            vertices_explored += 1
            
            # Check if end is reached
            if current_vertex == destination_vertex_name:
                break
            
            # Look at neighbors
            for neighbor, highway, edge_distance in graph.get_neighbors(current_vertex):
                edges_evaluated += 1
                
                # If neighbor not visited
                if neighbor not in visited:
                    neighbor_heuristic = graph.haversine_distance(neighbor, destination_vertex_name)
                    heapq.heappush(priority_queue, (neighbor_heuristic, neighbor))
                    
                    # Record the path
                    if neighbor not in previous_vertices:
                        previous_vertices[neighbor] = current_vertex
                        actual_distances[neighbor] = actual_distances[current_vertex] + edge_distance
        
        # If no path found
        if destination_vertex_name not in previous_vertices and destination_vertex_name != start_vertex_name:
            execution_time = time.time() - start_time
            return AlgorithmResult("", 0.0, vertices_explored, edges_evaluated, execution_time, False)
        path = []
        current = destination_vertex_name
        
        # Recreate the path
        while current != start_vertex_name:
            path.append(current)
            current = previous_vertices[current]
        path.append(start_vertex_name)
        path.reverse()
        textual_directions = " → ".join(path)
        total_distance = actual_distances[destination_vertex_name]
        execution_time = time.time() - start_time
        return AlgorithmResult(textual_directions, total_distance, vertices_explored, edges_evaluated, execution_time, True)
    
    def get_name(self):
        return "Greedy Best-First Search"
