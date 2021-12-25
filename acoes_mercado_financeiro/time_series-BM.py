#!/usr/bin/env python
# coding: utf-8

# # Análise de ações do mercado financeiro

# In[1]:


# Bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
import yfinance as yf #pip install yfinance


# #### 1.Aquisição dos dados de ações

# In[2]:


ticket = yf.Ticker('^BVSP')
#df = ticket.history(period='3y', interval='1mo')
df = ticket.history(interval='1d', start='2018-01-01', end='2021-01-01')


# In[3]:


df


# In[4]:


df.tail(5) # mostra os últimos valores da tabela


# #### 2.Decomposição de uma série temporal
# 
# ##### Modelos matemáticos
# 
# https://www.statsmodels.org/stable/generated/statsmodels.tsa.seasonal.seasonal_decompose.html <br/>
# . Additive Model <br/>
# <n/>.y(t) = Trend_t + Seasonality_t + Noise_t<br/>
# .Multiplicative Model<br/>
#     .y(t) = Trend * Seasonality_t * Noise_t<br/>

# In[5]:


# Pegando a data e o fechamento
df[['Close']]


# In[6]:


df[['Close']].info()


# In[7]:


df[['Close']].head()


# In[8]:


decomposicao = seasonal_decompose(df[['Close']],model='additive',period=30, extrapolate_trend=30)


# In[9]:


df[['Close']].plot()


# In[10]:


decomposicao.seasonal + decomposicao.resid + decomposicao.trend


# In[11]:


decomposicao.trend.iloc[0:5]


# In[12]:


decomposicao.plot();


# In[13]:


decomposicao_multi = seasonal_decompose(df[['Close']], model='multiplicative', period=30, extrapolate_trend=30)


# In[14]:


decomposicao.seasonal


# In[15]:


decomposicao_multi.seasonal


# In[16]:


max(decomposicao_multi.resid)


# In[17]:


ax, fig = plt.subplots(figsize=(15,8))
plt.plot(decomposicao.observed)
plt.plot(decomposicao.trend)


# In[18]:


fig, (ax1, ax2, ax3, ax4) = plt.subplots(4,1, figsize=(12,8))
decomposicao.observed.plot(ax=ax1)
decomposicao.trend.plot(ax=ax2)
decomposicao.seasonal.plot(ax=ax3)
decomposicao.resid.plot(ax=ax4)
plt.tight_layout()


# ### 3.Cálculo de média móvel

# In[19]:


df['Close']


# In[20]:


df['Close'].rolling(7).mean()


# In[21]:


media_movel7d = df['Close'].rolling(7).mean()
media_movel14d = df['Close'].rolling(14).mean()
media_movel21d = df['Close'].rolling(21).mean()


# In[22]:


fig, ax = plt.subplots(figsize=(12,5))
#plt.plt(media_movel7d, 'orange')
#plt.plot(media_movel14d, 'red')
plt.plot(media_movel21d, 'black')
plt.plot(df['Close'])


# ### 4.Extração de features

# In[23]:


df.head()


# In[24]:


df.reset_index(inplace=True)


# In[25]:


df.head()


# In[26]:


df['Date'].dt.year
#df['Date'].dt.day
#df['Date'].dt.month


# In[27]:


# Criar features para cada período
df['year'] = df['Date'].dt.year
df['month'] = df['Date'].dt.month
df['day'] = df['Date'].dt.day


# In[28]:


df.head()


# In[29]:


# Rentabilidade é o preço atual / preço anterior * 100 - 100
df[['Close']]


# In[30]:


df['Close'].head()


# In[31]:


df['Close'].shift()


# In[32]:


df['rentabilidade'] = df['Close'] / df['Close'].shift() *100 -100


# In[33]:


df.head()


# In[34]:


def features_extraction(df_):
    # criar features para cada período
    df_['year'] = df_['Date'].dt.year
    df_['month'] = df_['Date'].dt.month
    df_['day'] = df_['Date'].dt.day
    df_['rentabilidade'] = df_['Close'] / df_['Close'].shift() *100 -100


# In[35]:


df.reset_index(inplace=True)


# In[36]:


features_extraction(df)


# In[37]:


df.head()


# ### Hipotese 1.Existe um melhor mês para investir no ativo ? <br/>
# .Considerando 3 anos de dados de rentabilidade, o agrupamento da mostra que os meses de janeiro, junho e setembro são mais interessantes para investir

# In[38]:


df.groupby('month').agg({'rentabilidade':'sum'}).plot(kind='bar')


# In[39]:


df.set_index('Date', inplace=True)


# In[40]:


media_movel30d = df['Close'].rolling(30).mean()
media_movel90d = df['Close'].rolling(90).mean()
fig, ax = plt.subplots(figsize=(8,4))
plt.plot(df['Close'])
plt.plot(media_movel30d)
#plt.plot(media_movel90d)


# ### Hipotese 2.Existe um melhor dia para investir no ativo ?

# In[41]:


df.groupby('day').agg({'rentabilidade':'sum'}).plot(kind='bar')


# In[42]:


df.iloc[0]


# In[43]:


df.iloc[-1]


# In[44]:


df['Close'].iloc[-1] / df['Close'].iloc[0] *100 -100


# ### 5.Correlação de séries temporais

# In[45]:


tickets = ['VALE3.SA','ITUB4.SA','PETR4.SA','ABEV3.SA','BBDC4.SA','BBAS3.SA','^BVSP','USDBRL=X']


# In[46]:


dfs = []

for t in tickets:
    print('Reading ticker {}...'.format(t))
    ticket = yf.Ticker(t)
    aux = ticket.history(interval='1d', start='2018-01-01', end='2021-01-01')
    aux.reset_index(inplace=True)
    aux['ticket'] = t
    dfs.append(aux)


# In[47]:


dfs[0] # vale
#dfs[1] # itau


# In[48]:


for d in dfs:
    features_extraction(d)


# In[49]:


dfs[0]


# In[50]:


correlacao = pd.DataFrame()
for d in dfs:
    correlacao[d['ticket'].iloc[0]] = d['rentabilidade']


# In[51]:


correlacao.head()


# In[52]:


correlacao.corr()


# ## Visualização de dados usando Seaborn

# In[53]:


import seaborn as sns


# In[54]:


ax, fig = plt.subplots(figsize=(20,5))
ax = sns.heatmap(correlacao.corr(), annot=True)


# ## Visualização de dados usando Plotly

# In[55]:


import plotly.graph_objs as go #pip install plotly==5.5.0 


# In[56]:


def plot_lines(df_, columns=['Open','Close','High','Low']):
    
    fig = go.Figure()
    for c in columns:
        fig.add_trace(go.Scatter(x = list(df_.index),
                                y = df_[c],
                                mode = 'markers+lines',
                                name = c))
    return fig


# In[57]:


plot_lines(df)


# In[60]:


def plotCandleStick(df, acao='ticket'):
    trace1 = {
        'x': df.index,
        'open': df.Open,
        'close': df.Close,
        'high': df.High,
        'low': df.Low,
        'type': 'candlestick',
        'name': acao,
        'showlegend': False
    }
    
    data = [trace1]
    layout = go.Layout()
    
    fig = go.Figure(data=data, layout=layout)
    return fig


# In[61]:


plotCandleStick(df)


# In[ ]:




