class Solution {
public:
    int numberOfBeams(vector<string>& bank) {
        int prevcount=0;
        int ans=0;
        for(string row: bank){
            int curcount=0;
            for(char c:row){
                if(c=='1') curcount++;
            }
            if(curcount>0){
                ans+=(curcount*prevcount);
                prevcount=curcount;
            }
        }
        return ans;
    }
};