class Solution {
public:
    int possibleStringCount(string word) {
        int a=1;
        for(int i=1;i<word.length();i++){
            if(word[i]==word[i-1]){
                a=a+1;
            }
        }
        return a;
    }
};
