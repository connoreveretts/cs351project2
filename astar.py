import heapq
import time
from algorithm_result import AlgorithmResult

# A* Algoritmn
class AStarAlgorithm:
    # Main method to find the path
    def find_path(self, graph, start_vertex_name, destination_vertex_name):
        start_time = time.time()
        vertices_explored = 0
        edges_evaluated = 0
        
        # Check if start and end place exist
        if not graph.has_vertex(start_vertex_name) or not graph.has_vertex(destination_vertex_name):
            execution_time = time.time() - start_time
            return AlgorithmResult("", 0.0, vertices_explored, edges_evaluated, execution_time, False)
        
        # Setting the priority queue and scores
        g_scores = {start_vertex_name: 0}
        h_score = graph.haversine_distance(start_vertex_name, destination_vertex_name)
        f_score = g_scores[start_vertex_name] + h_score
        priority_queue = [(f_score, start_vertex_name)]
        previous_vertices = {}
        visited = set()
        
        # Main loop
        while priority_queue:
            current_f_score, current_vertex = heapq.heappop(priority_queue)
            
            # Skip if already visited
            if current_vertex in visited:
                continue
            visited.add(current_vertex)
            vertices_explored += 1
            
            # Check if end is reached
            if current_vertex == destination_vertex_name:
                break
        
            # Explore neighbors for better path
            for neighbor, highway, edge_distance in graph.get_neighbors(current_vertex):
                edges_evaluated += 1
                new_g_score = g_scores[current_vertex] + edge_distance
                
                # If a better path is found
                if neighbor not in g_scores or new_g_score < g_scores[neighbor]:
                    g_scores[neighbor] = new_g_score
                    h_score = graph.haversine_distance(neighbor, destination_vertex_name)
                    f_score = new_g_score + h_score
                    previous_vertices[neighbor] = current_vertex
                    heapq.heappush(priority_queue, (f_score, neighbor))
        
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
        total_distance = g_scores[destination_vertex_name]
        execution_time = time.time() - start_time
        return AlgorithmResult(textual_directions, total_distance, vertices_explored, edges_evaluated, execution_time, True)
    
    def get_name(self):
        return "A* Algorithm"
