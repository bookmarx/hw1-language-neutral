import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.io.*;


class JavaForm
{
    public static Map<String, String> getQueryMap(String query)
    {
        String[] params = query.split("&");
        Map<String, String> map = new HashMap<String, String>();
        for (String param : params)
        {
            String name = param.split("=")[0];
            String value = param.split("=")[1];
            map.put(name, value);
        }
        return map;
    }
    public static void main( String args[] )
    {
        System.out.println("Content-type: text/html\r\n\r\n");

        System.out.println("<!DOCTYPE html>" +
        "<html lang='en'>" +
        "<head>" +
        "<meta charset='UTF-8'>" +
        "<title>Java CGI Form</title>" +
        "</head>" +
        "<body>" +
        "<h1>Java Process Data</h1><hr />");

        Map<String, String> env = System.getenv();

        if(env.get("REQUEST_METHOD").equals("GET")){
            Map<String, String> map = getQueryMap(env.get("QUERY_STRING"));
            String username = map.get("username");
            String password = map.get("password");
            String magicnum = map.get("magicnum");
            for(int i = 0; i < Integer.parseInt(magicnum); i++){
                System.out.printf("<h1>Hello %s with a password of %s!</h1>",username, password);
            }
        } else if(env.get("REQUEST_METHOD").equals("POST")){
            // Scanner sc = new Scanner(System.in);
            // String postData = "";
            //
            // while(sc.hasNext()){
            //     postData += sc.nextLine();
            // }
            // Pattern p1 = Pattern.compile("\"username\"(.*)------",'i');
            // String m1 = p1.matcher(postData).group(1);
            //
            // Pattern p2 = Pattern.compile("\"password\"(.*)------");
            // String m2 = p2.matcher(postData).group(0);
            //
            // Pattern p3 = Pattern.compile("\"magicnum\"(.*)------");
            // String m3 = p3.matcher(postData).group(0);
            // System.out.printf("<h1>Hello %s with a password of %s!</h1>",m1);
            // for(int i = 0; i < Integer.parseInt(m3); i++){
            //     System.out.printf("<h1>Hello %s with a password of %s!</h1>",m1, m2);
            // }
        }
        System.out.println ("</body>" + "</html>");
    }
}
