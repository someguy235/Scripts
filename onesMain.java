//Determine how many ones are in all numbers up to a given limit 

public class onesMain {
	public static void main(String[] Args){
		int start = 0;
		int finish = 999999;
		int ones = 0;
		String num = "";
		for (int i=start; i<=finish; i++){
			Integer newInt = new Integer(i);
			num = newInt.toString();
			for (int j=0; j<num.length(); j++){
				if (num.charAt(j) == '1'){
					ones++;
				}
			}
		}
		System.out.println(ones);
	}
}

/*
9 (1)
99 (20):
999 (300):
9999 (4000):
99,999 (50,000)
999,999 (600,000)
*/
