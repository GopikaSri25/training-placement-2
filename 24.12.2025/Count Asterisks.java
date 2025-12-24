class Solution {
    public int countAsterisks(String s) {
        String str[] = s.split("|");
        int c=0,bar=0;
        for(int i=0;i<s.length();i++){
            char ch = s.charAt(i);
            if(ch=='|')
                bar++;
            if(bar%2==0 && ch=='*')
                c++;
        }
        return c;
    }
}
