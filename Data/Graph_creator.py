import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import Data_Processing as D_P

def main():
    df = pd.DataFrame.from_records(D_P.main(), columns=['DateTime', 'kWh_usage'])
    sns.set_style(style='darkgrid')
    bar_graph(df)

def line_graph(df):
    sns.lineplot(data=df, x='DateTime', y='kWh_usage')
    plt.show()

def bar_graph(df):
    sns.barplot(data=df, x='DateTime', y='kWh_usage')
    plt.show()
    
if __name__ == '__main__':
    main()