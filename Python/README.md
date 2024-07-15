## Algorithms

Sorting:
- [x] Merge sort;
- [x] Quick sort;
- [x] Selection sort;
- [x] Insertion sort;
- [x] Counting sort
- [x] Buble sort;
- [x] Heap sort;
- [x] Recursive selection sort;
- [x] Bucket sort;
- [ ] TimSort.

Graph:
- [x] Breadth First Search;
- [x] Depth First Search;
- [x] Dijkstra Shortest Path.

Metaheuristics:
- [x] Simulated Annealing;
- [x] Genetic Algorithms;
- [x] Tabu Search.
## Testing
```sh
$ pytest -v tests
```

## Docker
```sh
$ docker build -t python-algorithms:dev . -f .\Docker\Dockerfile
```

```sh
$ docker run -v .:/app -it python-algorithms:dev
```
