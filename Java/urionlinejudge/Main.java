import java.io.IOException;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) throws IOException {

  int N;
  Scanner input =new Scanner(System.in);
  
  N =input.nextInt();
  for (int i = 0; ((N*i) + 2) < 10000; i++) {
   System.out.print((N*i) + 2+"\n");
  }
    }

}