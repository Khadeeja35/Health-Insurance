#Khadeeja Bibi & Rita Elmahboubi
import pandas as pd
import seaborn as sns

df = pd.read_csv("insurance.csv")

#                            2. Preliminary Steps

# a) Initial data inspection


df.head()
print(df.head())

df.shape
print(df.shape)

df.info()
print(df.info())

df.describe()
print(df.describe())

df.sum()
print(df.sum())

df.nunique()
print(df.nunique())

# b) Handle duplicate entries

df.duplicated()
print(df.duplicated())

# c) Identify and manage missing values

df.isnull()
print(df.isnull())

df = df.dropna()
print(df)

# d) Correct data types and formats




#                     3. Univariate non-graphical EDA

# a) Numerical variables (mean, median, mode, standard deviation, variance, skewness, kurtosis and quartiles (0.25, 0.5, 0.75))

print(df.describe())

# b) Categorical variables (frequency counts, proportion, mode (most frequent category and the number of unique categories).)

print(df['sex'].value_counts())
print(df['sex'].value_counts(normalize=True))
print(df['region'].value_counts())
print(df['region'].value_counts(normalize=True))
print(df['smoker'].value_counts())
print(df['smoker'].value_counts(normalize=True))
print(df.mode())

#                     4. Univariate Graphical EDA

# a) Custom and appropriate number of bins

sns.displot (data = df, x = "age", aspect = 1, bins = 5)

# b) Conditioning on other variables

sns.displot (data = df, x = "bmi", hue = "sex", aspect = 1.5)

# c) Stacked histogram

sns.histplot (data = df, x = "charges", hue = "smoker")

# d) Dodge bars

sns.displot (data = df, x = "children", aspect = 1, hue = "region", multiple = "dodge")

# e) Normalized histogram statistics

sns.displot (data = df, x = "charges", hue = "sex", stat = "density", common_norm = False, aspect = 1)

# f) Kernel density estimation

sns.displot (data = df, x = "charges", bw_adjust = 1.5, kind = "kde")

# g)  Empirical cumulative distributions

sns.displot(data = df, x = "age", hue = "sex", kind = "ecdf")


#                        5. Multivariate non-graphical EDA

# a) Make use of this approach at least 3 times with different variables from your dataset

print(pd.crosstab(df['sex'], df['smoker']))
print(pd.crosstab(df['sex'], df['region']))
print(pd.crosstab(df['smoker'], df['region']))


# b) Now use proportions or percentages rather than raw counts (use the “normalize” parameter from crosstab())

print(pd.crosstab(df['sex'], df['smoker'],normalize=True ))


# c) Generate at least one three-way frequency table (3 or more variables, by giving a list of variables to crosstab() rather than single variables)

print(pd.crosstab(index=[df['sex'], df['smoker']], columns=df['region'], normalize=True))

# Issue encountered. Had to choose which variables are rows(using index=) and which are colums( using colums=)

#                         6. Multivariate graphical EDA

# 6.1 Visualizing statistical relationships

# a) 1 plot using Faceting feature

sns.relplot (data = df, x = "age", y = "charges", kind = "line", col = "smoker", height = 5, aspect = 1.5)

# b) 1 plot representing 5 variables at once

sns.relplot (data = df, x= "age", y = "charges", kind = "scatter", hue = "region", size = "smoker", col = "sex", height = 5, aspect = 1.5)

# c) 1 plot using line instead of points

sns.relplot (data = df, x= "age", y = "charges", kind = "line", hue = "smoker", height = 5, aspect = 1.5)

# d) 1 plot illustrating standard deviation

sns.relplot (data = df, x= "bmi", y = "charges", hue = "smoker", kind = "line", errorbar = "sd", height = 5, aspect = 1.5)

# e) 1 plot including a linear regression

sns.lmplot (data = df, x= "bmi", y = "charges", hue = "smoker", height = 5, aspect = 1.5)

# 6.2 Visualizing categorical data

# a) 1 categorical scatter plot with jitter enabled

sns.catplot (data=df, x= "region", y = "charges", jitter = True)

# b) 1 categorical scatter plot with jitter disabled

sns.catplot (data = df, x= "sex",  y = "charges", jitter=False)

# c) 1 “beeswarm” plot representing 3 variables

sns.swarmplot (data=df, x = "smoker", y = "charges", hue = "sex")

# d) 1 box plot representing 3 variables

sns.boxplot (data = df, x= "region", y = "charges", hue = "smoker")

# e) 1 box plot showing the shape of the distribution (boxenplot())

sns.boxenplot (data = df, x = "smoker", y = "charges")

# f) 1 split violin plot representing 3 variables with bandwidth adjusted for better visualization

sns.violinplot (data = df, x = "sex", y = "charges", hue = "smoker", split = True, bw_adjust = 0.5)

# g) 1 violin plot with scatter points inside the violin shapes

sns.violinplot (data = df, x="smoker", y="charges", inner = "point")

# h) 1 bar plot representing 3 variables showing 97% confidence intervals 

sns.catplot(data=df, x='sex', y='age', hue='smoker', kind='bars',errorbar=('pi',97))

# i) 1 point plot representing 3 variables showing 90% confidence intervals and lines in dashed style



# j) 1 bar plot showing the number of observations in each category



# 6.3 Visualizing bivariate distributions

# a) 1 “heatmap” plot representing 2 variables with color intensity bar and adjusted bin width.



# b) 1 distribution plot with 2 variables making use of bivariate density contours with amount of curves and its lowest level adjusted (use a kernel density estimation displot()).



# c) 1 “heatmap” plot representing 3 variables, again of kind kde.

