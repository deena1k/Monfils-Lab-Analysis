# Monfil-Lab-Analysis
Contains the code for running the analysis on the tracked Rat videos (using DEEPLABCUT)
The last thing for you to do in the write-up is run the python file! You can find it in this respiratory, titled "getting_values.py". Make sure that when you download the file you place it in the same directory as the csv file that you downloaded from the video you analyzed in DEEPLABCUT. 

The program will ask you a few questions about the file that you’re entering and the conversion scales, so answer those appropriately (you don’t need to put your answer in quotation marks because the program will already do that). 


These are the questions you will be asked:

“What is the file name of the csv file you want to input? Ex: Video17.csv”. → Enter the name of the csv file of the video that you want to look at.

"How many pixels are in an inch (according to ImageJ)? Ex: 22.75 " → Please enter in the number that you got earlier from the scale. Don’t enter any spaces.

"What second do you want to start the analysis at? Ex: 25" → Enter the second that all of the rats have been put in, after the researcher’s hand has disappeared/is no longer visible in the frame. The current code assumes that all of the videos are 60 fps. 


Once you enter each of these, you should get a really large output! The structure for it is so that the first large segment of code is a dictionary that contains the total distance traveled by each rat, plus their velocity every twenty seconds. There will also be a dash line, and after that there will be another dictionary, this time saying how long each rat interacted with each other in seconds. 

If you have a question on how the code works, be sure to check the comments on the file (these are marked with #). They will explain what most of the code is doing/implementing.


