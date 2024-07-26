#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 15:36:38 2024

@author: ondul
"""
import matplotlib.pyplot as plt

month = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
customer1 = [12,13,9,8,7,8,8,7,6,5,8,10]
customer2 = [14,16,11,7,6,6,7,6,5,8,9,12]



plt.plot(month,customer1, color = 'yellow', label = 'customer1', marker = 's')
plt.plot(month,customer2, color = 'red', label = 'customer2', marker = '^')
plt.xlabel("months")
plt.ylabel("customers")
plt.title("sample for learning only", {'fontsize':12, 'horizontalalignment':'right'   })
plt.legend() #works with the label
plt.legend(loc="upper right")
plt.show() #for rendering the graph  



#subplot to divide graph ito separate lines
#customer 1 
plt.subplot(1,2,1)
plt.plot(month,customer1, color = 'yellow', label = 'customer1', marker = 's')
plt.xlabel("months")
plt.ylabel("customers")
plt.title("sample for learning only customer1", {'fontsize':12, 'horizontalalignment':'right'   })
plt.legend() #works with the label
plt.legend(loc="upper right")
plt.show() #for rendering the graph  

#customer2
plt.subplot(1,2,2)
plt.plot(month,customer2, color = 'red', label = 'customer2', marker = '^')
plt.xlabel("months")
plt.title("sample for learning only customer2", {'fontsize':12, 'horizontalalignment':'right'   })
plt.legend() #works with the label
plt.show() #for rendering the graph  





