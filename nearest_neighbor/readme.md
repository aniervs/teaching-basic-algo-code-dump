# KD-Tree Nearest Neighbor Search Assignment

## 🎯 Objective

You will implement a **KD-Tree** from scratch in Python to find the **k-Nearest Neighbors (k-NN)** for a given query point.

You will then compare the performance of your KD-Tree search against a simple "brute-force" naive search. This will give you a hands-on understanding of algorithmic complexity and the practical benefits of using the right data structure for the job.

---

## 📂 Project Structure

This project consists of three main files:

* `kdtree.py`: This file contains the skeleton for the `KDTree` class. **Your main implementation work will be done here.**
* `main.py`: This is the main script used to run the performance comparison between your KD-Tree and the naive search. You will need to implement the naive search function and set up the test harness here.
* `README.md`: The file you are currently reading, which contains instructions and the questions for your final report.



---

## ✅ Your Task

Follow these steps to complete the assignment.

### Step 1: Implement the Naive Search

First, open `main.py` and complete the `naive_knn()` function. This is the straightforward "brute-force" approach. It should:
1.  Calculate the distance from the `query_point` to every other point in the dataset.
2.  Sort the points based on these distances.
3.  Return the `k` points with the smallest distances.

This will serve as your baseline to verify the correctness of your KD-Tree implementation.

### Step 2: Implement the KD-Tree Build Logic

Next, move to `kdtree.py`. Your first task here is to implement the `_build()` method. This method recursively builds the tree by:
1.  Selecting a splitting axis based on the current `depth`.
2.  Sorting the points along that axis to find the **median**.
3.  Using the median point as the current node and recursively building the left and right subtrees with the remaining points.

### Step 3: Implement the KD-Tree Search Logic

Now for the most interesting part! Implement the `_knn_search()` method in `kdtree.py`. This method performs the efficient k-NN search using the tree structure. The key steps are:
1.  Travel down the tree to find the region where the `query_point` would belong.
2.  As you backtrack (unwind the recursion), update a list of the `k` best neighbors found so far (a **min-heap**, implemented with Python's `heapq` module, is perfect for this).
3.  At each node during backtracking, perform the **pruning check**: determine if the "other" subtree could possibly contain a closer neighbor. You only need to explore it if the distance to the splitting plane is less than the distance to your current farthest neighbor. This is the step that makes the KD-Tree so fast!

### Step 4: Run the Comparison

Finally, return to `main.py` and complete the `main()` function.
1.  Uncomment the lines to instantiate your `KDTree`.
2.  Uncomment the lines that call `tree.find_k_nearest_neighbors()` and `naive_knn()` within the timing loops.
3.  Run the script from your terminal to see the performance results!
4.  Implement anything missing there.
---



