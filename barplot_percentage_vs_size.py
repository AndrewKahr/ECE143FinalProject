def bar_percent_wrt_company_size(input_df,column_name,val,p_title):
    import numpy as np
    import pandas as pd
    import datetime
    import seaborn as sns
    import matplotlib.pyplot as plt
    '''
    this function plots the percentage of certain output 'val' in a column with respect to company sizes
    :input_df: dataframe with the company size solumn and the other we want to look into
    :column_name: the name of the column we want to see the percentage of
    :val: the value we want the percentage of
    :p_title: plot title
    '''
    assert isinstance(input_df,pd.DataFrame) and isinstance(column_name,str) and isinstance(p_title,str)
    size = ['1-5', '6-25', '26-100', '100-500', '500-1000', 'More than 1000']
    df_dict = input_df[np.logical_and(input_df.employee_count != -1, input_df[column_name] != -1)]
    sample_num = df_dict.groupby('employee_count')[column_name].size().tolist()
    yes_num = df_dict[df_dict[column_name] == val].groupby('employee_count')[column_name].size()
    yes_percent = yes_num / sample_num * 100
    index = yes_percent.index
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.bar(index, yes_percent.values, width=0.3, color='g')
    plt.xticks(index, size)
    sns.despine()
    plt.ylim([0, 100])
    ax.set_xlabel('Company Size')
    ax.set_ylabel('Percentage')
    ax.set_title(p_title)