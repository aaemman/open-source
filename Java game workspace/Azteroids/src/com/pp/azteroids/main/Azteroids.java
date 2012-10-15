package com.pp.azteroids.main;

import com.pp.azteroids.frame.Frame;

public class Azteroids {
	
	static String frameTitle = "Azteroids - Alpha 0.001";
	static int frameWidth = 1080;
	static int frameHeight = 900;
	static boolean frameVisible = true;
	static boolean frameResizeable = false;
	
	public static void main (String[] args){
		
		new Frame(frameTitle, frameWidth, frameHeight, frameVisible, frameResizeable); // initializes a new window
	}
	
	public static int getScreenWidth(){
		return frameWidth;
	}
	
	public static int getScreenHeight(){
		return frameHeight;
	}

}
