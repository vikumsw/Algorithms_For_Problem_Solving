import org.testng.annotations.Test;

import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class ComplexityCalculator {
    @Test
    public void testSizeComplexity() throws IOException {
        FileReader fileReader = new FileReader("D:/Projects/DailyCoding/Algorithms_For_Problem_Solving/src/main/out/sample.java");
        BufferedReader br = new BufferedReader(fileReader);

        List<String> codeLines = new ArrayList<>();

        List<Integer> nKw = new ArrayList<>();
        List<Integer> nId = new ArrayList<>();
        List<Integer> nOp = new ArrayList<>();
        List<Integer> nNv = new ArrayList<>();
        List<Integer> nSl = new ArrayList<>();
        List<Integer> cS = new ArrayList<>();

        Integer wKw = 1;
        Integer wId = 1;
        Integer wOp = 1;
        Integer wNv = 1;
        Integer wSl = 1;

        String readLine;
        while((readLine = br.readLine())!= null){
            codeLines.add(readLine);
            nKw.add(getKeyWordCount(readLine));
            nId.add(getIdentifierCount(readLine));
            nOp.add(getOperatorCount(readLine));
            nNv.add(getNumericalValueCount(readLine));
            nSl.add(getStringLiteralCount(readLine));
        }

        for (int i = 0; i < codeLines.size(); i++) {
            cS.add(nKw.get(i)*wKw + nId.get(i)*wId + nOp.get(i)*wOp + nNv.get(i)*wNv + nSl.get(i)*wSl);
        }

        System.out.println("Nkw " + "Nid " + "Nop " + "Nnv " + "Nsl " + "Cs");
        for (int i = 0; i < codeLines.size(); i++) {
            System.out.println(nKw.get(i) + "   " + nId.get(i) + "   " +nOp.get(i) + "   " +nNv.get(i) + "   " +nSl.get(i) + "   " +cS.get(i));
        }
    }


    private int getKeyWordCount(String line){
        List<String> keyWords = Arrays.asList("class", "public", "void", "true", "else", "default", "return", "null", "break", "this", "static");

        String[] tokens = line.split("[ ()\\[\\]]");
        int count = 0;
        for (String token : tokens){
            if(keyWords.contains(token)){
                count ++;
            }
        }
        return count;
    }

    private int getIdentifierCount(String line) {
//        String[] split = line.split("[^A-Za-z0-9_]+");
//        for(String s:split){
//            System.out.println(s);
//        }
        return 0;
    }

    private int getOperatorCount(String line){
        List<String> operators = Arrays.asList(
                "+", "-", "*", "/", "%", "++", "--",
                "==", "!=", "<", ">", ">=", "<=",
                "&&", "||", "!",
                "|", "^", "~", "<<", ">>", ">>>", "<<<",
                ",", "->", ".", "::" ,
                "+=", "-=", "*=", "/=", "=", ">>>=", "|=", "&=", "%=", "<<=", ">>=", "^=" );

        String[] tokens = line.split(" |[0-9]+|[a-z]+|[A-Z]+");
        int count = 0;
        for (String token : tokens){
            if(operators.contains(token)){
                count ++;
            }
        }
        return count;
    }

    private int getNumericalValueCount(String line) {
        int count = 0;
        Pattern p = Pattern.compile("(\\d+)");
        Matcher m = p.matcher(line);

        while(m.find()) {
            count++;
        }
        return count;
    }

    private int getStringLiteralCount(String line) {
        int count = 0;
        Pattern p = Pattern.compile("\"[^\"\\\\]*(\\\\.[^\"\\\\]*)*\"");
        Matcher m = p.matcher(line);

        while(m.find()) {
            count++;
        }
        return count;
    }
}
