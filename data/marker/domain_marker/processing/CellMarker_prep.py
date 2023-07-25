# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 17:59:26 2022

@author: I.Azuma
"""
#%%
import pandas as pd
import codecs
import collections
import seaborn as sns
import matplotlib.pyplot as plt
import collections

#%%
# load total data
with codecs.open("/workspace/github/GLDADec/data/marker/raw_info/CellMarker/Cell_marker_All.csv", "r", "Shift-JIS", "ignore") as file:
    total_ref = pd.read_table(file, delimiter=",")

#%% PBMC
human_ref = total_ref[total_ref["species"].isin(["Human"])] # 60877
pbmc_ref = human_ref[human_ref["tissue_type"].isin(["Peripheral blood"])] # 2731

# Monocyte
mon_ref = pbmc_ref[pbmc_ref["cell_name"].isin(["Monocyte"])]
sym_mon = mon_ref["Symbol"].dropna().unique().tolist()

# Neutrophil
neu_ref = pbmc_ref[pbmc_ref["cell_name"].isin(["Neutrophil"])]
sym_neu = neu_ref["Symbol"].dropna().unique().tolist()

# NK
nk_ref = pbmc_ref[pbmc_ref["cell_name"].isin(["Natural killer cell"])]
sym_nk = nk_ref["Symbol"].dropna().unique().tolist()

# B
b_n_ref = pbmc_ref[pbmc_ref["cell_name"].isin(["Naive B cell","Resting naive B cell"])]
b_m_ref = pbmc_ref[pbmc_ref["cell_name"].isin(["Memory B cell","Resting memory B cell"])]
sym_bn = b_n_ref["Symbol"].dropna().unique().tolist()
sym_bm = b_m_ref["Symbol"].dropna().unique().tolist()

# CD4
cd4_m_ref = pbmc_ref[pbmc_ref["cell_name"].isin(["Memory CD4+ T cell"])]
cd4_n_ref = pbmc_ref[pbmc_ref["cell_name"].isin(["Naive CD4 T cell","Naive CD4+ T cell"])]
sym_cd4n = cd4_n_ref["Symbol"].dropna().unique().tolist()
sym_cd4m = cd4_m_ref["Symbol"].dropna().unique().tolist()

# CD8
cd8_ref = pbmc_ref[pbmc_ref["cell_name"].isin(["Activated CD8+ T cell","Activated naive CD8+ T cell","Activated memory CD8+ T cell","CD8 T cell","CD8+ T cell","Memory CD8 T cell","Memory CD8+ T cell","Naive CD8 T cell","Naive CD8+ T cell"])]
sym_cd8 = cd8_ref["Symbol"].dropna().unique().tolist()

# gamma delta
gd_ref = pbmc_ref[pbmc_ref["cell_name"].isin(["Gamma delta(γδ) T cell"])]
sym_gd = gd_ref["Symbol"].dropna().unique().tolist()

# detect cell specific marker
merge_marker = sym_mon + sym_nk + sym_bn + sym_bm + sym_cd4n + sym_cd4m + sym_cd8 + sym_gd
count_dic = dict(collections.Counter(merge_marker))
sort_count = sorted(count_dic.items(),key=lambda x : x[1])
unique_marker = []
for t in sort_count:
    if t[1] == 1:
        unique_marker.append(t[0])
    else:
        pass
    
# extract specific marker
a = [sym_mon,sym_neu,sym_nk,sym_bn,sym_bm,sym_cd4n,sym_cd4m,sym_cd8,sym_gd]
b = []
for t in a:
    b.append(list(set(t) & set(unique_marker)))
k = ["Monocytes","Neutrophils","NK cells","B cells naive","B cells memory","T cells CD4 naive","T cells CD4 memory","T cells CD8","T cells gamma delta"]

# summarize the result
cellmarker_dic = dict(zip(k,a))
cellmarker_spe_dic = dict(zip(k,b))

# %%
pd.to_pickle(cellmarker_dic,'/workspace/github/GLDADec/data/marker/domain_marker/results/CellMarker_gse65133_raw_dic.pkl')
pd.to_pickle(cellmarker_spe_dic,'/workspace/github/GLDADec/data/marker/domain_marker/results/CellMarker_gse65133_specific_dic.pkl')