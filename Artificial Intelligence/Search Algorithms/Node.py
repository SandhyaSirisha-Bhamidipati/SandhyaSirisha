class Node:
    def __init__(self, city_name, parent_node, total_cost, route_cost):
        self.city_name = city_name;
        self.parent_node = parent_node;
        self.total_cost = total_cost;
        self.route_cost = route_cost;