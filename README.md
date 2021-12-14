# Project: My First Crypto

## Request
Our client, MegaCoin Co.,  contracted our team to analyze and create a time series forecasting model that will predict cryptocurrency. The client also had a second request to design a website for first time buyers of cryptocurrencies (also known as cryptos). Our team, Best & Brightest Analysis, immediately began discussing what this type of project would require to give a broader understanding to new users and bring fortune to the world!

As our team began the project, we had a discussion about cryptocurrency and realized our own knowledge of cryptocurrency varied wildly with some having a broader understanding than others. We started our project with initial research into the history of crypto and how it came to be such a huge component in today’s market. We then found our data set and began developing our project: My First Crypto!
  
## Data 
We downloaded our data from Yahoo Finance. The site provided data for a variety of cryptocurrencies and allowed us the ability to select the time frame and frequency. The project team decided that we would create the demo for the project with four currently popular cryptos: Bitcoin, Litecoin, Ethereum, and XRP. We decided to pull the data for the last five years and set the time frame as 6 December, 2016 - 6 December 2021. The data consisted of daily data for each crypto. The data columns were of the opening and closing price, the adjusted closing price, the total volume of crypto sold, and the high/low price for each day. Fortunately, this was the exact format that we needed and no preprocessing or cleaning of the data was required.

## Tableau
This section was designed for the users to be able to play with the historical data of the four main cryptocurrencies that we decided to use in our model. The historical data was from 6 December, 2016 - 6 December, 2021. The dashboard was compiled using two different line graphs and a Japanese candlestick graph. The  Japanese candlesticks are visualising the tick data with ample information that tells us a story about the price movement. The four components of a candlestick are the price for open, high, low, close. Line Charts use points connected by line segments to demonstrate changes in values. The two line charts represent the Market Cap Value (total dollar market value) and Total Volumes of crypto sold.

<img src= "https://user-images.githubusercontent.com/85977271/145730696-990c1a70-106f-4dbd-801b-a5da83812df6.PNG" width="500" height="350"/>

The Dashboard was configured using parameters that connected the charts to the chosen cryptocurrency. This allows the user to choose the desired crypto in a popup menu which will alter the values in the dashboard. Additionally, the user has more control by utilizing the date selector and selecting if they’d like to see 1 day, 1 week, 1 month, 3 months, 1 year, or 5 years. 

<img src= "https://user-images.githubusercontent.com/85977271/145730868-b9756e82-9cdf-454d-b15d-3cdb795947c7.PNG" width="450" height="300"/>

## Machine Learning Model

### Arima Model for Time Series Forecasting

ARIMA is short for Auto-Regressive Integrated Moving Average which explains that a given time series based on its own past values creates its own equation to be used to forecast future values.
 
An ARIMA model can be understood by outlining each of its components as follows:
 * Autoregression (AR): refers to a model that shows a changing variable that regresses on its own lagged, or prior, values.
* Integrated (I): represents the differencing of raw observations to allow for the time series to become stationary such as data values being replaced by the difference between the data values and the previous values.
* Moving average (MA):  incorporates the dependency between an observation and a residual error from a moving average model applied to lagged observations.

Each component in ARIMA functions as a parameter with a standard notation of p, d, and q. Where the integer values substitute for the parameters to indicate the type of ARIMA model used.
 
The parameters can be defined as:
 * p: the number of lag observations in the model; also known as the lag order.
* d: the number of times that the raw observations are different; also known as the degree of difference.
* q: the size of the moving average window; also known as the order of the moving average.
 
Linear regression models work best when the predictors are not correlated and are independent of each other.

In order to identify the appropriate ARIMA model for time series data, we need to begin by identifying the orders. We used SARIMAX to evaluate if the order would fit the model because there are more than one order that is used. SARIMAX stands for Seasonal AutoRegressive Integrated Moving Average with eXogenous regressors and provided an output of models to use to provided an acuate representatio of furture forecast. The follow are the models we learn to help get an acurate analysis:

* ARIMA (0,0,0) = white noise model: mostly used in engineering models and will not be focused on in this report.

* ARIMA (1,0,0) = first-order autoregressive model: if the series is stationary and autocorrelated, perhaps it can be predicted as a multiple of its previous value, plus a constant.  
 
* ARIMA (2,0,0) second-order autoregressive model can be described as a system whose mean reversion takes place in a sinusoidally oscillating fashion, as the motion of a mass on a spring that is subjected to random shocks.
 
* ARIMA (0,1,0) = random walk:  a random walk is a mathematical term known as a stochastic or random process, that describes a path that consists of a succession of random steps. An example of a random walk is the random walk on the integer number which starts at 0 and at each step moves +1 or −1 with equal probability. Other examples include the path traced by a molecule as it travels from a liquid state to a gas state.
 
