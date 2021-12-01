def v_count_plot(df,y_name,x_name,p_title):
    '''
    :df: input dataframe with necessary columns
    :y_name: y axis label
    :x_name: x axis label
    :p_title: plot title
    this function plots the number count
    '''
    import numpy as np
    import pandas as pd
    import datetime
    import seaborn as sns
    import matplotlib.pyplot as plt
    assert isinstance(x_name,str) and isinstance(y_name,str) and isinstance(p_title,str) and isinstance(df,pd.Series)
    MH_dict=dict(df.value_counts())
    fig, ax = plt.subplots(figsize=(8, 12))
    disorder_name=list(MH_dict.keys())
    disorder_num=list(MH_dict.values())
    y=np.arange(len(disorder_name))
    ax.barh(y,disorder_num ,color='g')
    ax.set_yticks(y,labels=disorder_name,fontsize=21)
    ax.invert_yaxis()
    ax.tick_params(axis='x',labelsize=21)
    ax.set_xlabel(x_name,fontsize=21)
    ax.set_ylabel(y_name,fontsize=21)
    ax.set_title(p_title,fontsize=21)
    sns.despine()