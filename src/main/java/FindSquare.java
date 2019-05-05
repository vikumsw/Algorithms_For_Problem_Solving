import org.testng.Assert;
import org.testng.annotations.Test;

public class FindSquare {

    private static int goH(int[][] matrix, int row, int colStart, int check, int limit){
        int col = colStart;
        while (col < limit && matrix[row][col] == check) col++;
        return col - colStart;
    }

    private static int findSquare(int[][] matrix, int rowCount, int colCount){
        int maxR = 0;
        for(int row = 0; row < rowCount; row++){
            for(int col = 0; col < colCount; col++){
                maxR = Math.max(maxR, getSquare(matrix, rowCount, colCount, row, col));
            }
        }
        return maxR*maxR;
    }

    private static int getSquare(int[][] matrix, int rowCount, int colCount, int row, int col) {
        int w = goH(matrix, row, col, 1, colCount);

        if(w > 0){
            int marked = markLinked(matrix, rowCount, colCount, row, col);
            if(marked > 1 && marked == w*w){
                for(int rowIndex = row+1; rowIndex < w + row; rowIndex++){
                    int rowLen = goH(matrix, rowIndex, col, 2, colCount);
                    if(w != rowLen){
                        return 0;
                    }
                }
                return w;
            }
        }

        return 0;
    }

    static private int markLinked(int[][] matrix, int rowCnt, int colCnt, int row, int col){
        int marked = 0;
        if(     (row >= 0) && (row < rowCnt) &&
                (col >= 0) && (col < colCnt) &&
                (matrix[row][col] == 1))
        {
            marked = 1;
            matrix[row][col] = 2;
            marked +=   markLinked(matrix, rowCnt, colCnt, row + 1, col);
            marked +=   markLinked(matrix, rowCnt, colCnt, row - 1, col);
            marked +=   markLinked(matrix, rowCnt, colCnt, row, col + 1);
            marked +=   markLinked(matrix, rowCnt, colCnt, row, col - 1);
        }
        return marked;
    }

    @Test
    public void test1(){
        int[][] data = new int[][]{
                {1, 0, 0, 0},
                {0, 0, 1, 1},
                {1, 0, 1, 1},
                {1, 1, 0, 0},};

        Assert.assertEquals(findSquare(data, 4, 4), 4);
    }


    @Test
    public void test2(){
        int[][] data = new int[][]{
                {1, 0, 1, 1, 1},
                {0, 0, 1, 1, 1},
                {1, 0, 1, 1, 1},
                {1, 1, 0, 0, 0},};

        Assert.assertEquals(findSquare(data, 4, 5), 9);
    }

    @Test
    public void test3(){
        int[][] data = new int[][]{
                {1, 0, 1, 1, 1},
                {0, 0, 1, 1, 1},
                {1, 0, 1, 1, 1},
                {1, 1, 0, 1, 0},};

        Assert.assertEquals(findSquare(data, 4, 5), 0);
    }

    @Test
    public void test4(){
        int[][] data = new int[][]{
                {1, 0, 1, 1, 0},
                {0, 0, 1, 1, 0},
                {1, 1, 0, 1, 1},
                {1, 1, 0, 1, 1},};

        Assert.assertEquals(findSquare(data, 4, 5), 4);
    }

    @Test
    public void test5(){
        int[][] data = new int[][]{
                {1, 0, 0, 1, 0},
                {0, 1, 1, 0, 0},
                {1, 1, 1, 0, 1},
                {0, 0, 0, 0, 1},
                {1, 1, 0, 1, 1}};

        Assert.assertEquals(findSquare(data, 5, 5), 0);
    }

    @Test
    public void test6(){
        int[][] data = new int[][]{
                {1, 1, 0, 1, 0},
                {1, 0, 1, 0, 0},
                {1, 0, 1, 0, 1},
                {0, 0, 0, 0, 1},
                {1, 1, 0, 1, 1}};

        Assert.assertEquals(findSquare(data, 5, 5), 0);
    }

}
