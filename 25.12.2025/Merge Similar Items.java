class Solution {
    public List<List<Integer>> mergeSimilarItems(int[][] items1, int[][] items2) {
        int n = items1.length, m = items2.length;

        HashMap<Integer,Integer> dict1 = new HashMap<>();
        HashMap<Integer,Integer> dict2 = new HashMap<>();
        HashMap<Integer,Integer> d = new HashMap<>();

        for (int i = 0; i < n; i++){
            if (!dict1.containsKey(items1[i][0])){
                dict1.put(items1[i][0],items1[i][1]);
            }
        }

        for (int i = 0; i < m; i++){
            if (!dict2.containsKey(items2[i][0])){
                dict2.put(items2[i][0],items2[i][1]);
            }
        }

        for (int v: dict1.keySet()){
            if (dict2.containsKey(v)){
                d.put(v,dict1.get(v)+dict2.get(v));
            } else {
                d.put(v,dict1.get(v));
            }
        }

        for (int v: dict2.keySet()){
            if (!dict1.containsKey(v)){
                d.put(v,dict2.get(v));
            }
        }

        List<List<Integer>> result = new ArrayList<>();

        for (int v: d.keySet()){
            List<Integer> ans = new ArrayList<>();
            ans.add(v);
            ans.add(d.get(v));
            result.add(ans);
        }

        Collections.sort(result, (o1,o2) -> (o1.get(0)-o2.get(0)));

        return result;
    }
}
