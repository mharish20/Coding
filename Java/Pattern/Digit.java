package Java.Pattern;

import java.util.Scanner;

public class Digit {

	public static void main(String[] args) {
		Scanner num=new Scanner(System.in);
		int n,d;
		n=num.nextInt();
		
		while(n>0) {
			d=n%10;
			n=n/10;
			System.out.print(d+" ");
		}
	}

}
