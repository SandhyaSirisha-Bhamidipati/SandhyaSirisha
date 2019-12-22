import sys

from Node import Node


def read_file(file_name):
    data = []
    FileNotFound = None
    try:
        f = open(file_name, 'r')
    except FileNotFound:
        print ('Error: Cannot open file.')
    else:
        data = [line for line in f]
        f.close()

    return data


def adj_node(fringe, routes, vst_node):
    city_node = fringe[0]

    city_name = city_node.city_name

    current_cost = city_node.total_cost

    vst_node.append(city_name)

    del fringe[0]
    for route in routes:
        if city_name in route:

            if route[0] == city_name and not(route[1] in vst_node):
                adj_city = Node(route[1], city_node, int(current_cost)+int(route[2]), int(route[2]))
                fringe.append(adj_city)

            elif route[1] == city_name and not(route[0] in vst_node):
                adj_city = Node(route[0], city_node, int(current_cost)+int(route[2]), int(route[2]))
                fringe.append(adj_city)


def get_fringe(routes, source, dest_city):
    fringe = []

    vst_node = []

    fringe.append(source)
    vst_node.append(source.city_name)

    while True:

        if not fringe:
            return None

        if fringe[0].city_name == dest_city:
            return fringe[0]

        adj_node(fringe, routes, vst_node)

        fringe = sorted(fringe, key=lambda node: node.total_cost)


def path_retrace(dest_node):

    print ('Distance: %d Miles' % dest_node.total_cost)

    trace_city = []
    trace_cost = []
    while dest_node:
        trace_city.append(dest_node.city_name)
        trace_cost.append(dest_node.route_cost)
        dest_node = dest_node.parent_node
    trace_city.reverse()
    trace_cost.reverse()

    del trace_cost[0]

    print ('Route:')
    for i in range(0, len(trace_city)-1):
        trace_city[i] = trace_city[i][0].upper() + trace_city[i][1:]
        trace_city[i+1] = trace_city[i+1][0].upper() + trace_city[i+1][1:]
        print ('%s to %s, %d Miles' % (trace_city[i], trace_city[i+1], trace_cost[i]))


def ucs(routes, source, dest):
    result = get_fringe(routes, source, dest)
    if result == None:
        print ('Distance = Infinity')
        print ('Route:')
        print ('None')
    else:
        path_retrace(result)


def main():
    if len(sys.argv) < 4:
        print ('[Format] python ucs.py <file_name> <source> <dest>')
        print ('Note: Make sure that all the files are in the same directory')
        return

    file_name = sys.argv[1]
    source = sys.argv[2].lower()
    dest = sys.argv[3].lower()

    data = read_file(file_name)

    if not data:
        return

    routes = [route.lower().split() for route in data]

    del routes[len(routes)-1]
    del routes[len(routes)-1]

    start = Node(source, None, 0, 0)

    ucs(routes, start, dest)


if __name__ == "__main__":
    main()