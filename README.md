# Solving the subset generation problem with RBSC-SubGen

We focus on the *subset generation* problem of computational statistics and deploy the rank-biserial correlation (RBSC) [Kerby2014] based deck generation algorithm ``RBSC-SubGen`` in solving it [Yucel2020]. ``RBSC-SubGen`` is originally designed for automatically building a desired number of vocabulary decks (out of a large corpus) with a desired level of word frequency relation. 

Exploiting the fact that this objective shares many common aspects with the generic subset selection problem[Hong2020], we deployed ``RBSC-SubGen`` in generating subsets out of universal sets coming from different underlying distributions and of different sizes. We also imposed varying requirements on subset size, desired ranking relation and permissible disparity. 

Our results indicate that ``RBSC-SubGen`` can be used in subset selection, provided that it is formulated as a ranking relation [Kerby2014]. In addition, ``RBSC-SubGen`` is found to be sensitive to subset size, followed by desired RBSC, permissible disparity and finally universal set size.

We consider applying ``RBSC-SubGen`` not only on word corpora but any set of ranked items and study its resilience against various hyper-parameters, which are not treated in previous studies. Namely, we test ``RBSC-SubGen`` under various conditions and indicate the vulnerable aspects in terms of saturation and disparity on desired RBSC. 
 
 **References**

[Yucel2020] Zeynep Yücel, Parisa Supitayakul, Akito Monden, Pattara Leelaprute, 
An algorithm for automatic collation of vocabulary decks based on word frequency
IEICE Transactions on Information and Systems, Vol.E103-D, No.08, pp. 1865-1874, Aug. 2020.
doi: 10.1587/transinf.2019EDP7279

[Kerby2014] Dave S. Kerby, 
The simple difference formula: An approach to teaching nonparametric correlation. 
Comprehensive Psychology, 3, 11-IT, 2014.

[Hong2020] L. Jeff Hong, Weiwei Fan, Jun Luo,
Review on ranking and selection: A new perspective. 
Frontiers of Engineering Management, 8(3), 321-343, 2021.
