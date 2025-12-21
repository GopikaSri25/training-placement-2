class Solution {
   public static boolean isNumber(String s) {
       try{
        int num = Integer.parseInt(s);
        if(num >= 0 && num <= 100){
            return true;
        }
       }
        catch(NumberFormatException e){
            return false;
        }
        return false;
     
}

    public boolean areNumbersAscending(String s) {
        String arr[]=s.split("\\s+");
        List<Integer>list=new ArrayList<>();
        for(int i=0;i<arr.length;i++){
            String str=arr[i];
            if(isNumber(str)){

                int num=Integer.parseInt(str);
                list.add(num);
            }
        }
        for(int i=0;i<list.size()-1;i++){
            if(list.get(i)>=list.get(i+1))
            {
               return false;
            }
        }
        return true;
    }
}
