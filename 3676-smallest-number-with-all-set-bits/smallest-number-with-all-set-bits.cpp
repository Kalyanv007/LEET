class Solution {
public:
    int smallestNumber(int n) {
        // Find the smallest number of the form (2^k - 1) that is >= n
        // These are numbers with all bits set: 1, 3, 7, 15, 31, 63, 127...
      
        // Start with 2^0 = 1
        int powerOfTwo = 1;
      
        // Keep doubling the power of 2 until (powerOfTwo - 1) >= n
        // Left shift by 1 is equivalent to multiplying by 2
        while (powerOfTwo - 1 < n) {
            powerOfTwo <<= 1;  // powerOfTwo = powerOfTwo * 2
        }
      
        // Return the number with all bits set (2^k - 1)
        return powerOfTwo - 1;
    }
};