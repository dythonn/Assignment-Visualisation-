

# =============================================================================
#                             Importing Modules
# =============================================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as ani

from matplotlib import cm
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

import warnings
warnings.filterwarnings('ignore')

# =============================================================================
#                      Loading and displaying the data
# =============================================================================

pd.set_option('display.width', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

df = pd.read_csv('programming_data.csv')


def data():
    """ Returns dataframe shape and dataframe """
    print ("")
    print(" Dataframe ".center(66,'*'))
    print ("")
    print (df.head(4))
    print ("")
    print(" Information about Dataframe ".center(66,'*'))
    print ("")
    print ("Data set shape = ", (df.shape))
    print (df.info())
    return data

data()

# =============================================================================
#                             Pre-processing
# =============================================================================

#                   looking for NaN values (dataframe)
print ("")
print(" Total NaN in Dataframe ".center(66,'*'))
print ("")
look_for_nan_df = df.isnull().sum().sum()
print (look_for_nan_df)

#                   looking for NaN values by columns
print ("")
print(" NaN values by columns ".center(66,'*'))
print ("")
look_for_nan_col = df.isnull().sum()
print (look_for_nan_col)



#          Kept only common languages and dropped the rest

df = df.drop(['Dart', 'Go', 'Abap', 'Ada', 'Julia', 'Objective-C', 'C#', 'Perl',
              'Lua', 'Rust', 'Kotlin', 'Haskell', 'Scala', 'Swift', 'Dart',
              'Java', 'Cobol', 'TypeScript','Matlab', 'R', 'VBA',
              'Delphi/Pascal', 'Groovy'],   axis = 1)

    
#              converting string object to Date Time object

df['Date'] = pd.to_datetime(df['Date'])


# =============================================================================
#                             Line Chart
# =============================================================================

def line_graph():
    """ Returns x and y values of the line Graph attributes """
    
    plt.figure(figsize=(11, 8))
    
    # takes x and y as inputs to the plot
    x = df['Date']
    y = df [['JavaScript', 'C/C++', 'Ruby', 'Python', 'Visual Basic']]
    
    plt.plot(df['Date'], df['JavaScript'], label='JavaScript', linewidth = 1.2)
    plt.plot(df['Date'], df['C/C++'], label='C/C++', linewidth = 1.2)
    plt.plot(df['Date'], df['Ruby'], label='Ruby', linewidth = 1.2)
    plt.plot(df['Date'], df['Python'], label='Python', linewidth = 1.2)
    plt.plot(df['Date'], df['Visual Basic'], label='Visual Basic', linewidth = 1.2)
     
    # Labels and figure settings
    plt.title('Line Chart of Popular Languages', fontsize = 18)
    plt.xlabel('Years', fontsize = 16)
    plt.ylabel('Popularity', fontsize = 16)
    plt.legend(loc="upper left", fontsize = 12)
    plt.xticks(fontsize = 13)
    plt.yticks(fontsize = 13)
    plt.tight_layout()
    
    plt.savefig('linePlotLanguages.png')
    plt.show()
    return x, y

# Returns x and y positions
x, y = line_graph()


# =============================================================================
#                             Bar Chart
# =============================================================================

javascript = df['JavaScript'].sum()
c_lang = df['C/C++'].sum()
ruby = df['Ruby'].sum()
python = df['Python'].sum()
visual_basic = df['Visual Basic'].sum()


def bar_chart():
    """ Returns lang and users of the bar plot """

    fig = plt.figure(figsize=(11, 8))
    ax = fig.add_axes([0,0,1,1])
    
    # takes langs and users as x and y positions
    langs = ['JavaScript', 'C/C++', 'Ruby', 'Python', 'Visual Basic']
    users = [javascript, c_lang, ruby, python, visual_basic]
    
    # Labels and figure settings
    plt.title('Popular languages among users', fontsize = 18)
    plt.xlabel('Languages', fontsize = 16)
    plt.ylabel('Users', fontsize = 16)
    ax.bar(langs, users, color=['skyblue', 'brown', 'grey', 'teal', 'maroon'])
    plt.xticks(fontsize = 13)
    plt.yticks(fontsize = 13)
    plt.tight_layout()
    
    plt.savefig('BarPlot_Language.png')
    plt.show()
    
    return langs, users

# Returns x and y positions
langs, users = bar_chart()


# =============================================================================
#                             Pie Chart
# =============================================================================

def pie_chart():
    """ Returns lang and users of the bar plot """   
    
    fig = plt.figure(figsize=(11, 8))
    ax = fig.add_axes([0,0,1,1])
    
    # takes in slices and labels as inputs and labels
    slices = [javascript, c_lang, ruby, python, visual_basic]
    labels = ['JavaScript', 'C/C++', 'Ruby', 'Python', 'Visual Basic']
    
    # this is use to pop out the slice i.e. Python
    explode = [0, 0, 0, 0.07, 0] 

    # autopct is for percentages & wedgeprops is for edges width or color
    plt.pie(slices, labels=labels, explode=explode, shadow=True, startangle=90,
            autopct='%1.1f%%', wedgeprops={'linewidth': 1})

    # Labels and figure settings
    plt.title('Popularity of Programming Languages')
    plt.tight_layout()
    fig.savefig('PiePlot_Popularity.png')
    plt.show()
    
    return slices, labels

# Returns x and y positions
slices, labels = pie_chart()

