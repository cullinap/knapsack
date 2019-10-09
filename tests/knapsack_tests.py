from nose.tools import *
from models.knapsack import Basic 
import pandas as pd

def test_knapsack():
	data_ = {'values': [2,3,3,4,4,5], 
         'weights': [1,2,1,3,2,3],
         'volumes': [2,1,3,2,2,3],
         'radioactive': [3,1,3,2,1,2]
        }

	df = pd.DataFrame.from_dict(data_)
	x = Basic(6,4, df)
	assert_equal(x.knap_sack(6,4,5), 8)