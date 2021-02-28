#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 12:21:36 2021

@author: vrushali
"""


import pandas as pd
import numpy as np
import math as m
import matplotlib.pyplot as plt


def simulated_prices(StockPrice, RiskFreeRate, Volatility, NumberOfSteps, TimeToMaturity):
    NumberOfSimulations = 100
    SimulatedSteps = NumberOfSteps * TimeToMaturity
    
    #Define dt
    dt = 1 / NumberOfSteps
    
    #define drift and standard deviation of stocks to implement GBM
    Drift = (RiskFreeRate - 0.5 * Volatility * Volatility) * dt
    Sigmadt = Volatility * m.sqrt(dt)
    
    #getting the price of stock St as for time t
    StockPricet = np.zeros(shape = (SimulatedSteps, NumberOfSimulations))
    StockPricet[0,] = StockPrice #set the initial value of stock
    
    #Implementeing loop to simulate the price of stock
    for i in range(1, SimulatedSteps):
        for j in range(0, NumberOfSimulations):
            StandardNormalDistribution = np.random.randn(1)
            StockPricet[i,j] = StockPricet[i-1,j] * m.exp(Drift + Sigmadt * StandardNormalDistribution)
            
    return (StockPricet)

Prices = simulated_prices(100, 0.1, 0.07, 4, 22)

print(pd.DataFrame(Prices))

#plot the graph of simulated stock prices
plt.plot(Prices)
plt.title("Monte Carlo simulation")
plt.xlabel('Number  of simulated steps')
plt.ylabel("Simulated Stock Prices")
plt.show()

