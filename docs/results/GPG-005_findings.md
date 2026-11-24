# GPG-005 findings

- Rows: train 275,429, test 68,858. Base features: 96.

- **occ_pct_female** range: 0.031 - 0.904 (overall female share 0.489); correlation with target -0.128, with `female` 0.519.

- **edu_occ_interaction** correlation with target 0.412.

- VIF top features (collinearity check): 

occ_pct_female   1,000,799,917,193,443.5000
manager          1,000,799,917,193,443.5000
business         1,000,799,917,193,443.5000
scientist        1,000,799,917,193,443.5000
financialop      1,000,799,917,193,443.5000
computer         1,000,799,917,193,443.5000
architect        1,000,799,917,193,443.5000
postseceduc      1,000,799,917,193,443.5000

- LassoCV alpha=0.00025; features with near-zero coefficient: 10/98.

- RF importance rank of new features: occ_pct_female=#3, edu_occ_interaction=#1 (of 98).

- PCA / encoding comparison (5-fold CV R2 on ln_realhrwage):


         A_raw_dummies  B_pca  C_compact_encoding
mean_R2         0.4291 0.4269              0.4158
std_R2          0.0026 0.0026              0.0023


- PCA components needed for >=90% variance on the 36-column occ/industry block: k=27.

- **Best encoding by CV R2:** A_raw_dummies.

- Features dropped (near-zero in both Lasso and RF): none.

- **Final feature count:** 98.
