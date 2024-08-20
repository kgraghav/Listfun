# Class to create Plots grid

from itertools import product,cycle,combinations
import seaborn as sns
import matplotlib.pyplot as plt

class Plotsgrid:

    """ Creates a nxn grid of plots for an input df. Shows blank for grid values exceeding number of columns of df"""


    def __init__(self,df):
        self.df=df 

    def figure_params(self):
        df=self.df
        n_data_cols=len(df.columns)
        self.n_data_cols=n_data_cols 

        n_cols=int(n_data_cols**.5)
        n_rows=0
        while n_rows*n_cols<n_data_cols:
            n_rows+=1
        
        # Create the figure and axes grid
        fig, axs = plt.subplots(nrows=n_rows, ncols=n_cols,figsize=(int(20*n_data_cols/9),12))
        
        # Flatten the axs array for easier iteration
        self.axs = axs.flatten()

    # Loop through the axes and Hist plot
    def histplots(self,bins=-1):
        # Initialize figure 
        self.figure_params()
        # Create a cycler to iterate over the DataFrame columns
        cycler = self.cycle(self.df.columns)
        for i,ax in enumerate(self.axs):
            if i==self.n_data_cols:
                ax.set_visible(False)  # Hide any extra subplots if there are more subplots than columns
                break
            col = next(cycler)  # Get the next column name
            if bins==-1:
                sns.histplot(data=self.df, x=col, ax=ax)  # Plot the histogram on the current axis
            else:
                sns.histplot(data=self.df, x=col, ax=ax,bins=bins)  # Plot the histogram on the current axis

    # Loop through the axes and Line plot
    def lineplots(self):
        # Initialize figure 
        self.figure_params()
        # Create a cycler to iterate over the DataFrame columns
        cycler = self.cycle(self.df.columns)
        for i,ax in enumerate(self.axs):
            if i==self.n_data_cols:
                ax.set_visible(False)  # Hide any extra subplots if there are more subplots than columns
                break
            col = next(cycler)  # Get the next column name
            sns.lineplot(data=self.df,x=self.df.index,y=col, ax=ax)  # Plot the Line on the current axis

    # Loop through the axes and Scatter plot
    def scatterplots(self):
        # Initialize figure 
        self.figure_params()
        # Create a cycler to iterate over the DataFrame columns
        col_combs=list(self.combinations(self.df.columns,r=2))
        for i, (ax, (xval, yval)) in enumerate(zip(self.axs, col_combs)):
            if i==self.n_data_cols:
                ax.set_visible(False)  # Hide any extra subplots if there are more subplots than columns
                break
            sns.scatterplot(data=self.df, x=xval, y=yval,ax=ax,)  # Plot the Scatter on the current axis


    plt.tight_layout()
    plt.show()