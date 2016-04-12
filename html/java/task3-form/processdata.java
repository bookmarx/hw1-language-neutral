import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.io.*;
import java.net.URLDecoder;

class JavaForm
{
    public static Map<String, String> getQueryMap(String query) throws UnsupportedEncodingException
    {
        String[] params = query.split("&");
        Map<String, String> map = new HashMap<String, String>();
        for (String param : params)
        {
            String name = param.split("=")[0];
            String value = param.split("=")[1];
            map.put(name, URLDecoder.decode(value, "UTF-8"));
        }
        return map;
    }
    public static void main( String args[] ) throws UnsupportedEncodingException
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
            Scanner sc = new Scanner(System.in);
            String postData = "";

            while(sc.hasNext()){
                postData += sc.nextLine();
            }

            Map<String, String> map = getQueryMap(postData);
            String username = map.get("username");
            String password = map.get("password");
            String magicnum = map.get("magicnum");
            for(int i = 0; i < Integer.parseInt(magicnum); i++){
                System.out.printf("<h1>Hello %s with a password of %s!</h1>",username, password);
            }
        }
        System.out.println ("</body>" + "</html>");
    }
}
