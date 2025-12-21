class Solution {
    public String kthDistinct(String[] arr, int k) {
        int n = arr.length;

        HashMap<String,Integer> dict1 = new HashMap<>();

        for (int i = 0; i < arr.length; i++){
            if (!dict1.containsKey(arr[i])){
                dict1.put(arr[i],1);
            } else {
                dict1.put(arr[i],dict1.get(arr[i])+1);
            }
        }

        List<String> result = new ArrayList<>();

        for (int i = 0; i < n; i++){
            if (dict1.get(arr[i]) == 1){
                result.add(arr[i]);
            }
        }

        if (result.size() >= k){
            return result.get(k-1);
        } else {
            return "";
        }
    }
}
