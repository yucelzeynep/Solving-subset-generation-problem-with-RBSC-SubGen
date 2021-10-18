# Solving subset generation problem with RBSC-SubGen

This study focuses on the \textit{subset generation} problem of computational statistics and deploys the rank-biserial correlation (RBSC) based deck generation algorithm  ``RBSC-SubGen`` [1] in solving it. ``RBSC-SubGen`` is originally designed for automatically building a desired number of vocabulary decks (out of a large corpus) with a desired level of word frequency relation, which shares many common aspects with the generic subset selection problem. 
 In this article, we consider applying it not only on word corpora but any set of ranked items and study its resilience against various hyper-parameters, which are not treated in previous studies. Namely, we test \texttt{RBSC-SubGen} under various conditions and indicate the vulnerable aspects in terms of saturation and disparity on desired RBSC. 
 
 **References**

[Yucel2020] Zeynep Yücel, Parisa Supitayakul, Akito Monden, Pattara Leelaprute, 
An algorithm for automatic collation of vocabulary decks based on word frequency
IEICE Transactions on Information and Systems, Vol.E103-D, No.08, pp. 1865-1874, Aug. 2020.
doi: 10.1587/transinf.2019EDP7279
