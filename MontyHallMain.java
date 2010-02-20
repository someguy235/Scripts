//Demonstrate the probabilities involved in the Monty Hall Problem

import java.util.Random;

public class MontyHallMain {

	public static void main(String[] args) {
		Random gen = new Random();
		int sampleSize = 10000;
		int switchWins = 0;
		int stickWins = 0;
		int[] prize = new int[sampleSize];
		int[] player = new int[sampleSize];
		int[] monty = new int[sampleSize];
		
		//choose the prize door
		for (int i=0; i<sampleSize; i++){
			prize[i] = gen.nextInt(3);
		}
		//player chooses their door
		for (int i=0; i<sampleSize; i++){
			player[i] = gen.nextInt(3);
		}
		//monty reveals a door which is not the prize
		//and not alrady chosen by the player
		for (int i=0; i<sampleSize; i++){
			monty[i] = gen.nextInt(3);
			while ((monty[i] == player[i])||(monty[i] == prize[i])){
				monty[i] = gen.nextInt(3);
			}
		}
		//count number of wins for player sticking with their
		//door or switching
		for (int i=0; i<sampleSize; i++){
			if (player[i] == prize[i])
				stickWins++;
			else
				switchWins++;
		}
		System.out.println("Stick: " + stickWins + "/" + sampleSize);
		System.out.println("Switch: " + switchWins + "/" + sampleSize);
	}
}
