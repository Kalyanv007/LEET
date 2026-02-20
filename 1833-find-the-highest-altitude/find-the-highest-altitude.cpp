class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        
        int cur=0;
        int maxi=0;
        for(int g:gain){
            cur+=g;
            maxi=max(maxi,cur);
        }
        return maxi;
    }
};