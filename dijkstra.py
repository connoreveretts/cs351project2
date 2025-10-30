import heapq
import time
from algorithm_result import AlgorithmResult

# Dijkstra's Algorithm
class DijkstraAlgorithm:
    # Main method to find the path
    def find_path(self, graph, start_vertex_name, destination_vertex_name):
        start_time = time.time()
        vertices_explored = 0
        edges_evaluated = 0
        
        # Check if start and end place exist
        if not graph.has_vertex(start_vertex_name) or not graph.has_vertex(destination_vertex_name):
            execution_time = time.time() - start_time
            return AlgorithmResult("", 0.0, vertices_explored, edges_evaluated, execution_time, False)
        # Setting up distances and priority queue
        distances = {start_vertex_name: 0}
        previous_vertices = {}
        priority_queue = [(0, start_vertex_name)]
        visited = set()
        
        # Main loop
        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)
            
            # Skip if already visited
            if current_vertex in visited:
                continue
            visited.add(current_vertex)
            vertices_explored += 1
            
            # Check if end is reached
            if current_vertex == destination_vertex_name:
                break
            
            # Look at neighbors for better path
            for neighbor, highway, edge_distance in graph.get_neighbors(current_vertex):
                edges_evaluated += 1
                new_distance = current_distance + edge_distance
                
                # If a better path is found
                if neighbor not in distances or new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous_vertices[neighbor] = current_vertex
                    heapq.heappush(priority_queue, (new_distance, neighbor))
        
        # If no path found
        if destination_vertex_name not in previous_vertices and destination_vertex_name != start_vertex_name:
            execution_time = time.time() - start_time
            return AlgorithmResult("", 0.0, vertices_explored, edges_evaluated, execution_time, False)
        path = []
        current = destination_vertex_name
        
        # Reconstruct the path
        while current != start_vertex_name:
            path.append(current)
            current = previous_vertices[current]
        path.append(start_vertex_name)
        path.reverse()
        textual_directions = " → ".join(path)
        total_distance = distances[destination_vertex_name]
        execution_time = time.time() - start_time
        return AlgorithmResult(textual_directions, total_distance, vertices_explored, edges_evaluated, execution_time, True)
    
    def get_name(self):
        return "Dijkstra's Algorithm"
