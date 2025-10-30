import math

class Graph:
    def __init__(self):
        self.adjacency_list = {}
        self.coordinates = {}
    
    def add_vertex(self, vertex_name, latitude= None, longitude= None):
        if vertex_name not in self.adjacency_list:
            self.adjacency_list[vertex_name] = []
        if latitude is not None and longitude is not None:
            self.coordinates[vertex_name] = (latitude, longitude)
    
    def add_edge(self, source, destination, highway, distance):
        if source not in self.adjacency_list:
            self.add_vertex(source)
        if destination not in self.adjacency_list:
            self.add_vertex(destination)
        self.adjacency_list[source].append((destination, highway, distance))
    
    def get_neighbors(self, vertex):
        return self.adjacency_list.get(vertex, [])
    
    def get_coordinates(self, vertex):
        return self.coordinates.get(vertex, None)
    
    def has_vertex(self, vertex):
        return vertex in self.adjacency_list
    
    def haversine_distance(self, vertex1, vertex2):
        earth_radius_miles = 3959
        coords1 = self.get_coordinates(vertex1)
        coords2 = self.get_coordinates(vertex2)
        if coords1 is None or coords2 is None:
            return float('inf')
        
        lat1, lon1 = coords1
        lat2, lon2 = coords2
        lat1_rad = math.radians(lat1)
        lon1_rad = math.radians(lon1)
        lat2_rad = math.radians(lat2)
        lon2_rad = math.radians(lon2)
        delta_lat = lat2_rad - lat1_rad
        delta_lon = lon2_rad - lon1_rad
        a = math.sin(delta_lat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(delta_lon / 2) ** 2
        c = 2 * math.asin(math.sqrt(a))
        return earth_radius_miles * c
