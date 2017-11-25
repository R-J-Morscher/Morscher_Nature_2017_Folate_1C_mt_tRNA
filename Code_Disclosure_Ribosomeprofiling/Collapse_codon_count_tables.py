# -*- coding: utf-8 -*-
"""
# Read count tables, add identifier collumn, join count tables

#Created on Thu Aug 11 11:33:58 2016

#__version__ = "0.1"
#__authors__ = "Sophia Li & Raphael J. Morscher"
#__authors_email__ = "hsinli@princeton.edu; raphael.morscher@alumni.pmu.ac.at"

"""
import os
import glob
import re

# Define path and change directory
currentPath = '/Genomics/grid/users/morscher'
os.chdir(currentPath)

# Identify codon count file for each sample in directory
ListofFiles = glob.glob('*_codon_count.txt');

with open('collapsed_codon_count_table.txt',"w") as fout:
    
    # Loop through the tabular files in  folder
    i = 0
    for f in ListofFiles:
        with open(f,"r") as fin: 
            
            # Extract sample and sequence type from file name
            sample = re.split('\_',f)[1]
            
            # For each line, add  extra value which identifies condition
            first_line = fin.readline()
            if i ==0:
                first_line = first_line.rstrip('\n') + '\t' + 'sample' + '\n'
                fout.write(first_line)
            for line in fin:
                
                l = line.strip('\n').split('\t')
                new_line = '\t'.join(l) + '\t' + sample +  '\n' 
                                
#                new_line = line[:-3] + '\t' + sample + '\t' + seq_type + '\t.\n'
                fout.write(new_line)
        i = i + 1
