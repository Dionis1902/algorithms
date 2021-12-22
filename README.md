## All Algorithms and Data Structures

### [Site for visualisation all Algorithms and Data Structures](https://visualgo.net/ru)

<details>
  <summary>Navigation</summary>
  <ol>
    <li>
      <a href="#sorting-algorithms">Sorting algorithms</a>
      <ul>
        <li><a href="#quick-sort">Quick Sort</a></li>
        <li><a href="#merge-sort">Merge Sort</a></li>
        <li><a href="#heap-sort">Heap Sort</a></li>
        <li><a href="#bubble-sort">Bubble Sort</a></li>
        <li><a href="#insertion-sort">Insertion Sort</a></li>
        <li><a href="#selection-sort">Selection Sort</a></li>
        <li><a href="#random-sort">Random Sort</a></li>
      </ul>
    </li>
    <li>
      <a href="#data-structures">Data Structures</a>
      <ul>
        <li><a href="#priority-queue">Priority Queue</a></li>
        <li><a href="#deque">Deque</a></li>
        <li><a href="#binary-search-tree">Binary Search Tree</a></li>
        <li><a href="#hash-table">Hash Table</a></li>
        <li><a href="#stack">Stack</a></li>
      </ul>
    </li>
    <li>
      <a href="#graphs">Graphs</a>
      <ul>
        <li><a href="#breadth-first-search-(bfs)">Breadth First Search (BFS)</a></li>
        <li><a href="#depth-first-search-(dfs)">Depth First Search (DFS)</a></li>
      </ul>
    </li>
  </ol>
</details>

### Sorting algorithms
> ### [Quick Sort](Sorting/quick_sort.py)
> #### Complexity:
>  - Average - O(nlog(n))
>  - Worst - O(n²)
> 
> Quicksort is a divide-and-conquer algorithm. It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. For this reason, it is sometimes called partition-exchange sort. The sub-arrays are then sorted recursively. This can be done in-place, requiring small additional amounts of memory to perform the sorting.

> ### [Merge Sort](Sorting/merge_sort.py)
> #### Complexity:
>  - Average - O(nlog(n))
>  - Worst - O(nlog(n))
> 
> Like QuickSort, Merge Sort is a Divide and Conquer algorithm. It divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves.

> ### [Heap Sort](Sorting/heap_sort.py)
> #### Complexity:
>  - Average - O(nlog(n))
>  - Worst - O(nlog(n))
> 
> Heap sort is a comparison-based sorting technique based on Binary Heap data structure. It is similar to selection sort where we first find the minimum element and place the minimum element at the beginning. We repeat the same process for the remaining elements.

> ### [Bubble Sort](Sorting/bubble_sort.py)
> #### Complexity:
>  - Average - O(n²)
>  - Worst - O(n²)
> 
> Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.

> ### [Insertion Sort](Sorting/insertion_sort.py)
> #### Complexity:
>  - Average - O(n²)
>  - Worst - O(n²)
> 
> Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands. The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part.

> ### [Selection Sort](Sorting/selection_sort.py)
> #### Complexity:
>  - Average - O(n²)
>  - Worst - O(n²)
> 
> The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.

> ### [Random Sort](Sorting/random_sort.py)
> #### Complexity:
>  - Average - O(???)
>  - Worst - O(∞)
> 
> In computer science, RandomSort (also known as permutation sort, stupid sort, bogosort or slowsort) is a highly inefficient sorting algorithm based on the generate and test paradigm. The function successively generates permutations of its input until it finds one that is sorted. It is not useful for sorting, but may be used for educational purposes, to contrast it with more efficient algorithms.
***
### Data Structures
> ### [Priority Queue](Structures/priority_queue.py)
> #### Complexity:
>  - Insert - O(nlog(n))
>  - Peek - O(1)
> 
> Priority Queue is an extension of the queue with the following properties:
> - Every item has a priority associated with it.
> - An element with high priority is dequeued before an element with low priority.
> - If two elements have the same priority, they are served according to their order in the queue.

> ### [Deque](Structures/deque.py)
> #### Complexity:
>  - Insert - Front : O(1), Back : O(n)
>  - Peek - Front : O(1), Back : O(n)
> 
> Deque or Double Ended Queue is a generalized version of Queue data structure that allows insert and delete at both ends.

> ### [Binary Search Tree](Structures/binary_search_tree.py)
> #### Complexity:
>  - Insert - O(log(n))
>  - Peek - O(log(n))
> 
> The following is the definition of Binary Search Tree(BST) according to [Wikipedia](https://en.wikipedia.org/wiki/Binary_search_tree)
> Binary Search Tree is a node-based binary tree data structure which has the following properties:
> - The left subtree of a node contains only nodes with keys lesser than the node’s key.
> - The right subtree of a node contains only nodes with keys greater than the node’s key.
> - The left and right subtree each must also be a binary search tree. 
> - There must be no duplicate nodes.

> ### [Hash Table](Structures/hash_table.py)
> #### Complexity:
>  - Insert - O(1)
>  - Peek - O(1)
> 
> Hashing is a data structure that is used to store a large amount of data, which can be accessed in O(1) time by operations such as search, insert and delete. Various Applications of Hashing are:
> - Indexing in database
> - Cryptography
> - Symbol Tables in Compiler/Interpreter
> - Dictionaries, caches, etc.

> ### [Stack](Structures/stack.py)
> #### Complexity:
>  - Insert - O(1)
>  - Peek - O(1)
> 
> A stack is a linear data structure that stores items in a Last-In/First-Out (LIFO) or First-In/Last-Out (FILO) manner. In stack, a new element is added at one end and an element is removed from that end only. The insert and delete operations are often called push and pop.

***
### Graphs
> ### [Breadth First Search (BFS)](Graphs/bfs.py)
> #### Complexity:
>  - Search - O(V + E)
> 
> Breadth-first search (BFS) is an algorithm used for tree traversal on graphs or tree data structures. BFS can be easily implemented using recursion and data structures like dictionaries and lists.

> ### [Depth First Search (DFS)](Graphs/dfs.py)
> #### Complexity:
>  - Search - O(V + E)
> 
> Depth First Traversal (or Search) for a graph is similar to Depth First Traversal of a tree. The only catch here is, unlike trees, graphs may contain cycles (a node may be visited twice). To avoid processing a node more than once, use a boolean visited array. 


> ### [Dijkstra](Graphs/dijkstra.py)
> #### Complexity:
>  - Search -  O(V + Elog(V))
> 
> Dijkstra’s algorithm is very similar to Prim’s algorithm for minimum spanning tree. Like Prim’s MST, we generate an SPT (shortest path tree) with a given source as root. We maintain two sets, one set contains vertices included in the shortest-path tree, another set includes vertices not yet included in the shortest-path tree. At every step of the algorithm, we find a vertex that is in the other set (set of not yet included) and has a minimum distance from the source.

> ### [Bellman Ford](Graphs/bellman_ford.py)
> #### Complexity:
>  - Search -  O(VE)
> 
> Bellman Ford algorithm helps us find the shortest path from a vertex to all other vertices of a weighted graph. It is similar to Dijkstra's algorithm but it can work with graphs in which edges can have negative weights.