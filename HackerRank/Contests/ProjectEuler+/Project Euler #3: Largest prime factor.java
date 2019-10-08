import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

	static Boolean isPrime(long number){
		if(number == 1){
			return false;
		}

		if(number == 2){
			return true;
		}

		if (number%2 == 0){
			return false;
		}

		for(long i=3L; i*i<=number; i+=2){
			if(number%i==0){
				return false;
			}
		}

		return true;
	}

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int t = in.nextInt();
		for(int a0 = 0; a0 < t; a0++){
			long n = in.nextLong();


			for (long i = (long) Math.ceil(Math.sqrt(n)); i >= 1 ; i--) {
				if (n%i == 0){
					long a = i;
					long b = n/i;

					if(isPrime(a) && isPrime(b)){
						if(a>b){
							System.out.println(a);
							break;
						}else{
							System.out.println(b);
							break;
						}
					}else if(isPrime(a)){
						System.out.println(a);
						break;
					}else if(isPrime(b)){
						System.out.println(b);
						break;
					}
				}
			}


		}
	}
}
