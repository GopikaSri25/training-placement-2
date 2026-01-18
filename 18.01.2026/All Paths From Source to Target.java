class Solution {
    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        dfs(graph, 0, new ArrayList(), result);
        return result;
    }

    public void dfs(int[][] graph, int toVisit, ArrayList<Integer> path, List<List<Integer>> result) {
        if (toVisit == graph.length - 1) {
            path.add(toVisit);
            result.add((ArrayList<Integer>) path.clone());
            path.removeLast();
            return;
        }
        int[] next = graph[toVisit];
        if (next.length == 0)
            return;
        path.add(toVisit);
        for (int n : next) {
            dfs(graph, n, path, result);
        }
        path.removeLast();
    }
}
