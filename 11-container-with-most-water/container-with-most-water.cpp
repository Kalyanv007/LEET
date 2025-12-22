class Solution {
public:
    int maxArea(vector<int>& height) {
        int area = 0;
        int i = 0;
        int j = height.size() - 1;

        while (i < j) {
            int h = min(height[i], height[j]);
            area = max(area, h * (j - i));

            if (height[i] < height[j]) {
                i++;      // move smaller height
            } else {
                j--;      // move smaller height
            }
        }
        return area;
    }
};
