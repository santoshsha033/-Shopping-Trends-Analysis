
import java.util.*;
public class evenOdd {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a[] = new int[10];
		for(int i = 0; i < a.length; i++) {
			a[i] = Integer.parseInt(args[i]);
		}
		int count1 = 0, count2 = 0;
		for(int i = 0; i < a.length; i++) {
			if(a[i] % 2 == 0) {
				count1++;
			}else {
				count2++;
			}
		}
		System.out.println(count1);
		System.out.println(count2);
	}
}
