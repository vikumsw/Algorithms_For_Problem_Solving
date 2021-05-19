/*
Given a list of non-negative integers nums, arrange them such that they form the largest number.
Note: The result may be very large, so you need to return a string instead of an integer.
1 <= nums.length <= 100.
0 <= nums[i] <= 109.
*/

class numberComparator implements Comparator<Integer> 
{
    @Override
    public int compare(Integer a, Integer b)
    {
        if (a==b)
            return 0;

         String str_a = a.toString();
         String str_b = b.toString();

         Long l_1 = Long.parseLong(str_a + str_b);
         Long l_2 = Long.parseLong(str_b + str_a);

         if(l_1-l_2>0)
            return -1;

        return 1;
    }
}

public class Solution {
    public String largestNumber(int[] nums) {
        ArrayList<Integer> Numbers = new ArrayList<Integer>();
        
        for(int a : nums){
            Numbers.add(a);
        }
        
        Collections.sort(Numbers,new numberComparator());
        
        String largest="";
        for(Integer i : Numbers){
           largest +=  i.toString();
        }
        
        System.out.println(Numbers);
        
        if (largest.charAt(0) == '0')
            return "0";
        
        return largest;
    }
    
}
