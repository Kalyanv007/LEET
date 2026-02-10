class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int count=0;
        int n=nums.size();
        bool hasZero=false;
        if(n==1)return 0;
        for(int i=0;i<n;i++){
            if(nums[i]==0){
                hasZero=true;
                int left,right;
                int l=0,r=0;
                left=i-1;
                right=i+1;
                while(left>=0 && nums[left]==1){
                    left--;
                    l++;
                }
                while(right<n && nums[right]==1){
                    right++;
                    r++;

                }
                count=max(count,l+r);
            }
        }
        if(!hasZero){
            return n-1;
        }
        return count;
    }
};