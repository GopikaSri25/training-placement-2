class Solution {
    public boolean checkValid(int[][] matrix) {
        int n = matrix.length;

        for (int i = 0; i < n; i++){
            Set<Integer> visited = new HashSet<>();
            for (int j = 0; j < n; j++){
                if (1 <= matrix[i][j] && matrix[i][j] <= n){
                    visited.add(matrix[i][j]);
                }
            }
            if (visited.size() != n){
                return false;
            }
        }

        
        for (int j = 0; j < n; j++){
            Set<Integer> visited = new HashSet<>();
            for (int i = 0; i < n; i++){
                if (1 <= matrix[i][j] && matrix[i][j] <= n){
                    visited.add(matrix[i][j]);
                }
            }
            if (visited.size() != n){
                return false;
            }
        }

        return true;
    }
}
