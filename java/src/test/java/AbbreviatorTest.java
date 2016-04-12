import junit.framework.TestCase;
import org.junit.Test;

public class AbbreviatorTest extends TestCase {
    private Abbreviator abbr = new Abbreviator();

    @Test
    public void testInternationalization() {
        assertEquals("i18n", abbr.abbreviate("internationalization"));
    }

    @Test
    public void testInternationalization2() {
        assertEquals("i18n-w3d", abbr.abbreviate("internationalization-world"));
    }

    @Test
    public void testInternationalization3() {
        assertEquals("hi-w3d", abbr.abbreviate("hi-world"));
    }

    @Test
    public void test4(){
        assertEquals("mat-on, m8c: d3y-d4e-b6d'cat'b5n: b5n; cat",
                abbr.abbreviate("mat-on, monolithic: doggy-double-barreled'cat'balloon: balloon; cat"));
    }
}