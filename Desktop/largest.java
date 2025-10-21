
public class largest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int a = Integer.parseInt(args[0]);
		int b = Integer.parseInt(args[1]);
		int c = Integer.parseInt(args[2]);
		if(a > b) {
			if(a > c) {
				System.out.println(a);
			}else {
				System.out.println(c);
			}
		}else {
			if(b > c) {
				System.out.println(b);
			}else {
				System.out.println(c);
			}
		}
		
	}

}