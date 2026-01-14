class Solution {
    public boolean canIWin(int maxChoosableInteger, int desiredTotal) {
      int sum = maxChoosableInteger * (maxChoosableInteger + 1) / 2;
        if (desiredTotal <= 0) return true;
        if (sum < desiredTotal) return false;
        
        Map<Integer, Boolean> memo = new HashMap<>();
        return canWin(desiredTotal, 0, maxChoosableInteger, memo);
    }
    
    private boolean canWin(int total, int used, int maxInt, Map<Integer, Boolean> memo) {
        if (memo.containsKey(used)) return memo.get(used);
        
        for (int i = 0; i < maxInt; i++) {
            if (((used >> i) & 1) == 0) { 
                int newUsed = used | (1 << i);
                if (total <= i + 1 || !canWin(total - (i + 1), newUsed, maxInt, memo)) {
                    memo.put(used, true);
                    return true;
                }
            }
        }
        
        memo.put(used, false);
        return false;   
    }
}
