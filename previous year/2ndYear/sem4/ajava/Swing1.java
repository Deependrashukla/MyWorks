import javax.swing.*;
import java.awt.*;
public class Swing1 {
    public static void main(String[] args) {
 
        // JFrame f = new JFrame("button ex");
        JFrame f = new JFrame("label example");
        JButton b = new JButton(new ImageIcon("/home/deependra/Pictures/Screenshots/Screenshot from 2024-01-22 16-18-58.png"));
        b.setBounds(130,100,100,100);

        JLabel l1,l2;
        l1 = new JLabel("label1");
        l2 = new JLabel("label2");
        l1.setBounds(5,0,100,100);
        l2.setBounds(5,200,100,100);
        f.add(l1);
        f.add(l2);

        JTextField t1;
        t1=new JTextField("welcome to deependra platform");
        t1.setBounds(50,10,200,30);

        JTextArea area = new JTextArea("it is area");
        area.setBounds(70,80,200,200);
        f.add(area);

        f.add(t1);
        f.add(b);
        f.setSize(400,500);
        f.setLayout(null);
        f.setVisible(true);
        f.getContentPane().setBackground(Color.BLUE);
        
    }  
}
