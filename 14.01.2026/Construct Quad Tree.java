class Solution {
    public Node construct(int[][] grid) {
        return constructQuadTree(grid, 0, grid.length - 1, 0, grid[0].length - 1);
    }

    Node constructQuadTree(int[][] grid, int startRow, int finalRow, int startCol, int finalCol) {
        if (startRow == finalRow && startCol == finalCol) {
            int val = grid[startRow][startCol];
            return new Node(val == 1 ? true : false, true);
        }

        int splitRow = (startRow + finalRow) / 2;
        int splitCol = (startCol + finalCol) / 2;

        Node topLeft = constructQuadTree(grid, startRow, splitRow, startCol, splitCol);
        Node bottomLeft = constructQuadTree(grid, splitRow + 1, finalRow, startCol, splitCol);
        Node topRight = constructQuadTree(grid, startRow, splitRow, splitCol + 1, finalCol);
        Node bottomRight = constructQuadTree(grid, splitRow + 1, finalRow, splitCol + 1, finalCol);

        if (topLeft.isLeaf && topRight.isLeaf && bottomLeft.isLeaf && bottomRight.isLeaf
                && topLeft.val == topRight.val && topLeft.val == bottomLeft.val && topLeft.val == bottomRight.val) {
            return new Node(topLeft.val, true);
        } else {
            return new Node(true, false, topLeft, topRight, bottomLeft, bottomRight);
        }
    }
}
