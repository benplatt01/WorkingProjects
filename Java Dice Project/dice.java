import java.util.Scanner;

public class dice {
    public static void main(String[] args) {
        int dice1; // variable 1
        int dice2; // variable 2
        int sum; // variable 3

        Scanner userInput = new Scanner(System.in); // Opens a new scanner
        System.out.println("Would you like to roll? \n1 - Yes \n2 - No"); // Asks the user to select an answer

        String userAns = userInput.next(); // gets the users answer

        if (userAns.equals("1")) { // if statement 1
            dice1 = (int) (Math.random() * 6 + 1); // Dice 1 random number gen between 6-1
            dice2 = (int) (Math.random() * 6 + 1); // Dice 1 random number gen between 6-1
            sum = dice1 + dice2; // works out overall dice roll

            System.out.println("You rolled " + sum); // outputs to tell the user what they rolled
        }

        else if (userAns.equals("2")) { // if statement 2
            System.out.println("Thank you for playing!"); // output to thank user
            System.exit(0); // ends program
        }
    }
}