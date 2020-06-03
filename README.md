# dragraceAnalysis
First collect the data at the dragrace and save it as 3 component MSEED data files.

##### cleanData.ipynb
Clean the Data. Options: FALL 2019, SPRING 2019, Edit the scripts for your data.
This will retrieve the data from the listed times in a text file and save them into a local directory.

##### rotateData.ipynb
Rotate and Remove gravity from data.  Options: FALL 2019, SPRING 2019
This script will remove gravity from the z component.  The files are loaded from the same text file as in cleanData.ipynb.  Then they are rotated using the strike and dip measurements from the track.  Then gravity is removed from the vertical z component. The new data is saved in a new 'Corrected' directory.

##### plotWebsite.ipynb
To view the MSEED data files, use Obpsy website tool.  Options: ALL DATA saved locally
Load a station component to zoom in, apply filters, and plot the DFT of your data.  This is helpful to view the data after the rotation and gravity removal has been applied to check the data. 

##### peakACC.ipynb
Options: FALL 2019, SPRING 2019
Read in selected times from 'timestamp_Sp_ALL.txt' and produce a CSV file with this information in this order:
maxVmag , gMaxVmag , xVal , yVal , zVal , xVal_g , yVal_g , zVal_g , maxVmagTime , meanVmag , gMeanVmag , sta , springSta.index(sta) , line 

maxVmag = maximum vector magnitude
gMaxVmag = maxVmag in g's
xVal = x component of maximum vector magnitude
xVal_g = x com,ponent of maximum vector magnitude in g's
maxVmagTime = the time of the maximum vector magnitude recorded by device (GMT)
meanVmag = average vector magnitude from the entire time window
gMeanVmag = meanVmag in g's
sta = station (ie. 'FL')
springSta.index(sta) = an indexing system that gives a numeric value to the station code 
line = time stamp associated with the data

Be sure if you use this script to change the file paths of opening and saving files.
File out 'fa_vmag.csv' (FALL) 'sp_vmag.csv' (SPRING)

##### associateRaceInfoFall.ipynbT
##### associateRaceInfoSpring.ipynb
These scripts produce a JSON object that has a depth going in order of:
Category > Round > Heat > information in CSV file (fa_vmag/sp_vmag.csv)
ex. 
  "Funny Car": {
    "Q2": {
      "Heat 1": [
        [
          "124.2750329",
          "0.030340584",
          "37.82483507",
          "9",
          "-118.0362895",
          "0.009234579",
          "0.002197266",
          "-0.028817453",
          "2019-10-11T23:59:55.820800Z",
          "105.5302581",
          "0.025764223",
          "FL",
          "0",
          "2019-10-12T00:00:01Z",
          "Funny Car",
          "Q2",
          "Heat 1",
          "Friday"
        ],

Then using this JSON object, the script produces plots all heats of each station's peak acc values, peak magnitude for a given category & round.  To find these figures see 'additional figures' in the thesis.  


##### Selection of First Arrivals
dragraceAnalysis-master/fallClean/FirstArrivals/Fall_first_arrivals.xlsx
Each race was loaded into the website and zoomed in to record the first arrival of motion.  The above excel file was populated with these times and quick figures were drawn up.  This excel file helped to create the files that show the speed in kph or mph or m/s of the seismic wave and to create the lines in the record section. 

##### recordSectionFA.ipynb
##### recordSectionSP.ipynb
These scripts produce a record section of a selected race from the fall (FA) or spring (SP).  Change the file path to load the data from the chosen race and produce a record section. 
Function gData : create an obspy trace that is in g's be sure to change the 'stats' at the end if they are different than the given.

Function mkTime: create a domain of time for the record section to be plotted against.

Function posStream : Applies a given position value to where the record is plotted.  Example: station FL60 is plotted 60 units away from station FL. NOTE: value 250 on In[336] line 10 is the scale factor for the record. 250 was selected through trial and error.

The best fit line was calculated from the Selection of First Arrivals in excel and hard coded into the script (sorry)









