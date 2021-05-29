#!/usr/bin/env python
# coding: utf-8

# # Assignment 3 - Pandas Data Analysis Practice
# 
# *This assignment is a part of the course ["Data Analysis with Python: Zero to Pandas"](https://jovian.ml/learn/data-analysis-with-python-zero-to-pandas)*
# 
# In this assignment, you'll get to practice some of the concepts and skills covered this tutorial: https://jovian.ml/aakashns/python-pandas-data-analysis
# 
# As you go through this notebook, you will find a **???** in certain places. To complete this assignment, you must replace all the **???** with appropriate values, expressions or statements to ensure that the notebook runs properly end-to-end. 
# 
# Some things to keep in mind:
# 
# * Make sure to run all the code cells, otherwise you may get errors like `NameError` for undefined variables.
# * Do not change variable names, delete cells or disturb other existing code. It may cause problems during evaluation.
# * In some cases, you may need to add some code cells or new statements before or after the line of code containing the **???**. 
# * Since you'll be using a temporary online service for code execution, save your work by running `jovian.commit` at regular intervals.
# * Questions marked **(Optional)** will not be considered for evaluation, and can be skipped. They are for your learning.
# 
# You can make submissions on this page: https://jovian.ml/learn/data-analysis-with-python-zero-to-pandas/assignment/assignment-3-pandas-practice
# 
# If you are stuck, you can ask for help on the community forum: https://jovian.ml/forum/t/assignment-3-pandas-practice/11225/3 . You can get help with errors or ask for hints, describe your approach in simple words, link to documentation, but **please don't ask for or share the full working answer code** on the forum.
# 
# 
# ## How to run the code and save your work
# 
# The recommended way to run this notebook is to click the "Run" button at the top of this page, and select "Run on Binder". This will run the notebook on [mybinder.org](https://mybinder.org), a free online service for running Jupyter notebooks. 
# 
# Before staring the assignment, let's save a snapshot of the assignment to your Jovian.ml profile, so that you can access it later, and continue your work.

# In[3]:


import jovian


# In[4]:


jovian.commit(project='pandas-practice-assignment', environment=None)


# In[5]:


# Run the next line to install Pandas
get_ipython().system('pip install pandas --upgrade')


# In[6]:


import pandas as pd


# In this assignment, we're going to analyze an operate on data from a CSV file. Let's begin by downloading the CSV file.

# In[7]:


from urllib.request import urlretrieve

urlretrieve('https://hub.jovian.ml/wp-content/uploads/2020/09/countries.csv', 
            'countries.csv')


# Let's load the data from the CSV file into a Pandas data frame.

# In[8]:


countries_df = pd.read_csv('countries.csv')


# In[9]:


countries_df


# **Q: How many countries does the dataframe contain?**
# 
# Hint: Use the `.shape` method.

# In[10]:


num_countries = countries_df['location'].shape


# In[11]:


print('There are {} countries in the dataset'.format(num_countries))


# In[12]:


jovian.commit(project='pandas-practice-assignment', environment=None)


# **Q: Retrieve a list of continents from the dataframe?**
# 
# *Hint: Use the `.unique` method of a series.*

# In[13]:


continents = countries_df['continent'].unique


# In[14]:


continents


# In[15]:


jovian.commit(project='pandas-practice-assignment', environment=None)


# **Q: What is the total population of all the countries listed in this dataset?**

# In[16]:


total_population = countries_df['population'].sum()


# In[17]:


print('The total population is {}.'.format(int(total_population)))


# In[18]:


jovian.commit(project='pandas-practice-assignment', environment=None)


# **Q: (Optional) What is the overall life expectancy across in the world?**
# 
# *Hint: You'll need to take a weighted average of life expectancy using populations as weights.*

# In[21]:


overall= (countries_df['life_expectancy'].sum())/total_population


# In[22]:


print("overall life expectancy is {}".format(overall))


# In[23]:


jovian.commit(project='pandas-practice-assignment', environment=None)


# **Q: Create a dataframe containing 10 countries with the highest population.**
# 
# *Hint: Chain the `sort_values` and `head` methods.*

# In[26]:


most_populous_df = countries_df.sort_values('population',ascending=False).head(10)


# In[25]:


most_populous_df


# In[27]:


jovian.commit(project='pandas-practice-assignment', environment=None)


# **Q: Add a new column in `countries_df` to record the overall GDP per country (product of population & per capita GDP).**
# 
# 

# In[29]:


countries_df['gdp'] = countries_df['population']*countries_df['gdp_per_capita']


# In[30]:


countries_df


# In[31]:


jovian.commit(project='pandas-practice-assignment', environment=None)


# **Q: (Optional) Create a dataframe containing 10 countries with the lowest GDP per capita, among the counties with population greater than 100 million.**

# In[33]:


pop_100= countries_df[countries_df.population > 100000000]


# In[38]:


lowest_gdp= pop_100.sort_values('gdp_per_capita',ascending=True).head(10)


# In[39]:


lowest_gdp


# In[40]:


