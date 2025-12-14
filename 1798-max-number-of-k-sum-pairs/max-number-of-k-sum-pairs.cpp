class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
        unordered_map<int,int>freq;
        int count=0;
        for(int i=0;i<nums.size();i++){
            int rem=k-nums[i];
            if(freq[rem]>0){
                count++;
                freq[rem]--;
            }
            else freq[nums[i]]++;
        }
        return count;
    }
};