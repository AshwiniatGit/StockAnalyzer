# STOCK ANALYZER V.1
<img src="./Misc/iconStock.png" width="80" height="80">
<p style="font-size:5px"> Icon Source: http://www.freeiconspng.com/free-images/stock-exchange-icon-png-9909</p>

## Synopsis

Stock Analyzer V.1 is a native Python graphical user interface. The GUI allows user(s) to enter their desired stock ticker symbol to conduct stock analysis.
Current stock analysis features in the current version includes the ability to calculate the overall average of the opening, high, low, and closing prices,
and the volume of the stock. With the given csv file from <b>Yahoo CSV Finance API</b> for each stock, the average(s) calculates the start to end date. The current
version also supports histogram graph(s) for each stock ticker symbol. The histogram graph(s) are plotted based on desired days of <i>30 days</i>, <i>60 days</i>, or <i>90 days</i>.

## Technology Used

+ Python 3.5
+ Tkinter
+ Matplotlib
+ Numpy
+ Yahoo CSV Finance API
+ Py2App

## API Reference

<b>Yahoo CSV Finance API</b>: (http://ichart.finance.yahoo.com/table.csv?s="ticker_symbol")

## Installation

The application has already been packaged and bundled in an app format.

1. Download the zip file
2. Go to dist and click on the GUI.app or you can simply drag the dist folder out to your desktop and then open the folder, and GUI.app icon should be there to run the app.

However, if that doesn't work. Manually download with the following steps:

1. Download the zip file
2. Open up terminal and download all necessary Python dependencies 
3. Direct into the absolute path using Mac command cd stockanalyzer/stockanalyzer 
4. Run python GUI.py 

## How to use the program

There is a .xlsx file inside of the StockPrediction/Misc folder that has all the Ticker Symbols from <b>Yahoo Finance</b>.
The source link of the file can be found here: (http://investexcel.net/all-yahoo-finance-stock-tickers/)

Here is another resource for a list of ticker symbols for <b>New York Stock Exchange (NYSE)</b>,
(http://eoddata.com/symbols.aspx)

Once the program opens up, there are two main buttons at the start page, "Start" and "Close".
The "Start" button allows you to precede into the main page(s).
The "Close" button will close the program.

Once you are in the first main page after pressing "Start". You can enter the ticker symbol and select the open, high, close,
low, and/or volume check boxes that you wish conduct the average analysis on.
<i>You must enter a ticker symbol and select at least one of the check boxes option to precede or errors will occur.</i>
You can hit "Calculate" after you have done that, and the analysis will display on the bottom half of the page.

When you hit "Clear", the program will automatically clear all of the selected check boxes, displayed analyzed information, and
the ticker symbol you've inputted.

<i>Now, if you want to graph, you must calculate the ticker symbol first and have your desired selected check boxes option(s)
selected, or it will either show an error or no graph will be displayed.</i>

If you have successfully calculated and the results are displayed, then you can precede on to the graph by clicking on "Graph".
It will take you the next page.
<i>If you try to print graph without selecting the days you want the range to be of the particular stock, then an error will show up
and no graph will be displayed. </i>

Thus, in order to graph and display the graph, you can select the range of days you want the histogram(s) to be displayed as.

<b>Click on the image/screen viewer to view the entire video at regular speed.</b>

<a href="https://www.youtube.com/watch?v=o9JkgH6pPJE&feature=youtu.be" target="_blank">
 <img src="http://i.imgur.com/D6gTWai.gif" title="source: imgur.com"/>
</a>


### How does the graph works

If you select "Open" and "Close" on the first page after putting your ticker symbol into the entry, and you select 30 days for your desired
range analysis, then it will gather the last 30 days up to the most recent date from the CVS, and display how many of that opening and close price(s) there were
with the given days range fo 30 days.
In other words, let's say the most recent (current) day is December 16 and you select 30 days. Then it will gather all the opening prices from November 13 to December
16 which includes regular stock exchange business days. The histogram will then display how many of the opening prices there were with the given bins.

The "Print Graph" button allows you to constantly change colors of the graph. Each histogram will display a random color each time the "Print Graph" button is hit.
<i>You may plot more than one histogram within a graph.</i>
You may clear the graph if you'd like and re-graph or you can select a different range of days and it will automatically re-graph for you.

## Future feature implementations

+ Allow user(s) to have the option to select different types of plots including stock plots and charts.
+ Implement a navigation toolbar from matplotlib
+ Calculate outliers of opening, high, low, and closing prices.
+ Calculate the daily stock returns
+ Login menu and personalize the application to each user

## Issues

Feel free to submit issues and enhancement requests.

## Contributing

Refer to the "fork-and-pull" Git workflow.

 1. **Fork** the repo on GitHub
 2. **Clone** the project to your own machine
 3. **Commit** changes to your own branch
 4. **Push** your work back up to your fork
 5. Submit a **Pull request** so that we can review your changes

NOTE: Be sure to merge the latest from "upstream" before making a pull request.
