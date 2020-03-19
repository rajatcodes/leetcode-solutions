# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> visited = new HashMap<Character, Integer>();
        int i=0;
        int j=0;
        int n = s.length();
        if(n==0){
            return 0;
        }
        int max_len = 0;
       do{
           visit(s.charAt(j), visited);
           int tempVal = visited.get(s.charAt(j));
           while(tempVal==2){
               leave(s.charAt(i), visited);
               tempVal = visited.get(s.charAt(j));
               i+=1;
           }
           int current_len = j+1-i;
           if(max_len<current_len){
               max_len = current_len;
           }
           
           j=j==n-1?j:j+1;
                        
        } while(i<n-1);
        return max_len;
    }
    
    public void visit(char a, Map<Character, Integer> visited){
        if(visited.containsKey(a)){
            int val = visited.get(a);
            visited.put(a,val+1);
        }else{
            visited.put(a,1);
        }
    }
    
    public void leave(char a, Map<Character, Integer> visited){
        if(visited.containsKey(a)){
            int val = visited.get(a);
            visited.put(a,val-1);
        }
    }
}
