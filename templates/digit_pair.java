import java.util.ArrayList;
import java.util.Scanner;
import java.util.Vector;

public class DigitProblem {

	
	
	
	public static void main(String[] args) {
		
		Scanner s = new Scanner(System.in);
		int n = s.nextInt();
		int i,j;
		int a[] = new int[n];
		int bit_s[][] = new int[n][2];
		for( i=0;i<n;i++) {
			a[i] = s.nextInt();
		}
		
		for(i=0;i<n;i++) {
			int x = a[i];
			ArrayList <Integer> arr = null;
			arr.add(x%10);
			x/=10;
		}
        
		
		
		
		
		
		
		
	}
	
	
	
	
	
}
