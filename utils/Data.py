import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

# Data import
df = pd.read_csv('data_9hr.csv')

# Data wrangling
df['datetime'] = pd.to_datetime(df['datetime'])
df["time"] = df['datetime'].dt.time
df["date"] = df['datetime'].dt.date
df["ppl_out"] = df["ppl_out"]*-1 # Showing outflow of people as negative
df['Net Change'] = df['ppl_in'] + df['ppl_out']


# Group only by datetime
df_grouped_datetime = df.groupby(by="datetime").sum()[["ppl_out", "ppl_in", "Net Change"]]

# Group by all
df_grouped = df.groupby(['datetime', 'date', 'time', 'Car', 'door']).sum()
capacity_per_train = 76*2
df_grouped['Ppl Onboard'] = df_grouped['Net Change'].cumsum()
df_grouped['Occupancy Rate'] = df_grouped['Ppl Onboard'] / capacity_per_train

# Segregation of car and door
dfc1 = df[df['Car'] == 1]
dfc1_grped = df[df['Car'] == 1].groupby("datetime").sum()[["ppl_in", "ppl_out", "Net Change"]].reset_index()
dfc1d1 = dfc1[dfc1['door'] == 1]
dfc1d2 = dfc1[dfc1['door'] == 2]

# groupby time
c1_grouped = dfc1.groupby("time").mean()[["ppl_out", "ppl_in", "Net Change"]]
c1d1_grouped = dfc1d1.groupby("time").mean()[["ppl_out", "ppl_in", "Net Change"]]
c1d2_grouped = dfc1d2.groupby("time").mean()[["ppl_out", "ppl_in", "Net Change"]]

class C1_Subseries():

    def flow_plot():
        plt_flow = px.line(dfc1_grped, x='datetime', y=["ppl_in", "ppl_out"], title='[Car 1] People in and out over time')
        plt_flow.add_bar(x=dfc1_grped['datetime'], y=dfc1_grped["Net Change"], name="Net people flow")
        return plt_flow
    
    def min_subplot():
        plt_min_sub = px.line(c1_grouped, x=c1_grouped.index, y=["ppl_in", "ppl_out"], title='[Car 1] Average people inflow and outflow over time of every minute')
        plt_min_sub.add_bar(x=c1_grouped.index, y=c1_grouped["Net Change"], name="Net people flow")
        return plt_min_sub
    
    def d1_flow_plot():
        d1plt_flow = px.line(dfc1d1, x='datetime', y=["ppl_in", "ppl_out"], title='[Car 1] People in and out over time')
        d1plt_flow.add_bar(x=dfc1d1['datetime'], y=dfc1d1["Net Change"], name="Net people flow")
        return d1plt_flow

    def d1_min_subplot():
        d1plt_min_sub = px.line(c1d1_grouped, x=c1d1_grouped.index, y=["ppl_in", "ppl_out"], title='[Car 1] Average people flow per minute')
        d1plt_min_sub.add_bar(x=c1d1_grouped.index, y=dfc1d1["Net Change"], name="Net people flow")
        return d1plt_min_sub

    def d2_flow_plot():
        d2plt_flow = px.line(dfc1d2, x='datetime', y=["ppl_in", "ppl_out"], title='[Car 1] People in and out over time')
        d2plt_flow.add_bar(x=dfc1d2['datetime'], y=dfc1d2["Net Change"], name="Net people flow")
        return d2plt_flow

    def d2_min_subplot():
        d2plt_min_sub = px.line(c1d2_grouped, x=c1d2_grouped.index, y=["ppl_in", "ppl_out"], title='[Car 1] Average people flow per minute')
        d2plt_min_sub.add_bar(x=c1d2_grouped.index, y=dfc1d1["Net Change"], name="Net people flow")
        return d2plt_min_sub

dfc2 = df[df['Car'] == 2]
dfc2_grped = df[df['Car'] == 2].groupby("datetime").sum()[["ppl_in", "ppl_out", "Net Change"]].reset_index()
dfc2d1 = dfc2[dfc2['door'] == 1]
dfc2d2 = dfc2[dfc2['door'] == 2]

# C2
c2_grouped = dfc2.groupby("time").mean()[["ppl_out", "ppl_in", "Net Change"]]
c2d1_grouped = dfc2d1.groupby("time").mean()[["ppl_out", "ppl_in", "Net Change"]]
c2d2_grouped = dfc2d2.groupby("time").mean()[["ppl_out", "ppl_in", "Net Change"]]
    
