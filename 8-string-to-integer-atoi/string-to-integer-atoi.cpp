class Solution {
public:
    int myAtoi(string s) {
        int n = s.length();
        string str = "";
        int i = 0;

        // Skip leading spaces
        while (i < n && isspace(s[i])) {
            i++;
        }

        // Handle sign
        if (i < n && (s[i] == '+' || s[i] == '-')) {
            str += s[i];
            i++;
        }

        // Process digits
        while (i < n && isdigit(s[i])) {
            str += s[i];
            i++;
        }

        // If empty or only sign, return 0
        if (str.empty() || str == "+" || str == "-")
            return 0;

        // Convert safely using long long
        long long num = 0;
        int sign = 1;
        int start = 0;

        if (str[0] == '-') {
            sign = -1;
            start = 1;
        } else if (str[0] == '+') {
            start = 1;
        }

        for (int j = start; j < str.length(); j++) {
            num = num * 10 + (str[j] - '0');

            // Clamp during build
            if (sign == 1 && num > INT_MAX)
                return INT_MAX;
            if (sign == -1 && -num < INT_MIN)
                return INT_MIN;
        }

        return sign * num;
    }
};