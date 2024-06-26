#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import the necessary libraries
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.datasets import load_diabetes

# Setting SEED for reproducibility
SEED = 23

# Importing the dataset 
X, y = load_diabetes(return_X_y=True)

# Splitting dataset
train_X, test_X, train_y, test_y = train_test_split(X, y, 
													test_size = 0.25, 
													random_state = SEED)

# Instantiate Gradient Boosting Regressor
gbr = GradientBoostingRegressor(loss='absolute_error',
								learning_rate=0.1,
								n_estimators=300,
								max_depth = 1, 
								random_state = SEED,
								max_features = 5)

# Fit to training set
gbr.fit(train_X, train_y)

# Predict on test set
pred_y = gbr.predict(test_X)

# test set RMSE
test_rmse = mean_squared_error(test_y, pred_y) ** (1 / 2)

# Print rmse
print('Root mean Square error: {:.2f}'.format(test_rmse))


# In[2]:


# Import the necessary libraries
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.datasets import load_diabetes
 
# Setting SEED for reproducibility
SEED = 23
 
# Importing the dataset 
X, y = load_diabetes(return_X_y=True)
 
# Splitting dataset
train_X, test_X, train_y, test_y = train_test_split(X, y, 
                                                    test_size = 0.25, 
                                                    random_state = SEED)
 
# Instantiate Gradient Boosting Regressor
gbr = GradientBoostingRegressor(loss='absolute_error',
                                learning_rate=0.1,
                                n_estimators=300,
                                max_depth = 1, 
                                random_state = SEED,
                                max_features = 5)
 
# Fit to training set
gbr.fit(train_X, train_y)
 
# Predict on test set
pred_y = gbr.predict(test_X)
 
# test set RMSE
test_rmse = mean_squared_error(test_y, pred_y) ** (1 / 2)
 
# Print rmse
print('Root mean Square error: {:.2f}'.format(test_rmse))


# In[ ]:




