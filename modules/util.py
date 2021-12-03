from logging import StringTemplateStyle
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
def line_graph(data, title):
    """[Plot line graph of the data over the year]

    Args:
        data ([list]): [list of graphing data for each year]
        title ([string]): [title of the graph]
    """    
    assert isinstance(data, np.ndarray)
    assert isinstance(title, str)
    fig, ax = plt.subplots(figsize=(10,5))
    ax.set_ylim([0,100])
    ax.set_xlabel("Year")
    ax.set_ylabel("Percentage")
    ax.set_title(title)
    ax.plot(np.arange(5),data, 'go-')
    plt.xticks(np.arange(5), ['2016','2017','2018','2019','2020'])
    sns.despine()

def line_graph_double(data1, data2, legend1, legend2, title):
    """[Plot line graph of two sets of data over the year]

    Args:
        data1 ([list]): [list of graphing data for each year]
        data2 ([list]): [list of graphing data for each year]
        legend1 ([string]): [legend name of data 1]
        legend2 ([string]): [legend name of data 2]
        title ([string]): [title of the graph]
    """    
    assert isinstance(data1, np.ndarray)
    assert isinstance(title, str)
    assert isinstance(data2, np.ndarray)
    assert isinstance(legend1, str)
    assert isinstance(legend2, str)
    fig, ax = plt.subplots(figsize=(10,5))
    ax.set_ylim([0,100])
    ax.set_xlabel("Year")
    ax.set_ylabel("Percentage")
    ax.set_title(title)
    ax.plot(np.arange(5),data1, 'go-', label = legend1)
    ax.plot(np.arange(5), data2, 'ro-', label = legend2)
    plt.legend(loc=2, prop={'size': 6})
    plt.xticks(np.arange(5),['2016','2017','2018','2019','2020'])
    ax.legend()
    sns.despine()