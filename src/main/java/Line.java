
/**
 * Created by zhouyanhui on 3/16/16.
 */
public class Line {
    public static String WhoIsNext(String[] names, int n)
    {
        // Your code is here...
        final int personNum = names.length;
        int loop = 1;
        int curPersonQueueNum = personNum * loop;
        while (n > curPersonQueueNum){
            n -= curPersonQueueNum;
            loop*=2;
            curPersonQueueNum = personNum * loop;
        }
        n = (int) Math.ceil((double)n / loop);
        return names[n - 1];
    }

    public static void main(String[] args) {
            String[] names = new String[]  {"Sheldon", "Leonard", "Penny", "Rajesh", "Howard" };
            int n = 5033;
        System.out.println(new Line().WhoIsNext(names, n));
//            assertEquals("Penny", );

    }


}
