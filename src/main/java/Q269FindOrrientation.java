import org.testng.Assert;
import org.testng.annotations.Test;
import java.util.ArrayList;
import java.util.List;

public class Q269FindOrrientation {
    public String getDominoesOrrientation(String forces){
        char[] orrientation = forces.toCharArray();
        List<Integer> indices = new ArrayList<>();
        int i =0 ,cur = 0;
        for(char force : orrientation){
            if (force != '.')
                indices.add(i);
            ++i;
        }

        for (int next : indices){
            if (orrientation[cur] == '.' && orrientation[next] == 'L')
                setFixSide(cur, next, 'L', orrientation);

            else if (orrientation[cur] == 'R' && orrientation[next] == 'L'){
                if ((next-cur) %2 == 0)
                    setSideUnEvenly(cur, next, orrientation);
                else
                    setSideEvenly(cur, next, orrientation);
            }
            else if (orrientation[cur] == 'L' && orrientation[next] == 'L')
                setFixSide(cur, next, 'L', orrientation);
            else if (orrientation[cur] == 'R' && orrientation[next] == 'R')
                setFixSide(cur, next, 'R', orrientation);

            cur = next;
        }
        if (cur != orrientation.length && orrientation[cur] == 'R'){
            setFixSide(cur, orrientation.length, 'R', orrientation);
        }
        return new String(orrientation);
    }

    public void setSideEvenly(int start, int end, char [] orrientation){
        for (int i = start+1; i < end; i++)
            if (i < end+1 - start)
                orrientation[i] = 'R';
            else
                orrientation[i] = 'L';
    }

    public void setSideUnEvenly(int start, int end, char [] orrientation){
        for (int i = start+1; i < end; i++)
            if (i < end-start)
                orrientation[i] = 'R';
            else if (i > end -start)
                orrientation[i] = 'L';
    }

    public void setFixSide(int start, int end, char side, char [] orrientation){
        for (int i = start; i<end; i++)
            orrientation[i] = side;
    }

    @Test
    public void testDominoesOrrientation(){
        Assert.assertEquals(getDominoesOrrientation(".L.R....L"), "LL.RRRLLL");
        Assert.assertEquals(getDominoesOrrientation("..R...L.L"), "..RR.LLLL");
        Assert.assertEquals(getDominoesOrrientation("..L..."), "LLL...");
        Assert.assertEquals(getDominoesOrrientation("..R..."), "..RRRR");
    }
}
