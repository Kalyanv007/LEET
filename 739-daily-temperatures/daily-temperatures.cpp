class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        vector<int> answer(n, 0);
        stack<int> st;  // stores indices

        for (int i = n - 1; i >= 0; i--) {

            // Remove all colder or equal days
            while (!st.empty() && temperatures[i] >= temperatures[st.top()]) {
                st.pop();
            }

            // If stack not empty, top is next warmer day
            if (!st.empty()) {
                answer[i] = st.top() - i;
            }

            // Push current index
            st.push(i);
        }

        return answer;
    }
};