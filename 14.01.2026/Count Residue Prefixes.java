class Solution {
    public int residuePrefixes(String s) {
        Set <Character> unique = new HashSet<Character>();
        int residue = 0;
        for(int i=0;i<s.length();i++)
        {
            unique.add(s.charAt(i));
            if(unique.size()==((i+1)%3))
            {
                residue++;
            }
            if(unique.size()>2)
            {
                break;
            }
        }
        return residue;
    }
}
