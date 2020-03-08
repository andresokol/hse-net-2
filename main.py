import typing as tp
from copy import deepcopy

from as_net_hw2 import parsers, algo, models, dumpers, visualize

DEMO_PATH = 'demo/Abvt.graphml.xml'


def main(name: str, find_reserve: bool):
    graph = parsers.parse_graphml(DEMO_PATH)
    print('Parsed graph:', graph)
    dumpers.dump_topo(graph, name)

    dist, next_vertex = algo.floyd_warshall(graph)
    routes = []
    for i in range(graph.node_cnt):
        for j in range(graph.node_cnt):
            if i == j:
                continue
            direct_route = algo.extract_route(graph, i, j, dist, next_vertex)
            routes.append(direct_route)
            routes.append(algo.find_reserve_route(graph, i, j, direct_route.path))

    dumpers.dump_routes(graph, routes, name)
    visualize.visualize(graph, 'demo.html', routes[0], routes[1])


if __name__ == '__main__':
    main("demo", False)
