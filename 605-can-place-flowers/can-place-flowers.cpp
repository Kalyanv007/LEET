class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int count=0;
        int i=1;
        if(n==0)return true;
        if(flowerbed.size()==1){
           if(flowerbed[0]!=1)
            return true; 
            else return false;
        }

        
        if(flowerbed[0]==0 && flowerbed[1]!=1){
            flowerbed[0]=1;
            count++;
        }
        while(i<flowerbed.size()-1){
            if(flowerbed[i]!=1){
                if(flowerbed[i-1]==1||flowerbed[i+1]==1)i++;
                else{
                    flowerbed[i]=1;
                    count++;
                    i++;
                    if(count==n)break;
                }
            }
            else{
                i++;
            }
        }
        if(count<n){
            if(flowerbed[flowerbed.size()-1]==0 && flowerbed[flowerbed.size()-2]==0){
                count++;
            }
        }
        if(count>=n){
            return true;
        }
        else{
            return false;
        }
    }
};