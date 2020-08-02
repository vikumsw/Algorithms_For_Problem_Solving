import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    // Complete the minimumBribes function below.
    static void minimumBribes(int[] q) {
        int totalBribes = 0;
        int individualBribes = 0;
        for(int i=q.length-1;i>0;i--){
            for(int j=i;j<q.length;j++){
                int valR = q[j];
                int valL = q[j-1];
                //System.out.println("[valR="+valR+",valL="+valL+",i="+i+",j="+j+"]");
                if(valR < valL){
                    individualBribes++;
                    q[j-1] = valR;
                    q[j] = valL;
                }else{
                    break;
                }
            }
            if(individualBribes>2){
                System.out.println("Too chaotic");
                return;
            }else{
                totalBribes += individualBribes;
                individualBribes = 0;
            }
        }
            
        
        System.out.println(totalBribes);
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int t = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int tItr = 0; tItr < t; tItr++) {
            int n = scanner.nextInt();
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            int[] q = new int[n];

            String[] qItems = scanner.nextLine().split(" ");
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            for (int i = 0; i < n; i++) {
                int qItem = Integer.parseInt(qItems[i]);
                q[i] = qItem;
            }
            
            minimumBribes(q);
            
        }

        scanner.close();
    }
}
