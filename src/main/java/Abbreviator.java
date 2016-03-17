/**
 * Created by zhouyanhui on 3/16/16.
 */
public class Abbreviator {
    private boolean isAlphabeta(char c){
        return (c >= 'a' && c <= 'z') || (c >= 'A' && c<= 'Z');
    }

    public String abbreviate(String string) {
        String[] split = string.split("\\W");
        for (String s : split) {
            System.out.printf("%s\t", s);
        }
        int len = string.length();
        StringBuilder sb = new StringBuilder();
        boolean isWord = false;
        int start = -1;
        int end = -2;
        for (int i = 0; i < len; i++) {
            char c = string.charAt(i);
            if(isAlphabeta(c)){
                if(!isWord){
                    start = i;
                    end = i;
                    isWord =true;
                }else{
                    end++;
                }
            }
            else{
                if(isWord){
                    appendWord(sb, start, end, string);
                    isWord = false;
                    start = -1;
                    end = -2;
                }
                sb.append(c);
            }
        }
        appendWord(sb, start, end, string);
        return sb.toString();
    }

    private void appendWord(StringBuilder sb, int start, int end, String string) {
        int count = end - start + 1;
        if(count >= 4){
            sb.append(string.charAt(start));
            sb.append(count - 2);
            sb.append(string.charAt(end));
        }else if(count >= 0){
            sb.append(string.substring(start, end + 1));
        }
    }

}


