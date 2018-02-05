# Summary
This is a take home screening exercise I was given to create a LRUCache with 3 slots.

# Application Requirements
- Python 2.7.X (tested with 2.7.10) 

# How to run
$ python LRUCache.py

# Runtime Complexity (note: Going back to college days)
- GET (does not exist):  0(1) hash look up
- GET (exists) and SET: 0(n x 2) n = number of items in cache. Have to remove and append item in queue.
- SIZE operation: O(1)

# Limitations
- Input is limited to ascii values.

# Assumptions
- Cache size less than 1 is not allowed, results in "ERROR".

# Other Comments
I am not happy with my implmentation starting on line 39. I was limited by the queue library I choose. I wish deque would return removed object or None if not found, not throw an error. Try/except can be dangerous in this situation because what if someone adds additional code under the try that is bad; than its badness won't be detected.
