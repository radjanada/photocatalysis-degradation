# photocatalysis/catalytic-degradation
photocatalysis/catalytic or any type of  degradation in a period of time is a python code to help lab experiment data visualization

photocatalysisv2 is  a python code where:
the input is: time and absorbance values (from the UV-Vis spectrophotometer) , 
the output is: a figure of just ONE simple line plot.
on the Y-axis , Ln(A_t/A0) is plotted, where A_t= absorbance at a time t, A_0 = initial absorbance
on the X-axis is the time in minutes
the slope is the rate constant K, calculated from the reaction of 1st order, unit=min-1
the data that have been plotted is printed on the console

v2 capable of  plotting multiple plots ,
the input is: plot name, time values , time unit, color prefrences, plot number,absorbance values
output is : plot with multiple plots if wanted+table of data calculated+the results(Regression, equation and slope)

#*REQUIREMENTS*:
python ofc, then env,matplotlib, numpy,scipy

follow this (I use linux with python3.9)

python3.9 -m venv work3.9

source work3.9/bin/activate

pip install numpy scipy matplotlib

sudo apt-get install python3-tk (to show the plots, or it wouldn't)

#RUN
download the python code, got to its path the:

python photocatalysisv2.py

enter your inputs 

TaDa!! a beautiful plot and the data needed~
