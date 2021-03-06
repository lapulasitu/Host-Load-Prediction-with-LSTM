# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 22:11:00 2016

@author: tyrion

extract machined id
"""

project_path = '/home/tyrion/lannister/clusterdata-2011-2'

from pandas import read_csv
from os import path

machine_attri_csv_colnames = ['time', 'machine_id', 'attri_name', 'attri_value', 'attri_del']
    
machine_attri_df = read_csv(path.join(project_path,'machine_attributes','part-00000-of-00001.csv.gz'),
                header=None,index_col=False,compression='gzip',names=machine_attri_csv_colnames)
machine_id_df = machine_attri_df['machine_id']
print len(machine_id_df)
machine_id_set = set(machine_id_df)
print len(machine_id_set)

import pickle

with open(path.join(project_path,'python','info','machine_id.pkl'),'wb') as f:
    pickle.dump(machine_id_set, f)