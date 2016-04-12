import junit.framework.TestCase;
import org.junit.Test;

public class LineTest extends TestCase {

    @Test
    public void test1() {
        String[] names = new String[] { "Sheldon", "Leonard", "Penny", "Rajesh", "Howard" };
        int n = 1;
        assertEquals("Sheldon", new Line().WhoIsNext(names, n));
    }
    @Test
    public void test2() {
        String[] names = new String[] { "Sheldon", "Leonard", "Penny", "Rajesh", "Howard" };
        int n = 6;
        assertEquals("Sheldon", new Line().WhoIsNext(names, n));
    }
    @Test
    public void test3() {
        String[] names = new String[] { "Sheldon", "Leonard", "Penny", "Rajesh", "Howard" };
        int n = 1802;
        assertEquals("Penny", new Line().WhoIsNext(names, n));
    }
    @Test
    public void test4() {
        String[] names = new String[] { "Sheldon", "Leonard", "Penny", "Rajesh", "Howard" };
        int n =  2;
        assertEquals("Leonard", new Line().WhoIsNext(names, n));
    }
    @Test
    public void test6() {
        String[] names = new String[] { "Sheldon", "Leonard", "Penny", "Rajesh", "Howard" };
        int n = 10;
        assertEquals("Penny", new Line().WhoIsNext(names, n));
    }
    @Test
    public void test7() {
        String[] names = new String[] { "Sheldon", "Leonard", "Penny", "Rajesh", "Howard" };
        int n = 534;
        assertEquals("Rajesh", new Line().WhoIsNext(names, n));
    }
    @Test
    public void test8() {
        String[] names = new String[] { "Sheldon", "Leonard", "Penny", "Rajesh", "Howard" };
        int n = 5033;
        assertEquals("Howard", new Line().WhoIsNext(names, n));
    }
    @Test
    public void test9() {
        String[] names = new String[] { "Sheldon", "Leonard", "Penny", "Rajesh", "Howard" };
        int n = 10010;
        assertEquals("Howard", new Line().WhoIsNext(names, n));
    }
    @Test
    public void test10() {
        String[] names = new String[] { "Sheldon", "Leonard", "Penny", "Rajesh", "Howard" };
        int n = 63;
        assertEquals("Rajesh", new Line().WhoIsNext(names, n));
    }
    @Test
    public void test11() {
        String[] names = new String[] { "Sheldon", "Leonard", "Penny", "Rajesh", "Howard" };
        int n = 841;
        assertEquals("Leonard", new Line().WhoIsNext(names, n));
    }
    @Test
    public void test12() {
        String[] names = new String[] { "Sheldon", "Leonard", "Penny", "Rajesh", "Howard" };
        int n = 3667;
        assertEquals("Penny", new Line().WhoIsNext(names, n));
    }
    @Test
    public void test13() {
        String[] names = new String[] { "Sheldon", "Leonard", "Penny", "Rajesh", "Howard" };
        int n = 38614;
        assertEquals("Howard", new Line().WhoIsNext(names, n));
    }
    @Test
    public void test14() {
        String[] names = new String[] { "Sheldon", "Leonard", "Penny", "Rajesh", "Howard" };
        int n = 1745;
        assertEquals("Leonard", new Line().WhoIsNext(names, n));
    }
    @Test
    public void test15() {
        String[] names = new String[] { "Sheldon", "Leonard", "Penny", "Rajesh", "Howard" };
        int n = 8302;
        assertEquals("Rajesh", new Line().WhoIsNext(names, n));
    }
    @Test
    public void test16() {
        String[] names = new String[] { "Sheldon", "Leonard", "Penny", "Rajesh", "Howard" };
        int n = 12079;
        assertEquals("Sheldon", new Line().WhoIsNext(names, n));
    }
    @Test
    public void test17() {
        String[] names = new String[] { "Sheldon", "Leonard", "Penny", "Rajesh", "Howard" };
        int n = 28643950;
        assertEquals("Leonard", new Line().WhoIsNext(names, n));
    }
    @Test
    public void test18() {
        String[] names = new String[] { "Sheldon", "Leonard", "Penny", "Rajesh", "Howard" };
        int n = 159222638;
        assertEquals("Howard", new Line().WhoIsNext(names, n));
    }
    @Test
    public void test19() {
        String[] names = new String[] { "Sheldon", "Leonard", "Penny", "Rajesh", "Howard" };
        int n = 121580142;
        assertEquals("Penny", new Line().WhoIsNext(names, n));
    }
    @Test
    public void test20() {
        String[] names = new String[] { "Sheldon", "Leonard", "Penny", "Rajesh", "Howard" };
        int n = 1000000000;
        assertEquals("Penny", new Line().WhoIsNext(names, n));
    }
}