package com.pp.azteroids.frame;

import javax.swing.JFrame;

public class Frame {
	
	
	public Frame(String frameTitle, int frameWidth,int frameHeight,boolean frameVisible,boolean frameResizeable) {  //Main Frame Constructor
		JFrame frame = new JFrame();
		frame.add(new Background());
		frame.setTitle(frameTitle);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); // Very important, ensures the athe process terminates when the panel is closed
		frame.setSize(frameWidth, frameHeight);
		frame.setResizable(frameResizeable);
		frame.setLocationRelativeTo(null); // allows the window to start up in the center of the screen instead of left corner
		frame.setVisible(frameVisible);
		
	}

}
