class Solution {
    public int findCheapestPrice(int n, int[][] edges, int src, int dst, int k) {
        Queue<int[]> queue=new LinkedList<>();
        int[] dist=new int[n];
        List<List<int[]>> list=new ArrayList<>();
        for(int i=0;i<n;i++)
        {
            list.add(new ArrayList<>());
        } 
        for(int[] edge:edges)
        {
            list.get(edge[0]).add(new int[]{edge[1],edge[2]});
        }

        Arrays.fill(dist,-1);
        dist[src]=0;
        queue.add(new int[]{0,src,0});
        while(!queue.isEmpty())
        {
            int[] front=queue.poll();
            int stop=front[0];
            int u=front[1];
            int c=front[2];
            for(int[] nei:list.get(u))
            {
                int v1=nei[0];
                int c1=nei[1];
                if(stop<=k && (dist[v1]==-1 || c+c1<dist[v1]))
                { 
                    dist[v1]=c+c1;
                    queue.add(new int[]{stop+1,v1,dist[v1]}); 
                }
            }
        }

        return dist[dst];
    }
}
