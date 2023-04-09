import numpy as np
import pandas as pd
import plotly.express as px
from datetime import datetime

# Data import
df = pd.read_csv('data_v1.1.csv')

# Data wrangling
df['datetime'] = pd.to_datetime(df['datetime'])
df["time"] = df['datetime'].dt.time
df["date"] = df['datetime'].dt.date
df['Net Change'] = df['ppl_in'] - df['ppl_out']
df_grouped = df.groupby(['datetime', 'date', 'time', 'Car', 'door']).sum()
capacity_per_train = 76*2
df_grouped['Ppl Onboard'] = df_grouped['Net Change'].cumsum()
df_grouped['Occupancy Rate'] = df_grouped['Ppl Onboard'] / capacity_per_train

# Segregation of car and door
dfc1 = df[df['Car'] == 1]
dfc2 = df[df['Car'] == 2]
dfc1d1 = dfc1[dfc1['door'] == 1]
dfc1d2 = dfc1[dfc1['door'] == 2]
dfc2d1 = dfc2[dfc2['door'] == 1]
dfc2d2 = dfc2[dfc2['door'] == 2]

class C1_Subseries():
    def flow_plot():
        plt_flow = px.line(dfc1, x='datetime', y=["ppl_in", "ppl_out"], title='People in and out over time')
        return plt_flow
    
    def min_subplot():
        plt_min_sub = px.line(px.line(dfc1, x=dfc1['time'], y=["ppl_in", "ppl_out"], title='Average people inflow and outflow over time of every minute'))
        return plt_min_sub
    
    def net_change_plot():
        plt_net_change = px.line(dfc1, x=dfc1['datetime'], y=dfc1['Net Change'], title='Net Change')
        return plt_net_change
    
class C2_Subseries():
    def flow_plot():
        plt_flow = px.line(dfc2, x='datetime', y=["ppl_in", "ppl_out"], title='People in and out over time')
        return plt_flow
    
    def min_subplot():
        plt_min_sub = px.line(px.line(dfc2, x=dfc2['time'], y=["ppl_in", "ppl_out"], title='Average people inflow and outflow over time of every minute'))
        return plt_min_sub
    
    def net_change_plot():
        plt_net_change = px.line(dfc2, x=dfc2['datetime'], y=dfc2['Net Change'], title='Net Change')
        return plt_net_change

class KPI:

    def occupancy_rate_percent():
        occupancy_rate_percent = "{:.2%}".format(df_grouped['Occupancy Rate'][-1])
        return occupancy_rate_percent
    
    def traffic():
        traffic = int(df_grouped['ppl_in'].sum())
        return traffic
    
    def ppl_onboard():
        ppl_onboard = int(df_grouped['Ppl Onboard'].tail(1))
        return ppl_onboard
    
    def average_traffic():
        average_traffic = float((df_grouped['ppl_in'].mean()))
        return average_traffic


class Realtime:

    def summary_plot():
        plt_all = px.line(df_grouped, x=df_grouped.index.get_level_values("datetime"), y=df_grouped['Net Change'], title='Net Change')
        return plt_all

    def flow_plot():
        plt_flow = px.line(df_grouped, x=df_grouped.index.get_level_values("datetime"), y=['ppl_in', 'ppl_out'], title='People Entering and Exiting')
        return plt_flow
    
    def total_count_plot():
        plt_total_cnt = px.line(df_grouped, x=df_grouped.index.get_level_values("datetime"), y='Net Change', title='Total People Count')
        return plt_total_cnt
    
    def net_change_plot():
        plt_net_change = px.line(df_grouped, x=df_grouped.index.get_level_values("datetime"), y=df_grouped['Net Change'], title='Net Change')
        return plt_net_change