import javax.swing.*;

class Cigratte{

	int Scissors = 8;
	int Gold = 10;
	int MiniGold = 6;
	int Kings = 17;
	int EssayLights = 10;
	int EssayLightsBox = 110;
	int bigWills = 11;
	int mediumWills = 8;
	int miniWills = 5;
	int totalPrice;

	//public int totalAmount(int amount)

	public static void main(String[] args){
		System.out.println("This is going to be my project");
		JFrame f = new JFrame(); //Created a frame object named 'f'
		JButton b = new JButton("click"); //Created a button object named 'b'
		b.setBounds(200,0,100,50);
		f.add(b);
		
		f.setSize(500,700);
		f.setLayout(null);
		f.setVisible(true);
	}
}
