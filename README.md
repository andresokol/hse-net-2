## HW 2, Networks

**Соколов Андрей, группа 166**

Программа должна работать с Python 3.6+, библиотеки не нужны. Программа принимает на вход путь к файлу в формате GraphML.

Пример запуска программы:

```bash
>>> python3 ./main.py -t tests/AttMpls.graphml -r -s 2 -d 23
Namespace(build_reserve=True, destination_node_id='23', file_name='tests/AttMpls.graphml', source_node_id='2')
Parsed 25 nodes
Parsed 114 edges
Parsed graph: G(25 nodes, 114 edges)
Written topology to file tests/AttMpls.graphml_topo.csv
Written routes to file tests/AttMpls.graphml_routes.csv
Visualization available at file tests/AttMpls.graphml_demo.html
```

Программа генерирует два csv файла и, если указаны параметры -s и -d, один HTML файл с визуализацией графа. Для визуализации используется API Яндекс.Карт, прямой путь обозначается черным, резервный - красным.

Для вычисления расстояния между двумя точками, заданными в координатах, используется формула [greate-circle distance](https://en.wikipedia.org/wiki/Great-circle_distance).

Оценка времени работы программы - ```O(n^3)``` от количества вершин без построения резервных путей, ```O(n^4)``` в противном случае.
