class Solution {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {
        int i = 0;
        int count = 0;
        int oddCount = 0;
        int prefixEven = 0;

        for (int j = 0; j < nums.size(); j++) {

            if (nums[j] % 2 == 1) {
                oddCount++;
                prefixEven = 0;  // reset prefix count when new odd appears
            }

            while (oddCount == k) {
                prefixEven++;
                if (nums[i] % 2 == 1) {
                    oddCount--;
                }
                i++;
            }

            count += prefixEven;
        }

        return count;
    }
};