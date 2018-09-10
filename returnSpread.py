import DataInput
import TimeSeriesFit
import csv
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.backends.backend_pdf import PdfPages
import numpy


################################################################
#Retrieve all historical price time series in the specified directory
test = DataInput.DataInput("data")

timeSeries = test.generateTimeSeriesVector()

t0_date ="1995-03-01"
t0 = datetime.datetime.strptime(t0_date,'%Y-%m-%d')
############################################################
#with the above specified starting time
# for each price time series, estimate the continuous compounding
# rate of return under the model S = S0*exp(r(t-t0))
rates = dict() 
fits = dict();
for i in timeSeries:
	rate, fit = TimeSeriesFit.findGrowthRate(timeSeries[i],t0)
	rates[i] = rate
	fits [i] = fit 

#print rates

###########################################################
##### Calculate return spread relative to SPY, output formated to HTML table
r_spy = rates['SPY']



print '<h3> Starting date for Analysis (t0): %s </h3>' %t0_date

print '<h3> Fitted CAGR of the SPY ETF: %f%% </h3>' % (r_spy*100)

print 'Selected ETFs by Spreads above CAGR of SPY'

print '<table style="width:100%">'

print '<tr>'
print '<th> ETF Symbol </th>'
print '<th> CAGR </th>'
print '<th> Spread over SPY CAGR </th>'

spreads = dict()
for i in rates:
	spreads[i] = rates[i]-r_spy




for i in spreads:
    print '<tr>'
    print '<td>%s</td>' %i
    print '<td>%f%%</td>' %(rates[i]*100)
    print '<td>%f%%</td>' %(spreads[i]*100)
    print '</tr>'

print '</table>'



############################################################
################Generate Plots
# Create the PdfPages object to which we will save the pages:
# The with statement makes sure that the PdfPages object is closed properly at
# the end of the block, even if an Exception occurs.
with PdfPages('output.pdf') as pdf:
    for i in timeSeries:
        time_axis = sorted(timeSeries[i].keys())
        #	print(time_axis)
        tickerTimeSeries = []
        for j in time_axis:
            tickerTimeSeries.append(timeSeries[i][j])

        time_axis_fit = sorted(fits[i].keys())
        fitTimeSeries = []
        for j in time_axis_fit:
            fitTimeSeries.append(fits[i][j])
	
        #print(tickerTimeSeries)
        #print(len(tickerTimeSeries))
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
        plt.plot(time_axis,tickerTimeSeries, 'r^-',time_axis_fit,fitTimeSeries,'b^-')
        plt.ylabel('Closing Price')
        plt.xlabel('Time')
        plt.title('Symbol: %s, CAGR: %f%%, Spread: %f%%' %(i,rates[i]*100 ,spreads[i]*100))
        #save plot to pdf
        pdf.savefig()
        plt.close()

    d = pdf.infodict()
    d['Title'] = 'ETF Time Series and Exponential Fits '
    d['Author'] = u'Stuart Truax'
    d['Subject'] = 'ETF Time Series and Exponential Fits'
    d['Keywords'] = 'PdfPages multipage keywords author title subject'
    d['CreationDate'] = datetime.datetime(2017, 7, 15)
    d['ModDate'] = datetime.datetime.today()


