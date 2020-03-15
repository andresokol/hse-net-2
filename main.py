import argparse

from as_net_hw2 import parsers, algo, dumpers, visualize


def main(args):
    graph = parsers.parse_graphml(args.file_name)
    print('Parsed graph:', graph)
    dumpers.dump_topo(graph, args.file_name)

    dist, next_vertex = algo.floyd_warshall(graph)
    routes = []

    for i in range(graph.node_cnt):
        for j in range(graph.node_cnt):
            if i == j:
                continue
            direct_route = algo.extract_route(graph, i, j, dist, next_vertex)
            routes.append(direct_route)

            if args.build_reserve:
                routes.append(algo.find_reserve_route(graph, i, j, direct_route.path))

    dumpers.dump_routes(graph, routes, args.file_name)

    if args.source_node_id is not None and args.destination_node_id is not None:
        start_idx = graph.nodes_idx[args.source_node_id]
        dest_idx = graph.nodes_idx[args.destination_node_id]
        direct_route = algo.extract_route(graph, start_idx, dest_idx, dist, next_vertex)
        reserve_route = None
        if args.build_reserve:
            reserve_route = algo.find_reserve_route(graph, start_idx, dest_idx, direct_route.path)

        visualize.visualize(graph, args.file_name + '_demo.html', direct_route, reserve_route)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--file-name', required=True,
                        help='filename to parse, .gml or .graphml')
    parser.add_argument('-r', '--build-reserve', action='store_true', help='build reserve routes')
    parser.add_argument('-s', '--source-node-id', help='source node id to visualize')
    parser.add_argument('-d', '--destination-node-id', help='destination node id to visualize')
    args = parser.parse_args()
    print(args)
    main(args)
