
import os
from functools import lru_cache

import faiss
import numpy as np
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer


# Load environment variables from backend/.env
load_dotenv()

EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL",
    "sentence-transformers/all-MiniLM-L6-v2"
)


# =====================================================
# CODEQUEST DSA KNOWLEDGE BASE
# =====================================================

KNOWLEDGE_BASE = [

    # 1. ARRAYS
    {
        "topic": "Arrays",
        "content": (
            "Arrays store multiple elements in an ordered collection. "
            "Elements are accessed using zero-based indices. Common operations "
            "include traversal, searching, insertion, deletion, finding minimum "
            "and maximum elements, and reversing an array. Array access is O(1), "
            "while searching is generally O(n)."
        )
    },

    # 2. TWO POINTERS
    {
        "topic": "Two Pointers",
        "content": (
            "The two pointer technique uses two indices to traverse an array "
            "or string. One pointer may start at the beginning and another at "
            "the end. It is useful for reversing arrays, checking palindromes, "
            "pair sum in sorted arrays, and removing duplicates. It can reduce "
            "nested-loop solutions from O(n squared) to O(n)."
        )
    },

    # 3. HASH MAPS
    {
        "topic": "Hash Maps",
        "content": (
            "A hash map stores key-value pairs and supports average O(1) "
            "insertion, deletion, and lookup. It is useful for frequency "
            "counting, detecting duplicates, grouping elements, and solving "
            "Two Sum. Common implementations include HashMap in Java and "
            "dictionary in Python."
        )
    },

    # 4. BINARY SEARCH
    {
        "topic": "Binary Search",
        "content": (
            "Binary search works on sorted data. It repeatedly divides the "
            "search range into halves by calculating mid = low + (high-low)/2. "
            "If the target is smaller, search the left half; otherwise search "
            "the right half. Its time complexity is O(log n). Carefully check "
            "low, high, mid, and loop termination conditions."
        )
    },

    # 5. RECURSION
    {
        "topic": "Recursion",
        "content": (
            "Recursion occurs when a function calls itself to solve smaller "
            "instances of a problem. Every recursive solution needs a base "
            "case and a recursive case. Missing base cases can cause infinite "
            "recursion or stack overflow. Examples include factorial, Fibonacci, "
            "tree traversal, and recursive array problems."
        )
    },

    # 6. SORTING
    {
        "topic": "Sorting",
        "content": (
            "Sorting arranges elements in ascending or descending order. "
            "Bubble sort, selection sort, and insertion sort generally take "
            "O(n squared) time. Merge sort takes O(n log n) time and O(n) "
            "extra space. Average quicksort complexity is O(n log n), while "
            "its worst case is O(n squared)."
        )
    },

    # 7. TIME COMPLEXITY
    {
        "topic": "Time Complexity",
        "content": (
            "Time complexity describes how an algorithm's running time grows "
            "with input size. Common complexities are O(1), O(log n), O(n), "
            "O(n log n), O(n squared), and O(2 to the power n). Sequential "
            "loops usually add their complexities, while nested loops often "
            "multiply them. Ignore constants and lower-order terms."
        )
    },

    # 8. DEBUGGING
    {
        "topic": "Debugging",
        "content": (
            "When debugging code, check input parsing, variable initialization, "
            "loop boundaries, array indices, data types, return statements, "
            "and edge cases. Test empty inputs, single-element inputs, duplicate "
            "values, negative numbers, and maximum constraints. Read compiler "
            "errors and runtime exceptions carefully."
        )
    },

    # 9. STRINGS
    {
        "topic": "Strings",
        "content": (
            "Strings are sequences of characters. Common problems include "
            "reversing strings, checking palindromes, counting character "
            "frequencies, finding anagrams, and substring searching. Strings "
            "may be immutable in languages such as Java and Python. Character "
            "arrays or StringBuilder can help with modifications."
        )
    },

    # 10. DYNAMIC PROGRAMMING
    {
        "topic": "Dynamic Programming",
        "content": (
            "Dynamic programming solves problems by storing results of "
            "overlapping subproblems. Two approaches are memoization, which "
            "uses recursion and caching, and tabulation, which uses iterative "
            "tables. Identify the state, transition, base cases, and answer. "
            "Common problems include Fibonacci, climbing stairs, knapsack, "
            "and longest common subsequence."
        )
    },

    # 11. SLIDING WINDOW
    {
        "topic": "Sliding Window",
        "content": (
            "Sliding window maintains a range of elements using two boundaries. "
            "A fixed-size window is useful for maximum sum of a subarray of "
            "size k. A variable-size window expands or shrinks according to "
            "conditions. It is useful for longest substring without repeating "
            "characters and minimum-size subarray problems."
        )
    },

    # 12. PREFIX SUM
    {
        "topic": "Prefix Sum",
        "content": (
            "Prefix sum stores cumulative sums of array elements. If prefix[i] "
            "represents the sum up to index i, a range sum can be calculated "
            "using prefix[right] minus prefix[left-1]. Prefix sums allow "
            "efficient range-sum queries after O(n) preprocessing."
        )
    },

    # 13. KADANE ALGORITHM
    {
        "topic": "Kadane Algorithm",
        "content": (
            "Kadane's algorithm finds the maximum sum of a contiguous subarray "
            "in O(n) time. Maintain currentSum and maxSum. At each element, "
            "decide whether to extend the previous subarray or start a new "
            "subarray from the current element. Initialize carefully to handle "
            "arrays containing only negative numbers."
        )
    },

    # 14. LINKED LIST
    {
        "topic": "Linked List",
        "content": (
            "A linked list consists of nodes where each node stores data and "
            "a reference to the next node. Unlike arrays, nodes are not stored "
            "in contiguous memory. Common operations include insertion, "
            "deletion, traversal, and searching. Accessing an element by "
            "position takes O(n) time."
        )
    },

    # 15. REVERSE LINKED LIST
    {
        "topic": "Reverse Linked List",
        "content": (
            "A singly linked list can be reversed iteratively using three "
            "pointers: previous, current, and nextNode. Save the next node "
            "before changing current.next to previous. Move all pointers "
            "forward until current becomes null. The time complexity is O(n) "
            "and auxiliary space is O(1)."
        )
    },

    # 16. FAST AND SLOW POINTERS
    {
        "topic": "Fast and Slow Pointers",
        "content": (
            "Fast and slow pointers use two references moving at different "
            "speeds in a linked list. The slow pointer moves one step and "
            "the fast pointer moves two steps. This technique finds the middle "
            "node and detects cycles using Floyd's cycle detection algorithm."
        )
    },

    # 17. STACK
    {
        "topic": "Stack",
        "content": (
            "A stack follows Last In First Out, also called LIFO. Insertion "
            "is called push and removal is called pop. Common operations "
            "include push, pop, and peek. Stacks are useful for balanced "
            "parentheses, expression evaluation, recursion, and undo operations."
        )
    },

    # 18. QUEUE
    {
        "topic": "Queue",
        "content": (
            "A queue follows First In First Out, also called FIFO. Insertion "
            "is called enqueue and removal is called dequeue. Queues are used "
            "in level-order tree traversal, BFS, task scheduling, and buffering."
        )
    },

    # 19. MONOTONIC STACK
    {
        "topic": "Monotonic Stack",
        "content": (
            "A monotonic stack maintains elements in increasing or decreasing "
            "order. It is useful for Next Greater Element, Next Smaller Element, "
            "Daily Temperatures, Largest Rectangle in Histogram, and Stock "
            "Span problems. Each element is generally pushed and popped at "
            "most once, giving O(n) time complexity."
        )
    },

    # 20. BINARY TREE
    {
        "topic": "Binary Tree",
        "content": (
            "A binary tree is a hierarchical data structure where each node "
            "has at most two children: left and right. Important concepts "
            "include root, leaf, height, depth, and subtree. Common operations "
            "include insertion, searching, and traversal."
        )
    },

    # 21. TREE TRAVERSALS
    {
        "topic": "Tree Traversals",
        "content": (
            "Tree traversal visits every node in a tree. Preorder follows "
            "Root Left Right, inorder follows Left Root Right, and postorder "
            "follows Left Right Root. Level-order traversal uses a queue "
            "and processes nodes level by level. DFS traversals commonly "
            "use recursion or a stack."
        )
    },

    # 22. BINARY SEARCH TREE
    {
        "topic": "Binary Search Tree",
        "content": (
            "A Binary Search Tree is a binary tree where values smaller than "
            "a node are placed in its left subtree and larger values in its "
            "right subtree, subject to the duplicate-value convention. "
            "Inorder traversal of a BST produces sorted values. Average "
            "search, insertion, and deletion take O(log n) in a balanced tree."
        )
    },

    # 23. HEAP
    {
        "topic": "Heap",
        "content": (
            "A heap is a complete binary tree that follows the heap property. "
            "In a min heap, the parent is smaller than or equal to its children. "
            "In a max heap, the parent is greater than or equal to its children. "
            "Heaps are useful for priority queues, heap sort, and finding "
            "the kth largest or smallest element."
        )
    },

    # 24. GRAPH
    {
        "topic": "Graph",
        "content": (
            "A graph consists of vertices and edges. Graphs can be directed "
            "or undirected, weighted or unweighted. Common representations "
            "are adjacency matrix and adjacency list. Graph algorithms solve "
            "connectivity, shortest path, cycle detection, and traversal problems."
        )
    },

    # 25. BFS
    {
        "topic": "Breadth First Search",
        "content": (
            "Breadth First Search explores a graph level by level using a "
            "queue. Mark nodes visited when they are discovered to avoid "
            "repeated processing. BFS finds shortest paths in unweighted "
            "graphs. Its time complexity using an adjacency list is O(V + E)."
        )
    },

    # 26. DFS
    {
        "topic": "Depth First Search",
        "content": (
            "Depth First Search explores as far as possible along a path "
            "before backtracking. It can be implemented using recursion "
            "or an explicit stack. DFS is useful for connected components, "
            "cycle detection, path finding, and topological sorting. "
            "Its adjacency-list complexity is O(V + E)."
        )
    },

    # 27. TOPOLOGICAL SORT
    {
        "topic": "Topological Sorting",
        "content": (
            "Topological sorting produces a linear ordering of vertices in "
            "a Directed Acyclic Graph such that every directed edge u to v "
            "places u before v. It can be implemented using DFS or Kahn's "
            "algorithm with indegrees and a queue. A directed cycle prevents "
            "a valid topological ordering."
        )
    },

    # 28. SHORTEST PATH
    {
        "topic": "Shortest Path Algorithms",
        "content": (
            "Dijkstra's algorithm finds shortest paths from a source in "
            "graphs with non-negative edge weights, commonly using a "
            "priority queue. Bellman-Ford supports negative edge weights "
            "and detects reachable negative cycles. BFS can find shortest "
            "paths in unweighted graphs."
        )
    },

    # 29. BACKTRACKING
    {
        "topic": "Backtracking",
        "content": (
            "Backtracking explores possible choices recursively and reverses "
            "a choice when it cannot lead to a valid solution. The general "
            "pattern is choose, explore, and undo. Common problems include "
            "subsets, permutations, N-Queens, Sudoku, and combination sum."
        )
    },

    # 30. GREEDY ALGORITHM
    {
        "topic": "Greedy Algorithm",
        "content": (
            "A greedy algorithm makes the locally best choice at each step. "
            "It is useful when the problem has a greedy-choice property "
            "and optimal substructure. Examples include activity selection, "
            "fractional knapsack, interval scheduling, and Huffman coding. "
            "A greedy strategy does not work for every optimization problem."
        )
    },

    # 31. BIT MANIPULATION
    {
        "topic": "Bit Manipulation",
        "content": (
            "Bit manipulation operates directly on binary representations. "
            "Important operators are AND, OR, XOR, NOT, left shift, and "
            "right shift. Common techniques include checking whether a "
            "number is odd using n AND 1, checking a power of two using "
            "n AND n-1, and finding a unique element using XOR."
        )
    },

    # 32. TRIE
    {
        "topic": "Trie",
        "content": (
            "A Trie is a tree-like data structure used to store strings "
            "character by character. Each path represents a prefix. "
            "Tries are useful for autocomplete, prefix search, and dictionary "
            "word lookup. Search and insertion take O(L) time, where L is "
            "the length of the word, assuming constant-time child access."
        )
    },

    # 33. DISJOINT SET UNION
    {
        "topic": "Disjoint Set Union",
        "content": (
            "Disjoint Set Union, also called Union Find, maintains groups "
            "of connected elements. It supports find and union operations. "
            "Path compression and union by rank or size make operations "
            "almost constant time on average. DSU is useful for cycle "
            "detection and Kruskal's minimum spanning tree algorithm."
        )
    },

    # 34. MINIMUM SPANNING TREE
    {
        "topic": "Minimum Spanning Tree",
        "content": (
            "A Minimum Spanning Tree connects all vertices of a connected "
            "weighted undirected graph with minimum total edge weight and "
            "no cycles. Kruskal's algorithm sorts edges and uses DSU. "
            "Prim's algorithm grows the tree using a priority queue."
        )
    },

    # 35. FLOYD WARSHALL
    {
        "topic": "Floyd Warshall Algorithm",
        "content": (
            "Floyd Warshall finds shortest paths between every pair of "
            "vertices. It uses dynamic programming and checks whether "
            "going through an intermediate vertex gives a shorter path. "
            "Its time complexity is O(V cubed) and space complexity is O(V squared)."
        )
    },

    # 36. KNAPSACK
    {
        "topic": "Knapsack Problem",
        "content": (
            "The 0/1 Knapsack problem chooses items with given weights and "
            "values to maximize total value without exceeding capacity. "
            "Each item can be selected at most once. Dynamic programming "
            "uses a state based on item index and remaining capacity. "
            "The standard solution takes O(n times capacity) time."
        )
    },

    # 37. LONGEST COMMON SUBSEQUENCE
    {
        "topic": "Longest Common Subsequence",
        "content": (
            "Longest Common Subsequence finds the longest sequence appearing "
            "in two strings in the same relative order, but not necessarily "
            "contiguously. Dynamic programming compares characters. If they "
            "match, add one to the diagonal state; otherwise take the maximum "
            "of the two neighboring states. Standard complexity is O(n*m)."
        )
    },

    # 38. EDGE CASES
    {
        "topic": "Edge Cases",
        "content": (
            "Edge cases are unusual or boundary inputs that may break an "
            "algorithm. Always test empty arrays, one-element arrays, "
            "duplicate values, negative numbers, already sorted arrays, "
            "reverse sorted arrays, large inputs, and boundary values. "
            "Carefully consider integer overflow and null references."
        )
    },

    # 39. SPACE COMPLEXITY
    {
        "topic": "Space Complexity",
        "content": (
            "Space complexity measures how much additional memory an "
            "algorithm uses as input size grows. Auxiliary space excludes "
            "the input itself in many common definitions. Recursive calls "
            "use call stack memory. In-place algorithms aim to use O(1) "
            "auxiliary space."
        )
    },

    # 40. JAVA COLLECTIONS
    {
        "topic": "Java Collections",
        "content": (
            "Java Collections provide reusable data structures. ArrayList "
            "supports dynamic arrays, LinkedList supports linked nodes, "
            "HashMap stores key-value pairs, HashSet stores unique elements, "
            "Stack represents LIFO behavior, and Queue represents FIFO "
            "behavior. PriorityQueue implements a heap-based priority queue."
        )
    }
]


