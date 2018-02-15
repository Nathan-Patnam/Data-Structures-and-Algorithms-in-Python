import java.util.Random;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;;


//to run javac randomNumber.java
//java randomNumber
public class randomNumber{

    public static void main(String [] args)
	{
        randomNumber rn = new randomNumber();
        Map<Integer, Integer> probabilityResults = new HashMap<Integer, Integer>();
        for(int i = 0; i < 1000000; i++){
            int randomNumber = rn.myRand13();
            if (probabilityResults.get(randomNumber) != null) {
                //increment count if random number already present in dict
                probabilityResults.put(randomNumber, probabilityResults.get(randomNumber) + 1);

            } 
            else {
                probabilityResults.put(randomNumber, 0);
            }
        }
        System.out.println(Arrays.toString(probabilityResults.entrySet().toArray()));
    
		
    }
    
    
    
    /**
     * here was the general idea for this. There is a matrix with 121 possible spots (11  * 11).
     * I filled up the matrix with 9 copies of each number from 1 - 13 yielding 117 spots taken
     * (13 * 9). The other 4 spots I put in 0's as placeholders. Then the way the algorithms works
     * is that i randomly pick a number from 1-11 using rand11() for both the column and row. If the number
     * in the cel in the matrix is a 0, then I will repick until I find a number that's not 0. The chance of this happening is 4/121. The only downside to this approach is there the possiblity
     * of being stuck in the infinite loop, but the chance of that happening is (4/121) ^ n where n is some large number.
     * Additionally, with this implementation there is a 4/121 chance that the rand 11 function will be called
     * 4 times (two times to find the column and 2 times to find the row) and 117/121 chance to be called just twice. I have another implementation
     * that is commented out at the bottom of this file. This method myRand13() is better than the other implementation mainly for how the data is preserved
     * in myRand13() when I hit a 0 I find another random cell in the matrix, however in the other implementation if I hit a number
     * between 117-121, I just try to find another number again without keeping track I failed to hit a number.
     * 
     */
    public int myRand13()
    {
        int[][] vals = {
            { 1 , 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 },
            { 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9},
            { 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7},
            { 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5 },
            { 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3 },
            {4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1},
            {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12},
            {13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10},
            {11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8},
            {9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6},
            {7, 8, 9, 10, 11, 12, 13, 0, 0, 0, 0}
        };
    
        int result = 0;
        while (result == 0)
        {
            int i = rand11();
            int j = rand11();
            result = vals[i-1][j-1];
        }
        return result;
    }
    public int rand11(){
        return (int )(Math.random() * 10 + 1);
    }
}




/** Implementation 2
 * 
 int i;
 do
 {
  i = 11 * (rand11() - 1) + rand11();  // i is now uniformly random between 1 and 121
} while(i > 117);
// i is now uniformly random between 1 and 117
return i % 13 + 1;  // result is now uniformly random between 1 and 13
 * 
 * 
 */
