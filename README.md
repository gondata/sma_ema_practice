# README

This project is focused on analyzing stock prices using Simple Moving Averages (SMA) and Exponential Moving Averages (EMA).

## Requirements


- numpy
- pandas
- pandas_datareader
- yfinance
- matplotlib

## Usage

1. First, we import the required libraries


2. Next, we download the stock data by specifying the ticker symbol, start date, and end date. In this example, we use Google stock (ticker symbol: **GOOG**) and the dates range from **'2012-01-01'** to **'2023-02-02'**.


3. Then, we define two functions to compute SMA and EMA respectively. The **computeSMA** function takes the data and the window size as input, and returns the SMA values. The **computeEMA** function takes the data and the span as input, and returns the EMA values.


4. After that, we define a **construct_df** function to construct the final dataframe that includes both SMA and EMA values for different window/span sizes (ranging from 50 to 250 in steps of 50).


5. We use the **plot_data_SMA** function to plot the stock prices and the SMA values. Similarly, the **plot_data_EMA** function is used to plot the stock prices and the EMA values.

## Example

The example in the code uses the **GOOG** stock, but you can easily modify the code to use any other stock by changing the **ticker** variable.
