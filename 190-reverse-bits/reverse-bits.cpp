class Solution {
public:
    int reverseBits(int n) {
        unsigned int result=0;
        unsigned int num=(unsigned int)n;
        for(int i=0;i<32;i++){
            result <<= 1;          
            result |= (num & 1); 
            num >>= 1;
        }
        return (int)result;
    }
};