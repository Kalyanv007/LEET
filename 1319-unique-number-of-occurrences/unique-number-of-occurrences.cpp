class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        unordered_map<int,int>freq;
        for(int num:arr){
            freq[num]++;
        }
        unordered_set<int>s1;
        for(auto &it:freq){
            if(s1.count(it.second))
            return false;
            s1.insert(it.second);
        }
        return true;
    }
};