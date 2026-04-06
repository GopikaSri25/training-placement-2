import java.util.*;

public class Solution {

    public static boolean canWin(int leap, int[] game) {
        return canWinHelper(leap, game, 0);
    }

    private static boolean canWinHelper(int leap, int[] game, int i) {

        
        if (i >= game.length) {
            return true;
        }

        
        if (i < 0 || game[i] == 1) {
            return false;
        }

        game[i] = 1;

      
        return canWinHelper(leap, game, i + leap) ||
               canWinHelper(leap, game, i + 1) ||
               canWinHelper(leap, game, i - 1);
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int q = scan.nextInt();

        while (q-- > 0) {
            int n = scan.nextInt();
            int leap = scan.nextInt();

            int[] game = new int[n];
            for (int i = 0; i < n; i++) {
                game[i] = scan.nextInt();
            }

            System.out.println(canWin(leap, game) ? "YES" : "NO");
        }

        scan.close();
    }
}