* ARIMA (1,1,0) = differenced first-order autoregressive model: one in which the current value is based on the immediately preceding value.
 
* ARIMA (0,1,1) Single Exponential smoothing: The model uses a technique for smoothing time series data using the exponential window function. Whereas in the simple moving average the past observations are weighted equally, exponential functions are used to assign exponentially decreasing weights over time. It is an easily learned and easily applied procedure for making some determination based on prior assumptions by the user, such as seasonality.
 
* ARIMA (0,2,1) or (0,2,2) Double Exponential Smoothing: a Model that an exponential moving average that takes into account the tendency of data to either increases or decrease over time without repeating

***Note: The difference between single and double exponential is that single exponential smoothing uses a weighted moving average with exponentially decreasing weights.**


### Bitcoin Results
In these graphs, you can see that Bitcoin continues with a steady rise with slide decreases in price. The largest dip in price is predicted to be in mid-2023 with the highest peak being in early 2024. Our predictions show that Bitcoin will rise to roughly $90,000 - $110,000 in the next three years. Our recommendation: Buy now to maximize your profits!

<img src= "https://user-images.githubusercontent.com/85977271/145919514-927f5b54-9db2-4735-bea8-52ec7537c8fe.PNG" width="800" height="250"/>

<img src= "https://user-images.githubusercontent.com/85977271/145919565-88831128-4a34-45b3-a5c2-e022219de282.PNG" width="800" height="250"/>

### Ethereum Results
In these graphs, you can see that Ethereum is predicted to have a meteoric rise in the next three years. It will be on the continuous rise until 2024 and we predict that the price will be somewhere between $25,000 - $35,000. Our recommendation: Buy now to maximize your profits!

<img src= "https://user-images.githubusercontent.com/85977271/145919586-26af9c8a-6792-42df-8e06-120a60300c7d.PNG" width="800" height="250"/>

<img src= "https://user-images.githubusercontent.com/85977271/145919609-a0cceb0e-e885-445b-9c5e-f6c8ebd20d2c.PNG" width="800" height="250"/>

### Litecoin Results
In these graphs, you can see that Litecoin has many dips and peaks until 2024. We predict that the lowest dip will be in late 2023 and the highest peak will be in early 2024. Our recommendation: Be Cautious and keep your eye on the price changes! Remember to buy low and sell high!

<img src= "https://user-images.githubusercontent.com/85977271/145919693-aa23dc79-7584-48f0-bf98-1c40884f8072.PNG" width="800" height="250"/>

<img src= "https://user-images.githubusercontent.com/85977271/145923006-ce06eb50-0682-4a08-8e14-1e400cbe6109.PNG" width="800" height="250"/>

### XRP Results
In these graphs, you can see that XRP is extremely inconsistent over the next three years with wildly contrasting changes in price. According to our predictions, the pattern does hold consistent with the dips occuring early every year and the peaks occuring a few months afterward. Our recommendation: Be cautious and time your purchases! Remember to buy low and sell high!

<img src= "https://user-images.githubusercontent.com/85977271/145919644-f7d02ab8-3b04-458a-b96c-70ac1d4d23ef.PNG" width="800" height="250"/>

<img src= "https://user-images.githubusercontent.com/85977271/145919672-58de51a5-1d0b-4b9b-a809-97d9ce43fa53.PNG" width="800" height="250"/>

## Web Design 
After initializing a Flask-powered API, we used Heroku to deploy the web page to the cloud. We decided to use Bootstrap to create the themes for the website. This theme provided large imagery and text space for our visualizations and analysis. The theme’s imagery was updated with cryptocurrency photography provided from pexels.com to express the intricacies of cryptocurrency. When it came to understanding cryptocurrency, we wanted to approach our  web design in a clean and simple way. We created an easy-to-use menu that provided the user the ability to see the landing page with a quick history and explanation of cryptocurrency, recommendations from the results of the SARIMA model, an analysis page that included the Tableau of our historical data, our report from the project, a works cited page, and the project teams information. 

Click here to explore our demo! https://my-first-crypto.herokuapp.com/

## Model Limitations
The project team had several limitations during the development of our demo page: 
* Our main limitation were time constraints
* Cryptocurrency is highly volatile. Outside variables affect the price which could cause the model to be incorrect. 
* Our model used historical data and not live data. This renders our model unable to adjust to unforeseen variables affecting the price. 

## Future Goals 
The project team plans on continueing the development of the demo page by including some of the following goals: 
* Link the model to live data so that it can predict more accurately. 
* Update the model so that it can predict using daily fluctuations in data instead of monthly. 
* Increase the number of cryptocurrencies used. 

## Project 4 Team: Best and Brightest Analysis
  <b>
&emsp;  - Celenia Chapa
&emsp;  - Tyler Cutrer
&emsp; - Daniella Mayoral
  </b>
