class Solution {
    public String generateTag(String caption) {
        StringBuilder sb=new StringBuilder();
        sb.append("#");
        String[] word=caption.split(" ");
        int is=1;
        for(String w:word){
            if(w.length()==0){
                continue;
            }
            w=w.toLowerCase();
            if(is==1){
                sb.append(w);
                is=0;
            }
            else{
                sb.append(Character.toUpperCase(w.charAt(0)));
                sb.append(w.substring(1));
            }
        }
        if(sb.length()>100){
            return sb.substring(0,100);
        }
        return sb.toString();
    }
}
