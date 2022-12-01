#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np#importing numpys
np.set_printoptions(suppress=True) #Creating array
coin_value=np.array([1,5,10,25,50,100]) 
alpha=0.10 
coin_obs_mean = 10.3828
coin_obs_var = 257.9547
coin_weight=np.exp(alpha*coin_value)
print(coin_weight)
print("Observed mean:",coin_obs_mean)
print("Observed variance:", coin_obs_var)


# In[4]:


def coin_weights(alpha,coin_obs_mean,coin_value,print_probs):
    exp_alhpa_x = np.exp(alpha*coin_value)
    prob_coin = exp_alhpa_x/sum(exp_alhpa_x)
    coin_mean = sum(coin_value * prob_coin)
    mean_diff = abs(coin_mean - coin_obs_mean)
    if (not print_probs):
        return mean_diff
    else :
        return prob_coin, coin_mean, mean_diff 


# In[5]:


alpha = -0.01
obj_value = coin_weights(alpha,coin_obs_mean,coin_value,True)
print("probability of coin flip:",obj_value[0])
print("Coin mean:",obj_value[1])
print("mean difference:",obj_value[2])


# In[7]:


alpha = -0.03768
obj_value = coin_weights(alpha,coin_obs_mean,coin_value,True)
diff = obj_value[2]
print("Diff between observed--estimted mean with alpha value {0} is {1}".format(alpha,diff))


# In[15]:


alpha = -0.03
obj_value = coin_weights(alpha,coin_obs_mean,coin_value,True)
diff = obj_value[2]
print("difference in observed and estimted mean of alpha value {0} is {1}".format(alpha,diff))


# In[16]:


alpha = -0.04
obj_value = coin_weights(alpha,coin_obs_mean,coin_value,True)
diff = obj_value[2]
print("difference in observed and estimted mean of alpha value {0} is {1}".format(alpha,diff))


# In[13]:


alpha = -0.036
obj_value = coin_weights(alpha,coin_obs_mean,coin_value,True)
diff = obj_value[2]
print("difference in observed and estimted mean of alpha value {0} is {1}".format(alpha,diff))


# In[57]:


alpha = -0.0376
obj_value = coin_weights(alpha,coin_obs_mean,coin_value,True)
diff = obj_value[2]
print("difference in observed and estimted mean of alpha value {0} is {1}".format(alpha,diff))


# In[61]:


alpha = -0.03768
obj_value = coin_weights(alpha,coin_obs_mean,coin_value,True)
diff = obj_value[2]
print("difference in observed and estimted mean of alpha value {0} is {1}".format(alpha,diff))


# In[62]:


#2iEstimate the optimal "alpha" value
print("optimal alpha value :",alpha)


# In[64]:


#2iiEstimating the optimal probabilities
print("optimal probabilities:",obj_value[0])


# In[65]:


#2iiidifference in your estimated coin mean and the observed coin mean
print("difference in your estimated coin mean and the observed coin mean is:", diff)


# In[1]:


# The maximum entropy probabilities would be equal to 
print(1/6)

