import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
def line_graph(data, title):
    fig, ax = plt.subplots(figsize=(10,5))
    ax.set_ylim([0,100])
    ax.set_xlabel("Year")
    ax.set_ylabel("Percentage")
    ax.set_title(title)
    ax.plot(np.arange(5),data, 'go-')
    plt.xticks(np.arange(5), ['2016','2017','2018','2019','2020'])
    sns.despine()
    #plt.savefig('1.png', transparent=True)

def line_graph_double(data1, data2, legend1, legend2, title):
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
    #plt.savefig('2.png', transparent=True)