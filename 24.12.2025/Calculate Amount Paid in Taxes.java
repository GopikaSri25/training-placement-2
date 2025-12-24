class Solution {
    public double calculateTax(int[][] brackets, int income) {
        
        int upper =0;
        double sum=0;
        for(int i=0;i<brackets.length;i++){
            int x=brackets[i][0];
            if(x>income) x=income;
                upper= x - upper;
                double percentage= (double ) (upper * ((double) brackets[i][1]/100));
                upper=brackets[i][0];
                if(percentage>0)
                sum+=percentage;
        }
        return sum;
    }
}