# =====================================================
# LOAD LOCAL EMBEDDING MODEL
# =====================================================

@lru_cache(maxsize=1)
def get_embedding_model():
    """
    Load the embedding model once and reuse it.

    The model runs locally on the computer.
    No external embedding API key is needed.
    """

    print(f"Loading local embedding model: {EMBEDDING_MODEL}")

    model = SentenceTransformer(
        EMBEDDING_MODEL,
        device="cpu"
    )

    print("Local embedding model loaded successfully.")

    return model


# =====================================================
# BUILD FAISS KNOWLEDGE INDEX
# =====================================================

@lru_cache(maxsize=1)
def build_knowledge_index():
    """
    Convert knowledge-base documents into vectors
    and create a FAISS similarity-search index.
    """

    model = get_embedding_model()

    documents = [
        f"{item['topic']}: {item['content']}"
        for item in KNOWLEDGE_BASE
    ]

    vectors = model.encode(
        documents,
        convert_to_numpy=True,
        normalize_embeddings=True,
        show_progress_bar=False
    )

    vectors = np.asarray(vectors, dtype="float32")

    # Inner product on normalized vectors gives cosine similarity.
    index = faiss.IndexFlatIP(vectors.shape[1])

    index.add(vectors)

    print(
        f"FAISS knowledge index created with "
        f"{index.ntotal} documents."
    )

    return index, documents


# =====================================================
# RETRIEVE RELEVANT DSA CONTEXT
# =====================================================

def retrieve_context(query: str, top_k: int = 3) -> str:
    """
    Find the most relevant DSA knowledge
    for a student's question.
    """

    if not query or not query.strip():
        return "No coding context was provided."

    model = get_embedding_model()

    index, documents = build_knowledge_index()

    query_vector = model.encode(
        [query.strip()],
        convert_to_numpy=True,
        normalize_embeddings=True,
        show_progress_bar=False
    )

    query_vector = np.asarray(
        query_vector,
        dtype="float32"
    )

    number_of_results = min(
        max(top_k, 1),
        len(documents)
    )

    scores, indices = index.search(
        query_vector,
        number_of_results
    )

    retrieved_documents = []

    for position, document_index in enumerate(indices[0]):

        if document_index >= 0:
            retrieved_documents.append(
                documents[document_index]
            )

    if not retrieved_documents:
        return "No closely related coding knowledge was found."

    return "\n\n".join(retrieved_documents)
