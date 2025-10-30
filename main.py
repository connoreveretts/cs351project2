from graph import Graph
from dijkstra import DijkstraAlgorithm
from greedy_best_first import GreedyBestFirstSearch
from astar import AStarAlgorithm

# Main function
def load_graph():
    graph = Graph()
    
    # Load files
    with open('vertices_v1.txt', 'r') as file:
        lines = file.readlines()
        for line in lines[1:]:
            line = line.strip()
            if line:
                parts = line.split(',')
                vertex_name = parts[0]
                latitude = float(parts[1])
                longitude = float(parts[2])
                graph.add_vertex(vertex_name, latitude, longitude)
    
    # Load edges
    with open('graph_v2.txt', 'r') as file:
        lines = file.readlines()
        for line in lines[1:]:
            line = line.strip()
            if line:
                parts = line.split(',')
                source = parts[0]
                destination = parts[1]
                highway = parts[2]
                distance = float(parts[3])
                graph.add_edge(source, destination, highway, distance)
    return graph

# Function to display results
def display_result(result, algorithm_name):
    print(f"\nRunning {algorithm_name}...")
    if not result.path_found:
        print("\nNo path found")
        print(f"Vertices explored: {result.vertices_explored}")
        print(f"Edges evaluated: {result.edges_evaluated}")
        print(f"Execution time: {result.execution_time:.6f} seconds")
    else:
        print(f"\nPath found: {result.textual_directions}")
        print(f"Total distance: {result.total_distance:.1f} miles")
        print(f"Vertices explored: {result.vertices_explored}")
        print(f"Edges evaluated: {result.edges_evaluated}")
        print(f"Execution time: {result.execution_time:.6f} seconds")

# Main program loop
def main():
    graph = load_graph()
    algorithms = {
        1: DijkstraAlgorithm(),
        2: GreedyBestFirstSearch(),
        3: AStarAlgorithm()
    }
    
    # User interface
    while True:
        print("\n" + "="*50)
        print("Oregon Pathfinder")
        print("="*50)
        print("\nSelect pathfinding algorithm:")
        print("1. Dijkstra's Algorithm")
        print("2. Greedy Best-First Search")
        print("3. A* Algorithm")
        print("4. Exit")
        
        # Get user choice and options
        try:
            choice = int(input("\nEnter choice (1-4): "))
            if choice == 4:
                print("\nnGoodnight")
                break
            
            if choice not in [1, 2, 3]:
                print("\nInvalid entry. Please enter a number between 1 and 4.")
                continue
            start_city = input("Enter start city: ").strip()
            destination_city = input("Enter destination city: ").strip()
            
            if not graph.has_vertex(start_city):
                print(f"\nError: '{start_city}' is not valid city in the dataset.")
                continue
            
            if not graph.has_vertex(destination_city):
                print(f"\nError: '{destination_city}' is not a valid city in the dataset.")
                continue
            algorithm = algorithms[choice]
            result = algorithm.find_path(graph, start_city, destination_city)
            display_result(result, algorithm.get_name())
        except ValueError:
            print("\nInvalid entry. Please enter a number.")
        except KeyboardInterrupt:
            print("\n\nGoodnight")
            break
        except Exception as e:
            print(f"\nerror: {e}")

if __name__ == "__main__":
    main()
