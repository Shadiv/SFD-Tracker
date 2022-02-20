# SFD-Tracker

SFD = Stock Fundamental Data Tracker

This program is meant to be a helpful tool for fundamental stock analysis.
Even though stock fundamental data is available for free on the internet, it's not very easy to access such information
quickly. Getting access to accounting data of particular company for several years might be time-consuming task. 
Furthermore, whole point of performing a fundamental analysis of particular stock is to decide whether it is 
undervalued or not. And if it is not, whole analysis is basically pointless.

That is why I want to develop a tool, that can help small investors make their fundamental analysis more swift and efficient. 

It should be able to display all crutual financial information of particular company (accounting data), including 
general information about current price movements, beta coefficient, covariation, and dividend information 
pre-calculated ratios (P/E, P/S, ROA, ROE, etc.) and other information, necessary for fundamental stock analysis 
(hope that will be possible). Such overview should provide user with ability to gain general understanding of company's 
financial situation and help them quickly decide whether the fundamental analysis of the stock is even worth performing. 


Working notes:
Program components (planned):
1) Parser (parsing sec.gov and getting accounting data based on given ticker)
2) Database (store accounting data, prices, etc.)
3) Fundamental analysis calculator - tool for basic FA calculations (WACC, ratios, etc.)
4) Envelope - web app to envelope all the components for convinient usage and interaction with a user
5) Knowledge hub = links to study materials, basic information about stock fundamental analysis 
6) News parser - small program that gets recent news for given ticker
7) AI stock price predictor??
