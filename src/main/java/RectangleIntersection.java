import org.testng.Assert;
import org.testng.annotations.Test;

public class RectangleIntersection {
    private class Rectangle {
        int topLeftX;
        int topLeftY;
        int width;
        int height;

        Rectangle(int x, int y, int width, int height){
            this.topLeftX = x;
            this.topLeftY = y;
            this.width = width;
            this.height = height;
        }
    }

    private int GetRectangleIntersectionArea(Rectangle A, Rectangle B){

        if (A.topLeftX > B.topLeftX + B.width || B.topLeftX > A.topLeftX + A.width) // If one rectangle is on left side of other
            return 0;
        if (A.topLeftY < B.topLeftY - B.height || B.topLeftY < A.topLeftY - A.height) // If one rectangle is above other
            return 0;

        /*  x_distance for intersecting rectangle =  min(r1.x, r2.x) – max(l1.x, l2.x)
            y_distance for 1st rectangle = min(r1.y, r2.y) – max(l1.y, l2.y) */

        int intersectWidth = Math.min(A.topLeftX + A.width, B.topLeftX + B.width) - Math.max(A.topLeftX, B.topLeftX);
        int intersectHeight = Math.min(A.topLeftY, B.topLeftY) - Math.max(A.topLeftY - A.height, B.topLeftY - B.height);

        return Math.abs(intersectWidth*intersectHeight);
    }

    @Test
    public void testIntersectedArea1(){
        Rectangle A = new Rectangle(1,4,3,3);
        Rectangle B = new Rectangle(0,5,4,3);
        Assert.assertEquals(GetRectangleIntersectionArea(A, B), 6);
    }

    @Test
    public void testIntersectedArea2(){
        Rectangle A = new Rectangle(0,10,20,10);
        Rectangle B = new Rectangle(2,8,28,3);
        Assert.assertEquals(GetRectangleIntersectionArea(A, B), 54);
    }
}
