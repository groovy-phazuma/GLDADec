# -*- coding: utf-8 -*-
"""
Created on 2023-11-21 (Tue) 19:37:50

@author: I.Azuma
"""
# %%
import numpy as np
import pandas as pd
import seaborn as sns
import sys
sys.path.append('/workspace/github/LiverDeconv')
import liver_deconv

# %%
# up to 10
rat_df = pd.read_csv('/workspace/github/GLDADec/data/expression/rat/Morita_rat/vs_APAP/rat_dili_APAP_expression.csv',index_col=0)
ref_df = pd.read_csv('/workspace/github/LiverDeconv/Data/processed/ref_13types.csv',index_col=0)


dat = liver_deconv.LiverDeconv()
dat.set_data(df_mix=rat_df, df_all=ref_df)
dat.pre_processing(do_ann=False,ann_df=None,do_log2=True,do_quantile=False,do_trimming=False,do_drop=True)
dat.narrow_intersec()
dat.create_ref(sep="_",number=10,limit_CV=10,limit_FC=1.5,log2=False,verbose=True,do_plot=True)
deg_dic = dat.deg_dic

pd.to_pickle(deg_dic,'/workspace/github/GLDADec/data/expression/rat/marker/MouseLM13_DEGs/lm13_10_APAP.pkl')

# up to 20
rat_df = pd.read_csv('/workspace/github/GLDADec/data/expression/rat/Morita_rat/vs_APAP/rat_dili_APAP_expression.csv',index_col=0)
ref_df = pd.read_csv('/workspace/github/LiverDeconv/Data/processed/ref_13types.csv',index_col=0)


dat = liver_deconv.LiverDeconv()
dat.set_data(df_mix=rat_df, df_all=ref_df)
dat.pre_processing(do_ann=False,ann_df=None,do_log2=True,do_quantile=False,do_trimming=False,do_drop=True)
dat.narrow_intersec()
dat.create_ref(sep="_",number=20,limit_CV=10,limit_FC=1.5,log2=False,verbose=True,do_plot=True)
deg_dic = dat.deg_dic

pd.to_pickle(deg_dic,'/workspace/github/GLDADec/data/expression/rat/marker/MouseLM13_DEGs/lm13_20_APAP.pkl')