class C2_Subseries():
    def flow_plot():
        plt_flow = px.line(dfc2_grped, x='datetime', y=["ppl_in", "ppl_out"], title='[Car 2] People in and out over time')
        plt_flow.add_bar(x=dfc2_grped['datetime'], y=dfc2_grped["Net Change"], name="Net people flow")
        return plt_flow
    
    def min_subplot():
        plt_min_sub = px.line(c2_grouped, x=c2_grouped.index, y=["ppl_in", "ppl_out"], title='[Car 2] Average people inflow and outflow over time of every minute')
        plt_min_sub.add_bar(x=c2_grouped.index, y=c2_grouped["Net Change"], name="Net people flow")
        return plt_min_sub
    
    def d1_flow_plot():
        d1plt_flow = px.line(dfc2d1, x='datetime', y=["ppl_in", "ppl_out"], title='[Car 2] People in and out over time')
        d1plt_flow.add_bar(x=dfc2d1['datetime'], y=dfc2d1["Net Change"], name="Net people flow")
        return d1plt_flow

    def d1_min_subplot():
        d1plt_min_sub = px.line(c2d1_grouped, x=c2d1_grouped.index, y=["ppl_in", "ppl_out"], title='[Car 2] Average people flow per minute')
        d1plt_min_sub.add_bar(x=c2d1_grouped.index, y=dfc1d1["Net Change"], name="Net people flow")
        return d1plt_min_sub

    def d2_flow_plot():
        d2plt_flow = px.line(dfc2d2, x='datetime', y=["ppl_in", "ppl_out"], title='[Car 2] People in and out over time')
        d2plt_flow.add_bar(x=dfc2d2['datetime'], y=dfc2d2["Net Change"], name="Net people flow")
        return d2plt_flow

    def d2_min_subplot():
        d2plt_min_sub = px.line(c2d2_grouped, x=c2d2_grouped.index, y=["ppl_in", "ppl_out"], title='[Car 2] Average people flow per minute')
        d2plt_min_sub.add_bar(x=c2d2_grouped.index, y=dfc1d1["Net Change"], name="Net people flow")
        return d2plt_min_sub

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
        # plt_all = px.line(df_grouped, x=df_grouped.index.get_level_values("datetime"), y=df_grouped['Net Change'], title='Net Change')
        plt_all = px.line(df_grouped_datetime, x=df_grouped_datetime.index.get_level_values("datetime"), y=["ppl_out", "ppl_in"], title="Overall people flow overtime")
        plt_all.add_bar(x=df_grouped_datetime.index.get_level_values("datetime"), y=df_grouped_datetime["Net Change"], name="Net people flow")
        plt_all.update_yaxes(title_text="Number of people")

        # buttons for timeframe selection
        plt_all.update_layout(
            xaxis=dict(
                rangeselector=dict(
                    buttons=list([
                        dict(count=1,
                            label="1h",
                            step="hour",
                            stepmode="backward"),    
                        dict(count=1,
                            label="1d",
                            step="day",
                            stepmode="backward"), 
                        dict(count=1,
                            label="all",
                            step="all",
                            stepmode="backward")                        
                    ])
                ),
                rangeslider=dict(
                    visible=True
                ),
                type="date"
            )
        )

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
    
class Analysis():

    def MA():
        windows = ["15min", "H", "D"]
        df_windows = df_grouped_datetime[["ppl_in", "ppl_out", "Net Change"]].reset_index()

        MA_graphs = {}

        for time in windows:
            df_windows_grped = df_windows.groupby(pd.Grouper(key="datetime", freq=time)).sum()
            plt_timeframe = px.line(df_windows_grped, x=df_windows_grped.index, y=["ppl_out", "ppl_in"])
            MA_graphs[time] = plt_timeframe

        return MA_graphs
    
    def hourly_analysis():
        # extrcating time only
        df_qhourly = df_grouped_datetime.reset_index()
        df_qhourly["time"] = df_qhourly["datetime"].dt.time
        df_qhourly.drop("datetime", axis=1)

        # rearranging columns
        df_qhourly = df_qhourly[["time", "ppl_out", "ppl_in"]]
        df_qhourly.sort_values("time", inplace=True)

        # daily mean
        df_daily_mean = df_qhourly.groupby(by="time").mean()

        # plotting by hour
        plt_hourly = px.scatter(df_qhourly, x="time", y=["ppl_out", "ppl_in"], marginal_y="histogram")

        plt_hourly.update_traces(marker=dict(size=3.5, opacity=0.3), selector=dict(mode='markers'))

        plt_hourly.add_trace(
            go.Scatter(
                x=df_daily_mean.index, 
                y=df_daily_mean["ppl_out"],
                mode="lines",
                line=go.scatter.Line(color="blue", width=1),
                name="Daily out mean")
        )

        plt_hourly.add_trace(
            go.Scatter(
                x=df_daily_mean.index, 
                y=df_daily_mean["ppl_in"],
                mode="lines",
                line=go.scatter.Line(color="red", width=1),
                name="Daily in mean")
        )
        
        plt_hourly.update_yaxes(title_text="Number of people")

        return plt_hourly