import java.util.Scanner;
public class Operators
{
	public static void main(String[] args)
	{
		Scanner sc = new Scanner(System.in);
		System.out.print("Enter number:");
		int a = sc.nextInt();
		System.out.print("Enter number:");
		int b = sc.nextInt();
		int ans;
		
		System.out.println("a is "+a +" and b is "+b);
		
		ans = a + b;
		System.out.println("a+b is "+ans);
		
		ans = a - b;
		System.out.println("a-b is "+ans);
		
		ans = a * b;
		System.out.println("a*b is "+ans);
		
		ans = a / b;
		System.out.println("a/b is "+ans);
		
		ans = a % b;
		System.out.println("a%b is "+ans);
		
		ans = ++a;
		System.out.println("a after incrementing by 1 is "+ans);
		
		ans = --a;
		System.out.println("a after decrementing by 1 is "+ans);
	
		
	}
}
