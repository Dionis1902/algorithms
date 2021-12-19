## All algorithms and structures

<details>
  <summary>Table of Contents</summary>
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
      <a href="#structures">Structures</a>
      <ul>
        <li><a href="#priority-queue">Priority Queue</a></li>
        <li><a href="#deque">Deque</a></li>
        <li><a href="#binary-search-tree">Binary Search Tree</a></li>
      </ul>
    </li>
  </ol>
</details>

### Sorting algorithms
>  ### Quick Sort 
> #### Complexity:
>  - Average - O(nlog(n))
>  - Worst - O(n²)
> 
> Quicksort is a divide-and-conquer algorithm. It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. For this reason, it is sometimes called partition-exchange sort. The sub-arrays are then sorted recursively. This can be done in-place, requiring small additional amounts of memory to perform the sorting.
  
> ### Merge Sort
> #### Complexity:
>  - Average - O(nlog(n))
>  - Worst - O(nlog(n))
> 
> Like QuickSort, Merge Sort is a Divide and Conquer algorithm. It divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves.

> ### Heap Sort
> #### Complexity:
>  - Average - O(nlog(n))
>  - Worst - O(nlog(n))
> 
> Heap sort is a comparison-based sorting technique based on Binary Heap data structure. It is similar to selection sort where we first find the minimum element and place the minimum element at the beginning. We repeat the same process for the remaining elements.

> ### Bubble Sort
> #### Complexity:
>  - Average - O(n²)
>  - Worst - O(n²)
> 
> Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.

> ### Insertion Sort
> #### Complexity:
>  - Average - O(n²)
>  - Worst - O(n²)
> 
> Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands. The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part.

> ### Selection Sort
> #### Complexity:
>  - Average - O(n²)
>  - Worst - O(n²)
> 
> The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.

> ### Random Sort
> #### Complexity:
>  - Average - O(???)
>  - Worst - O(∞)
> 
> In computer science, RandomSort (also known as permutation sort, stupid sort, bogosort or slowsort) is a highly inefficient sorting algorithm based on the generate and test paradigm. The function successively generates permutations of its input until it finds one that is sorted. It is not useful for sorting, but may be used for educational purposes, to contrast it with more efficient algorithms.
***
### Structures
> ### Priority Queue
> #### Complexity:
>  - Insert - O(nlog(n))
>  - Peek - O(1)
> 
> Priority Queue is an extension of the queue with the following properties:
> - Every item has a priority associated with it.
> - An element with high priority is dequeued before an element with low priority.
> - If two elements have the same priority, they are served according to their order in the queue.

> ### Deque
> #### Complexity:
>  - Insert - Front : O(1), Back : O(n)
>  - Peek - Front : O(1), Back : O(n)
> 
> Deque or Double Ended Queue is a generalized version of Queue data structure that allows insert and delete at both ends.

> ### Binary Search Tree
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
