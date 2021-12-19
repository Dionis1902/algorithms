## All algorithms and structures
### Sorting algorithms
>  ### QuickSort 
> #### Complexity:
>  - Average - O(nlog(n))
>  - Worst - O(n²)
> 
> Quicksort is a divide-and-conquer algorithm. It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. For this reason, it is sometimes called partition-exchange sort. The sub-arrays are then sorted recursively. This can be done in-place, requiring small additional amounts of memory to perform the sorting.
  
> ### MergeSort
> #### Complexity:
>  - Average - O(nlog(n))
>  - Worst - O(nlog(n))
> 
> Like QuickSort, Merge Sort is a Divide and Conquer algorithm. It divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves.

> ### HeapSort
> #### Complexity:
>  - Average - O(nlog(n))
>  - Worst - O(nlog(n))
> 
> Heap sort is a comparison-based sorting technique based on Binary Heap data structure. It is similar to selection sort where we first find the minimum element and place the minimum element at the beginning. We repeat the same process for the remaining elements.

> ### BubbleSort
> #### Complexity:
>  - Average - O(n²)
>  - Worst - O(n²)
> 
> Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.

> ### InsertionSort
> #### Complexity:
>  - Average - O(n²)
>  - Worst - O(n²)
> 
> Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands. The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part.

> ### SelectionSort
> #### Complexity:
>  - Average - O(n²)
>  - Worst - O(n²)
> 
> The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.
### Structures
> ### PriorityQueue
> #### Complexity:
>  - Insert - O(nlog(n))
>  - Peek - O(1)
> 
> Priority Queue is an extension of the queue with the following properties:
> - Every item has a priority associated with it.
> - An element with high priority is dequeued before an element with low priority.
> - If two elements have the same priority, they are served according to their order in the queue.