import csv
import datetime
import matplotlib.dates as mdates
import matplotlib.mlab as mlab
import os
from os.path import isfile, join
import numpy



class DataInput(object):
	def __init__(self,dataDir):
		self.dataDir = dataDir 
		try:
			self.fileListFull = [join(dataDir,f) for f in os.listdir(dataDir) if isfile(join(dataDir,f))]
			self.fileListShort = [f for f in os.listdir(dataDir) if isfile(join(dataDir,f))]
		except OSError : 
			print("Directory Listing Failed")

	def generateTimeSeriesVector(self):
		# main collection of time series is a dictionary
		# mapping ticker symbols to time series
		# each symbol-associated time series is itself a dictionary
		timeSeries = dict()

		for s in self.fileListShort:
			with open(join(self.dataDir,s),'rU') as csvfile:
				reader = csv.reader(csvfile)
				#skip over first line (column names)
				reader.next()

				tempTimeSeries = dict()
				
				for row in reader:
					#reader pops from last column to first
					closingPrice = float(row.pop())
 					#skip to date column
					for i in range(1,6):
						row.pop()
				
					temp_date = row.pop()
					date = datetime.datetime.strptime(temp_date,'%Y-%m-%d')
					tempTimeSeries[date] = closingPrice

				#parse out the ticker symbol from the filename
                                # should be <ticker_symbol>.csv
				tickerSymbol = s.split(".")[0]

				timeSeries[tickerSymbol] = tempTimeSeries


		self.timeSeries = timeSeries
		return timeSeries				


	def readTickerShares(self,sharesfile):
		#import shares per tickersymbol
		with open(sharesfile,'rU') as csvfile:
  			reader = csv.reader(csvfile)
			reader.next()

			tickerShares = dict()

			for row in reader:
				numShares = float(row.pop())
				tickerSymbol = row.pop()
				tickerShares[tickerSymbol] = numShares
		self.tickerShares=tickerShares
		return tickerShares



	def printDirectoryList(self):
		for f in self.fileListFull:
			print(f)		 