jovian.commit(project='pandas-practice-assignment', environment=None)


# **Q: Create a data frame that counts the number countries in each continent?**
# 
# *Hint: Use `groupby`, select the `location` column and aggregate using `count`.*

# In[41]:


country_counts_df = countries_df.groupby('location').sum()


# In[42]:


country_counts_df


# In[43]:


jovian.commit(project='pandas-practice-assignment', environment=None)


# **Q: Create a data frame showing the total population of each continent.**
# 
# *Hint: Use `groupby`, select the population column and aggregate using `sum`.*

# In[44]:


continent_populations_df = countries_df.groupby('continent').sum()


# In[45]:


continent_populations_df


# In[46]:


jovian.commit(project='pandas-practice-assignment', environment=None)


# Let's download another CSV file containing overall Covid-19 stats for various countires, and read the data into another Pandas data frame.

# In[47]:


urlretrieve('https://hub.jovian.ml/wp-content/uploads/2020/09/covid-countries-data.csv', 
            'covid-countries-data.csv')


# In[48]:


covid_data_df = pd.read_csv('covid-countries-data.csv')


# In[49]:


covid_data_df


# **Q: Count the number of countries for which the `total_tests` data is missing.**
# 
# *Hint: Use the `.isna` method.*

# In[54]:


total_tests_missing = covid_data_df.isnull().sum()


# In[56]:


print("The data for total tests is missing for {} countries.".format((total_tests_missing)))


# In[57]:


jovian.commit(project='pandas-practice-assignment', environment=None)


# Let's merge the two data frames, and compute some more metrics.
# 
# **Q: Merge `countries_df` with `covid_data_df` on the `location` column.**
# 
# *Hint: Use the `.merge` method on `countries_df`.

# In[58]:


combined_df = countries_df.merge(covid_data_df,on='location')


# In[59]:


combined_df


# In[60]:


jovian.commit(project='pandas-practice-assignment', environment=None)


# **Q: Add columns `tests_per_million`, `cases_per_million` and `deaths_per_million` into `combined_df`.**

# In[61]:


combined_df['tests_per_million'] = combined_df['total_tests'] * 1e6 / combined_df['population']


# In[63]:


combined_df['cases_per_million'] = combined_df.total_cases * 1e6 / combined_df.population


# In[64]:


combined_df['deaths_per_million'] = combined_df.total_deaths * 1e6 / combined_df.population


# In[65]:


combined_df


# In[66]:


jovian.commit(project='pandas-practice-assignment', environment=None)


# **Q: Create a dataframe with 10 countires that have highest number of tests per million people.**

# In[67]:


highest_tests_df = combined_df.sort_values('tests_per_million',ascending=False).head(10)


# In[68]:


highest_tests_df


# In[69]:


jovian.commit(project='pandas-practice-assignment', environment=None)


# **Q: Create a dataframe with 10 countires that have highest number of positive cases per million people.**

# In[71]:


highest_cases_df = combined_df.sort_values('cases_per_million',ascending=False).head(10)


# In[72]:


highest_cases_df


# In[73]:


jovian.commit(project='pandas-practice-assignment', environment=None)


# **Q: Create a dataframe with 10 countires that have highest number of deaths cases per million people?**

# In[74]:


highest_deaths_df = combined_df.sort_values('deaths_per_million',ascending=False).head(10)


# In[75]:


highest_deaths_df


# In[76]:


jovian.commit(project='pandas-practice-assignment', environment=None)


# **(Optional) Q: Count number of countries that feature in both the lists of "highest number of tests per million" and "highest number of cases per million".**

# In[91]:


merged_df = highest_tests_df.merge(highest_cases_df, on="location")


# In[85]:


merged_df


# In[ ]:





# In[86]:


jovian.commit(project='pandas-practice-assignment', environment=None)


# **(Optional) Q: Count number of countries that feature in both the lists "20 countries with lowest GDP per capita" and "20 countries with the lowest number of hospital beds per thousand population". Only consider countries with a population higher than 10 million while creating the list.**

# In[87]:


lowest_gdp= combined_df.sort_values('gdp_per_capita',ascending=False).head(20)


# In[88]:


lowest_gdp


# In[89]:


lowest_bed=combined_df.sort_values('hospital_beds_per_thousand',ascending=False).head(10)


# In[90]:


lowest_bed


# In[92]:


merged_df1 = lowest_gdp.merge(lowest_bed, on="location")


# In[93]:


merged_df1


# In[94]:


import jovian


# In[96]:


jovian.commit(project='pandas-data-analysis', environment=None)


# ## Submission 
# 
# Congratulations on making it this far! You've reached the end of this assignment, and you just completed your first real-world data analysis problem. It's time to record one final version of your notebook for submission.
# 
# Make a submission here by filling the submission form: https://jovian.ml/learn/data-analysis-with-python-zero-to-pandas/assignment/assignment-3-pandas-practice
# 
# Also make sure to help others on the forum: https://jovian.ml/forum/t/assignment-3-pandas-practice/11225/2

# In[ ]:




