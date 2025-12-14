class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
        // unordered_map<int,int>freq;
        // int count=0;
        // for(int i=0;i<nums.size();i++){
        //     int rem=k-nums[i];
        //     if(freq[rem]>0){
        //         count++;
        //         freq[rem]--;
        //     }
        //     else freq[nums[i]]++;
        // }
        // return count;
        sort(nums.begin(),nums.end());
        int sum=0;
        int i=0,j=nums.size()-1;
        int count=0;
        while(i<j){
            sum=nums[i]+nums[j];
            if(sum>k && i<j){
                j--;
            }
            else if(sum<k && i<j){
                i++;

            }
            else{
                count++;
                i++;
                j--;
            }
        }
        return count;
    }
};