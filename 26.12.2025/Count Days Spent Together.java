class Solution {
    public int countDaysTogether(String arriveAlice, String leaveAlice, String arriveBob, String leaveBob) {
      int ar[]={31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
      int daySum[]=new int[13];
      int sum=0;
      for(int i=0;i<ar.length;i++)
      {
         sum+=ar[i];
         daySum[i+1]=sum;
      }
      int arrivalAliceDays=daySum[Integer.valueOf(arriveAlice.substring(0,2))-1]+Integer.valueOf(arriveAlice.substring(3,5));
      int leaveAliceDays=daySum[Integer.valueOf(leaveAlice.substring(0,2))-1]+Integer.valueOf(leaveAlice.substring(3,5));
      int arrivalBobDays=daySum[Integer.valueOf(arriveBob.substring(0,2))-1]+Integer.valueOf(arriveBob.substring(3,5));
      int leaveBobDays=daySum[Integer.valueOf(leaveBob.substring(0,2))-1]+Integer.valueOf(leaveBob.substring(3,5));
       int count=0;
      for(int i=arrivalAliceDays;i<=leaveAliceDays;i++)
      {
        if(i>=arrivalBobDays && i<=leaveBobDays)
        count++;
      }
      return count;
    }
}
