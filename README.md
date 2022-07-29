# Monfils-Lab-Analysis
## Overview

If you have not labeled the videos yet, please follow these steps listed here: [Write Up](https://docs.google.com/document/d/1Wt5_wa7j12gE9fzmw9T9nHWQkvUncxSEwznl5go_s2M/edit?usp=sharing).<br />

The last thing for you to do in the write-up is run the python file which calculates the average velocity, distance, and amount of interactions between each rat! You can find it in this respiratory, titled "getting_values.py". Make sure that when you download the file you place it in the same directory as the csv file that you downloaded from the video you analyzed in DEEPLABCUT. 

The program will ask you a few questions about the file that you’re entering and the conversion scales, so answer those appropriately (you don’t need to put your answer in quotation marks because the program will already do that). 

## User Inputs
These are the questions you will be asked:

1. “What is the file name of the csv file you want to input? Ex: Video17.csv”. → Enter the name of the csv file of the video that you want to look at.

2. "How many pixels are in an inch (according to ImageJ)? Ex: 22.75 " → Please enter in the number that you got earlier from the scale. Don’t enter any spaces.

3. "What second do you want to start the analysis at? Ex: 25" → Enter the second that all of the rats have been put in, after the researcher’s hand has disappeared/is no longer visible in the frame. The current code assumes that all of the videos are 60 fps. 

4. “What would you like to call the velocity and total distance file? Please include .csv at the end of the name" → Enter the name that you would like to call the file that contains all of the velocity/total distance data. An example would be “velocity.csv”. This will appear in whatever folder you’re currently located in (so wherever your getting_values.py file is located). 

5. "What would you like to call the interaction data file? Please inlcude .csv at the end of the name." → Enter the name that you would like to call the file that contains all of the interaction data. An example would be “interactions.csv”. This will appear in whatever folder you’re currently located in (so wherever your getting_values.py file is located). 

Once you enter these you should get two csv files located in the directory that getting_vales.py is in!


