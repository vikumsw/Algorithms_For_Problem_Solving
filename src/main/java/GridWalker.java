public class GridWalker {

    final static int M = 4;
    final static int N = 4;

    static Node nodes[][] = new Node[M][N];

    static class Node{
        int x;
        int y;

        int bestDist = Integer.MAX_VALUE;
        boolean blockedNode = false;

        Node(int x, int y){
            this.x = x;
            this.y = y;
        }

        void go(int dist){
            if(!blockedNode && dist < bestDist){
                bestDist = dist;
                if(x > 0) nodes[x-1][y].go(dist+1);
                if(x < M-1) nodes[x+1][y].go(dist+1);
                if(y > 0) nodes[x][y-1].go(dist+1);
                if(y < N-1) nodes[x][y+1].go(dist+1);
            }
        }
    }

    public static void main(String[] args) {
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                nodes[i][j] = new Node(i, j);
            }
        }

        nodes[1][0].blockedNode = true;
        nodes[1][1].blockedNode = true;
        nodes[1][2].blockedNode = false;
        nodes[1][3].blockedNode = true;

        Node start = nodes[3][0];
        Node end = nodes[0][0];

        start.go(0);

        if(end.bestDist < Integer.MAX_VALUE)
            System.out.println("Reached in : " + end.bestDist);
        else
            System.out.println("Can't reach.");
    }
}
