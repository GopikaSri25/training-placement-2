class Solution {
    public boolean validPath(int n, int[][] edges, int source, int destination) {
        UnionFind uf  = new UnionFind(n);
        for(int i = 0; i < edges.length; i++) {
           uf.union(edges[i][0], edges[i][1]);
        }
        return uf.connected(source, destination);
    }
    class UnionFind {
        int[] rank;
        int[] parent;
        public UnionFind(int n) {
            rank = new int[n];
            parent = new int[n];
            for(int i =0; i <n; i++) {
                rank[i] =1;
                parent[i] = i;
            }
        }
        public boolean connected (int x, int y) {
            return find(x) == find(y);
        }
        public void union(int x, int y) {
            int rootX = find(x);
            int rootY = find(y);
            if(rootX!= rootY) {
                if (rank[rootX] > rank[rootY]) {
                    parent[rootY] = parent[rootX];
                }
                else if(rank[rootY] > rank[rootX]) {
                    parent[rootX] = parent[rootY];
                }
                else {
                    parent[rootX] = rootY;
                    rank[rootY]++;
                }
            }
        }
        public int find (int x) {
            if (parent[x] != x) {
                parent[x] = find(parent[x]);
            }
            return parent[x];
        }
    } 
}
