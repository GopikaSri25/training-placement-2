class Solution {
    public String decodeMessage(String key, String message) {
        StringBuilder sb=new StringBuilder();
        char[] arr=new char[26];
        int index=0;
        for(int i=0;i<key.length();i++){
            char ch=key.charAt(i);
            if(ch==' ') continue;
            else if(sb.indexOf(String.valueOf(ch))==-1){
                sb.append(ch);
                arr[index]=ch;
                index++;
            }
        }
        sb=new StringBuilder();
        for(int j=0;j<message.length();j++){
            char ch=message.charAt(j);
            if(ch==' ') sb.append(" ");
            else{

                for(int i=0;i<26;i++){
                    if(ch==arr[i]){
                        sb.append((char)('a'+i));
                        break;

                    }
                }
            }
        }
        return sb.toString();
    }
}
