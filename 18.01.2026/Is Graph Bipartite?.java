class Solution {
    public boolean isBipartite(int[][] graph) {
        int n = graph.length;
        int[] colors = new int[n]; 
        for (int i = 0; i < n; i++) {
            if (colors[i] != 0) continue;

            if (!dfs(i, colors, graph, 1)) return false;
        }

        return true;
    }

    private boolean dfs(int cur, int[] colors, int[][] graph, int color) {
        if (colors[cur] != 0) {
            return colors[cur] == color;
        }
        colors[cur] = color;
        int nextColor = color == 1 ? 2 : 1;

        for (int u : graph[cur]) {
            if (!dfs(u, colors, graph, nextColor)) return false;
        }

        return true;
    }
}
