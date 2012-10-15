package com.pp.azteroids.frame;

import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Image;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;

import javax.swing.ImageIcon;
import javax.swing.JPanel;
import javax.swing.Timer;

import com.pp.azteroids.main.Azteroids;
import com.pp.azteroids.player.Player;

public class Background extends JPanel implements ActionListener {

	Player p;
	Image img;
	Timer time;
	
	public Background(){
		p = new Player();
		addKeyListener(new AL());
		setFocusable(true);
		ImageIcon i = new ImageIcon();
		img = i.getImage();
		
		time = new Timer(5, this);
		time.start();
		
				
		
	}
	
	public void checkBounds(){
		if (p.getX() > Azteroids.getScreenWidth()){
			p.setX(0);
		}
		
		if (p.getX() < 0){
			p.setX(Azteroids.getScreenWidth());
		}
		
		if (p.getY() > (Azteroids.getScreenHeight())){
			p.setY(0);
		}
		
		if (p.getY() < 0){
			p.setY(Azteroids.getScreenWidth());
		}
	}

	@Override
	public void actionPerformed(ActionEvent arg0) {
		// TODO Auto-generated method stub
		p.move();
		
		checkBounds();
		repaint();
	}
	
	public void paint(Graphics g){
		super.paint(g);
		Graphics2D g2d = (Graphics2D) g;
		
		g2d.drawImage(img, 0, 0, null);
		g2d.drawImage(p.getPlayerImage(), p.getX(),p.getY(),null);
	}
	
	
	private class AL extends KeyAdapter{
	
		public void KeyReleased(KeyEvent e){
			p.keyReleased(e);
		}
		
		public void keyPressed(KeyEvent e){
			p.keyPressed(e);
		}
	}
}
