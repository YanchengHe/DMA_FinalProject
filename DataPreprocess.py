import pandas as pd
import numpy as np

# -- import data --
data = pd.read_csv("subscribers.csv")
data_tier = pd.read_csv('subid_tier_spend.csv')
data.head()
data.shape

# -- drop uninformative data --
data1 = data.copy()
data1 = data.drop(['num_weekly_services_utilized','num_ideal_streaming_services','language','country',
                   'months_per_bill_period','trial_end_date','next_payment','payment_type',
                   'initial_credit_card_declined','plan_type','account_creation_date','cancel_date',
                   'last_payment'],axis = 1)

##show the first 10 rows to see if the data is correct
data1.head(10)

##check columns index
data1.columns

# -- remove missing values --
data1.isnull().sum(axis = 0)
data1.dropna(axis=0,subset=['package_type','intended_use','age', 'male_TF', 'attribution_survey','join_fee'], inplace=True)
data1.drop('Unnamed: 0', axis=1, inplace=True)
print(data1.head())
print(data1.shape)

# -- process extreme data --
data1.drop(data1[data1.age > 80].index, inplace=True)
data1.drop(data1[data1.age < 15].index, inplace=True)
data1.head()
data1.shape

# -- export cleaned data to new csv --
data_cleaned = data1.copy()
data_cleaned.to_csv('subscribers_cleaned.csv', index=False)

# -- covert booleans to dummies --
data1['male_TF'] = data1['male_TF'].astype(int)
data1['current_sub_TF'] = data1['current_sub_TF'].astype(int)
data1['trial_completed'] = data1['trial_completed'].astype(int)
print(data1.head())
data1.columns

# -- covert categorical variables to dummies --
data2 = pd.get_dummies(data=data1, columns=['package_type', 'preferred_genre',
                                                    'intended_use',
                                                    'attribution_technical','attribution_survey','op_sys'])
print(data2.columns)
print(data2.shape)
data2.head()

# -- export --
data_cleaned_dummified = data2.copy()
data_cleaned_dummified = pd.merge(data_cleaned_dummified, data_tier, on='subid')
data_cleaned_dummified.to_csv('subscribers_cleaned_dummified.csv', index=False)
data1 = data2.copy()


