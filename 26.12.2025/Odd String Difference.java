class Solution {
    public String oddString(String[] w) {
       String a=diff(w[0]).equals(diff(w[1]))?diff(w[0]):diff(w[2]);
       for(int i=0;i<w.length;i++){
        if(!diff(w[i]).equals(a)) return w[i];
       }
    return "";
    }

 String diff(String w){
    StringBuilder e=new StringBuilder();
    for(int i=1;i<w.length();i++){
        e.append(w.charAt(i)-w.charAt(i-1)).append("#");
    }
    return e.toString();
 }
 }
