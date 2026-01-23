class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        # 1. Doubly Linked List Simulation
        # We use arrays to store the index of the left and right neighbors for every element.
        left = list(range(-1, n - 1))  # left[i] = i - 1
        right = list(range(1, n + 1))  # right[i] = i + 1
        right[n - 1] = -1              # Last element has no right neighbor
        
        # Track which indices are currently valid parts of the list
        alive = [True] * n

        # 2. Initialize Violation Count
        # A "violation" is when a current number is strictly greater than the next number.
        violations = 0
        i = 0
        while i != -1:
            next_node = right[i]
            if next_node != -1 and nums[i] > nums[next_node]:
                violations += 1
            i = next_node

        # 3. Min-Heap Initialization
        # Stores tuples: (sum_of_pair, left_index_of_pair)
        # Python's heap automatically handles the "leftmost" tie-breaker because 
        # it compares the second element (index) if the sums are equal.
        heap = []
        i = 0
        while i != -1:
            next_node = right[i]
            if next_node != -1:
                heapq.heappush(heap, (nums[i] + nums[next_node], i))
            i = next_node

        ops = 0

        # 4. Greedy Simulation
        while violations > 0:
            if not heap:
                break
            
            pair_sum, i = heapq.heappop(heap)
            j = right[i]

            # --- VALIDATION CHECKS (Lazy Deletion Handling) ---
            # 1. Check if 'i' or its neighbor 'j' are dead/invalid
            if not alive[i] or j == -1 or not alive[j]:
                continue
            
            # 2. STALE CHECK: Ensure the sum in the heap matches the current values.
            # This is crucial because 'nums[i]' might have changed from a previous merge.
            if pair_sum != nums[i] + nums[j]:
                continue

            # Identify extended neighbors
            li = left[i]
            rj = right[j]

            # --- REMOVE OLD VIOLATIONS ---
            # We are about to merge i and j, so remove their contribution to the violation count.
            if li != -1 and nums[li] > nums[i]:
                violations -= 1
            if nums[i] > nums[j]:
                violations -= 1
            if rj != -1 and nums[j] > nums[rj]:
                violations -= 1

            # --- EXECUTE MERGE ---
            nums[i] = pair_sum   # i absorbs j
            alive[j] = False     # j is removed
            
            # Update Pointers (Skip over j)
            right[i] = rj
            if rj != -1:
                left[rj] = i

            # --- ADD NEW VIOLATIONS ---
            # Check if the new merged value creates new violations with current neighbors.
            if li != -1 and nums[li] > nums[i]:
                violations += 1
            if rj != -1 and nums[i] > nums[rj]:
                violations += 1

            # --- PUSH NEW PAIRS ---
            # Add potential merges for the new neighbors to the heap.
            if li != -1:
                heapq.heappush(heap, (nums[li] + nums[i], li))
            if rj != -1:
                heapq.heappush(heap, (nums[i] + nums[rj], i))

            ops += 1

        return ops