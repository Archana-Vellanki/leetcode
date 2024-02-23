// 703. Kth Largest Element in a Stream
// Solved
// Easy
// Topics
// Companies
// Design a class to find the kth largest element in a stream. Note that it is
// the kth largest element in the sorted order, not the kth distinct element.

// Implement KthLargest class:

// KthLargest(int k, int[] nums) Initializes the object with the integer k and
// the stream of integers nums.
// int add(int val) Appends the integer val to the stream and returns the
// element representing the kth largest element in the stream.

// Example 1:

// Input
// ["KthLargest", "add", "add", "add", "add", "add"]
// [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
// Output
// [null, 4, 5, 5, 8, 8]

// Explanation
// KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
// kthLargest.add(3); // return 4
// kthLargest.add(5); // return 5
// kthLargest.add(10); // return 5
// kthLargest.add(9); // return 8
// kthLargest.add(4); // return 8

// Constraints:

// 1 <= k <= 104
// 0 <= nums.length <= 104
// -104 <= nums[i] <= 104
// -104 <= val <= 104
// At most 104 calls will be made to add.
// It is guaranteed that there will be at least k elements in the array when you
// search for the kth element.

// APPROACH: Use a stream. Add the elements of nums to the stream. If the stream's size crosses k, poll the elements till the size becomes k. Because the smaller elements are never used. 
// Ex: if the array is [8,4,5,2] and k = 3, our stream only contains [8,4,5]. If the next offered element is 3 or 1, we will peek for the smallest = 4 but not remove 4. 
// And of 3 or 1 is added, we would have to pop it since the size exceeds k

// add method: offer the val to the stream and if adding it crosses the size beyond k, pop the smallest element. Then return the smallest element in the updated stream. Remember not to pop the element, just pek and return it.

// Time Complexity: Constructor: O(nlogk), Add method: O(logk)
//Space complexity: O(k)

class KthLargest {
    PriorityQueue<Integer> stream;
    int k;

    public KthLargest(int k, int[] nums) {
        this.stream = new PriorityQueue<>();
        this.k = k;
        for (int i = 0; i < nums.length; i++) { // O(n)
            // { O(logk)
            stream.offer(nums[i]);
            if (stream.size() > this.k) {
                stream.poll();
            }
            // }
        }
        // System.out.println("Stream: " + stream);
        // while (stream.size() > k) {
        // stream.poll();
        // }
        // System.out.println("Stream k size: " + stream);

    }

    public int add(int val) {
        stream.offer(val);
        if (stream.size() > this.k) {
            stream.poll();
        }
        return stream.peek();
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.add(val);
 */