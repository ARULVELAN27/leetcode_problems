class Solution {
    public int possibleStringCount(String word) {
        int a=1;
        int o=word.length();
        for(int i=1;i<o;i++){
            if(word.charAt(i)==word.charAt(i-1)){
                a+=1;
            }
        }
        return a;
    }
}
