# ETF_Return_Spread

Python code which fits exponential curves to time series price data of several ETFs. The the growth rate of the fitted exponential curve for a particular ETF is compared to that of the exponential fit for the SPY (S&P 500) ETF to determine the return spread for that particular ETF.

See resulting output at http://www.stuarttruax.com/?p=340
 
## Getting Started

### Prerequisites

A. Python 2.7 or later

B. The python libraries:

*DataInput

*TimeSeriesFit

*csv

*datetime

*matplotlib.pyplot

*matplotlib.dates

*matplotlib.backends.backend_pdf 

*numpy



## Running the code

From the command line, use:

*python returnSpread.py*

An HTML-formatted table will be output to the command line will be output to standard I/O. A pdf file with the fitted exponential curves and time-series data will be output to the working directory. 

ETF data is derived from .csv files in the *data* directory. 



## Authors

* **Stuart Truax** - *Initial work* - (https://github.com/StuartTruax)

## License





