import datetime
import matplotlib.pyplot as plt
#import matplotlib.dates as mdates
import numpy
from scipy.optimize import curve_fit



def findGrowthRate(timeSeries,t0):

	#extract time series subset from starting timei
	subTimeSeries = dict()
	for i in timeSeries:
		if(i>= t0):
			subTimeSeries[i-t0] = timeSeries[i]

	#find log of time series
	#index the time series 
	annualizedTimeSeries = dict()
	normalizationFactor =subTimeSeries[sorted(subTimeSeries.keys())[0]]
	for i in subTimeSeries:
		annualizedTimeSeries[i.days/(365.0)] = subTimeSeries[i]/normalizationFactor


	#reverse the vector in terms of time
	#print annualizedTimeSeries.keys()[0]
	#do fit
	t = annualizedTimeSeries.keys()
#	print t
	try:
		popt,pcov = curve_fit(expGrowth,annualizedTimeSeries.keys(),annualizedTimeSeries.values())
	except RuntimeError:
		return 0, dict() 

#	print popt
#	print pcov
	fit = dict()
	for i in t:
		fit[i] = normalizationFactor*expGrowth(i,popt[0],popt[1])
#	print len(t)
#	print len(fit)
#        plt.plot(fit.keys(),fit.values())
#        plt.show()


	fitToRet= dict()
	j=0
	for i in timeSeries:
		if(i >= t0):
			fitToRet[i] = fit[(i-t0).days/365.0]
			j=j+1 

#	print fitToRet	
	return popt[1],fitToRet



def expGrowth(t,A,B):
	return A*numpy.exp(B*t);	
