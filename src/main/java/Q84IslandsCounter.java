/*
Challenge #84:
This problem was asked by Amazon.

Given a matrix of 1s and 0s, return the number of "islands" in the matrix.
A 1 represents land and 0 represents water, so an island is a group of 1s
that are neighboring whose perimeter is surrounded by water.

For example, this matrix has 4 islands.

1 0 0 0 0
0 0 1 1 0
0 1 1 0 0
0 0 0 0 0
1 1 0 0 1
1 1 0 0 1
* */

import org.testng.Assert;
import org.testng.annotations.Test;

public class Q84IslandsCounter {
    private int traversMap(int[][] map, int i, int j, boolean canGo){
        int nodeValue = map[i][j];
        if (nodeValue == 1)
            canGo = true;

        map[i][j] = 0;

        if ((nodeValue == 1) && (j+1 < map[i].length) && (map[i][j+1]==1))
            traversMap(map, i, j+1, canGo);
        if ((nodeValue == 1) && (i+1 < map.length) && (map[i+1][j] == 1))
            traversMap(map, i+1, j, canGo);
        if ((nodeValue == 1) && (j-1 >= 0) && (map[i][j-1] == 1))
            traversMap(map, i, j-1, canGo);
        if ((nodeValue == 1) && (i-1 >= 0) && (map[i-1][j] == 1))
            traversMap(map, i-1, j, canGo);

        if (canGo == true)
            return 1;
        else
            return 0;
    }

    private int go(int[][] map){
        int count = 0;
        for (int i = 0; i < map.length; ++i)
            for (int j =0; j < map[i].length; ++j)
                count += traversMap(map, i, j, false);
        return count;
    }

    @Test
    private void testIslandCount(){
        int[][] map1 = {{1,0,0,0,0},{0,0,1,1,0},{0,1,1,0,0},{0,0,0,0,0},{1,1,0,0,1},{1,1,0,0,0}};
        Assert.assertEquals(go(map1), 4);

        int[][] map2 = {{1,0,0,0,0},{0,0,1,1,0},{0,1,1,0,0},{0,1,0,0,0},{1,1,0,0,1},{1,1,0,0,0}};
        Assert.assertEquals(go(map2), 3);

        int[][] map3 = {{1,0,0,0,0},{0,0,1,1,0},{0,1,1,0,0},{0,0,0,1,0},{1,1,0,0,1},{1,1,0,0,0}};
        Assert.assertEquals(go(map3), 5);
    }
}
