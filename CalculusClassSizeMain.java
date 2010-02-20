//An old CarTalk Puzzler
//Smallest number of classes with the same number of students in each

public class CalculusClassSizeMain {

	public static void main(String args[]){
		//System.out.println("test");
		int students = 529 ;
		for (int i=1; i<265; i++){
			//long remainder = students%i;
			//System.out.println(i + ", " + remainder);
			if (students%i == 0){
				System.out.println(i);
			}
		}
	}
}
