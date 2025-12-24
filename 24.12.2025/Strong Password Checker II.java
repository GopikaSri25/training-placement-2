class Solution {
    public boolean strongPasswordCheckerII(String password) {

        if(password.length ()<8){
            return false;
        }
        boolean haslower=false;
        boolean hasupper=false;
        boolean hasdigit=false;
        boolean hasspecial=false;

        String specialchars="!@#$%^&*()-+";
        for(int i=0;i<password.length();i++){
            char c =password.charAt(i);
            if(i>0 && password.charAt(i)==password.charAt(i-1)){
                return false;
            }
            if(Character.isLowerCase(c)){
                haslower=true;
            } else if (Character.isUpperCase(c)){
                hasupper=true;
            } else if (Character.isDigit(c)){
                hasdigit=true;
            } else if(specialchars.indexOf(c)!=-1){
                hasspecial=true;
            }
        }
        return haslower && hasupper && hasdigit && hasspecial;
    }
}
