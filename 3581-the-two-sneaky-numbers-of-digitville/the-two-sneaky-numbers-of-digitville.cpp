class Solution {
public:
    vector<int> getSneakyNumbers(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<int> sneaky;

        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] == nums[i - 1]) {
                sneaky.push_back(nums[i]);
            }
            if(sneaky.size()==2){
                return sneaky;
            }
        }

        return sneaky;
    }
};
