class Solution {
    public int minimumCost(int[] cost) {
        if(cost.length==1)return cost[0];
        if(cost.length==2)return cost[0]+cost[1];
        Arrays.sort(cost);
        List<Integer> list=new ArrayList<>();
        for(int i:cost)list.add(i);
        int sum=0;
        while(list.size()>2){
            int tot=list.get(list.size()-1)+list.get(list.size()-2);
            list.remove(list.size()-1);
            list.remove(list.size()-1);
            sum+=tot;
            list.remove(list.size()-1);
        }
        if(list.size()==1)sum+=list.get(0);
        if(list.size()==2)sum+=list.get(1)+list.get(0);
        return sum;
    }
}
