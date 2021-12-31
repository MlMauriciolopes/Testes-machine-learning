#!/usr/bin/env python
# coding: utf-8

# In[1]:


#pip install --upgrade mplfinance


# In[2]:


# import libraries
import yfinance as yf
import mplfinance as mpf # pip install --upgrade mplfinance
import matplotlib.pyplot as plt
import pandas as pd


# ### Basic information

# In[3]:


yf.Ticker('msft').info # microsoft info


# In[4]:


tsla = yf.Ticker("TSLA") # Tesla info
tsla.info


# In[5]:


tsla.info.keys()


# In[6]:


tsla.info['enterpriseValue']


# In[7]:


print(f"Market Cap : {tsla.info['marketCap']}\n")
print(f"Employees : {tsla.info['fullTimeEmployees']}\n")
print(f"Business Summary : \n{tsla.info['longBusinessSummary']}")


# ### OHLCV data

# In[8]:


tsla.history(period='5d')


# In[9]:


# Remove actions 
tsla.history(period='5d', actions='False')


# In[10]:


# Getting data using start date and end date
tsla = yf.Ticker('tsla')
df = tsla.history(start='2021-02-20', end='2021-03-06', action=False)
df


# In[11]:


df.shape


# In[12]:


# yf.Ticker('tsla').history()
yf.Ticker('tsla').history('5y', interval='3mo')


# ### Intraday plot

# In[13]:


# precisa colocar a horário real atualizado, senão dá erro
# need to put the actual time updated, otherwise it gives an error
tsla.history(start='2021-12-31', end='2022-01-01', 
                 interval = "1m", actions=False)


# In[14]:


# precisa colocar a horário real atualizado, senão dá erro
# need to put the actual time updated, otherwise it gives an error
hist=tsla.history(start='2021-12-31', end='2022-01-01', 
                 interval = "1m", actions=False)

mpf.plot(hist, type='candle', volume=True, style='yahoo', mav=(20),
        title='TSLA : 31 DEC 2021', tight_layout=True)


# In[15]:


# AMZN = Amazon, AAPL = Apple, TSLA = Tesla
data = yf.download("AMZN AAPL TSLA", period="ytd",
                  group_by='ticker', actions=False)
amzn=data['AMZN']
aap=data['AAPL']


# In[16]:


amzn.head()


# ### Convert data into csv

# In[17]:


amzn.to_csv('amzn.csv')


# ## Other functions in Ticker Module

# In[18]:


# actions
aapl = yf.Ticker('AAPL')
aapl.actions.tail(5)


# In[19]:


# dividends
aapl.dividends


# In[20]:


# splits
aapl.splits.tail()


# In[21]:


# major_holders
aapl.major_holders


# In[22]:


# institucional_holders
aapl.institutional_holders


# In[23]:


# sustainability
aapl.sustainability


# In[24]:


# Analyst recommendations
aapl.recommendations.tail()


# In[25]:


# Show the upcoming events
aapl.calendar


# In[26]:


# Show ISIN code: International Securities Identification Number
aapl.isin


# In[27]:


# Avaliable option expiration dates
aapl.options


# In[28]:


aapl.option_chain('2021-12-31').puts

