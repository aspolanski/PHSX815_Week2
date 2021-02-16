#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import math
import numpy as np
import matplotlib.pyplot as plt

# import our Random class from python/Random.py file
sys.path.append(".")
from MySort import MySort

# main function for our CookieAnalysis Python code
if __name__ == "__main__":
   
    haveInput = False

    for i in range(1,len(sys.argv)):
        if sys.argv[i] == '-h' or sys.argv[i] == '--help':
            continue

        InputFile = sys.argv[i]
        haveInput = True
    
    if '-h' in sys.argv or '--help' in sys.argv or not haveInput:
        print ("Usage: %s [options] [input file]" % sys.argv[0])
        print ("  options:")
        print ("   --help(-h)          print options")
        print
        sys.exit(1)
    
    Nmeas = 1
    times = []
    times_avg = []

    need_rate = True
    
    with open(InputFile) as ifile:
        for line in ifile:
            if need_rate:
                need_rate = False
                rate = float(line)
                continue
            
            lineVals = line.split()
            Nmeas = len(lineVals)
            t_avg = 0
            for v in lineVals:
                t_avg += float(v)
                times.append(float(v))

            t_avg /= Nmeas
            times_avg.append(t_avg)

    Sorter = MySort()

    times = Sorter.DefaultSort(times)
    times_avg = Sorter.DefaultSort(times_avg)
    # try some other methods! see how long they take
    # times_avg = Sorter.BubbleSort(times_avg)
    # times_avg = Sorter.InsertionSort(times_avg)
    # times_avg = Sorter.QuickSort(times_avg)

    # ADD YOUR CODE TO PLOT times AND times_avg HERE

#    print("hello",times, times_avg)
    

    #Calculate the weights such that my histogram is plotting probability on the y axis
    weights1 = np.ones_like(times) / len(times)
    weights2 = np.ones_like(times_avg) / len(times_avg)

    #Calculate the quantiles I need (68-95-99.7 rule)

    q68 = np.quantile(times_avg, [0.32,0.68])
    q95 = np.quantile(times_avg, [0.05,0.95])
    q997 = np.quantile(times_avg, [0.003,0.997])


    fig1, ax1 = plt.subplots(figsize=(11,8.5))
    ax1.hist(times,weights=weights1,bins=50,histtype='stepfilled',facecolor='#809fff',edgecolor='black')
    ax1.set_yscale('log')
    ax1.set_ylim(0.0,1.0)
    ax1.set_xlabel("Time Between Missing Cookies [days]", fontsize=22)
    ax1.set_ylabel("Probability",fontsize=22)
    ax1.tick_params(axis='both', which='both', direction = 'in',labelsize=20)
    ax1.tick_params(axis='both', which='major', direction = 'in',labelsize=20,length=7,width=2)
    ax1.tick_params(axis='both', which='minor', direction = 'in',labelsize=20,length=4,width=2)
    
    fig1.savefig('./times_hist.pdf', format='pdf', orientation='landscape')
    
    fig2, ax2 = plt.subplots(figsize=(11,8.5))

    ax2.hist(times_avg, weights=weights2,bins=50,histtype='stepfilled',facecolor='#809fff',edgecolor='black')
    ax2.vlines(q68,ymin=0.0,ymax=1.0,linestyles='dashed',linewidths=2,color='black')
    ax2.vlines(q95,ymin=0.0,ymax=1.0,linestyles='dashed',linewidths=2,color='black')
    ax2.vlines(q997,ymin=0.0,ymax=1.0,linestyles='dashed',linewidths=2,color='black')
    ax2.vlines(np.median(times_avg),ymin=0.0,ymax=1.0,linewidths=2,color='black')
    ax2.set_yscale('log')
    ax2.set_ylim(0.0,1.0)
    ax2.set_xlabel("Avg Time Between Missing Cookies [days]", fontsize=22)
    ax2.set_ylabel("Probability", fontsize=22)
    ax2.tick_params(axis='both', which='major', direction = 'in',labelsize=20,length=7,width=2)
    ax2.tick_params(axis='both', which='minor', direction = 'in',labelsize=20,length=4,width=2)
    
    fig2.savefig('./times_avg_hist.pdf', format='pdf', orientation='landscape')
    

