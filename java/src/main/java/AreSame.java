import java.util.Arrays;

/**
 * Created by zhouyanhui on 3/16/16.
 */
public class AreSame {
    public static boolean comp(int[] a, int[] b) {
        if(a==null || b == null){
            return false;
        }
        if(a.length == 0){
            return b.length == 0;
        }
        for (int i = 0; i < a.length; i++) {
            a[i] = Math.abs(a[i]);
        }
        Arrays.sort(a);
        Arrays.sort(b);
        for (int i = 0; i < a.length; i++) {
            if(b[i] != a[i]*a[i]){
                return false;
            }
        }
        return true;

    }
}
