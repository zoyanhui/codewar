import java.util.function.Function;
import java.util.regex.Matcher;
import java.util.regex.Pattern;


/**
 * Created by zhouyanhui on 3/16/16.
 */
public class Opstrings1 {
    public static String rot(String strng) {
        // your code
        StringBuilder sb = new StringBuilder();
        char[] chars = strng.toCharArray();
        for (int i = chars.length-1; i >=0 ; i--) {
            sb.append(chars[i]);
        }
        return sb.toString();
    }

    public static String selfieAndRot(String strng) {
        // your code
        StringBuffer sb = new StringBuffer();
        Pattern pattern = Pattern.compile("\\w+");
        Matcher matcher = pattern.matcher(strng);
        while (matcher.find()){
            String replacement= matcher.group();
            int dotcount = replacement.length();
            for (int i = 0; i < dotcount; i++) {
                replacement += ".";
            }
            matcher.appendReplacement(sb, replacement);
        }
        matcher.appendTail(sb);
        String self = sb.toString();
        return self + "\n" + rot(self);
    }

    public static String oper(Function<String,String> operator, String s) {
        // your code and complete ... before operator
        return operator.apply(s);
    }
}
