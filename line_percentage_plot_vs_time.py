def line_plot_time_vs_multi_var(input_df,split_cname,y_cname,split_vals,val,label_list):
    '''
    this function plots multiple percentage lines for different answer in one column and shows trends with time
    :input_df: dataframe with all necessary columns
    :split_cname: the column that we need to divide up the data for other column
    :y_cname: the column name that we want the percentage of
    :split_vals: list of values that we want different line for
    :val: the value we want to find out the percentage for
    :label_list: name of each line for split_vals
    '''
    import numpy as np
    import pandas as pd
    import datetime
    import seaborn as sns
    import matplotlib.pyplot as plt
    assert isinstance(split_cname,str) and isinstance(y_cname,str) and isinstance(label_list, list) and isinstance(split_vals,list) and isinstance(input_df,pd.DataFrame)
    assert len(split_vals)==len(label_list)
    year = ['2016', '2017', '2018', '2019', '2020'] 
    # state of mental health vs discuss mental health with employers
    size_dict = {}
    idx = 0
    # drop answers of "don't know" which is mapped as 1 because 2016 doesn't have this selection
    for i in split_vals:  
        size_dict[idx] = input_df[np.logical_and(input_df[split_cname] == i, input_df[y_cname] != -1)]
        idx += 1    
    # get number of each year
    sample_num = {}
    for i in range(len(split_vals)):
        sample_num[i] = size_dict[i].groupby('year')[y_cname].size()
    yes_dict = {}
    for i in range(len(split_vals)):
    # get number answering yes
        yes_dict[i] = size_dict[i][size_dict[i][y_cname] == val].groupby('year').size()
    lines = ['ro-', 'bo-', 'go-', 'yo-', 'co-', 'mo-']
    x = np.arange(5)
    fig, ax = plt.subplots(figsize=(10, 5))
    for i in range(len(split_vals)):
        ax.plot(x, yes_dict[i].values / sample_num[i].values * 100, lines[i], label=label_list[i])
        plt.xticks(x, year)
        ax.legend()
    ax.set_title("Percentage of Employees Willing to Discuss\nMH with Supervisors")
    ax.set_ylim([0, 100])
    sns.despine()
    ax.set_ylabel("Percentage")
    ax.set_xlabel("Year")