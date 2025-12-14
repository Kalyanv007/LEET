class Solution {
public:
    vector<vector<int>> findDifference(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int,int>map1;
        unordered_map<int,int>map2;
        vector<int>ans1;
        vector<int>ans2;
        unordered_set<int> s1(nums1.begin(), nums1.end());
        unordered_set<int> s2(nums2.begin(), nums2.end());


        for (int x : s1) {
            if (s2.find(x) == s2.end()) {
                ans1.push_back(x);
            }
        }

        for (int x : s2) {
            if (s1.find(x) == s1.end()) {
                ans2.push_back(x);
            }
        }
        return{ans1,ans2};
    }
};