class Solution {
    class Pair implements Comparable<Pair>
    {
        int freq;
        int data;

        Pair(int freq,int data)
        {
            this.freq=freq;
            this.data=data;
        }

        public int compareTo(Pair that)
        {
            int cnt =Integer.compare(that.freq,this.freq);
            if(cnt!=0) return cnt;
            return Integer.compare(this.data, that.data);
        }
    }

    public int mostFrequentEven(int[] nums) {
        HashMap<Integer,Integer> mp = new HashMap<>();
        PriorityQueue<Pair> pq = new PriorityQueue<>(Collections.reverseOrder());
        for(int i=0;i<nums.length;i++)
        {   if(nums[i]%2==0)
            mp.put(nums[i],mp.getOrDefault(nums[i],0)+1);
        }

        for(Map.Entry<Integer, Integer> entry : mp.entrySet())
        {
            Integer key = entry.getKey();
            Integer value = entry.getValue();
            pq.add(new Pair(value,key));
            if(pq.size()>1)
            {
                pq.poll();
            }
        }
        
        return pq.isEmpty()?-1:pq.peek().data;

    }
}
