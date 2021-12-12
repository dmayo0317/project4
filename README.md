# Project: My First Crypto

## Request
Our client, MegaCoin Co.,  contracted our team to analyze and create a time series forecasting model that will predict cryptocurrency. The client also had a second request to design a website for first time buyers of cryptocurrencies (also known as cryptos). Our team, Best & Brightest Analysis, immediately began discussing what this type of project would require to give a broader understanding to new users and bring fortune to the world!

As our team began the project, we had a discussion about cryptocurrency and realized our own knowledge of cryptocurrency varied wildly with some having a broader understanding than others. We started our project with initial research into the history of crypto and how it came to be such a huge component in today’s market. We then found our data set and began developing our project: My First Crypto!
  
## Data 
We downloaded our data from Yahoo Finance. The site provided data for a variety of cryptocurrencies and allowed us the ability to select the time frame and frequency. The project team decided that we would create the demo for the project with four currently popular cryptos: Bitcoin, Litecoin, Ethereum, and XRP. We decided to pull the data for the last five years and set the time frame as 6 December, 2016 - 6 December 2021. The data consisted of daily data for each crypto. The data columns were of the opening and closing price, the adjusted closing price, the total volume of crypto sold, and the high/low price for each day. Fortunately, this was the exact format that we needed and no preprocessing or cleaning of the data was required.

## Machine Learning Model

## Tableau
This section was designed for the users to be able to play with the historical data of the four main cryptocurrencies that we decided to use in our model. The historical data was from 6 December, 2016 - 6 December, 2021. The dashboard was compiled using two different line graphs and a Japanese candlestick graph. The  Japanese candlesticks are visualising the tick data with ample information that tells us a story about the price movement. The four components of a candlestick are the price for open, high, low, close. Line Charts use points connected by line segments to demonstrate changes in values. The two line charts represent the Market Cap Value (total dollar market value) and Total Volumes of crypto sold.

<img src= "https://user-images.githubusercontent.com/85977271/145730696-990c1a70-106f-4dbd-801b-a5da83812df6.PNG" width="500" height="350"/>

The Dashboard was configured using parameters that connected the charts to the chosen cryptocurrency. This allows the user to choose the desired crypto in a popup menu which will alter the values in the dashboard. Additionally, the user has more control by utilizing the date selector and selecting if they’d like to see 1 day, 1 week, 1 month, 3 months, 1 year, or 5 years. 

<img src= "https://user-images.githubusercontent.com/85977271/145730868-b9756e82-9cdf-454d-b15d-3cdb795947c7.PNG" width="500" height="350"/>

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
