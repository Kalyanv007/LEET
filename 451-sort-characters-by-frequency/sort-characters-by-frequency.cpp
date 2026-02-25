class Solution {
private: 
    static bool comparator(pair<int,char> p1, pair<int,char> p2) {
        if (p1.first > p2.first) return true;
        if (p1.first < p2.first) return false;
        return p1.second < p2.second;
    }

public:
    string frequencySort(string s) {

        unordered_map<char,int> mp;

        // Count frequencies
        for (char ch : s) {
            mp[ch]++;
        }

        // Move map data into vector<pair<int,char>>
        vector<pair<int,char>> freq;
        for (auto &it : mp) {
            freq.push_back({it.second, it.first});
        }

        // Sort using your comparator
        sort(freq.begin(), freq.end(), comparator);

        // Build final string
        string ans = "";
        for (auto &p : freq) {
            ans.append(p.first, p.second);
        }

        return ans;
    }
};