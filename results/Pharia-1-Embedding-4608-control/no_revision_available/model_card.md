---
model-index:
- name: no_model_name_available
  results:
  - dataset:
      config: en
      name: MTEB AmazonCounterfactualClassification (en)
      revision: e8379541af4e31359cca9fbcf4b00f2671dba205
      split: test
      type: mteb/amazon_counterfactual
    metrics:
    - type: accuracy
      value: 76.80597014925374
    - type: ap
      value: 40.24385686359556
    - type: ap_weighted
      value: 40.24385686359556
    - type: f1
      value: 70.85889268685499
    - type: f1_weighted
      value: 78.83700898523932
    - type: main_score
      value: 76.80597014925374
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB AmazonPolarityClassification (default)
      revision: e2d317d38cd51312af73b3d32a06d1a08b442046
      split: test
      type: mteb/amazon_polarity
    metrics:
    - type: accuracy
      value: 93.78540000000001
    - type: ap
      value: 90.86221567818902
    - type: ap_weighted
      value: 90.86221567818902
    - type: f1
      value: 93.781287546184
    - type: f1_weighted
      value: 93.781287546184
    - type: main_score
      value: 93.78540000000001
    task:
      type: Classification
  - dataset:
      config: en
      name: MTEB AmazonReviewsClassification (en)
      revision: 1399c76144fd37290681b995c656ef9b2e06e26d
      split: test
      type: mteb/amazon_reviews_multi
    metrics:
    - type: accuracy
      value: 48.647999999999996
    - type: f1
      value: 48.006836273573924
    - type: f1_weighted
      value: 48.006836273573924
    - type: main_score
      value: 48.647999999999996
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB ArguAna (default)
      revision: c22ab2a51041ffd869aaddef7af8d8215647e41a
      split: test
      type: mteb/arguana
    metrics:
    - type: main_score
      value: 51.093999999999994
    - type: map_at_1
      value: 24.751
    - type: map_at_10
      value: 41.696
    - type: map_at_100
      value: 41.696
    - type: map_at_1000
      value: 41.696
    - type: map_at_20
      value: 41.696
    - type: map_at_3
      value: 36.415
    - type: map_at_5
      value: 39.566
    - type: mrr_at_1
      value: 25.462304409672832
    - type: mrr_at_10
      value: 41.95703222019007
    - type: mrr_at_100
      value: 41.95703222019007
    - type: mrr_at_1000
      value: 41.95703222019007
    - type: mrr_at_20
      value: 41.95703222019007
    - type: mrr_at_3
      value: 36.664295874822116
    - type: mrr_at_5
      value: 39.81863442389757
    - type: nauc_map_at_1000_diff1
      value: 5.287521722084061
    - type: nauc_map_at_1000_max
      value: -18.8807502257075
    - type: nauc_map_at_1000_std
      value: 10.319971348705288
    - type: nauc_map_at_100_diff1
      value: 5.287521722084061
    - type: nauc_map_at_100_max
      value: -18.8807502257075
    - type: nauc_map_at_100_std
      value: 10.319971348705288
    - type: nauc_map_at_10_diff1
      value: 5.287521722084061
    - type: nauc_map_at_10_max
      value: -18.8807502257075
    - type: nauc_map_at_10_std
      value: 10.319971348705288
    - type: nauc_map_at_1_diff1
      value: 9.00627871559177
    - type: nauc_map_at_1_max
      value: -19.71182784333016
    - type: nauc_map_at_1_std
      value: 6.247406552449815
    - type: nauc_map_at_20_diff1
      value: 5.287521722084061
    - type: nauc_map_at_20_max
      value: -18.8807502257075
    - type: nauc_map_at_20_std
      value: 10.319971348705288
    - type: nauc_map_at_3_diff1
      value: 5.359686412527949
    - type: nauc_map_at_3_max
      value: -18.54756878028347
    - type: nauc_map_at_3_std
      value: 11.290131397919595
    - type: nauc_map_at_5_diff1
      value: 5.123086619332984
    - type: nauc_map_at_5_max
      value: -19.045395209271597
    - type: nauc_map_at_5_std
      value: 10.713267161999788
    - type: nauc_mrr_at_1000_diff1
      value: 3.3067238996968062
    - type: nauc_mrr_at_1000_max
      value: -19.9337433732939
    - type: nauc_mrr_at_1000_std
      value: 9.168551504970006
    - type: nauc_mrr_at_100_diff1
      value: 3.3067238996968062
    - type: nauc_mrr_at_100_max
      value: -19.9337433732939
    - type: nauc_mrr_at_100_std
      value: 9.168551504970006
    - type: nauc_mrr_at_10_diff1
      value: 3.3067238996968062
    - type: nauc_mrr_at_10_max
      value: -19.9337433732939
    - type: nauc_mrr_at_10_std
      value: 9.168551504970006
    - type: nauc_mrr_at_1_diff1
      value: 6.67045613630327
    - type: nauc_mrr_at_1_max
      value: -20.182884901102696
    - type: nauc_mrr_at_1_std
      value: 5.607396765799536
    - type: nauc_mrr_at_20_diff1
      value: 3.3067238996968062
    - type: nauc_mrr_at_20_max
      value: -19.9337433732939
    - type: nauc_mrr_at_20_std
      value: 9.168551504970006
    - type: nauc_mrr_at_3_diff1
      value: 3.409895883588307
    - type: nauc_mrr_at_3_max
      value: -19.788578117851216
    - type: nauc_mrr_at_3_std
      value: 10.065546067934092
    - type: nauc_mrr_at_5_diff1
      value: 3.047498354254481
    - type: nauc_mrr_at_5_max
      value: -20.20542973668601
    - type: nauc_mrr_at_5_std
      value: 9.470273325408648
    - type: nauc_ndcg_at_1000_diff1
      value: 4.437356340270406
    - type: nauc_ndcg_at_1000_max
      value: -18.857920712813804
    - type: nauc_ndcg_at_1000_std
      value: 11.275627285066623
    - type: nauc_ndcg_at_100_diff1
      value: 4.437356340270406
    - type: nauc_ndcg_at_100_max
      value: -18.857920712813804
    - type: nauc_ndcg_at_100_std
      value: 11.275627285066623
    - type: nauc_ndcg_at_10_diff1
      value: 4.437356340270406
    - type: nauc_ndcg_at_10_max
      value: -18.857920712813804
    - type: nauc_ndcg_at_10_std
      value: 11.275627285066623
    - type: nauc_ndcg_at_1_diff1
      value: 9.00627871559177
    - type: nauc_ndcg_at_1_max
      value: -19.71182784333016
    - type: nauc_ndcg_at_1_std
      value: 6.247406552449815
    - type: nauc_ndcg_at_20_diff1
      value: 4.437356340270406
    - type: nauc_ndcg_at_20_max
      value: -18.857920712813804
    - type: nauc_ndcg_at_20_std
      value: 11.275627285066623
    - type: nauc_ndcg_at_3_diff1
      value: 4.5472767749778455
    - type: nauc_ndcg_at_3_max
      value: -18.258200016929667
    - type: nauc_ndcg_at_3_std
      value: 13.047083546033122
    - type: nauc_ndcg_at_5_diff1
      value: 4.065981673435836
    - type: nauc_ndcg_at_5_max
      value: -19.163119856817726
    - type: nauc_ndcg_at_5_std
      value: 12.101145305652754
    - type: nauc_precision_at_1000_diff1
      value: 0.6538383808997599
    - type: nauc_precision_at_1000_max
      value: -18.977289895139897
    - type: nauc_precision_at_1000_std
      value: 15.36430396605875
    - type: nauc_precision_at_100_diff1
      value: 0.6538383808998183
    - type: nauc_precision_at_100_max
      value: -18.977289895139844
    - type: nauc_precision_at_100_std
      value: 15.364303966058865
    - type: nauc_precision_at_10_diff1
      value: 0.6538383808996919
    - type: nauc_precision_at_10_max
      value: -18.977289895139908
    - type: nauc_precision_at_10_std
      value: 15.364303966058843
    - type: nauc_precision_at_1_diff1
      value: 9.00627871559177
    - type: nauc_precision_at_1_max
      value: -19.71182784333016
    - type: nauc_precision_at_1_std
      value: 6.247406552449815
    - type: nauc_precision_at_20_diff1
      value: 0.6538383808996919
    - type: nauc_precision_at_20_max
      value: -18.977289895139908
    - type: nauc_precision_at_20_std
      value: 15.364303966058843
    - type: nauc_precision_at_3_diff1
      value: 2.361338023494055
    - type: nauc_precision_at_3_max
      value: -17.467286075889053
    - type: nauc_precision_at_3_std
      value: 18.034616082175134
    - type: nauc_precision_at_5_diff1
      value: 0.6630446238085804
    - type: nauc_precision_at_5_max
      value: -19.728854975002083
    - type: nauc_precision_at_5_std
      value: 16.5323114943452
    - type: nauc_recall_at_1000_diff1
      value: 0.6538383808998558
    - type: nauc_recall_at_1000_max
      value: -18.97728989513981
    - type: nauc_recall_at_1000_std
      value: 15.364303966058856
    - type: nauc_recall_at_100_diff1
      value: 0.6538383808998558
    - type: nauc_recall_at_100_max
      value: -18.97728989513981
    - type: nauc_recall_at_100_std
      value: 15.364303966058856
    - type: nauc_recall_at_10_diff1
      value: 0.6538383808998558
    - type: nauc_recall_at_10_max
      value: -18.97728989513981
    - type: nauc_recall_at_10_std
      value: 15.364303966058856
    - type: nauc_recall_at_1_diff1
      value: 9.00627871559177
    - type: nauc_recall_at_1_max
      value: -19.71182784333016
    - type: nauc_recall_at_1_std
      value: 6.247406552449815
    - type: nauc_recall_at_20_diff1
      value: 0.6538383808998558
    - type: nauc_recall_at_20_max
      value: -18.97728989513981
    - type: nauc_recall_at_20_std
      value: 15.364303966058856
    - type: nauc_recall_at_3_diff1
      value: 2.361338023494055
    - type: nauc_recall_at_3_max
      value: -17.46728607588907
    - type: nauc_recall_at_3_std
      value: 18.034616082175134
    - type: nauc_recall_at_5_diff1
      value: 0.6630446238086205
    - type: nauc_recall_at_5_max
      value: -19.728854975002076
    - type: nauc_recall_at_5_std
      value: 16.5323114943452
    - type: ndcg_at_1
      value: 24.751
    - type: ndcg_at_10
      value: 51.093999999999994
    - type: ndcg_at_100
      value: 51.093999999999994
    - type: ndcg_at_1000
      value: 51.093999999999994
    - type: ndcg_at_20
      value: 51.093999999999994
    - type: ndcg_at_3
      value: 40.351
    - type: ndcg_at_5
      value: 46.031
    - type: precision_at_1
      value: 24.751
    - type: precision_at_10
      value: 8.100999999999999
    - type: precision_at_100
      value: 0.8099999999999999
    - type: precision_at_1000
      value: 0.08099999999999999
    - type: precision_at_20
      value: 4.05
    - type: precision_at_3
      value: 17.259
    - type: precision_at_5
      value: 13.114999999999998
    - type: recall_at_1
      value: 24.751
    - type: recall_at_10
      value: 81.01
    - type: recall_at_100
      value: 81.01
    - type: recall_at_1000
      value: 81.01
    - type: recall_at_20
      value: 81.01
    - type: recall_at_3
      value: 51.778
    - type: recall_at_5
      value: 65.57600000000001
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB ArxivClusteringP2P (default)
      revision: a122ad7f3f0291bf49cc6f4d32aa80929df69d5d
      split: test
      type: mteb/arxiv-clustering-p2p
    metrics:
    - type: main_score
      value: 48.388032173937816
    - type: v_measure
      value: 48.388032173937816
    - type: v_measure_std
      value: 13.89813553018536
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB ArxivClusteringS2S (default)
      revision: f910caf1a6075f7329cdf8c1a6135696f37dbd53
      split: test
      type: mteb/arxiv-clustering-s2s
    metrics:
    - type: main_score
      value: 42.02493344504581
    - type: v_measure
      value: 42.02493344504581
    - type: v_measure_std
      value: 14.178026000180873
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB AskUbuntuDupQuestions (default)
      revision: 2000358ca161889fa9c082cb41daa8dcfb161a54
      split: test
      type: mteb/askubuntudupquestions-reranking
    metrics:
    - type: main_score
      value: 61.71076079069853
    - type: map
      value: 61.71076079069853
    - type: mrr
      value: 75.78342786791539
    - type: nAUC_map_diff1
      value: 18.34118760336641
    - type: nAUC_map_max
      value: 26.088465762514662
    - type: nAUC_map_std
      value: 16.155537748643763
    - type: nAUC_mrr_diff1
      value: 24.70331193710489
    - type: nAUC_mrr_max
      value: 37.57962564332208
    - type: nAUC_mrr_std
      value: 19.710461817989604
    task:
      type: Reranking
  - dataset:
      config: default
      name: MTEB BIOSSES (default)
      revision: d3fb88f8f02e40887cd149695127462bbcf29b4a
      split: test
      type: mteb/biosses-sts
    metrics:
    - type: cosine_pearson
      value: 87.67726128689128
    - type: cosine_spearman
      value: 84.56036050011757
    - type: euclidean_pearson
      value: 82.27656584225211
    - type: euclidean_spearman
      value: 78.99878799278262
    - type: main_score
      value: 84.56036050011757
    - type: manhattan_pearson
      value: 82.1839930424134
    - type: manhattan_spearman
      value: 78.59215222128661
    - type: pearson
      value: 87.67726128689128
    - type: spearman
      value: 84.56036050011757
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB Banking77Classification (default)
      revision: 0fd18e25b25c072e09e0d92ab615fda904d66300
      split: test
      type: mteb/banking77
    metrics:
    - type: accuracy
      value: 86.37337662337663
    - type: f1
      value: 86.29800648431724
    - type: f1_weighted
      value: 86.29800648431724
    - type: main_score
      value: 86.37337662337663
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB BiorxivClusteringP2P (default)
      revision: 65b79d1d13f80053f67aca9498d9402c2d9f1f40
      split: test
      type: mteb/biorxiv-clustering-p2p
    metrics:
    - type: main_score
      value: 40.45050398480514
    - type: v_measure
      value: 40.45050398480514
    - type: v_measure_std
      value: 1.1467728982399217
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB BiorxivClusteringS2S (default)
      revision: 258694dd0231531bc1fd9de6ceb52a0853c6d908
      split: test
      type: mteb/biorxiv-clustering-s2s
    metrics:
    - type: main_score
      value: 36.4296240228475
    - type: v_measure
      value: 36.4296240228475
    - type: v_measure_std
      value: 0.5089128728605434
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB CQADupstackAndroidRetrieval (default)
      revision: f46a197baaae43b4f621051089b82a364682dfeb
      split: test
      type: mteb/cqadupstack-android
    metrics:
    - type: main_score
      value: 47.926
    - type: map_at_1
      value: 28.347
    - type: map_at_10
      value: 41.004000000000005
    - type: map_at_100
      value: 41.004000000000005
    - type: map_at_1000
      value: 41.004000000000005
    - type: map_at_20
      value: 41.004000000000005
    - type: map_at_3
      value: 37.089
    - type: map_at_5
      value: 39.106
    - type: mrr_at_1
      value: 34.763948497854074
    - type: mrr_at_10
      value: 46.32502214047277
    - type: mrr_at_100
      value: 46.32502214047277
    - type: mrr_at_1000
      value: 46.32502214047277
    - type: mrr_at_20
      value: 46.32502214047277
    - type: mrr_at_3
      value: 43.80066762041011
    - type: mrr_at_5
      value: 45.159752026704815
    - type: nauc_map_at_1000_diff1
      value: 45.307496589180666
    - type: nauc_map_at_1000_max
      value: 28.811250276183575
    - type: nauc_map_at_1000_std
      value: 56.64832755376863
    - type: nauc_map_at_100_diff1
      value: 45.307496589180666
    - type: nauc_map_at_100_max
      value: 28.811250276183575
    - type: nauc_map_at_100_std
      value: 56.64832755376863
    - type: nauc_map_at_10_diff1
      value: 45.307496589180666
    - type: nauc_map_at_10_max
      value: 28.811250276183575
    - type: nauc_map_at_10_std
      value: 56.64832755376863
    - type: nauc_map_at_1_diff1
      value: 48.8045429929244
    - type: nauc_map_at_1_max
      value: 23.889133144709312
    - type: nauc_map_at_1_std
      value: 52.44184874983103
    - type: nauc_map_at_20_diff1
      value: 45.307496589180666
    - type: nauc_map_at_20_max
      value: 28.811250276183575
    - type: nauc_map_at_20_std
      value: 56.64832755376863
    - type: nauc_map_at_3_diff1
      value: 45.74271847768184
    - type: nauc_map_at_3_max
      value: 27.016473219047004
    - type: nauc_map_at_3_std
      value: 55.97752934230137
    - type: nauc_map_at_5_diff1
      value: 44.95916434291984
    - type: nauc_map_at_5_max
      value: 27.565282879956403
    - type: nauc_map_at_5_std
      value: 56.388460693308865
    - type: nauc_mrr_at_1000_diff1
      value: 45.07114585822204
    - type: nauc_mrr_at_1000_max
      value: 30.900601369900237
    - type: nauc_mrr_at_1000_std
      value: 56.845558030490515
    - type: nauc_mrr_at_100_diff1
      value: 45.07114585822204
    - type: nauc_mrr_at_100_max
      value: 30.900601369900237
    - type: nauc_mrr_at_100_std
      value: 56.845558030490515
    - type: nauc_mrr_at_10_diff1
      value: 45.07114585822204
    - type: nauc_mrr_at_10_max
      value: 30.900601369900237
    - type: nauc_mrr_at_10_std
      value: 56.845558030490515
    - type: nauc_mrr_at_1_diff1
      value: 49.00879820342306
    - type: nauc_mrr_at_1_max
      value: 29.10494357396966
    - type: nauc_mrr_at_1_std
      value: 56.17937540756398
    - type: nauc_mrr_at_20_diff1
      value: 45.07114585822204
    - type: nauc_mrr_at_20_max
      value: 30.900601369900237
    - type: nauc_mrr_at_20_std
      value: 56.845558030490515
    - type: nauc_mrr_at_3_diff1
      value: 45.337695780478874
    - type: nauc_mrr_at_3_max
      value: 30.487173553281426
    - type: nauc_mrr_at_3_std
      value: 57.74079320896689
    - type: nauc_mrr_at_5_diff1
      value: 44.755697336104674
    - type: nauc_mrr_at_5_max
      value: 30.513055241951164
    - type: nauc_mrr_at_5_std
      value: 56.761905571142314
    - type: nauc_ndcg_at_1000_diff1
      value: 43.498227346267
    - type: nauc_ndcg_at_1000_max
      value: 30.376201490105153
    - type: nauc_ndcg_at_1000_std
      value: 56.49345159819683
    - type: nauc_ndcg_at_100_diff1
      value: 43.50123222070514
    - type: nauc_ndcg_at_100_max
      value: 30.370144044142055
    - type: nauc_ndcg_at_100_std
      value: 56.49312567382997
    - type: nauc_ndcg_at_10_diff1
      value: 43.74041351455868
    - type: nauc_ndcg_at_10_max
      value: 30.829864536338135
    - type: nauc_ndcg_at_10_std
      value: 56.59665106631016
    - type: nauc_ndcg_at_1_diff1
      value: 49.00879820342306
    - type: nauc_ndcg_at_1_max
      value: 29.10494357396966
    - type: nauc_ndcg_at_1_std
      value: 56.17937540756398
    - type: nauc_ndcg_at_20_diff1
      value: 43.56717164407831
    - type: nauc_ndcg_at_20_max
      value: 30.399589794731597
    - type: nauc_ndcg_at_20_std
      value: 56.49561640414091
    - type: nauc_ndcg_at_3_diff1
      value: 44.96216189786845
    - type: nauc_ndcg_at_3_max
      value: 29.745154636517235
    - type: nauc_ndcg_at_3_std
      value: 57.4250325398855
    - type: nauc_ndcg_at_5_diff1
      value: 43.40837653865346
    - type: nauc_ndcg_at_5_max
      value: 29.290175497018094
    - type: nauc_ndcg_at_5_std
      value: 56.65245585606393
    - type: nauc_precision_at_1000_diff1
      value: 16.2195041096972
    - type: nauc_precision_at_1000_max
      value: 26.59910382439098
    - type: nauc_precision_at_1000_std
      value: 28.35133298212075
    - type: nauc_precision_at_100_diff1
      value: 16.219504109697162
    - type: nauc_precision_at_100_max
      value: 26.59910382439096
    - type: nauc_precision_at_100_std
      value: 28.351332982120724
    - type: nauc_precision_at_10_diff1
      value: 16.219504109697162
    - type: nauc_precision_at_10_max
      value: 26.59910382439096
    - type: nauc_precision_at_10_std
      value: 28.351332982120738
    - type: nauc_precision_at_1_diff1
      value: 49.00879820342306
    - type: nauc_precision_at_1_max
      value: 29.10494357396966
    - type: nauc_precision_at_1_std
      value: 56.17937540756398
    - type: nauc_precision_at_20_diff1
      value: 16.219504109697162
    - type: nauc_precision_at_20_max
      value: 26.59910382439096
    - type: nauc_precision_at_20_std
      value: 28.351332982120738
    - type: nauc_precision_at_3_diff1
      value: 33.93313550718347
    - type: nauc_precision_at_3_max
      value: 31.284686596733547
    - type: nauc_precision_at_3_std
      value: 51.11456336583655
    - type: nauc_precision_at_5_diff1
      value: 23.63160290597576
    - type: nauc_precision_at_5_max
      value: 28.3764222451566
    - type: nauc_precision_at_5_std
      value: 41.20948905007788
    - type: nauc_recall_at_1000_diff1
      value: 34.78840999412229
    - type: nauc_recall_at_1000_max
      value: 30.15047702525799
    - type: nauc_recall_at_1000_std
      value: 51.23656938577233
    - type: nauc_recall_at_100_diff1
      value: 34.78840999412229
    - type: nauc_recall_at_100_max
      value: 30.15047702525799
    - type: nauc_recall_at_100_std
      value: 51.23656938577233
    - type: nauc_recall_at_10_diff1
      value: 34.78840999412229
    - type: nauc_recall_at_10_max
      value: 30.15047702525799
    - type: nauc_recall_at_10_std
      value: 51.23656938577233
    - type: nauc_recall_at_1_diff1
      value: 48.8045429929244
    - type: nauc_recall_at_1_max
      value: 23.889133144709312
    - type: nauc_recall_at_1_std
      value: 52.44184874983103
    - type: nauc_recall_at_20_diff1
      value: 34.78840999412229
    - type: nauc_recall_at_20_max
      value: 30.15047702525799
    - type: nauc_recall_at_20_std
      value: 51.23656938577233
    - type: nauc_recall_at_3_diff1
      value: 38.908566333502186
    - type: nauc_recall_at_3_max
      value: 25.798049597928713
    - type: nauc_recall_at_3_std
      value: 54.12421733066435
    - type: nauc_recall_at_5_diff1
      value: 35.902170720645074
    - type: nauc_recall_at_5_max
      value: 25.7399296845002
    - type: nauc_recall_at_5_std
      value: 52.325349885923444
    - type: ndcg_at_1
      value: 34.764
    - type: ndcg_at_10
      value: 47.926
    - type: ndcg_at_100
      value: 47.632000000000005
    - type: ndcg_at_1000
      value: 47.629
    - type: ndcg_at_20
      value: 47.692
    - type: ndcg_at_3
      value: 42.321999999999996
    - type: ndcg_at_5
      value: 44.574000000000005
    - type: precision_at_1
      value: 34.764
    - type: precision_at_10
      value: 9.886000000000001
    - type: precision_at_100
      value: 0.989
    - type: precision_at_1000
      value: 0.099
    - type: precision_at_20
      value: 4.9430000000000005
    - type: precision_at_3
      value: 21.221
    - type: precision_at_5
      value: 15.479000000000001
    - type: recall_at_1
      value: 28.347
    - type: recall_at_10
      value: 61.516999999999996
    - type: recall_at_100
      value: 61.516999999999996
    - type: recall_at_1000
      value: 61.516999999999996
    - type: recall_at_20
      value: 61.516999999999996
    - type: recall_at_3
      value: 45.521
    - type: recall_at_5
      value: 51.715
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackEnglishRetrieval (default)
      revision: ad9991cb51e31e31e430383c75ffb2885547b5f0
      split: test
      type: mteb/cqadupstack-english
    metrics:
    - type: main_score
      value: 46.577
    - type: map_at_1
      value: 30.569000000000003
    - type: map_at_10
      value: 40.892
    - type: map_at_100
      value: 40.892
    - type: map_at_1000
      value: 40.892
    - type: map_at_20
      value: 40.892
    - type: map_at_3
      value: 37.675
    - type: map_at_5
      value: 39.457
    - type: mrr_at_1
      value: 39.04458598726115
    - type: mrr_at_10
      value: 46.861768274188684
    - type: mrr_at_100
      value: 46.861768274188684
    - type: mrr_at_1000
      value: 46.861768274188684
    - type: mrr_at_20
      value: 46.861768274188684
    - type: mrr_at_3
      value: 44.723991507431016
    - type: mrr_at_5
      value: 45.95329087048835
    - type: nauc_map_at_1000_diff1
      value: 51.59325087594866
    - type: nauc_map_at_1000_max
      value: 40.01714338030341
    - type: nauc_map_at_1000_std
      value: 66.39378358753018
    - type: nauc_map_at_100_diff1
      value: 51.59325087594866
    - type: nauc_map_at_100_max
      value: 40.01714338030341
    - type: nauc_map_at_100_std
      value: 66.39378358753018
    - type: nauc_map_at_10_diff1
      value: 51.59325087594866
    - type: nauc_map_at_10_max
      value: 40.01714338030341
    - type: nauc_map_at_10_std
      value: 66.39378358753018
    - type: nauc_map_at_1_diff1
      value: 54.95614889469027
    - type: nauc_map_at_1_max
      value: 33.02062971532801
    - type: nauc_map_at_1_std
      value: 58.20910329512018
    - type: nauc_map_at_20_diff1
      value: 51.59325087594866
    - type: nauc_map_at_20_max
      value: 40.01714338030341
    - type: nauc_map_at_20_std
      value: 66.39378358753018
    - type: nauc_map_at_3_diff1
      value: 52.38126823709418
    - type: nauc_map_at_3_max
      value: 38.239259273525846
    - type: nauc_map_at_3_std
      value: 65.28848305873221
    - type: nauc_map_at_5_diff1
      value: 51.72231687350387
    - type: nauc_map_at_5_max
      value: 39.500297147320865
    - type: nauc_map_at_5_std
      value: 66.2427354706394
    - type: nauc_mrr_at_1000_diff1
      value: 48.7314178264995
    - type: nauc_mrr_at_1000_max
      value: 43.56207621807911
    - type: nauc_mrr_at_1000_std
      value: 63.501736442641764
    - type: nauc_mrr_at_100_diff1
      value: 48.7314178264995
    - type: nauc_mrr_at_100_max
      value: 43.56207621807911
    - type: nauc_mrr_at_100_std
      value: 63.501736442641764
    - type: nauc_mrr_at_10_diff1
      value: 48.7314178264995
    - type: nauc_mrr_at_10_max
      value: 43.56207621807911
    - type: nauc_mrr_at_10_std
      value: 63.501736442641764
    - type: nauc_mrr_at_1_diff1
      value: 51.497235334671544
    - type: nauc_mrr_at_1_max
      value: 42.512670181562704
    - type: nauc_mrr_at_1_std
      value: 60.99182008301
    - type: nauc_mrr_at_20_diff1
      value: 48.7314178264995
    - type: nauc_mrr_at_20_max
      value: 43.56207621807911
    - type: nauc_mrr_at_20_std
      value: 63.501736442641764
    - type: nauc_mrr_at_3_diff1
      value: 49.006326021524416
    - type: nauc_mrr_at_3_max
      value: 44.019771950656114
    - type: nauc_mrr_at_3_std
      value: 63.644988819916136
    - type: nauc_mrr_at_5_diff1
      value: 48.5852036620964
    - type: nauc_mrr_at_5_max
      value: 43.69630569147122
    - type: nauc_mrr_at_5_std
      value: 63.45667906843618
    - type: nauc_ndcg_at_1000_diff1
      value: 50.01928177638235
    - type: nauc_ndcg_at_1000_max
      value: 41.1783132311158
    - type: nauc_ndcg_at_1000_std
      value: 66.83503256486011
    - type: nauc_ndcg_at_100_diff1
      value: 50.01928177638235
    - type: nauc_ndcg_at_100_max
      value: 41.1783132311158
    - type: nauc_ndcg_at_100_std
      value: 66.83503256486011
    - type: nauc_ndcg_at_10_diff1
      value: 49.76914444330484
    - type: nauc_ndcg_at_10_max
      value: 42.12507108429919
    - type: nauc_ndcg_at_10_std
      value: 66.4516103913136
    - type: nauc_ndcg_at_1_diff1
      value: 51.497235334671544
    - type: nauc_ndcg_at_1_max
      value: 42.512670181562704
    - type: nauc_ndcg_at_1_std
      value: 60.99182008301
    - type: nauc_ndcg_at_20_diff1
      value: 49.95918005677622
    - type: nauc_ndcg_at_20_max
      value: 41.52729257412745
    - type: nauc_ndcg_at_20_std
      value: 66.72869797733141
    - type: nauc_ndcg_at_3_diff1
      value: 49.94907841842356
    - type: nauc_ndcg_at_3_max
      value: 42.510842012830004
    - type: nauc_ndcg_at_3_std
      value: 65.48198009263466
    - type: nauc_ndcg_at_5_diff1
      value: 49.64110644163196
    - type: nauc_ndcg_at_5_max
      value: 42.449748864801705
    - type: nauc_ndcg_at_5_std
      value: 66.15748173722798
    - type: nauc_precision_at_1000_diff1
      value: 14.454986382608478
    - type: nauc_precision_at_1000_max
      value: 39.15828643647158
    - type: nauc_precision_at_1000_std
      value: 35.51446029268021
    - type: nauc_precision_at_100_diff1
      value: 14.454986382608498
    - type: nauc_precision_at_100_max
      value: 39.15828643647165
    - type: nauc_precision_at_100_std
      value: 35.51446029268022
    - type: nauc_precision_at_10_diff1
      value: 14.454986382608487
    - type: nauc_precision_at_10_max
      value: 39.158286436471656
    - type: nauc_precision_at_10_std
      value: 35.514460292680226
    - type: nauc_precision_at_1_diff1
      value: 51.497235334671544
    - type: nauc_precision_at_1_max
      value: 42.512670181562704
    - type: nauc_precision_at_1_std
      value: 60.99182008301
    - type: nauc_precision_at_20_diff1
      value: 14.454986382608487
    - type: nauc_precision_at_20_max
      value: 39.158286436471656
    - type: nauc_precision_at_20_std
      value: 35.514460292680226
    - type: nauc_precision_at_3_diff1
      value: 31.777694517874178
    - type: nauc_precision_at_3_max
      value: 45.09330080424064
    - type: nauc_precision_at_3_std
      value: 56.17214709908195
    - type: nauc_precision_at_5_diff1
      value: 22.819311458577378
    - type: nauc_precision_at_5_max
      value: 43.45870695370017
    - type: nauc_precision_at_5_std
      value: 48.038200242240606
    - type: nauc_recall_at_1000_diff1
      value: 45.549682529359295
    - type: nauc_recall_at_1000_max
      value: 38.497937186942835
    - type: nauc_recall_at_1000_std
      value: 66.36204096399673
    - type: nauc_recall_at_100_diff1
      value: 45.549682529359295
    - type: nauc_recall_at_100_max
      value: 38.497937186942835
    - type: nauc_recall_at_100_std
      value: 66.36204096399673
    - type: nauc_recall_at_10_diff1
      value: 45.549682529359295
    - type: nauc_recall_at_10_max
      value: 38.497937186942835
    - type: nauc_recall_at_10_std
      value: 66.36204096399673
    - type: nauc_recall_at_1_diff1
      value: 54.95614889469027
    - type: nauc_recall_at_1_max
      value: 33.02062971532801
    - type: nauc_recall_at_1_std
      value: 58.20910329512018
    - type: nauc_recall_at_20_diff1
      value: 45.549682529359295
    - type: nauc_recall_at_20_max
      value: 38.497937186942835
    - type: nauc_recall_at_20_std
      value: 66.36204096399673
    - type: nauc_recall_at_3_diff1
      value: 48.356646729516164
    - type: nauc_recall_at_3_max
      value: 38.27146468151798
    - type: nauc_recall_at_3_std
      value: 66.34203053195698
    - type: nauc_recall_at_5_diff1
      value: 46.02009210246526
    - type: nauc_recall_at_5_max
      value: 38.731658821447944
    - type: nauc_recall_at_5_std
      value: 66.71238188849223
    - type: ndcg_at_1
      value: 39.045
    - type: ndcg_at_10
      value: 46.577
    - type: ndcg_at_100
      value: 46.188
    - type: ndcg_at_1000
      value: 46.188
    - type: ndcg_at_20
      value: 46.312999999999995
    - type: ndcg_at_3
      value: 42.278999999999996
    - type: ndcg_at_5
      value: 44.192
    - type: precision_at_1
      value: 39.045
    - type: precision_at_10
      value: 8.911
    - type: precision_at_100
      value: 0.8909999999999999
    - type: precision_at_1000
      value: 0.089
    - type: precision_at_20
      value: 4.455
    - type: precision_at_3
      value: 20.616
    - type: precision_at_5
      value: 14.624
    - type: recall_at_1
      value: 30.569000000000003
    - type: recall_at_10
      value: 56.425000000000004
    - type: recall_at_100
      value: 56.425000000000004
    - type: recall_at_1000
      value: 56.425000000000004
    - type: recall_at_20
      value: 56.425000000000004
    - type: recall_at_3
      value: 43.436
    - type: recall_at_5
      value: 48.961
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackGamingRetrieval (default)
      revision: 4885aa143210c98657558c04aaf3dc47cfb54340
      split: test
      type: mteb/cqadupstack-gaming
    metrics:
    - type: main_score
      value: 50.303
    - type: map_at_1
      value: 32.34
    - type: map_at_10
      value: 44.021
    - type: map_at_100
      value: 44.021
    - type: map_at_1000
      value: 44.021
    - type: map_at_20
      value: 44.021
    - type: map_at_3
      value: 40.386
    - type: map_at_5
      value: 42.445
    - type: mrr_at_1
      value: 37.4294670846395
    - type: mrr_at_10
      value: 47.52781509678069
    - type: mrr_at_100
      value: 47.52781509678069
    - type: mrr_at_1000
      value: 47.52781509678069
    - type: mrr_at_20
      value: 47.52781509678069
    - type: mrr_at_3
      value: 44.6603970741902
    - type: mrr_at_5
      value: 46.34378265412756
    - type: nauc_map_at_1000_diff1
      value: 43.71878632944867
    - type: nauc_map_at_1000_max
      value: 33.45354025441653
    - type: nauc_map_at_1000_std
      value: 52.31486917336369
    - type: nauc_map_at_100_diff1
      value: 43.71878632944867
    - type: nauc_map_at_100_max
      value: 33.45354025441653
    - type: nauc_map_at_100_std
      value: 52.31486917336369
    - type: nauc_map_at_10_diff1
      value: 43.71878632944867
    - type: nauc_map_at_10_max
      value: 33.45354025441653
    - type: nauc_map_at_10_std
      value: 52.31486917336369
    - type: nauc_map_at_1_diff1
      value: 49.01455882973119
    - type: nauc_map_at_1_max
      value: 29.569061362270197
    - type: nauc_map_at_1_std
      value: 45.629979279180866
    - type: nauc_map_at_20_diff1
      value: 43.71878632944867
    - type: nauc_map_at_20_max
      value: 33.45354025441653
    - type: nauc_map_at_20_std
      value: 52.31486917336369
    - type: nauc_map_at_3_diff1
      value: 44.66471221323296
    - type: nauc_map_at_3_max
      value: 33.35342401529258
    - type: nauc_map_at_3_std
      value: 51.65733942767628
    - type: nauc_map_at_5_diff1
      value: 43.98259392061898
    - type: nauc_map_at_5_max
      value: 33.34563110247236
    - type: nauc_map_at_5_std
      value: 52.03378884479179
    - type: nauc_mrr_at_1000_diff1
      value: 43.231589705585044
    - type: nauc_mrr_at_1000_max
      value: 34.67506659386198
    - type: nauc_mrr_at_1000_std
      value: 51.909259670002086
    - type: nauc_mrr_at_100_diff1
      value: 43.231589705585044
    - type: nauc_mrr_at_100_max
      value: 34.67506659386198
    - type: nauc_mrr_at_100_std
      value: 51.909259670002086
    - type: nauc_mrr_at_10_diff1
      value: 43.231589705585044
    - type: nauc_mrr_at_10_max
      value: 34.67506659386198
    - type: nauc_mrr_at_10_std
      value: 51.909259670002086
    - type: nauc_mrr_at_1_diff1
      value: 47.93926347678726
    - type: nauc_mrr_at_1_max
      value: 33.91822092308767
    - type: nauc_mrr_at_1_std
      value: 49.29494308637904
    - type: nauc_mrr_at_20_diff1
      value: 43.231589705585044
    - type: nauc_mrr_at_20_max
      value: 34.67506659386198
    - type: nauc_mrr_at_20_std
      value: 51.909259670002086
    - type: nauc_mrr_at_3_diff1
      value: 43.962879911381314
    - type: nauc_mrr_at_3_max
      value: 35.375735148482555
    - type: nauc_mrr_at_3_std
      value: 52.33398617233791
    - type: nauc_mrr_at_5_diff1
      value: 43.265910118483184
    - type: nauc_mrr_at_5_max
      value: 34.8169303538183
    - type: nauc_mrr_at_5_std
      value: 51.84739125873769
    - type: nauc_ndcg_at_1000_diff1
      value: 41.65818872363347
    - type: nauc_ndcg_at_1000_max
      value: 33.87302015789601
    - type: nauc_ndcg_at_1000_std
      value: 53.393009927267464
    - type: nauc_ndcg_at_100_diff1
      value: 41.65818872363347
    - type: nauc_ndcg_at_100_max
      value: 33.87302015789601
    - type: nauc_ndcg_at_100_std
      value: 53.393009927267464
    - type: nauc_ndcg_at_10_diff1
      value: 41.619230940482055
    - type: nauc_ndcg_at_10_max
      value: 33.95868499330838
    - type: nauc_ndcg_at_10_std
      value: 53.3758711319078
    - type: nauc_ndcg_at_1_diff1
      value: 47.93926347678726
    - type: nauc_ndcg_at_1_max
      value: 33.91822092308767
    - type: nauc_ndcg_at_1_std
      value: 49.29494308637904
    - type: nauc_ndcg_at_20_diff1
      value: 41.65529584552956
    - type: nauc_ndcg_at_20_max
      value: 33.87192889353174
    - type: nauc_ndcg_at_20_std
      value: 53.392586798006825
    - type: nauc_ndcg_at_3_diff1
      value: 43.3438175004258
    - type: nauc_ndcg_at_3_max
      value: 34.56789066347093
    - type: nauc_ndcg_at_3_std
      value: 52.960931341164205
    - type: nauc_ndcg_at_5_diff1
      value: 42.15860604409089
    - type: nauc_ndcg_at_5_max
      value: 34.05226069100548
    - type: nauc_ndcg_at_5_std
      value: 52.984800162217326
    - type: nauc_precision_at_1000_diff1
      value: 14.545684497754783
    - type: nauc_precision_at_1000_max
      value: 27.530032579516483
    - type: nauc_precision_at_1000_std
      value: 36.88798348122979
    - type: nauc_precision_at_100_diff1
      value: 14.545684497754847
    - type: nauc_precision_at_100_max
      value: 27.530032579516522
    - type: nauc_precision_at_100_std
      value: 36.88798348122987
    - type: nauc_precision_at_10_diff1
      value: 14.545684497754795
    - type: nauc_precision_at_10_max
      value: 27.530032579516515
    - type: nauc_precision_at_10_std
      value: 36.88798348122984
    - type: nauc_precision_at_1_diff1
      value: 47.93926347678726
    - type: nauc_precision_at_1_max
      value: 33.91822092308767
    - type: nauc_precision_at_1_std
      value: 49.29494308637904
    - type: nauc_precision_at_20_diff1
      value: 14.545684497754795
    - type: nauc_precision_at_20_max
      value: 27.530032579516515
    - type: nauc_precision_at_20_std
      value: 36.88798348122984
    - type: nauc_precision_at_3_diff1
      value: 31.191721828964887
    - type: nauc_precision_at_3_max
      value: 37.148877919887155
    - type: nauc_precision_at_3_std
      value: 52.30854726313182
    - type: nauc_precision_at_5_diff1
      value: 23.490842213279556
    - type: nauc_precision_at_5_max
      value: 32.75565950262029
    - type: nauc_precision_at_5_std
      value: 45.78849026434844
    - type: nauc_recall_at_1000_diff1
      value: 32.94644407115746
    - type: nauc_recall_at_1000_max
      value: 31.5431828063933
    - type: nauc_recall_at_1000_std
      value: 54.64210632020876
    - type: nauc_recall_at_100_diff1
      value: 32.94644407115746
    - type: nauc_recall_at_100_max
      value: 31.5431828063933
    - type: nauc_recall_at_100_std
      value: 54.64210632020876
    - type: nauc_recall_at_10_diff1
      value: 32.94644407115746
    - type: nauc_recall_at_10_max
      value: 31.5431828063933
    - type: nauc_recall_at_10_std
      value: 54.64210632020876
    - type: nauc_recall_at_1_diff1
      value: 49.01455882973119
    - type: nauc_recall_at_1_max
      value: 29.569061362270197
    - type: nauc_recall_at_1_std
      value: 45.629979279180866
    - type: nauc_recall_at_20_diff1
      value: 32.94644407115746
    - type: nauc_recall_at_20_max
      value: 31.5431828063933
    - type: nauc_recall_at_20_std
      value: 54.64210632020876
    - type: nauc_recall_at_3_diff1
      value: 39.29734520238664
    - type: nauc_recall_at_3_max
      value: 33.68907532668754
    - type: nauc_recall_at_3_std
      value: 53.94935431029162
    - type: nauc_recall_at_5_diff1
      value: 35.71787436446087
    - type: nauc_recall_at_5_max
      value: 32.221491201897244
    - type: nauc_recall_at_5_std
      value: 53.49262034742359
    - type: ndcg_at_1
      value: 37.429
    - type: ndcg_at_10
      value: 50.303
    - type: ndcg_at_100
      value: 50.236999999999995
    - type: ndcg_at_1000
      value: 50.236999999999995
    - type: ndcg_at_20
      value: 50.239
    - type: ndcg_at_3
      value: 43.9
    - type: ndcg_at_5
      value: 47.053
    - type: precision_at_1
      value: 37.429
    - type: precision_at_10
      value: 8.502
    - type: precision_at_100
      value: 0.8500000000000001
    - type: precision_at_1000
      value: 0.08499999999999999
    - type: precision_at_20
      value: 4.251
    - type: precision_at_3
      value: 19.916
    - type: precision_at_5
      value: 14.194
    - type: recall_at_1
      value: 32.34
    - type: recall_at_10
      value: 65.664
    - type: recall_at_100
      value: 65.664
    - type: recall_at_1000
      value: 65.664
    - type: recall_at_20
      value: 65.664
    - type: recall_at_3
      value: 48.39
    - type: recall_at_5
      value: 56.103
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackGisRetrieval (default)
      revision: 5003b3064772da1887988e05400cf3806fe491f2
      split: test
      type: mteb/cqadupstack-gis
    metrics:
    - type: main_score
      value: 34.985
    - type: map_at_1
      value: 20.455000000000002
    - type: map_at_10
      value: 29.580000000000002
    - type: map_at_100
      value: 29.580000000000002
    - type: map_at_1000
      value: 29.580000000000002
    - type: map_at_20
      value: 29.580000000000002
    - type: map_at_3
      value: 26.545999999999996
    - type: map_at_5
      value: 28.22
    - type: mrr_at_1
      value: 22.48587570621469
    - type: mrr_at_10
      value: 31.69424266881894
    - type: mrr_at_100
      value: 31.69424266881894
    - type: mrr_at_1000
      value: 31.69424266881894
    - type: mrr_at_20
      value: 31.69424266881894
    - type: mrr_at_3
      value: 28.870056497175174
    - type: mrr_at_5
      value: 30.412429378531087
    - type: nauc_map_at_1000_diff1
      value: 33.24550173717404
    - type: nauc_map_at_1000_max
      value: 15.969981584019955
    - type: nauc_map_at_1000_std
      value: 40.70029359884254
    - type: nauc_map_at_100_diff1
      value: 33.24550173717404
    - type: nauc_map_at_100_max
      value: 15.969981584019955
    - type: nauc_map_at_100_std
      value: 40.70029359884254
    - type: nauc_map_at_10_diff1
      value: 33.24550173717404
    - type: nauc_map_at_10_max
      value: 15.969981584019955
    - type: nauc_map_at_10_std
      value: 40.70029359884254
    - type: nauc_map_at_1_diff1
      value: 38.670851513282415
    - type: nauc_map_at_1_max
      value: 16.75377301174682
    - type: nauc_map_at_1_std
      value: 40.6311885488597
    - type: nauc_map_at_20_diff1
      value: 33.24550173717404
    - type: nauc_map_at_20_max
      value: 15.969981584019955
    - type: nauc_map_at_20_std
      value: 40.70029359884254
    - type: nauc_map_at_3_diff1
      value: 34.390917624561126
    - type: nauc_map_at_3_max
      value: 15.388164110564848
    - type: nauc_map_at_3_std
      value: 40.32590995910493
    - type: nauc_map_at_5_diff1
      value: 33.99563383687065
    - type: nauc_map_at_5_max
      value: 15.456586125803723
    - type: nauc_map_at_5_std
      value: 40.79258151539866
    - type: nauc_mrr_at_1000_diff1
      value: 31.67689594961523
    - type: nauc_mrr_at_1000_max
      value: 16.68974038291927
    - type: nauc_mrr_at_1000_std
      value: 40.26184065004142
    - type: nauc_mrr_at_100_diff1
      value: 31.67689594961523
    - type: nauc_mrr_at_100_max
      value: 16.68974038291927
    - type: nauc_mrr_at_100_std
      value: 40.26184065004142
    - type: nauc_mrr_at_10_diff1
      value: 31.67689594961523
    - type: nauc_mrr_at_10_max
      value: 16.68974038291927
    - type: nauc_mrr_at_10_std
      value: 40.26184065004142
    - type: nauc_mrr_at_1_diff1
      value: 37.23119529469353
    - type: nauc_mrr_at_1_max
      value: 17.954238375826176
    - type: nauc_mrr_at_1_std
      value: 41.06416015417585
    - type: nauc_mrr_at_20_diff1
      value: 31.67689594961523
    - type: nauc_mrr_at_20_max
      value: 16.68974038291927
    - type: nauc_mrr_at_20_std
      value: 40.26184065004142
    - type: nauc_mrr_at_3_diff1
      value: 32.88514642209214
    - type: nauc_mrr_at_3_max
      value: 16.60927210883201
    - type: nauc_mrr_at_3_std
      value: 40.52722870715327
    - type: nauc_mrr_at_5_diff1
      value: 32.61065074987751
    - type: nauc_mrr_at_5_max
      value: 16.410060126697708
    - type: nauc_mrr_at_5_std
      value: 40.842537928791266
    - type: nauc_ndcg_at_1000_diff1
      value: 30.673601120002708
    - type: nauc_ndcg_at_1000_max
      value: 16.352776754218628
    - type: nauc_ndcg_at_1000_std
      value: 40.57479523675407
    - type: nauc_ndcg_at_100_diff1
      value: 30.673601120002708
    - type: nauc_ndcg_at_100_max
      value: 16.352776754218628
    - type: nauc_ndcg_at_100_std
      value: 40.57479523675407
    - type: nauc_ndcg_at_10_diff1
      value: 30.673601120002708
    - type: nauc_ndcg_at_10_max
      value: 16.352776754218628
    - type: nauc_ndcg_at_10_std
      value: 40.57479523675407
    - type: nauc_ndcg_at_1_diff1
      value: 37.23119529469353
    - type: nauc_ndcg_at_1_max
      value: 17.954238375826176
    - type: nauc_ndcg_at_1_std
      value: 41.06416015417585
    - type: nauc_ndcg_at_20_diff1
      value: 30.673601120002708
    - type: nauc_ndcg_at_20_max
      value: 16.352776754218628
    - type: nauc_ndcg_at_20_std
      value: 40.57479523675407
    - type: nauc_ndcg_at_3_diff1
      value: 32.692059371935684
    - type: nauc_ndcg_at_3_max
      value: 15.388484446361897
    - type: nauc_ndcg_at_3_std
      value: 40.31798919556859
    - type: nauc_ndcg_at_5_diff1
      value: 32.33787822186148
    - type: nauc_ndcg_at_5_max
      value: 15.37441444307225
    - type: nauc_ndcg_at_5_std
      value: 41.080327309664504
    - type: nauc_precision_at_1000_diff1
      value: 18.64454273809176
    - type: nauc_precision_at_1000_max
      value: 19.148390272445123
    - type: nauc_precision_at_1000_std
      value: 36.88763361884904
    - type: nauc_precision_at_100_diff1
      value: 18.644542738091822
    - type: nauc_precision_at_100_max
      value: 19.148390272445155
    - type: nauc_precision_at_100_std
      value: 36.88763361884907
    - type: nauc_precision_at_10_diff1
      value: 18.644542738091754
    - type: nauc_precision_at_10_max
      value: 19.14839027244509
    - type: nauc_precision_at_10_std
      value: 36.88763361884904
    - type: nauc_precision_at_1_diff1
      value: 37.23119529469353
    - type: nauc_precision_at_1_max
      value: 17.954238375826176
    - type: nauc_precision_at_1_std
      value: 41.06416015417585
    - type: nauc_precision_at_20_diff1
      value: 18.644542738091754
    - type: nauc_precision_at_20_max
      value: 19.14839027244509
    - type: nauc_precision_at_20_std
      value: 36.88763361884904
    - type: nauc_precision_at_3_diff1
      value: 27.94995141293583
    - type: nauc_precision_at_3_max
      value: 16.51406325384133
    - type: nauc_precision_at_3_std
      value: 40.19351675721699
    - type: nauc_precision_at_5_diff1
      value: 25.19257303691455
    - type: nauc_precision_at_5_max
      value: 16.265888721273452
    - type: nauc_precision_at_5_std
      value: 40.66731811007547
    - type: nauc_recall_at_1000_diff1
      value: 23.738180706212336
    - type: nauc_recall_at_1000_max
      value: 15.954285393176399
    - type: nauc_recall_at_1000_std
      value: 39.1687719365175
    - type: nauc_recall_at_100_diff1
      value: 23.738180706212336
    - type: nauc_recall_at_100_max
      value: 15.954285393176399
    - type: nauc_recall_at_100_std
      value: 39.1687719365175
    - type: nauc_recall_at_10_diff1
      value: 23.738180706212336
    - type: nauc_recall_at_10_max
      value: 15.954285393176399
    - type: nauc_recall_at_10_std
      value: 39.1687719365175
    - type: nauc_recall_at_1_diff1
      value: 38.670851513282415
    - type: nauc_recall_at_1_max
      value: 16.75377301174682
    - type: nauc_recall_at_1_std
      value: 40.6311885488597
    - type: nauc_recall_at_20_diff1
      value: 23.738180706212336
    - type: nauc_recall_at_20_max
      value: 15.954285393176399
    - type: nauc_recall_at_20_std
      value: 39.1687719365175
    - type: nauc_recall_at_3_diff1
      value: 30.07079049671837
    - type: nauc_recall_at_3_max
      value: 14.153285818065308
    - type: nauc_recall_at_3_std
      value: 39.51862221525536
    - type: nauc_recall_at_5_diff1
      value: 28.8773619633831
    - type: nauc_recall_at_5_max
      value: 13.964789033166072
    - type: nauc_recall_at_5_std
      value: 41.0091940854079
    - type: ndcg_at_1
      value: 22.486
    - type: ndcg_at_10
      value: 34.985
    - type: ndcg_at_100
      value: 34.985
    - type: ndcg_at_1000
      value: 34.985
    - type: ndcg_at_20
      value: 34.985
    - type: ndcg_at_3
      value: 29.125
    - type: ndcg_at_5
      value: 31.878
    - type: precision_at_1
      value: 22.486
    - type: precision_at_10
      value: 5.774
    - type: precision_at_100
      value: 0.577
    - type: precision_at_1000
      value: 0.058
    - type: precision_at_20
      value: 2.887
    - type: precision_at_3
      value: 12.767999999999999
    - type: precision_at_5
      value: 9.22
    - type: recall_at_1
      value: 20.455000000000002
    - type: recall_at_10
      value: 49.730000000000004
    - type: recall_at_100
      value: 49.730000000000004
    - type: recall_at_1000
      value: 49.730000000000004
    - type: recall_at_20
      value: 49.730000000000004
    - type: recall_at_3
      value: 33.855000000000004
    - type: recall_at_5
      value: 40.528999999999996
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackMathematicaRetrieval (default)
      revision: 90fceea13679c63fe563ded68f3b6f06e50061de
      split: test
      type: mteb/cqadupstack-mathematica
    metrics:
    - type: main_score
      value: 27.786
    - type: map_at_1
      value: 13.752
    - type: map_at_10
      value: 22.272
    - type: map_at_100
      value: 22.272
    - type: map_at_1000
      value: 22.272
    - type: map_at_20
      value: 22.272
    - type: map_at_3
      value: 19.789
    - type: map_at_5
      value: 20.919999999999998
    - type: mrr_at_1
      value: 16.791044776119403
    - type: mrr_at_10
      value: 26.279564479191343
    - type: mrr_at_100
      value: 26.279564479191343
    - type: mrr_at_1000
      value: 26.279564479191343
    - type: mrr_at_20
      value: 26.279564479191343
    - type: mrr_at_3
      value: 24.004975124378113
    - type: mrr_at_5
      value: 25.0
    - type: nauc_map_at_1000_diff1
      value: 28.565163649134224
    - type: nauc_map_at_1000_max
      value: 20.57078498641585
    - type: nauc_map_at_1000_std
      value: 42.11193185966052
    - type: nauc_map_at_100_diff1
      value: 28.565163649134224
    - type: nauc_map_at_100_max
      value: 20.57078498641585
    - type: nauc_map_at_100_std
      value: 42.11193185966052
    - type: nauc_map_at_10_diff1
      value: 28.565163649134224
    - type: nauc_map_at_10_max
      value: 20.57078498641585
    - type: nauc_map_at_10_std
      value: 42.11193185966052
    - type: nauc_map_at_1_diff1
      value: 39.52496173835783
    - type: nauc_map_at_1_max
      value: 22.002138432171094
    - type: nauc_map_at_1_std
      value: 43.18688068965491
    - type: nauc_map_at_20_diff1
      value: 28.565163649134224
    - type: nauc_map_at_20_max
      value: 20.57078498641585
    - type: nauc_map_at_20_std
      value: 42.11193185966052
    - type: nauc_map_at_3_diff1
      value: 29.78439884235976
    - type: nauc_map_at_3_max
      value: 19.189863662264965
    - type: nauc_map_at_3_std
      value: 41.785114765566114
    - type: nauc_map_at_5_diff1
      value: 28.83139234624586
    - type: nauc_map_at_5_max
      value: 19.831992565409827
    - type: nauc_map_at_5_std
      value: 42.231379171304525
    - type: nauc_mrr_at_1000_diff1
      value: 28.963400243652877
    - type: nauc_mrr_at_1000_max
      value: 22.607452927117603
    - type: nauc_mrr_at_1000_std
      value: 42.36888344973805
    - type: nauc_mrr_at_100_diff1
      value: 28.963400243652877
    - type: nauc_mrr_at_100_max
      value: 22.607452927117603
    - type: nauc_mrr_at_100_std
      value: 42.36888344973805
    - type: nauc_mrr_at_10_diff1
      value: 28.963400243652877
    - type: nauc_mrr_at_10_max
      value: 22.607452927117603
    - type: nauc_mrr_at_10_std
      value: 42.36888344973805
    - type: nauc_mrr_at_1_diff1
      value: 38.3618539615043
    - type: nauc_mrr_at_1_max
      value: 23.36626951426822
    - type: nauc_mrr_at_1_std
      value: 43.4038386288295
    - type: nauc_mrr_at_20_diff1
      value: 28.963400243652877
    - type: nauc_mrr_at_20_max
      value: 22.607452927117603
    - type: nauc_mrr_at_20_std
      value: 42.36888344973805
    - type: nauc_mrr_at_3_diff1
      value: 29.461207522274467
    - type: nauc_mrr_at_3_max
      value: 21.528176439244913
    - type: nauc_mrr_at_3_std
      value: 42.277120357283806
    - type: nauc_mrr_at_5_diff1
      value: 29.247502737795493
    - type: nauc_mrr_at_5_max
      value: 22.40274657626829
    - type: nauc_mrr_at_5_std
      value: 42.75961118843948
    - type: nauc_ndcg_at_1000_diff1
      value: 25.53386246841583
    - type: nauc_ndcg_at_1000_max
      value: 21.51055573746011
    - type: nauc_ndcg_at_1000_std
      value: 41.552253169721645
    - type: nauc_ndcg_at_100_diff1
      value: 25.53386246841583
    - type: nauc_ndcg_at_100_max
      value: 21.51055573746011
    - type: nauc_ndcg_at_100_std
      value: 41.552253169721645
    - type: nauc_ndcg_at_10_diff1
      value: 25.531307733326496
    - type: nauc_ndcg_at_10_max
      value: 21.507985952276393
    - type: nauc_ndcg_at_10_std
      value: 41.54975835506802
    - type: nauc_ndcg_at_1_diff1
      value: 38.3618539615043
    - type: nauc_ndcg_at_1_max
      value: 23.36626951426822
    - type: nauc_ndcg_at_1_std
      value: 43.4038386288295
    - type: nauc_ndcg_at_20_diff1
      value: 25.53386246841583
    - type: nauc_ndcg_at_20_max
      value: 21.51055573746011
    - type: nauc_ndcg_at_20_std
      value: 41.552253169721645
    - type: nauc_ndcg_at_3_diff1
      value: 26.815878961857482
    - type: nauc_ndcg_at_3_max
      value: 19.295720947580314
    - type: nauc_ndcg_at_3_std
      value: 41.408500189329075
    - type: nauc_ndcg_at_5_diff1
      value: 26.03353479737335
    - type: nauc_ndcg_at_5_max
      value: 20.329026740897373
    - type: nauc_ndcg_at_5_std
      value: 42.16247064849272
    - type: nauc_precision_at_1000_diff1
      value: 12.94322598880752
    - type: nauc_precision_at_1000_max
      value: 22.752393514763654
    - type: nauc_precision_at_1000_std
      value: 33.57990524065754
    - type: nauc_precision_at_100_diff1
      value: 12.943225988807509
    - type: nauc_precision_at_100_max
      value: 22.75239351476369
    - type: nauc_precision_at_100_std
      value: 33.579905240657546
    - type: nauc_precision_at_10_diff1
      value: 12.943225988807535
    - type: nauc_precision_at_10_max
      value: 22.752393514763654
    - type: nauc_precision_at_10_std
      value: 33.57990524065756
    - type: nauc_precision_at_1_diff1
      value: 38.3618539615043
    - type: nauc_precision_at_1_max
      value: 23.36626951426822
    - type: nauc_precision_at_1_std
      value: 43.4038386288295
    - type: nauc_precision_at_20_diff1
      value: 12.943225988807535
    - type: nauc_precision_at_20_max
      value: 22.752393514763654
    - type: nauc_precision_at_20_std
      value: 33.57990524065756
    - type: nauc_precision_at_3_diff1
      value: 17.68072798961056
    - type: nauc_precision_at_3_max
      value: 17.945919812743245
    - type: nauc_precision_at_3_std
      value: 38.98852109308557
    - type: nauc_precision_at_5_diff1
      value: 14.28895617817815
    - type: nauc_precision_at_5_max
      value: 19.60870888413918
    - type: nauc_precision_at_5_std
      value: 38.03024769005399
    - type: nauc_recall_at_1000_diff1
      value: 16.809256536304286
    - type: nauc_recall_at_1000_max
      value: 20.686006825507334
    - type: nauc_recall_at_1000_std
      value: 36.72858030878618
    - type: nauc_recall_at_100_diff1
      value: 16.809256536304286
    - type: nauc_recall_at_100_max
      value: 20.686006825507334
    - type: nauc_recall_at_100_std
      value: 36.72858030878618
    - type: nauc_recall_at_10_diff1
      value: 16.809256536304286
    - type: nauc_recall_at_10_max
      value: 20.686006825507334
    - type: nauc_recall_at_10_std
      value: 36.72858030878618
    - type: nauc_recall_at_1_diff1
      value: 39.52496173835783
    - type: nauc_recall_at_1_max
      value: 22.002138432171094
    - type: nauc_recall_at_1_std
      value: 43.18688068965491
    - type: nauc_recall_at_20_diff1
      value: 16.809256536304286
    - type: nauc_recall_at_20_max
      value: 20.686006825507334
    - type: nauc_recall_at_20_std
      value: 36.72858030878618
    - type: nauc_recall_at_3_diff1
      value: 20.482487915325148
    - type: nauc_recall_at_3_max
      value: 16.071143841702145
    - type: nauc_recall_at_3_std
      value: 38.99651083311669
    - type: nauc_recall_at_5_diff1
      value: 18.755675770598902
    - type: nauc_recall_at_5_max
      value: 18.44041416181758
    - type: nauc_recall_at_5_std
      value: 39.91225476889826
    - type: ndcg_at_1
      value: 16.791
    - type: ndcg_at_10
      value: 27.786
    - type: ndcg_at_100
      value: 27.785
    - type: ndcg_at_1000
      value: 27.785
    - type: ndcg_at_20
      value: 27.785
    - type: ndcg_at_3
      value: 23.058
    - type: ndcg_at_5
      value: 24.708
    - type: precision_at_1
      value: 16.791
    - type: precision_at_10
      value: 5.473
    - type: precision_at_100
      value: 0.547
    - type: precision_at_1000
      value: 0.055
    - type: precision_at_20
      value: 2.7359999999999998
    - type: precision_at_3
      value: 11.567
    - type: precision_at_5
      value: 8.259
    - type: recall_at_1
      value: 13.752
    - type: recall_at_10
      value: 40.646
    - type: recall_at_100
      value: 40.646
    - type: recall_at_1000
      value: 40.646
    - type: recall_at_20
      value: 40.646
    - type: recall_at_3
      value: 27.315
    - type: recall_at_5
      value: 31.595000000000002
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackPhysicsRetrieval (default)
      revision: 79531abbd1fb92d06c6d6315a0cbbbf5bb247ea4
      split: test
      type: mteb/cqadupstack-physics
    metrics:
    - type: main_score
      value: 46.561
    - type: map_at_1
      value: 27.559
    - type: map_at_10
      value: 39.736
    - type: map_at_100
      value: 39.736
    - type: map_at_1000
      value: 39.736
    - type: map_at_20
      value: 39.736
    - type: map_at_3
      value: 35.863
    - type: map_at_5
      value: 37.927
    - type: mrr_at_1
      value: 35.99615014436959
    - type: mrr_at_10
      value: 45.78100890661042
    - type: mrr_at_100
      value: 45.78100890661042
    - type: mrr_at_1000
      value: 45.78100890661042
    - type: mrr_at_20
      value: 45.78100890661042
    - type: mrr_at_3
      value: 42.90984921398777
    - type: mrr_at_5
      value: 44.57009945460372
    - type: nauc_map_at_1000_diff1
      value: 46.50994189730359
    - type: nauc_map_at_1000_max
      value: 31.0862905256805
    - type: nauc_map_at_1000_std
      value: 55.762364082195326
    - type: nauc_map_at_100_diff1
      value: 46.50994189730359
    - type: nauc_map_at_100_max
      value: 31.0862905256805
    - type: nauc_map_at_100_std
      value: 55.762364082195326
    - type: nauc_map_at_10_diff1
      value: 46.50994189730359
    - type: nauc_map_at_10_max
      value: 31.0862905256805
    - type: nauc_map_at_10_std
      value: 55.762364082195326
    - type: nauc_map_at_1_diff1
      value: 50.84926359956214
    - type: nauc_map_at_1_max
      value: 27.978796191157596
    - type: nauc_map_at_1_std
      value: 51.2526114783127
    - type: nauc_map_at_20_diff1
      value: 46.50994189730359
    - type: nauc_map_at_20_max
      value: 31.0862905256805
    - type: nauc_map_at_20_std
      value: 55.762364082195326
    - type: nauc_map_at_3_diff1
      value: 48.04148749097593
    - type: nauc_map_at_3_max
      value: 30.990786685893735
    - type: nauc_map_at_3_std
      value: 55.7721988748342
    - type: nauc_map_at_5_diff1
      value: 47.42321118236435
    - type: nauc_map_at_5_max
      value: 30.869965679478568
    - type: nauc_map_at_5_std
      value: 56.04664212501582
    - type: nauc_mrr_at_1000_diff1
      value: 44.57872078707285
    - type: nauc_mrr_at_1000_max
      value: 34.41370896160418
    - type: nauc_mrr_at_1000_std
      value: 54.43323584435783
    - type: nauc_mrr_at_100_diff1
      value: 44.57872078707285
    - type: nauc_mrr_at_100_max
      value: 34.41370896160418
    - type: nauc_mrr_at_100_std
      value: 54.43323584435783
    - type: nauc_mrr_at_10_diff1
      value: 44.57872078707285
    - type: nauc_mrr_at_10_max
      value: 34.41370896160418
    - type: nauc_mrr_at_10_std
      value: 54.43323584435783
    - type: nauc_mrr_at_1_diff1
      value: 47.27904297245325
    - type: nauc_mrr_at_1_max
      value: 34.640460910526166
    - type: nauc_mrr_at_1_std
      value: 51.99834691106755
    - type: nauc_mrr_at_20_diff1
      value: 44.57872078707285
    - type: nauc_mrr_at_20_max
      value: 34.41370896160418
    - type: nauc_mrr_at_20_std
      value: 54.43323584435783
    - type: nauc_mrr_at_3_diff1
      value: 44.90407181887466
    - type: nauc_mrr_at_3_max
      value: 34.98073324655902
    - type: nauc_mrr_at_3_std
      value: 54.80082399502317
    - type: nauc_mrr_at_5_diff1
      value: 44.9505367941623
    - type: nauc_mrr_at_5_max
      value: 34.51091988817032
    - type: nauc_mrr_at_5_std
      value: 54.61446143745533
    - type: nauc_ndcg_at_1000_diff1
      value: 44.604668825094066
    - type: nauc_ndcg_at_1000_max
      value: 31.328185259215076
    - type: nauc_ndcg_at_1000_std
      value: 56.089533147480864
    - type: nauc_ndcg_at_100_diff1
      value: 44.604668825094066
    - type: nauc_ndcg_at_100_max
      value: 31.328185259215076
    - type: nauc_ndcg_at_100_std
      value: 56.089533147480864
    - type: nauc_ndcg_at_10_diff1
      value: 44.53946120564986
    - type: nauc_ndcg_at_10_max
      value: 31.374136408270786
    - type: nauc_ndcg_at_10_std
      value: 56.011805154048545
    - type: nauc_ndcg_at_1_diff1
      value: 47.27904297245325
    - type: nauc_ndcg_at_1_max
      value: 34.640460910526166
    - type: nauc_ndcg_at_1_std
      value: 51.99834691106755
    - type: nauc_ndcg_at_20_diff1
      value: 44.57941006837825
    - type: nauc_ndcg_at_20_max
      value: 31.31194627057667
    - type: nauc_ndcg_at_20_std
      value: 56.054464082774416
    - type: nauc_ndcg_at_3_diff1
      value: 45.85373404740718
    - type: nauc_ndcg_at_3_max
      value: 33.198376538354005
    - type: nauc_ndcg_at_3_std
      value: 56.20402420365163
    - type: nauc_ndcg_at_5_diff1
      value: 45.79289869364121
    - type: nauc_ndcg_at_5_max
      value: 31.810585370387372
    - type: nauc_ndcg_at_5_std
      value: 56.464212503002045
    - type: nauc_precision_at_1000_diff1
      value: 11.321235280177994
    - type: nauc_precision_at_1000_max
      value: 27.351406205647894
    - type: nauc_precision_at_1000_std
      value: 29.57985982427862
    - type: nauc_precision_at_100_diff1
      value: 11.32123528017804
    - type: nauc_precision_at_100_max
      value: 27.351406205647965
    - type: nauc_precision_at_100_std
      value: 29.57985982427867
    - type: nauc_precision_at_10_diff1
      value: 11.321235280177982
    - type: nauc_precision_at_10_max
      value: 27.351406205647905
    - type: nauc_precision_at_10_std
      value: 29.579859824278625
    - type: nauc_precision_at_1_diff1
      value: 47.27904297245325
    - type: nauc_precision_at_1_max
      value: 34.640460910526166
    - type: nauc_precision_at_1_std
      value: 51.99834691106755
    - type: nauc_precision_at_20_diff1
      value: 11.321235280177982
    - type: nauc_precision_at_20_max
      value: 27.351406205647905
    - type: nauc_precision_at_20_std
      value: 29.579859824278625
    - type: nauc_precision_at_3_diff1
      value: 29.723525494820617
    - type: nauc_precision_at_3_max
      value: 33.703717115687596
    - type: nauc_precision_at_3_std
      value: 47.13186396299145
    - type: nauc_precision_at_5_diff1
      value: 22.680771913201752
    - type: nauc_precision_at_5_max
      value: 30.707151821829786
    - type: nauc_precision_at_5_std
      value: 40.99049761300301
    - type: nauc_recall_at_1000_diff1
      value: 37.21087912373446
    - type: nauc_recall_at_1000_max
      value: 24.99107249684149
    - type: nauc_recall_at_1000_std
      value: 53.57172622454311
    - type: nauc_recall_at_100_diff1
      value: 37.21087912373446
    - type: nauc_recall_at_100_max
      value: 24.99107249684149
    - type: nauc_recall_at_100_std
      value: 53.57172622454311
    - type: nauc_recall_at_10_diff1
      value: 37.21087912373446
    - type: nauc_recall_at_10_max
      value: 24.99107249684149
    - type: nauc_recall_at_10_std
      value: 53.57172622454311
    - type: nauc_recall_at_1_diff1
      value: 50.84926359956214
    - type: nauc_recall_at_1_max
      value: 27.978796191157596
    - type: nauc_recall_at_1_std
      value: 51.2526114783127
    - type: nauc_recall_at_20_diff1
      value: 37.21087912373446
    - type: nauc_recall_at_20_max
      value: 24.99107249684149
    - type: nauc_recall_at_20_std
      value: 53.57172622454311
    - type: nauc_recall_at_3_diff1
      value: 43.82466367630047
    - type: nauc_recall_at_3_max
      value: 29.711359894942696
    - type: nauc_recall_at_3_std
      value: 55.99772649886031
    - type: nauc_recall_at_5_diff1
      value: 42.52306596019424
    - type: nauc_recall_at_5_max
      value: 27.076507086553086
    - type: nauc_recall_at_5_std
      value: 55.975717794405156
    - type: ndcg_at_1
      value: 35.996
    - type: ndcg_at_10
      value: 46.561
    - type: ndcg_at_100
      value: 46.474
    - type: ndcg_at_1000
      value: 46.474
    - type: ndcg_at_20
      value: 46.492
    - type: ndcg_at_3
      value: 40.696
    - type: ndcg_at_5
      value: 43.279
    - type: precision_at_1
      value: 35.996
    - type: precision_at_10
      value: 9.066
    - type: precision_at_100
      value: 0.907
    - type: precision_at_1000
      value: 0.091
    - type: precision_at_20
      value: 4.533
    - type: precision_at_3
      value: 20.468
    - type: precision_at_5
      value: 14.591000000000001
    - type: recall_at_1
      value: 27.559
    - type: recall_at_10
      value: 60.912
    - type: recall_at_100
      value: 60.912
    - type: recall_at_1000
      value: 60.912
    - type: recall_at_20
      value: 60.912
    - type: recall_at_3
      value: 43.821
    - type: recall_at_5
      value: 51.052
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackProgrammersRetrieval (default)
      revision: 6184bc1440d2dbc7612be22b50686b8826d22b32
      split: test
      type: mteb/cqadupstack-programmers
    metrics:
    - type: main_score
      value: 43.294
    - type: map_at_1
      value: 25.477
    - type: map_at_10
      value: 36.772
    - type: map_at_100
      value: 36.772
    - type: map_at_1000
      value: 36.772
    - type: map_at_20
      value: 36.772
    - type: map_at_3
      value: 32.925
    - type: map_at_5
      value: 35.08
    - type: mrr_at_1
      value: 31.963470319634702
    - type: mrr_at_10
      value: 42.19078422845543
    - type: mrr_at_100
      value: 42.19078422845543
    - type: mrr_at_1000
      value: 42.19078422845543
    - type: mrr_at_20
      value: 42.19078422845543
    - type: mrr_at_3
      value: 39.40258751902586
    - type: mrr_at_5
      value: 41.13203957382036
    - type: nauc_map_at_1000_diff1
      value: 37.07798677153753
    - type: nauc_map_at_1000_max
      value: 33.99192907065488
    - type: nauc_map_at_1000_std
      value: 47.55377888091406
    - type: nauc_map_at_100_diff1
      value: 37.07798677153753
    - type: nauc_map_at_100_max
      value: 33.99192907065488
    - type: nauc_map_at_100_std
      value: 47.55377888091406
    - type: nauc_map_at_10_diff1
      value: 37.07798677153753
    - type: nauc_map_at_10_max
      value: 33.99192907065488
    - type: nauc_map_at_10_std
      value: 47.55377888091406
    - type: nauc_map_at_1_diff1
      value: 42.419411970459215
    - type: nauc_map_at_1_max
      value: 29.66944804367997
    - type: nauc_map_at_1_std
      value: 42.950983463920494
    - type: nauc_map_at_20_diff1
      value: 37.07798677153753
    - type: nauc_map_at_20_max
      value: 33.99192907065488
    - type: nauc_map_at_20_std
      value: 47.55377888091406
    - type: nauc_map_at_3_diff1
      value: 38.41124249748572
    - type: nauc_map_at_3_max
      value: 32.38111657167785
    - type: nauc_map_at_3_std
      value: 46.73160843405491
    - type: nauc_map_at_5_diff1
      value: 37.65580985726711
    - type: nauc_map_at_5_max
      value: 33.39682727352024
    - type: nauc_map_at_5_std
      value: 47.460096743048304
    - type: nauc_mrr_at_1000_diff1
      value: 38.143683085527044
    - type: nauc_mrr_at_1000_max
      value: 37.238784689973585
    - type: nauc_mrr_at_1000_std
      value: 46.724801400312245
    - type: nauc_mrr_at_100_diff1
      value: 38.143683085527044
    - type: nauc_mrr_at_100_max
      value: 37.238784689973585
    - type: nauc_mrr_at_100_std
      value: 46.724801400312245
    - type: nauc_mrr_at_10_diff1
      value: 38.143683085527044
    - type: nauc_mrr_at_10_max
      value: 37.238784689973585
    - type: nauc_mrr_at_10_std
      value: 46.724801400312245
    - type: nauc_mrr_at_1_diff1
      value: 43.88636776512273
    - type: nauc_mrr_at_1_max
      value: 36.07938357610354
    - type: nauc_mrr_at_1_std
      value: 45.142839817174426
    - type: nauc_mrr_at_20_diff1
      value: 38.143683085527044
    - type: nauc_mrr_at_20_max
      value: 37.238784689973585
    - type: nauc_mrr_at_20_std
      value: 46.724801400312245
    - type: nauc_mrr_at_3_diff1
      value: 39.39429773165717
    - type: nauc_mrr_at_3_max
      value: 36.60271776237658
    - type: nauc_mrr_at_3_std
      value: 46.595534225671464
    - type: nauc_mrr_at_5_diff1
      value: 38.45998693910314
    - type: nauc_mrr_at_5_max
      value: 37.364024875359675
    - type: nauc_mrr_at_5_std
      value: 46.92246740887524
    - type: nauc_ndcg_at_1000_diff1
      value: 34.9371726997422
    - type: nauc_ndcg_at_1000_max
      value: 35.627744616525206
    - type: nauc_ndcg_at_1000_std
      value: 47.89298257012013
    - type: nauc_ndcg_at_100_diff1
      value: 34.934552921953824
    - type: nauc_ndcg_at_100_max
      value: 35.62286249224728
    - type: nauc_ndcg_at_100_std
      value: 47.89401821537334
    - type: nauc_ndcg_at_10_diff1
      value: 34.86158162684409
    - type: nauc_ndcg_at_10_max
      value: 35.56935177575266
    - type: nauc_ndcg_at_10_std
      value: 47.88041876532769
    - type: nauc_ndcg_at_1_diff1
      value: 43.88636776512273
    - type: nauc_ndcg_at_1_max
      value: 36.07938357610354
    - type: nauc_ndcg_at_1_std
      value: 45.142839817174426
    - type: nauc_ndcg_at_20_diff1
      value: 34.9110800442083
    - type: nauc_ndcg_at_20_max
      value: 35.58594469152604
    - type: nauc_ndcg_at_20_std
      value: 47.9025953139408
    - type: nauc_ndcg_at_3_diff1
      value: 37.29547245225055
    - type: nauc_ndcg_at_3_max
      value: 34.02707256081843
    - type: nauc_ndcg_at_3_std
      value: 47.0265771043486
    - type: nauc_ndcg_at_5_diff1
      value: 35.87284242063545
    - type: nauc_ndcg_at_5_max
      value: 35.05440985869865
    - type: nauc_ndcg_at_5_std
      value: 47.99253888919296
    - type: nauc_precision_at_1000_diff1
      value: 12.911477386465883
    - type: nauc_precision_at_1000_max
      value: 30.92662072599725
    - type: nauc_precision_at_1000_std
      value: 29.231756598869996
    - type: nauc_precision_at_100_diff1
      value: 12.911477386465945
    - type: nauc_precision_at_100_max
      value: 30.926620725997317
    - type: nauc_precision_at_100_std
      value: 29.23175659887004
    - type: nauc_precision_at_10_diff1
      value: 12.911477386465892
    - type: nauc_precision_at_10_max
      value: 30.926620725997296
    - type: nauc_precision_at_10_std
      value: 29.23175659887004
    - type: nauc_precision_at_1_diff1
      value: 43.88636776512273
    - type: nauc_precision_at_1_max
      value: 36.07938357610354
    - type: nauc_precision_at_1_std
      value: 45.142839817174426
    - type: nauc_precision_at_20_diff1
      value: 12.911477386465892
    - type: nauc_precision_at_20_max
      value: 30.926620725997296
    - type: nauc_precision_at_20_std
      value: 29.23175659887004
    - type: nauc_precision_at_3_diff1
      value: 29.098769196244355
    - type: nauc_precision_at_3_max
      value: 37.23123674195833
    - type: nauc_precision_at_3_std
      value: 44.019103653217556
    - type: nauc_precision_at_5_diff1
      value: 21.4653647961267
    - type: nauc_precision_at_5_max
      value: 35.59769066715319
    - type: nauc_precision_at_5_std
      value: 39.59848225185617
    - type: nauc_recall_at_1000_diff1
      value: 25.09837546027115
    - type: nauc_recall_at_1000_max
      value: 34.0468774344344
    - type: nauc_recall_at_1000_std
      value: 45.93502087452988
    - type: nauc_recall_at_100_diff1
      value: 25.09837546027115
    - type: nauc_recall_at_100_max
      value: 34.0468774344344
    - type: nauc_recall_at_100_std
      value: 45.93502087452988
    - type: nauc_recall_at_10_diff1
      value: 25.09837546027115
    - type: nauc_recall_at_10_max
      value: 34.0468774344344
    - type: nauc_recall_at_10_std
      value: 45.93502087452988
    - type: nauc_recall_at_1_diff1
      value: 42.419411970459215
    - type: nauc_recall_at_1_max
      value: 29.66944804367997
    - type: nauc_recall_at_1_std
      value: 42.950983463920494
    - type: nauc_recall_at_20_diff1
      value: 25.09837546027115
    - type: nauc_recall_at_20_max
      value: 34.0468774344344
    - type: nauc_recall_at_20_std
      value: 45.93502087452988
    - type: nauc_recall_at_3_diff1
      value: 32.86620481094869
    - type: nauc_recall_at_3_max
      value: 30.830405809177268
    - type: nauc_recall_at_3_std
      value: 46.03533087782885
    - type: nauc_recall_at_5_diff1
      value: 28.730500801807057
    - type: nauc_recall_at_5_max
      value: 33.07096929355136
    - type: nauc_recall_at_5_std
      value: 46.72288564354017
    - type: ndcg_at_1
      value: 31.963
    - type: ndcg_at_10
      value: 43.294
    - type: ndcg_at_100
      value: 43.227
    - type: ndcg_at_1000
      value: 43.225
    - type: ndcg_at_20
      value: 43.248
    - type: ndcg_at_3
      value: 37.183
    - type: ndcg_at_5
      value: 40.113
    - type: precision_at_1
      value: 31.963
    - type: precision_at_10
      value: 8.447000000000001
    - type: precision_at_100
      value: 0.845
    - type: precision_at_1000
      value: 0.084
    - type: precision_at_20
      value: 4.224
    - type: precision_at_3
      value: 18.303
    - type: precision_at_5
      value: 13.469999999999999
    - type: recall_at_1
      value: 25.477
    - type: recall_at_10
      value: 57.135000000000005
    - type: recall_at_100
      value: 57.135000000000005
    - type: recall_at_1000
      value: 57.135000000000005
    - type: recall_at_20
      value: 57.135000000000005
    - type: recall_at_3
      value: 40.128
    - type: recall_at_5
      value: 47.954
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackRetrieval (default)
      revision: CQADupstackRetrieval_is_a_combined_dataset
      split: test
      type: CQADupstackRetrieval_is_a_combined_dataset
    metrics:
    - type: main_score
      value: 38.92541666666667
    - type: ndcg_at_10
      value: 38.92541666666667
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackStatsRetrieval (default)
      revision: 65ac3a16b8e91f9cee4c9828cc7c335575432a2a
      split: test
      type: mteb/cqadupstack-stats
    metrics:
    - type: main_score
      value: 33.300999999999995
    - type: map_at_1
      value: 20.810000000000002
    - type: map_at_10
      value: 28.505000000000003
    - type: map_at_100
      value: 28.505000000000003
    - type: map_at_1000
      value: 28.505000000000003
    - type: map_at_20
      value: 28.505000000000003
    - type: map_at_3
      value: 25.790999999999997
    - type: map_at_5
      value: 27.172
    - type: mrr_at_1
      value: 23.619631901840492
    - type: mrr_at_10
      value: 31.09230450871553
    - type: mrr_at_100
      value: 31.09230450871553
    - type: mrr_at_1000
      value: 31.09230450871553
    - type: mrr_at_20
      value: 31.09230450871553
    - type: mrr_at_3
      value: 28.604294478527613
    - type: mrr_at_5
      value: 29.88496932515337
    - type: nauc_map_at_1000_diff1
      value: 39.340765188626065
    - type: nauc_map_at_1000_max
      value: 21.41828875451805
    - type: nauc_map_at_1000_std
      value: 49.18483191716705
    - type: nauc_map_at_100_diff1
      value: 39.340765188626065
    - type: nauc_map_at_100_max
      value: 21.41828875451805
    - type: nauc_map_at_100_std
      value: 49.18483191716705
    - type: nauc_map_at_10_diff1
      value: 39.340765188626065
    - type: nauc_map_at_10_max
      value: 21.41828875451805
    - type: nauc_map_at_10_std
      value: 49.18483191716705
    - type: nauc_map_at_1_diff1
      value: 47.63517446476202
    - type: nauc_map_at_1_max
      value: 20.68411509423654
    - type: nauc_map_at_1_std
      value: 51.60260244924134
    - type: nauc_map_at_20_diff1
      value: 39.340765188626065
    - type: nauc_map_at_20_max
      value: 21.41828875451805
    - type: nauc_map_at_20_std
      value: 49.18483191716705
    - type: nauc_map_at_3_diff1
      value: 41.26341800757779
    - type: nauc_map_at_3_max
      value: 20.47610904932267
    - type: nauc_map_at_3_std
      value: 50.156300424206755
    - type: nauc_map_at_5_diff1
      value: 40.37813209574792
    - type: nauc_map_at_5_max
      value: 21.444052532531778
    - type: nauc_map_at_5_std
      value: 49.96408195886608
    - type: nauc_mrr_at_1000_diff1
      value: 37.94302704007151
    - type: nauc_mrr_at_1000_max
      value: 23.674970672786696
    - type: nauc_mrr_at_1000_std
      value: 49.34299760040942
    - type: nauc_mrr_at_100_diff1
      value: 37.94302704007151
    - type: nauc_mrr_at_100_max
      value: 23.674970672786696
    - type: nauc_mrr_at_100_std
      value: 49.34299760040942
    - type: nauc_mrr_at_10_diff1
      value: 37.94302704007151
    - type: nauc_mrr_at_10_max
      value: 23.674970672786696
    - type: nauc_mrr_at_10_std
      value: 49.34299760040942
    - type: nauc_mrr_at_1_diff1
      value: 45.84174672470855
    - type: nauc_mrr_at_1_max
      value: 24.887540977494833
    - type: nauc_mrr_at_1_std
      value: 54.11093910469758
    - type: nauc_mrr_at_20_diff1
      value: 37.94302704007151
    - type: nauc_mrr_at_20_max
      value: 23.674970672786696
    - type: nauc_mrr_at_20_std
      value: 49.34299760040942
    - type: nauc_mrr_at_3_diff1
      value: 39.809395549356466
    - type: nauc_mrr_at_3_max
      value: 23.51220536405679
    - type: nauc_mrr_at_3_std
      value: 50.90294372903915
    - type: nauc_mrr_at_5_diff1
      value: 38.87643311455097
    - type: nauc_mrr_at_5_max
      value: 24.08588595914513
    - type: nauc_mrr_at_5_std
      value: 50.22568642142716
    - type: nauc_ndcg_at_1000_diff1
      value: 35.513968470994214
    - type: nauc_ndcg_at_1000_max
      value: 21.549300465719945
    - type: nauc_ndcg_at_1000_std
      value: 46.930088631228436
    - type: nauc_ndcg_at_100_diff1
      value: 35.513968470994214
    - type: nauc_ndcg_at_100_max
      value: 21.549300465719945
    - type: nauc_ndcg_at_100_std
      value: 46.930088631228436
    - type: nauc_ndcg_at_10_diff1
      value: 35.50151526810374
    - type: nauc_ndcg_at_10_max
      value: 21.471647229455545
    - type: nauc_ndcg_at_10_std
      value: 46.825159460727114
    - type: nauc_ndcg_at_1_diff1
      value: 45.84174672470855
    - type: nauc_ndcg_at_1_max
      value: 24.887540977494833
    - type: nauc_ndcg_at_1_std
      value: 54.11093910469758
    - type: nauc_ndcg_at_20_diff1
      value: 35.513968470994214
    - type: nauc_ndcg_at_20_max
      value: 21.549300465719945
    - type: nauc_ndcg_at_20_std
      value: 46.930088631228436
    - type: nauc_ndcg_at_3_diff1
      value: 38.74140085544354
    - type: nauc_ndcg_at_3_max
      value: 20.926100554441643
    - type: nauc_ndcg_at_3_std
      value: 49.19762424088564
    - type: nauc_ndcg_at_5_diff1
      value: 37.506741231131755
    - type: nauc_ndcg_at_5_max
      value: 22.08388859209447
    - type: nauc_ndcg_at_5_std
      value: 48.70462822803331
    - type: nauc_precision_at_1000_diff1
      value: 17.38534542950445
    - type: nauc_precision_at_1000_max
      value: 24.523592660749017
    - type: nauc_precision_at_1000_std
      value: 36.578539473373446
    - type: nauc_precision_at_100_diff1
      value: 17.385345429504472
    - type: nauc_precision_at_100_max
      value: 24.523592660749006
    - type: nauc_precision_at_100_std
      value: 36.578539473373475
    - type: nauc_precision_at_10_diff1
      value: 17.385345429504497
    - type: nauc_precision_at_10_max
      value: 24.523592660749035
    - type: nauc_precision_at_10_std
      value: 36.57853947337345
    - type: nauc_precision_at_1_diff1
      value: 45.84174672470855
    - type: nauc_precision_at_1_max
      value: 24.887540977494833
    - type: nauc_precision_at_1_std
      value: 54.11093910469758
    - type: nauc_precision_at_20_diff1
      value: 17.385345429504497
    - type: nauc_precision_at_20_max
      value: 24.523592660749035
    - type: nauc_precision_at_20_std
      value: 36.57853947337345
    - type: nauc_precision_at_3_diff1
      value: 30.221055550515146
    - type: nauc_precision_at_3_max
      value: 25.580351124580464
    - type: nauc_precision_at_3_std
      value: 48.21548802322659
    - type: nauc_precision_at_5_diff1
      value: 24.79214284557074
    - type: nauc_precision_at_5_max
      value: 27.291933293284355
    - type: nauc_precision_at_5_std
      value: 44.38058780570317
    - type: nauc_recall_at_1000_diff1
      value: 25.03074747243053
    - type: nauc_recall_at_1000_max
      value: 18.732000278189222
    - type: nauc_recall_at_1000_std
      value: 38.48652624679034
    - type: nauc_recall_at_100_diff1
      value: 25.03074747243053
    - type: nauc_recall_at_100_max
      value: 18.732000278189222
    - type: nauc_recall_at_100_std
      value: 38.48652624679034
    - type: nauc_recall_at_10_diff1
      value: 25.03074747243053
    - type: nauc_recall_at_10_max
      value: 18.732000278189222
    - type: nauc_recall_at_10_std
      value: 38.48652624679034
    - type: nauc_recall_at_1_diff1
      value: 47.63517446476202
    - type: nauc_recall_at_1_max
      value: 20.68411509423654
    - type: nauc_recall_at_1_std
      value: 51.60260244924134
    - type: nauc_recall_at_20_diff1
      value: 25.03074747243053
    - type: nauc_recall_at_20_max
      value: 18.732000278189222
    - type: nauc_recall_at_20_std
      value: 38.48652624679034
    - type: nauc_recall_at_3_diff1
      value: 34.57956172601732
    - type: nauc_recall_at_3_max
      value: 18.354739836921897
    - type: nauc_recall_at_3_std
      value: 46.47170022105493
    - type: nauc_recall_at_5_diff1
      value: 31.229991310165612
    - type: nauc_recall_at_5_max
      value: 20.842957699893862
    - type: nauc_recall_at_5_std
      value: 44.61614916730002
    - type: ndcg_at_1
      value: 23.62
    - type: ndcg_at_10
      value: 33.300999999999995
    - type: ndcg_at_100
      value: 33.266
    - type: ndcg_at_1000
      value: 33.266
    - type: ndcg_at_20
      value: 33.266
    - type: ndcg_at_3
      value: 28.114
    - type: ndcg_at_5
      value: 30.365
    - type: precision_at_1
      value: 23.62
    - type: precision_at_10
      value: 5.6129999999999995
    - type: precision_at_100
      value: 0.561
    - type: precision_at_1000
      value: 0.055999999999999994
    - type: precision_at_20
      value: 2.807
    - type: precision_at_3
      value: 12.321
    - type: precision_at_5
      value: 8.926
    - type: recall_at_1
      value: 20.810000000000002
    - type: recall_at_10
      value: 45.554
    - type: recall_at_100
      value: 45.554
    - type: recall_at_1000
      value: 45.554
    - type: recall_at_20
      value: 45.554
    - type: recall_at_3
      value: 31.169999999999998
    - type: recall_at_5
      value: 36.674
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackTexRetrieval (default)
      revision: 46989137a86843e03a6195de44b09deda022eec7
      split: test
      type: mteb/cqadupstack-tex
    metrics:
    - type: main_score
      value: 23.681
    - type: map_at_1
      value: 12.620000000000001
    - type: map_at_10
      value: 19.323999999999998
    - type: map_at_100
      value: 19.323999999999998
    - type: map_at_1000
      value: 19.323999999999998
    - type: map_at_20
      value: 19.323999999999998
    - type: map_at_3
      value: 17.079
    - type: map_at_5
      value: 18.307000000000002
    - type: mrr_at_1
      value: 15.794907088781832
    - type: mrr_at_10
      value: 22.674829853942065
    - type: mrr_at_100
      value: 22.674829853942065
    - type: mrr_at_1000
      value: 22.674829853942065
    - type: mrr_at_20
      value: 22.674829853942065
    - type: mrr_at_3
      value: 20.526496902959398
    - type: mrr_at_5
      value: 21.667240192704778
    - type: nauc_map_at_1000_diff1
      value: 29.63154354609521
    - type: nauc_map_at_1000_max
      value: 20.589931296268936
    - type: nauc_map_at_1000_std
      value: 43.162803923115995
    - type: nauc_map_at_100_diff1
      value: 29.63154354609521
    - type: nauc_map_at_100_max
      value: 20.589931296268936
    - type: nauc_map_at_100_std
      value: 43.162803923115995
    - type: nauc_map_at_10_diff1
      value: 29.63154354609521
    - type: nauc_map_at_10_max
      value: 20.589931296268936
    - type: nauc_map_at_10_std
      value: 43.162803923115995
    - type: nauc_map_at_1_diff1
      value: 36.02598320477385
    - type: nauc_map_at_1_max
      value: 22.403645417757712
    - type: nauc_map_at_1_std
      value: 43.25177762898499
    - type: nauc_map_at_20_diff1
      value: 29.63154354609521
    - type: nauc_map_at_20_max
      value: 20.589931296268936
    - type: nauc_map_at_20_std
      value: 43.162803923115995
    - type: nauc_map_at_3_diff1
      value: 30.061555010611162
    - type: nauc_map_at_3_max
      value: 20.153805520054995
    - type: nauc_map_at_3_std
      value: 43.27987607958122
    - type: nauc_map_at_5_diff1
      value: 29.767148401145665
    - type: nauc_map_at_5_max
      value: 20.404207801448642
    - type: nauc_map_at_5_std
      value: 43.40361159503011
    - type: nauc_mrr_at_1000_diff1
      value: 29.250362083863134
    - type: nauc_mrr_at_1000_max
      value: 23.553108585644875
    - type: nauc_mrr_at_1000_std
      value: 44.118346699771784
    - type: nauc_mrr_at_100_diff1
      value: 29.250362083863134
    - type: nauc_mrr_at_100_max
      value: 23.553108585644875
    - type: nauc_mrr_at_100_std
      value: 44.118346699771784
    - type: nauc_mrr_at_10_diff1
      value: 29.250362083863134
    - type: nauc_mrr_at_10_max
      value: 23.553108585644875
    - type: nauc_mrr_at_10_std
      value: 44.118346699771784
    - type: nauc_mrr_at_1_diff1
      value: 35.76262009909674
    - type: nauc_mrr_at_1_max
      value: 27.352062378565538
    - type: nauc_mrr_at_1_std
      value: 46.45905133319154
    - type: nauc_mrr_at_20_diff1
      value: 29.250362083863134
    - type: nauc_mrr_at_20_max
      value: 23.553108585644875
    - type: nauc_mrr_at_20_std
      value: 44.118346699771784
    - type: nauc_mrr_at_3_diff1
      value: 29.81656057732247
    - type: nauc_mrr_at_3_max
      value: 23.862219716074424
    - type: nauc_mrr_at_3_std
      value: 44.91021388085251
    - type: nauc_mrr_at_5_diff1
      value: 29.49776795979136
    - type: nauc_mrr_at_5_max
      value: 23.681786119891367
    - type: nauc_mrr_at_5_std
      value: 44.66056313728314
    - type: nauc_ndcg_at_1000_diff1
      value: 27.76274474660903
    - type: nauc_ndcg_at_1000_max
      value: 20.24494476203865
    - type: nauc_ndcg_at_1000_std
      value: 42.308082352017976
    - type: nauc_ndcg_at_100_diff1
      value: 27.771721146065993
    - type: nauc_ndcg_at_100_max
      value: 20.2560297355208
    - type: nauc_ndcg_at_100_std
      value: 42.3163717857178
    - type: nauc_ndcg_at_10_diff1
      value: 27.836785217160553
    - type: nauc_ndcg_at_10_max
      value: 20.517038399686406
    - type: nauc_ndcg_at_10_std
      value: 42.38900929529116
    - type: nauc_ndcg_at_1_diff1
      value: 35.76262009909674
    - type: nauc_ndcg_at_1_max
      value: 27.352062378565538
    - type: nauc_ndcg_at_1_std
      value: 46.45905133319154
    - type: nauc_ndcg_at_20_diff1
      value: 27.841459088719866
    - type: nauc_ndcg_at_20_max
      value: 20.372068873326313
    - type: nauc_ndcg_at_20_std
      value: 42.38036377943528
    - type: nauc_ndcg_at_3_diff1
      value: 28.49511029315987
    - type: nauc_ndcg_at_3_max
      value: 21.21893077651459
    - type: nauc_ndcg_at_3_std
      value: 43.897980690487834
    - type: nauc_ndcg_at_5_diff1
      value: 27.95045798126578
    - type: nauc_ndcg_at_5_max
      value: 20.820410959928008
    - type: nauc_ndcg_at_5_std
      value: 43.43269152680635
    - type: nauc_precision_at_1000_diff1
      value: 21.106954747640394
    - type: nauc_precision_at_1000_max
      value: 23.76283065744553
    - type: nauc_precision_at_1000_std
      value: 39.76602060237657
    - type: nauc_precision_at_100_diff1
      value: 21.106954747640465
    - type: nauc_precision_at_100_max
      value: 23.762830657445573
    - type: nauc_precision_at_100_std
      value: 39.76602060237664
    - type: nauc_precision_at_10_diff1
      value: 21.106954747640437
    - type: nauc_precision_at_10_max
      value: 23.76283065744557
    - type: nauc_precision_at_10_std
      value: 39.76602060237662
    - type: nauc_precision_at_1_diff1
      value: 35.76262009909674
    - type: nauc_precision_at_1_max
      value: 27.352062378565538
    - type: nauc_precision_at_1_std
      value: 46.45905133319154
    - type: nauc_precision_at_20_diff1
      value: 21.106954747640437
    - type: nauc_precision_at_20_max
      value: 23.76283065744557
    - type: nauc_precision_at_20_std
      value: 39.76602060237662
    - type: nauc_precision_at_3_diff1
      value: 24.295975811187308
    - type: nauc_precision_at_3_max
      value: 23.221923860347125
    - type: nauc_precision_at_3_std
      value: 45.76520609599524
    - type: nauc_precision_at_5_diff1
      value: 23.53529553697355
    - type: nauc_precision_at_5_max
      value: 24.206957343690796
    - type: nauc_precision_at_5_std
      value: 44.80142267296062
    - type: nauc_recall_at_1000_diff1
      value: 22.501191041636005
    - type: nauc_recall_at_1000_max
      value: 16.04298370470302
    - type: nauc_recall_at_1000_std
      value: 36.98944619538275
    - type: nauc_recall_at_100_diff1
      value: 22.501191041636005
    - type: nauc_recall_at_100_max
      value: 16.04298370470302
    - type: nauc_recall_at_100_std
      value: 36.98944619538275
    - type: nauc_recall_at_10_diff1
      value: 22.501191041636005
    - type: nauc_recall_at_10_max
      value: 16.04298370470302
    - type: nauc_recall_at_10_std
      value: 36.98944619538275
    - type: nauc_recall_at_1_diff1
      value: 36.02598320477385
    - type: nauc_recall_at_1_max
      value: 22.403645417757712
    - type: nauc_recall_at_1_std
      value: 43.25177762898499
    - type: nauc_recall_at_20_diff1
      value: 22.501191041636005
    - type: nauc_recall_at_20_max
      value: 16.04298370470302
    - type: nauc_recall_at_20_std
      value: 36.98944619538275
    - type: nauc_recall_at_3_diff1
      value: 24.110976114471665
    - type: nauc_recall_at_3_max
      value: 16.679437506306368
    - type: nauc_recall_at_3_std
      value: 40.633892965203025
    - type: nauc_recall_at_5_diff1
      value: 23.066232701583843
    - type: nauc_recall_at_5_max
      value: 16.620458152597724
    - type: nauc_recall_at_5_std
      value: 40.085383339808004
    - type: ndcg_at_1
      value: 15.795
    - type: ndcg_at_10
      value: 23.681
    - type: ndcg_at_100
      value: 23.578
    - type: ndcg_at_1000
      value: 23.575
    - type: ndcg_at_20
      value: 23.612
    - type: ndcg_at_3
      value: 19.622999999999998
    - type: ndcg_at_5
      value: 21.448
    - type: precision_at_1
      value: 15.795
    - type: precision_at_10
      value: 4.721
    - type: precision_at_100
      value: 0.47200000000000003
    - type: precision_at_1000
      value: 0.047
    - type: precision_at_20
      value: 2.3609999999999998
    - type: precision_at_3
      value: 9.716
    - type: precision_at_5
      value: 7.260999999999999
    - type: recall_at_1
      value: 12.620000000000001
    - type: recall_at_10
      value: 33.343
    - type: recall_at_100
      value: 33.343
    - type: recall_at_1000
      value: 33.343
    - type: recall_at_20
      value: 33.343
    - type: recall_at_3
      value: 21.98
    - type: recall_at_5
      value: 26.705000000000002
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackUnixRetrieval (default)
      revision: 6c6430d3a6d36f8d2a829195bc5dc94d7e063e53
      split: test
      type: mteb/cqadupstack-unix
    metrics:
    - type: main_score
      value: 41.806
    - type: map_at_1
      value: 26.732
    - type: map_at_10
      value: 36.344
    - type: map_at_100
      value: 36.344
    - type: map_at_1000
      value: 36.344
    - type: map_at_20
      value: 36.344
    - type: map_at_3
      value: 33.311
    - type: map_at_5
      value: 34.966
    - type: mrr_at_1
      value: 32.18283582089552
    - type: mrr_at_10
      value: 40.780916844349655
    - type: mrr_at_100
      value: 40.780916844349655
    - type: mrr_at_1000
      value: 40.780916844349655
    - type: mrr_at_20
      value: 40.780916844349655
    - type: mrr_at_3
      value: 38.4017412935323
    - type: mrr_at_5
      value: 39.74502487562182
    - type: nauc_map_at_1000_diff1
      value: 42.029865084452986
    - type: nauc_map_at_1000_max
      value: 30.672467177971445
    - type: nauc_map_at_1000_std
      value: 51.349352827486584
    - type: nauc_map_at_100_diff1
      value: 42.029865084452986
    - type: nauc_map_at_100_max
      value: 30.672467177971445
    - type: nauc_map_at_100_std
      value: 51.349352827486584
    - type: nauc_map_at_10_diff1
      value: 42.029865084452986
    - type: nauc_map_at_10_max
      value: 30.672467177971445
    - type: nauc_map_at_10_std
      value: 51.349352827486584
    - type: nauc_map_at_1_diff1
      value: 47.770753057017004
    - type: nauc_map_at_1_max
      value: 28.726394573540848
    - type: nauc_map_at_1_std
      value: 50.29370260960708
    - type: nauc_map_at_20_diff1
      value: 42.029865084452986
    - type: nauc_map_at_20_max
      value: 30.672467177971445
    - type: nauc_map_at_20_std
      value: 51.349352827486584
    - type: nauc_map_at_3_diff1
      value: 43.242643415917655
    - type: nauc_map_at_3_max
      value: 29.726836734478386
    - type: nauc_map_at_3_std
      value: 51.246308285602595
    - type: nauc_map_at_5_diff1
      value: 42.82947959717131
    - type: nauc_map_at_5_max
      value: 29.920552631724213
    - type: nauc_map_at_5_std
      value: 51.751563444499446
    - type: nauc_mrr_at_1000_diff1
      value: 41.051778302448646
    - type: nauc_mrr_at_1000_max
      value: 34.294793983793696
    - type: nauc_mrr_at_1000_std
      value: 51.210441459559775
    - type: nauc_mrr_at_100_diff1
      value: 41.051778302448646
    - type: nauc_mrr_at_100_max
      value: 34.294793983793696
    - type: nauc_mrr_at_100_std
      value: 51.210441459559775
    - type: nauc_mrr_at_10_diff1
      value: 41.051778302448646
    - type: nauc_mrr_at_10_max
      value: 34.294793983793696
    - type: nauc_mrr_at_10_std
      value: 51.210441459559775
    - type: nauc_mrr_at_1_diff1
      value: 47.330043498847715
    - type: nauc_mrr_at_1_max
      value: 35.52052571129342
    - type: nauc_mrr_at_1_std
      value: 53.92090037195486
    - type: nauc_mrr_at_20_diff1
      value: 41.051778302448646
    - type: nauc_mrr_at_20_max
      value: 34.294793983793696
    - type: nauc_mrr_at_20_std
      value: 51.210441459559775
    - type: nauc_mrr_at_3_diff1
      value: 42.01454063575604
    - type: nauc_mrr_at_3_max
      value: 33.94799724881562
    - type: nauc_mrr_at_3_std
      value: 51.81896198860591
    - type: nauc_mrr_at_5_diff1
      value: 41.74371227113812
    - type: nauc_mrr_at_5_max
      value: 33.99297679011106
    - type: nauc_mrr_at_5_std
      value: 51.924171394847164
    - type: nauc_ndcg_at_1000_diff1
      value: 38.97354461831701
    - type: nauc_ndcg_at_1000_max
      value: 31.86216172053149
    - type: nauc_ndcg_at_1000_std
      value: 50.25257450957372
    - type: nauc_ndcg_at_100_diff1
      value: 38.97354461831701
    - type: nauc_ndcg_at_100_max
      value: 31.86216172053149
    - type: nauc_ndcg_at_100_std
      value: 50.25257450957372
    - type: nauc_ndcg_at_10_diff1
      value: 38.97323332101555
    - type: nauc_ndcg_at_10_max
      value: 31.854802401854887
    - type: nauc_ndcg_at_10_std
      value: 50.24403093426471
    - type: nauc_ndcg_at_1_diff1
      value: 47.330043498847715
    - type: nauc_ndcg_at_1_max
      value: 35.52052571129342
    - type: nauc_ndcg_at_1_std
      value: 53.92090037195486
    - type: nauc_ndcg_at_20_diff1
      value: 38.97354461831701
    - type: nauc_ndcg_at_20_max
      value: 31.86216172053149
    - type: nauc_ndcg_at_20_std
      value: 50.25257450957372
    - type: nauc_ndcg_at_3_diff1
      value: 41.21072676739527
    - type: nauc_ndcg_at_3_max
      value: 31.006078186548887
    - type: nauc_ndcg_at_3_std
      value: 51.415502114544076
    - type: nauc_ndcg_at_5_diff1
      value: 40.77020818469095
    - type: nauc_ndcg_at_5_max
      value: 30.71158548001669
    - type: nauc_ndcg_at_5_std
      value: 51.62615750639233
    - type: nauc_precision_at_1000_diff1
      value: 18.27474545261557
    - type: nauc_precision_at_1000_max
      value: 31.44407983379977
    - type: nauc_precision_at_1000_std
      value: 36.92562977111628
    - type: nauc_precision_at_100_diff1
      value: 18.274745452615576
    - type: nauc_precision_at_100_max
      value: 31.444079833799808
    - type: nauc_precision_at_100_std
      value: 36.925629771116256
    - type: nauc_precision_at_10_diff1
      value: 18.274745452615583
    - type: nauc_precision_at_10_max
      value: 31.444079833799783
    - type: nauc_precision_at_10_std
      value: 36.925629771116256
    - type: nauc_precision_at_1_diff1
      value: 47.330043498847715
    - type: nauc_precision_at_1_max
      value: 35.52052571129342
    - type: nauc_precision_at_1_std
      value: 53.92090037195486
    - type: nauc_precision_at_20_diff1
      value: 18.274745452615583
    - type: nauc_precision_at_20_max
      value: 31.444079833799783
    - type: nauc_precision_at_20_std
      value: 36.925629771116256
    - type: nauc_precision_at_3_diff1
      value: 30.15305794068517
    - type: nauc_precision_at_3_max
      value: 33.58541265944281
    - type: nauc_precision_at_3_std
      value: 47.665100293401544
    - type: nauc_precision_at_5_diff1
      value: 27.013297248810492
    - type: nauc_precision_at_5_max
      value: 32.512488477925174
    - type: nauc_precision_at_5_std
      value: 45.98720957802227
    - type: nauc_recall_at_1000_diff1
      value: 28.678533383368414
    - type: nauc_recall_at_1000_max
      value: 29.87424579158725
    - type: nauc_recall_at_1000_std
      value: 43.8184814696736
    - type: nauc_recall_at_100_diff1
      value: 28.678533383368414
    - type: nauc_recall_at_100_max
      value: 29.87424579158725
    - type: nauc_recall_at_100_std
      value: 43.8184814696736
    - type: nauc_recall_at_10_diff1
      value: 28.678533383368414
    - type: nauc_recall_at_10_max
      value: 29.87424579158725
    - type: nauc_recall_at_10_std
      value: 43.8184814696736
    - type: nauc_recall_at_1_diff1
      value: 47.770753057017004
    - type: nauc_recall_at_1_max
      value: 28.726394573540848
    - type: nauc_recall_at_1_std
      value: 50.29370260960708
    - type: nauc_recall_at_20_diff1
      value: 28.678533383368414
    - type: nauc_recall_at_20_max
      value: 29.87424579158725
    - type: nauc_recall_at_20_std
      value: 43.8184814696736
    - type: nauc_recall_at_3_diff1
      value: 35.77737462859877
    - type: nauc_recall_at_3_max
      value: 27.52111447389709
    - type: nauc_recall_at_3_std
      value: 47.576055790438296
    - type: nauc_recall_at_5_diff1
      value: 33.93411578123683
    - type: nauc_recall_at_5_max
      value: 27.09224153326718
    - type: nauc_recall_at_5_std
      value: 47.98520555873462
    - type: ndcg_at_1
      value: 32.183
    - type: ndcg_at_10
      value: 41.806
    - type: ndcg_at_100
      value: 41.801
    - type: ndcg_at_1000
      value: 41.801
    - type: ndcg_at_20
      value: 41.801
    - type: ndcg_at_3
      value: 36.869
    - type: ndcg_at_5
      value: 39.119
    - type: precision_at_1
      value: 32.183
    - type: precision_at_10
      value: 7.2010000000000005
    - type: precision_at_100
      value: 0.72
    - type: precision_at_1000
      value: 0.07200000000000001
    - type: precision_at_20
      value: 3.601
    - type: precision_at_3
      value: 17.195
    - type: precision_at_5
      value: 11.996
    - type: recall_at_1
      value: 26.732
    - type: recall_at_10
      value: 54.056000000000004
    - type: recall_at_100
      value: 54.056000000000004
    - type: recall_at_1000
      value: 54.056000000000004
    - type: recall_at_20
      value: 54.056000000000004
    - type: recall_at_3
      value: 40.348
    - type: recall_at_5
      value: 46.317
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackWebmastersRetrieval (default)
      revision: 160c094312a0e1facb97e55eeddb698c0abe3571
      split: test
      type: mteb/cqadupstack-webmasters
    metrics:
    - type: main_score
      value: 42.730000000000004
    - type: map_at_1
      value: 25.717000000000002
    - type: map_at_10
      value: 35.931999999999995
    - type: map_at_100
      value: 35.931999999999995
    - type: map_at_1000
      value: 35.931999999999995
    - type: map_at_20
      value: 35.931999999999995
    - type: map_at_3
      value: 32.792
    - type: map_at_5
      value: 34.413
    - type: mrr_at_1
      value: 31.818181818181817
    - type: mrr_at_10
      value: 41.293995859213275
    - type: mrr_at_100
      value: 41.293995859213275
    - type: mrr_at_1000
      value: 41.293995859213275
    - type: mrr_at_20
      value: 41.293995859213275
    - type: mrr_at_3
      value: 38.63636363636366
    - type: mrr_at_5
      value: 39.93083003952572
    - type: nauc_map_at_1000_diff1
      value: 37.15147635810975
    - type: nauc_map_at_1000_max
      value: 26.019085437988455
    - type: nauc_map_at_1000_std
      value: 50.05555340774839
    - type: nauc_map_at_100_diff1
      value: 37.15147635810975
    - type: nauc_map_at_100_max
      value: 26.019085437988455
    - type: nauc_map_at_100_std
      value: 50.05555340774839
    - type: nauc_map_at_10_diff1
      value: 37.15147635810975
    - type: nauc_map_at_10_max
      value: 26.019085437988455
    - type: nauc_map_at_10_std
      value: 50.05555340774839
    - type: nauc_map_at_1_diff1
      value: 38.64478745314396
    - type: nauc_map_at_1_max
      value: 20.752144790784918
    - type: nauc_map_at_1_std
      value: 40.56093018871689
    - type: nauc_map_at_20_diff1
      value: 37.15147635810975
    - type: nauc_map_at_20_max
      value: 26.019085437988455
    - type: nauc_map_at_20_std
      value: 50.05555340774839
    - type: nauc_map_at_3_diff1
      value: 38.44112116581778
    - type: nauc_map_at_3_max
      value: 24.75177783141159
    - type: nauc_map_at_3_std
      value: 49.071152773241344
    - type: nauc_map_at_5_diff1
      value: 37.0639655139737
    - type: nauc_map_at_5_max
      value: 25.9285703525919
    - type: nauc_map_at_5_std
      value: 49.30581385914585
    - type: nauc_mrr_at_1000_diff1
      value: 36.28534996720877
    - type: nauc_mrr_at_1000_max
      value: 30.434225828730938
    - type: nauc_mrr_at_1000_std
      value: 50.27657668258579
    - type: nauc_mrr_at_100_diff1
      value: 36.28534996720877
    - type: nauc_mrr_at_100_max
      value: 30.434225828730938
    - type: nauc_mrr_at_100_std
      value: 50.27657668258579
    - type: nauc_mrr_at_10_diff1
      value: 36.28534996720877
    - type: nauc_mrr_at_10_max
      value: 30.434225828730938
    - type: nauc_mrr_at_10_std
      value: 50.27657668258579
    - type: nauc_mrr_at_1_diff1
      value: 36.139272676150654
    - type: nauc_mrr_at_1_max
      value: 30.684054392787765
    - type: nauc_mrr_at_1_std
      value: 46.25402131822708
    - type: nauc_mrr_at_20_diff1
      value: 36.28534996720877
    - type: nauc_mrr_at_20_max
      value: 30.434225828730938
    - type: nauc_mrr_at_20_std
      value: 50.27657668258579
    - type: nauc_mrr_at_3_diff1
      value: 37.049546252383756
    - type: nauc_mrr_at_3_max
      value: 30.13038641842545
    - type: nauc_mrr_at_3_std
      value: 50.04662570120962
    - type: nauc_mrr_at_5_diff1
      value: 36.607211390652935
    - type: nauc_mrr_at_5_max
      value: 30.947339568488147
    - type: nauc_mrr_at_5_std
      value: 50.10713308342655
    - type: nauc_ndcg_at_1000_diff1
      value: 36.428352883380335
    - type: nauc_ndcg_at_1000_max
      value: 27.190912957917302
    - type: nauc_ndcg_at_1000_std
      value: 51.705737226010285
    - type: nauc_ndcg_at_100_diff1
      value: 36.41697226532888
    - type: nauc_ndcg_at_100_max
      value: 27.194288719423355
    - type: nauc_ndcg_at_100_std
      value: 51.70153467351315
    - type: nauc_ndcg_at_10_diff1
      value: 36.96181682477244
    - type: nauc_ndcg_at_10_max
      value: 28.08637051301156
    - type: nauc_ndcg_at_10_std
      value: 52.50752866306804
    - type: nauc_ndcg_at_1_diff1
      value: 36.139272676150654
    - type: nauc_ndcg_at_1_max
      value: 30.684054392787765
    - type: nauc_ndcg_at_1_std
      value: 46.25402131822708
    - type: nauc_ndcg_at_20_diff1
      value: 36.70663039014047
    - type: nauc_ndcg_at_20_max
      value: 27.510326422163526
    - type: nauc_ndcg_at_20_std
      value: 52.01162683625703
    - type: nauc_ndcg_at_3_diff1
      value: 38.449356197166175
    - type: nauc_ndcg_at_3_max
      value: 28.9372985651693
    - type: nauc_ndcg_at_3_std
      value: 52.67714664095088
    - type: nauc_ndcg_at_5_diff1
      value: 36.78608996385
    - type: nauc_ndcg_at_5_max
      value: 29.446680194989344
    - type: nauc_ndcg_at_5_std
      value: 51.861059419384034
    - type: nauc_precision_at_1000_diff1
      value: 19.54683747160824
    - type: nauc_precision_at_1000_max
      value: 32.259555283834636
    - type: nauc_precision_at_1000_std
      value: 44.81416994918333
    - type: nauc_precision_at_100_diff1
      value: 19.546837471608264
    - type: nauc_precision_at_100_max
      value: 32.259555283834665
    - type: nauc_precision_at_100_std
      value: 44.81416994918333
    - type: nauc_precision_at_10_diff1
      value: 19.546837471608246
    - type: nauc_precision_at_10_max
      value: 32.25955528383466
    - type: nauc_precision_at_10_std
      value: 44.814169949183366
    - type: nauc_precision_at_1_diff1
      value: 36.139272676150654
    - type: nauc_precision_at_1_max
      value: 30.684054392787765
    - type: nauc_precision_at_1_std
      value: 46.25402131822708
    - type: nauc_precision_at_20_diff1
      value: 19.546837471608246
    - type: nauc_precision_at_20_max
      value: 32.25955528383466
    - type: nauc_precision_at_20_std
      value: 44.814169949183366
    - type: nauc_precision_at_3_diff1
      value: 29.899118400378445
    - type: nauc_precision_at_3_max
      value: 36.14935234131955
    - type: nauc_precision_at_3_std
      value: 54.074350990330366
    - type: nauc_precision_at_5_diff1
      value: 22.26374571818644
    - type: nauc_precision_at_5_max
      value: 36.82682867306063
    - type: nauc_precision_at_5_std
      value: 48.56421424761333
    - type: nauc_recall_at_1000_diff1
      value: 31.915712169391735
    - type: nauc_recall_at_1000_max
      value: 23.941811598232462
    - type: nauc_recall_at_1000_std
      value: 51.02924010623434
    - type: nauc_recall_at_100_diff1
      value: 31.915712169391735
    - type: nauc_recall_at_100_max
      value: 23.941811598232462
    - type: nauc_recall_at_100_std
      value: 51.02924010623434
    - type: nauc_recall_at_10_diff1
      value: 31.915712169391735
    - type: nauc_recall_at_10_max
      value: 23.941811598232462
    - type: nauc_recall_at_10_std
      value: 51.02924010623434
    - type: nauc_recall_at_1_diff1
      value: 38.64478745314396
    - type: nauc_recall_at_1_max
      value: 20.752144790784918
    - type: nauc_recall_at_1_std
      value: 40.56093018871689
    - type: nauc_recall_at_20_diff1
      value: 31.915712169391735
    - type: nauc_recall_at_20_max
      value: 23.941811598232462
    - type: nauc_recall_at_20_std
      value: 51.02924010623434
    - type: nauc_recall_at_3_diff1
      value: 37.957699811362914
    - type: nauc_recall_at_3_max
      value: 24.500389095147042
    - type: nauc_recall_at_3_std
      value: 51.49128830665207
    - type: nauc_recall_at_5_diff1
      value: 33.160730479813274
    - type: nauc_recall_at_5_max
      value: 27.23186207348286
    - type: nauc_recall_at_5_std
      value: 50.51117952860018
    - type: ndcg_at_1
      value: 31.818
    - type: ndcg_at_10
      value: 42.730000000000004
    - type: ndcg_at_100
      value: 42.076
    - type: ndcg_at_1000
      value: 42.064
    - type: ndcg_at_20
      value: 42.315000000000005
    - type: ndcg_at_3
      value: 37.669000000000004
    - type: ndcg_at_5
      value: 39.735
    - type: precision_at_1
      value: 31.818
    - type: precision_at_10
      value: 8.458
    - type: precision_at_100
      value: 0.8460000000000001
    - type: precision_at_1000
      value: 0.08499999999999999
    - type: precision_at_20
      value: 4.229
    - type: precision_at_3
      value: 18.445
    - type: precision_at_5
      value: 13.161999999999999
    - type: recall_at_1
      value: 25.717000000000002
    - type: recall_at_10
      value: 55.78999999999999
    - type: recall_at_100
      value: 55.78999999999999
    - type: recall_at_1000
      value: 55.78999999999999
    - type: recall_at_20
      value: 55.78999999999999
    - type: recall_at_3
      value: 40.577000000000005
    - type: recall_at_5
      value: 46.371
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackWordpressRetrieval (default)
      revision: 4ffe81d471b1924886b33c7567bfb200e9eec5c4
      split: test
      type: mteb/cqadupstack-wordpress
    metrics:
    - type: main_score
      value: 28.155
    - type: map_at_1
      value: 16.55
    - type: map_at_10
      value: 23.706
    - type: map_at_100
      value: 23.706
    - type: map_at_1000
      value: 23.706
    - type: map_at_20
      value: 23.706
    - type: map_at_3
      value: 21.482
    - type: map_at_5
      value: 22.483
    - type: mrr_at_1
      value: 18.11460258780037
    - type: mrr_at_10
      value: 25.34944107032831
    - type: mrr_at_100
      value: 25.34944107032831
    - type: mrr_at_1000
      value: 25.34944107032831
    - type: mrr_at_20
      value: 25.34944107032831
    - type: mrr_at_3
      value: 23.16697473813924
    - type: mrr_at_5
      value: 24.1743684534812
    - type: nauc_map_at_1000_diff1
      value: 28.22330065610974
    - type: nauc_map_at_1000_max
      value: 21.430401018604762
    - type: nauc_map_at_1000_std
      value: 36.84924288926676
    - type: nauc_map_at_100_diff1
      value: 28.22330065610974
    - type: nauc_map_at_100_max
      value: 21.430401018604762
    - type: nauc_map_at_100_std
      value: 36.84924288926676
    - type: nauc_map_at_10_diff1
      value: 28.22330065610974
    - type: nauc_map_at_10_max
      value: 21.430401018604762
    - type: nauc_map_at_10_std
      value: 36.84924288926676
    - type: nauc_map_at_1_diff1
      value: 32.681510347450356
    - type: nauc_map_at_1_max
      value: 17.051782508120215
    - type: nauc_map_at_1_std
      value: 30.881101638873425
    - type: nauc_map_at_20_diff1
      value: 28.22330065610974
    - type: nauc_map_at_20_max
      value: 21.430401018604762
    - type: nauc_map_at_20_std
      value: 36.84924288926676
    - type: nauc_map_at_3_diff1
      value: 28.04218955485086
    - type: nauc_map_at_3_max
      value: 20.805844753735585
    - type: nauc_map_at_3_std
      value: 36.31203017688765
    - type: nauc_map_at_5_diff1
      value: 28.320198219248482
    - type: nauc_map_at_5_max
      value: 21.552154452885212
    - type: nauc_map_at_5_std
      value: 36.38879700659056
    - type: nauc_mrr_at_1000_diff1
      value: 28.719359576549518
    - type: nauc_mrr_at_1000_max
      value: 23.386465285712855
    - type: nauc_mrr_at_1000_std
      value: 37.66116865065753
    - type: nauc_mrr_at_100_diff1
      value: 28.719359576549518
    - type: nauc_mrr_at_100_max
      value: 23.386465285712855
    - type: nauc_mrr_at_100_std
      value: 37.66116865065753
    - type: nauc_mrr_at_10_diff1
      value: 28.719359576549518
    - type: nauc_mrr_at_10_max
      value: 23.386465285712855
    - type: nauc_mrr_at_10_std
      value: 37.66116865065753
    - type: nauc_mrr_at_1_diff1
      value: 33.42797714029809
    - type: nauc_mrr_at_1_max
      value: 19.823834907701166
    - type: nauc_mrr_at_1_std
      value: 33.2739158700565
    - type: nauc_mrr_at_20_diff1
      value: 28.719359576549518
    - type: nauc_mrr_at_20_max
      value: 23.386465285712855
    - type: nauc_mrr_at_20_std
      value: 37.66116865065753
    - type: nauc_mrr_at_3_diff1
      value: 28.796403747397964
    - type: nauc_mrr_at_3_max
      value: 23.09383896570769
    - type: nauc_mrr_at_3_std
      value: 37.4629984467181
    - type: nauc_mrr_at_5_diff1
      value: 28.962467923588232
    - type: nauc_mrr_at_5_max
      value: 23.690277715243212
    - type: nauc_mrr_at_5_std
      value: 37.342152739301156
    - type: nauc_ndcg_at_1000_diff1
      value: 27.200061060638813
    - type: nauc_ndcg_at_1000_max
      value: 23.012989178637977
    - type: nauc_ndcg_at_1000_std
      value: 38.97519004233306
    - type: nauc_ndcg_at_100_diff1
      value: 27.200061060638813
    - type: nauc_ndcg_at_100_max
      value: 23.012989178637977
    - type: nauc_ndcg_at_100_std
      value: 38.97519004233306
    - type: nauc_ndcg_at_10_diff1
      value: 27.200061060638813
    - type: nauc_ndcg_at_10_max
      value: 23.012989178637977
    - type: nauc_ndcg_at_10_std
      value: 38.97519004233306
    - type: nauc_ndcg_at_1_diff1
      value: 33.42797714029809
    - type: nauc_ndcg_at_1_max
      value: 19.823834907701166
    - type: nauc_ndcg_at_1_std
      value: 33.2739158700565
    - type: nauc_ndcg_at_20_diff1
      value: 27.200061060638813
    - type: nauc_ndcg_at_20_max
      value: 23.012989178637977
    - type: nauc_ndcg_at_20_std
      value: 38.97519004233306
    - type: nauc_ndcg_at_3_diff1
      value: 27.107513163290562
    - type: nauc_ndcg_at_3_max
      value: 22.429004710620433
    - type: nauc_ndcg_at_3_std
      value: 38.20992212508275
    - type: nauc_ndcg_at_5_diff1
      value: 27.6250616300774
    - type: nauc_ndcg_at_5_max
      value: 23.618100080712356
    - type: nauc_ndcg_at_5_std
      value: 38.140240440024044
    - type: nauc_precision_at_1000_diff1
      value: 24.845221820449083
    - type: nauc_precision_at_1000_max
      value: 25.957519924425494
    - type: nauc_precision_at_1000_std
      value: 42.0979991669019
    - type: nauc_precision_at_100_diff1
      value: 24.845221820449073
    - type: nauc_precision_at_100_max
      value: 25.957519924425497
    - type: nauc_precision_at_100_std
      value: 42.097999166901886
    - type: nauc_precision_at_10_diff1
      value: 24.84522182044909
    - type: nauc_precision_at_10_max
      value: 25.957519924425476
    - type: nauc_precision_at_10_std
      value: 42.09799916690188
    - type: nauc_precision_at_1_diff1
      value: 33.42797714029809
    - type: nauc_precision_at_1_max
      value: 19.823834907701166
    - type: nauc_precision_at_1_std
      value: 33.2739158700565
    - type: nauc_precision_at_20_diff1
      value: 24.84522182044909
    - type: nauc_precision_at_20_max
      value: 25.957519924425476
    - type: nauc_precision_at_20_std
      value: 42.09799916690188
    - type: nauc_precision_at_3_diff1
      value: 26.049155943036673
    - type: nauc_precision_at_3_max
      value: 27.046435493366506
    - type: nauc_precision_at_3_std
      value: 42.86258167530946
    - type: nauc_precision_at_5_diff1
      value: 26.70694367882625
    - type: nauc_precision_at_5_max
      value: 28.78111627237881
    - type: nauc_precision_at_5_std
      value: 42.04730024886258
    - type: nauc_recall_at_1000_diff1
      value: 23.221002401395342
    - type: nauc_recall_at_1000_max
      value: 24.26969464402613
    - type: nauc_recall_at_1000_std
      value: 42.07125420035887
    - type: nauc_recall_at_100_diff1
      value: 23.221002401395342
    - type: nauc_recall_at_100_max
      value: 24.26969464402613
    - type: nauc_recall_at_100_std
      value: 42.07125420035887
    - type: nauc_recall_at_10_diff1
      value: 23.221002401395342
    - type: nauc_recall_at_10_max
      value: 24.26969464402613
    - type: nauc_recall_at_10_std
      value: 42.07125420035887
    - type: nauc_recall_at_1_diff1
      value: 32.681510347450356
    - type: nauc_recall_at_1_max
      value: 17.051782508120215
    - type: nauc_recall_at_1_std
      value: 30.881101638873425
    - type: nauc_recall_at_20_diff1
      value: 23.221002401395342
    - type: nauc_recall_at_20_max
      value: 24.26969464402613
    - type: nauc_recall_at_20_std
      value: 42.07125420035887
    - type: nauc_recall_at_3_diff1
      value: 23.67549226196366
    - type: nauc_recall_at_3_max
      value: 24.320398943643582
    - type: nauc_recall_at_3_std
      value: 41.543691625059786
    - type: nauc_recall_at_5_diff1
      value: 24.789779839467872
    - type: nauc_recall_at_5_max
      value: 26.537498096700755
    - type: nauc_recall_at_5_std
      value: 40.543714338623715
    - type: ndcg_at_1
      value: 18.115000000000002
    - type: ndcg_at_10
      value: 28.155
    - type: ndcg_at_100
      value: 28.155
    - type: ndcg_at_1000
      value: 28.155
    - type: ndcg_at_20
      value: 28.155
    - type: ndcg_at_3
      value: 23.514
    - type: ndcg_at_5
      value: 25.234
    - type: precision_at_1
      value: 18.115000000000002
    - type: precision_at_10
      value: 4.695
    - type: precision_at_100
      value: 0.47000000000000003
    - type: precision_at_1000
      value: 0.047
    - type: precision_at_20
      value: 2.348
    - type: precision_at_3
      value: 10.413
    - type: precision_at_5
      value: 7.2459999999999996
    - type: recall_at_1
      value: 16.55
    - type: recall_at_10
      value: 40.455999999999996
    - type: recall_at_100
      value: 40.455999999999996
    - type: recall_at_1000
      value: 40.455999999999996
    - type: recall_at_20
      value: 40.455999999999996
    - type: recall_at_3
      value: 27.522999999999996
    - type: recall_at_5
      value: 31.688
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB DBPedia (default)
      revision: c0f706b76e590d620bd6618b3ca8efdd34e2d659
      split: test
      type: mteb/dbpedia
    metrics:
    - type: ndcg_at_1
      value: 14.75
    - type: ndcg_at_3
      value: 13.477
    - type: ndcg_at_5
      value: 13.34
    - type: ndcg_at_10
      value: 13.392999999999999
    - type: ndcg_at_20
      value: 11.338
    - type: ndcg_at_100
      value: 10.196
    - type: ndcg_at_1000
      value: 10.111
    - type: map_at_1
      value: 2.344
    - type: map_at_3
      value: 3.859
    - type: map_at_5
      value: 4.646999999999999
    - type: map_at_10
      value: 5.5489999999999995
    - type: map_at_20
      value: 5.5489999999999995
    - type: map_at_100
      value: 5.5489999999999995
    - type: map_at_1000
      value: 5.5489999999999995
    - type: recall_at_1
      value: 2.344
    - type: recall_at_3
      value: 4.814
    - type: recall_at_5
      value: 6.768000000000001
    - type: recall_at_10
      value: 9.524000000000001
    - type: recall_at_20
      value: 9.524000000000001
    - type: recall_at_100
      value: 9.524000000000001
    - type: recall_at_1000
      value: 9.524000000000001
    - type: precision_at_1
      value: 21.75
    - type: precision_at_3
      value: 16.916999999999998
    - type: precision_at_5
      value: 14.85
    - type: precision_at_10
      value: 12.174999999999999
    - type: precision_at_20
      value: 6.088
    - type: precision_at_100
      value: 1.217
    - type: precision_at_1000
      value: 0.122
    - type: mrr_at_1
      value: 21.75
    - type: mrr_at_3
      value: 27.5833
    - type: mrr_at_5
      value: 29.1458
    - type: mrr_at_10
      value: 30.4068
    - type: mrr_at_20
      value: 30.4068
    - type: mrr_at_100
      value: 30.4068
    - type: mrr_at_1000
      value: 30.4068
    - type: nauc_ndcg_at_1_max
      value: 4.685700000000001
    - type: nauc_ndcg_at_1_std
      value: 32.619
    - type: nauc_ndcg_at_1_diff1
      value: 29.4841
    - type: nauc_ndcg_at_3_max
      value: -1.9144
    - type: nauc_ndcg_at_3_std
      value: 34.5188
    - type: nauc_ndcg_at_3_diff1
      value: 21.5183
    - type: nauc_ndcg_at_5_max
      value: -4.1678
    - type: nauc_ndcg_at_5_std
      value: 32.8297
    - type: nauc_ndcg_at_5_diff1
      value: 18.1603
    - type: nauc_ndcg_at_10_max
      value: -5.1773
    - type: nauc_ndcg_at_10_std
      value: 35.0285
    - type: nauc_ndcg_at_10_diff1
      value: 17.366200000000003
    - type: nauc_ndcg_at_20_max
      value: -7.290000000000001
    - type: nauc_ndcg_at_20_std
      value: 34.4193
    - type: nauc_ndcg_at_20_diff1
      value: 15.523100000000001
    - type: nauc_ndcg_at_100_max
      value: -8.4054
    - type: nauc_ndcg_at_100_std
      value: 33.5331
    - type: nauc_ndcg_at_100_diff1
      value: 13.9865
    - type: nauc_ndcg_at_1000_max
      value: -8.4555
    - type: nauc_ndcg_at_1000_std
      value: 33.5598
    - type: nauc_ndcg_at_1000_diff1
      value: 13.7126
    - type: nauc_map_at_1_max
      value: -9.9378
    - type: nauc_map_at_1_std
      value: 34.7291
    - type: nauc_map_at_1_diff1
      value: 27.4634
    - type: nauc_map_at_3_max
      value: -8.2735
    - type: nauc_map_at_3_std
      value: 35.4337
    - type: nauc_map_at_3_diff1
      value: 18.3254
    - type: nauc_map_at_5_max
      value: -9.8167
    - type: nauc_map_at_5_std
      value: 33.2556
    - type: nauc_map_at_5_diff1
      value: 14.5853
    - type: nauc_map_at_10_max
      value: -9.1811
    - type: nauc_map_at_10_std
      value: 33.7894
    - type: nauc_map_at_10_diff1
      value: 13.2381
    - type: nauc_map_at_20_max
      value: -9.1811
    - type: nauc_map_at_20_std
      value: 33.7894
    - type: nauc_map_at_20_diff1
      value: 13.2381
    - type: nauc_map_at_100_max
      value: -9.1811
    - type: nauc_map_at_100_std
      value: 33.7894
    - type: nauc_map_at_100_diff1
      value: 13.2381
    - type: nauc_map_at_1000_max
      value: -9.1811
    - type: nauc_map_at_1000_std
      value: 33.7894
    - type: nauc_map_at_1000_diff1
      value: 13.2381
    - type: nauc_recall_at_1_max
      value: -9.9378
    - type: nauc_recall_at_1_std
      value: 34.7291
    - type: nauc_recall_at_1_diff1
      value: 27.4634
    - type: nauc_recall_at_3_max
      value: -9.2842
    - type: nauc_recall_at_3_std
      value: 33.6327
    - type: nauc_recall_at_3_diff1
      value: 12.1882
    - type: nauc_recall_at_5_max
      value: -12.795100000000001
    - type: nauc_recall_at_5_std
      value: 27.832
    - type: nauc_recall_at_5_diff1
      value: 6.1798
    - type: nauc_recall_at_10_max
      value: -11.4108
    - type: nauc_recall_at_10_std
      value: 28.7157
    - type: nauc_recall_at_10_diff1
      value: 4.4436
    - type: nauc_recall_at_20_max
      value: -11.4108
    - type: nauc_recall_at_20_std
      value: 28.7157
    - type: nauc_recall_at_20_diff1
      value: 4.4436
    - type: nauc_recall_at_100_max
      value: -11.4108
    - type: nauc_recall_at_100_std
      value: 28.7157
    - type: nauc_recall_at_100_diff1
      value: 4.4436
    - type: nauc_recall_at_1000_max
      value: -11.4108
    - type: nauc_recall_at_1000_std
      value: 28.7157
    - type: nauc_recall_at_1000_diff1
      value: 4.4436
    - type: nauc_precision_at_1_max
      value: 6.6856
    - type: nauc_precision_at_1_std
      value: 33.1612
    - type: nauc_precision_at_1_diff1
      value: 30.251099999999997
    - type: nauc_precision_at_3_max
      value: 1.0049000000000001
    - type: nauc_precision_at_3_std
      value: 33.6587
    - type: nauc_precision_at_3_diff1
      value: 19.3978
    - type: nauc_precision_at_5_max
      value: 0.7034
    - type: nauc_precision_at_5_std
      value: 30.701099999999997
    - type: nauc_precision_at_5_diff1
      value: 15.4892
    - type: nauc_precision_at_10_max
      value: 3.0372
    - type: nauc_precision_at_10_std
      value: 32.453700000000005
    - type: nauc_precision_at_10_diff1
      value: 14.877
    - type: nauc_precision_at_20_max
      value: 3.0372
    - type: nauc_precision_at_20_std
      value: 32.453700000000005
    - type: nauc_precision_at_20_diff1
      value: 14.877
    - type: nauc_precision_at_100_max
      value: 3.0372
    - type: nauc_precision_at_100_std
      value: 32.453700000000005
    - type: nauc_precision_at_100_diff1
      value: 14.877
    - type: nauc_precision_at_1000_max
      value: 3.0372
    - type: nauc_precision_at_1000_std
      value: 32.453700000000005
    - type: nauc_precision_at_1000_diff1
      value: 14.877
    - type: nauc_mrr_at_1_max
      value: 6.6856
    - type: nauc_mrr_at_1_std
      value: 33.1612
    - type: nauc_mrr_at_1_diff1
      value: 30.251099999999997
    - type: nauc_mrr_at_3_max
      value: 3.5292999999999997
    - type: nauc_mrr_at_3_std
      value: 37.400800000000004
    - type: nauc_mrr_at_3_diff1
      value: 27.319300000000002
    - type: nauc_mrr_at_5_max
      value: 3.3163
    - type: nauc_mrr_at_5_std
      value: 37.5503
    - type: nauc_mrr_at_5_diff1
      value: 27.358900000000002
    - type: nauc_mrr_at_10_max
      value: 3.1353
    - type: nauc_mrr_at_10_std
      value: 37.5727
    - type: nauc_mrr_at_10_diff1
      value: 27.0299
    - type: nauc_mrr_at_20_max
      value: 3.1353
    - type: nauc_mrr_at_20_std
      value: 37.5727
    - type: nauc_mrr_at_20_diff1
      value: 27.0299
    - type: nauc_mrr_at_100_max
      value: 3.1353
    - type: nauc_mrr_at_100_std
      value: 37.5727
    - type: nauc_mrr_at_100_diff1
      value: 27.0299
    - type: nauc_mrr_at_1000_max
      value: 3.1353
    - type: nauc_mrr_at_1000_std
      value: 37.5727
    - type: nauc_mrr_at_1000_diff1
      value: 27.0299
    - type: main_score
      value: 13.392999999999999
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB EmotionClassification (default)
      revision: 4f58c6b202a23cf9a4da393831edf4f9183cad37
      split: test
      type: mteb/emotion
    metrics:
    - type: accuracy
      value: 51.77
    - type: f1
      value: 47.530116264827214
    - type: f1_weighted
      value: 53.80990920561022
    - type: main_score
      value: 51.77
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB FiQA2018 (default)
      revision: 27a168819829fe9bcd655c2df245fb19452e8e06
      split: test
      type: mteb/fiqa
    metrics:
    - type: ndcg_at_1
      value: 16.975
    - type: ndcg_at_3
      value: 15.792
    - type: ndcg_at_5
      value: 16.72
    - type: ndcg_at_10
      value: 18.874
    - type: ndcg_at_20
      value: 18.861
    - type: ndcg_at_100
      value: 18.861
    - type: ndcg_at_1000
      value: 18.861
    - type: map_at_1
      value: 7.13
    - type: map_at_3
      value: 11.068
    - type: map_at_5
      value: 12.187000000000001
    - type: map_at_10
      value: 13.442000000000002
    - type: map_at_20
      value: 13.442000000000002
    - type: map_at_100
      value: 13.442000000000002
    - type: map_at_1000
      value: 13.442000000000002
    - type: recall_at_1
      value: 7.13
    - type: recall_at_3
      value: 14.232
    - type: recall_at_5
      value: 17.957
    - type: recall_at_10
      value: 24.336
    - type: recall_at_20
      value: 24.336
    - type: recall_at_100
      value: 24.336
    - type: recall_at_1000
      value: 24.336
    - type: precision_at_1
      value: 16.975
    - type: precision_at_3
      value: 11.368
    - type: precision_at_5
      value: 8.889
    - type: precision_at_10
      value: 6.111
    - type: precision_at_20
      value: 3.056
    - type: precision_at_100
      value: 0.611
    - type: precision_at_1000
      value: 0.061
    - type: mrr_at_1
      value: 16.975299999999997
    - type: mrr_at_3
      value: 21.6307
    - type: mrr_at_5
      value: 23.0504
    - type: mrr_at_10
      value: 24.1934
    - type: mrr_at_20
      value: 24.1934
    - type: mrr_at_100
      value: 24.1934
    - type: mrr_at_1000
      value: 24.1934
    - type: nauc_ndcg_at_1_max
      value: 13.7211
    - type: nauc_ndcg_at_1_std
      value: 38.2932
    - type: nauc_ndcg_at_1_diff1
      value: 30.3772
    - type: nauc_ndcg_at_3_max
      value: 12.790099999999999
    - type: nauc_ndcg_at_3_std
      value: 37.8198
    - type: nauc_ndcg_at_3_diff1
      value: 26.2762
    - type: nauc_ndcg_at_5_max
      value: 11.8568
    - type: nauc_ndcg_at_5_std
      value: 38.674
    - type: nauc_ndcg_at_5_diff1
      value: 26.3819
    - type: nauc_ndcg_at_10_max
      value: 11.7226
    - type: nauc_ndcg_at_10_std
      value: 35.989900000000006
    - type: nauc_ndcg_at_10_diff1
      value: 24.681800000000003
    - type: nauc_ndcg_at_20_max
      value: 11.6709
    - type: nauc_ndcg_at_20_std
      value: 35.9892
    - type: nauc_ndcg_at_20_diff1
      value: 24.6629
    - type: nauc_ndcg_at_100_max
      value: 11.6709
    - type: nauc_ndcg_at_100_std
      value: 35.9892
    - type: nauc_ndcg_at_100_diff1
      value: 24.6629
    - type: nauc_ndcg_at_1000_max
      value: 11.6709
    - type: nauc_ndcg_at_1000_std
      value: 35.9892
    - type: nauc_ndcg_at_1000_diff1
      value: 24.6629
    - type: nauc_map_at_1_max
      value: 14.129900000000001
    - type: nauc_map_at_1_std
      value: 37.9865
    - type: nauc_map_at_1_diff1
      value: 35.599199999999996
    - type: nauc_map_at_3_max
      value: 12.8558
    - type: nauc_map_at_3_std
      value: 38.8084
    - type: nauc_map_at_3_diff1
      value: 29.391499999999997
    - type: nauc_map_at_5_max
      value: 12.8072
    - type: nauc_map_at_5_std
      value: 40.0669
    - type: nauc_map_at_5_diff1
      value: 28.699599999999997
    - type: nauc_map_at_10_max
      value: 12.9994
    - type: nauc_map_at_10_std
      value: 39.313199999999995
    - type: nauc_map_at_10_diff1
      value: 27.090199999999996
    - type: nauc_map_at_20_max
      value: 12.9994
    - type: nauc_map_at_20_std
      value: 39.313199999999995
    - type: nauc_map_at_20_diff1
      value: 27.090199999999996
    - type: nauc_map_at_100_max
      value: 12.9994
    - type: nauc_map_at_100_std
      value: 39.313199999999995
    - type: nauc_map_at_100_diff1
      value: 27.090199999999996
    - type: nauc_map_at_1000_max
      value: 12.9994
    - type: nauc_map_at_1000_std
      value: 39.313199999999995
    - type: nauc_map_at_1000_diff1
      value: 27.090199999999996
    - type: nauc_recall_at_1_max
      value: 14.129900000000001
    - type: nauc_recall_at_1_std
      value: 37.9865
    - type: nauc_recall_at_1_diff1
      value: 35.599199999999996
    - type: nauc_recall_at_3_max
      value: 8.4322
    - type: nauc_recall_at_3_std
      value: 33.333600000000004
    - type: nauc_recall_at_3_diff1
      value: 23.3184
    - type: nauc_recall_at_5_max
      value: 8.3074
    - type: nauc_recall_at_5_std
      value: 33.8013
    - type: nauc_recall_at_5_diff1
      value: 22.7607
    - type: nauc_recall_at_10_max
      value: 7.3909
    - type: nauc_recall_at_10_std
      value: 27.2268
    - type: nauc_recall_at_10_diff1
      value: 18.0679
    - type: nauc_recall_at_20_max
      value: 7.3909
    - type: nauc_recall_at_20_std
      value: 27.2268
    - type: nauc_recall_at_20_diff1
      value: 18.0679
    - type: nauc_recall_at_100_max
      value: 7.3909
    - type: nauc_recall_at_100_std
      value: 27.2268
    - type: nauc_recall_at_100_diff1
      value: 18.0679
    - type: nauc_recall_at_1000_max
      value: 7.3909
    - type: nauc_recall_at_1000_std
      value: 27.2268
    - type: nauc_recall_at_1000_diff1
      value: 18.0679
    - type: nauc_precision_at_1_max
      value: 13.7211
    - type: nauc_precision_at_1_std
      value: 38.2932
    - type: nauc_precision_at_1_diff1
      value: 30.3772
    - type: nauc_precision_at_3_max
      value: 13.503499999999999
    - type: nauc_precision_at_3_std
      value: 38.1701
    - type: nauc_precision_at_3_diff1
      value: 22.2937
    - type: nauc_precision_at_5_max
      value: 12.357
    - type: nauc_precision_at_5_std
      value: 40.03
    - type: nauc_precision_at_5_diff1
      value: 20.424
    - type: nauc_precision_at_10_max
      value: 11.8008
    - type: nauc_precision_at_10_std
      value: 33.3441
    - type: nauc_precision_at_10_diff1
      value: 14.9469
    - type: nauc_precision_at_20_max
      value: 11.8008
    - type: nauc_precision_at_20_std
      value: 33.3441
    - type: nauc_precision_at_20_diff1
      value: 14.9469
    - type: nauc_precision_at_100_max
      value: 11.8008
    - type: nauc_precision_at_100_std
      value: 33.3441
    - type: nauc_precision_at_100_diff1
      value: 14.9469
    - type: nauc_precision_at_1000_max
      value: 11.8008
    - type: nauc_precision_at_1000_std
      value: 33.3441
    - type: nauc_precision_at_1000_diff1
      value: 14.9469
    - type: nauc_mrr_at_1_max
      value: 13.7211
    - type: nauc_mrr_at_1_std
      value: 38.2932
    - type: nauc_mrr_at_1_diff1
      value: 30.3772
    - type: nauc_mrr_at_3_max
      value: 12.1531
    - type: nauc_mrr_at_3_std
      value: 35.2193
    - type: nauc_mrr_at_3_diff1
      value: 25.9477
    - type: nauc_mrr_at_5_max
      value: 12.1404
    - type: nauc_mrr_at_5_std
      value: 35.3919
    - type: nauc_mrr_at_5_diff1
      value: 25.7488
    - type: nauc_mrr_at_10_max
      value: 12.606800000000002
    - type: nauc_mrr_at_10_std
      value: 34.5276
    - type: nauc_mrr_at_10_diff1
      value: 25.3029
    - type: nauc_mrr_at_20_max
      value: 12.606800000000002
    - type: nauc_mrr_at_20_std
      value: 34.5276
    - type: nauc_mrr_at_20_diff1
      value: 25.3029
    - type: nauc_mrr_at_100_max
      value: 12.606800000000002
    - type: nauc_mrr_at_100_std
      value: 34.5276
    - type: nauc_mrr_at_100_diff1
      value: 25.3029
    - type: nauc_mrr_at_1000_max
      value: 12.606800000000002
    - type: nauc_mrr_at_1000_std
      value: 34.5276
    - type: nauc_mrr_at_1000_diff1
      value: 25.3029
    - type: main_score
      value: 18.874
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB ImdbClassification (default)
      revision: 3d86128a09e091d6018b6d26cad27f2739fc2db7
      split: test
      type: mteb/imdb
    metrics:
    - type: accuracy
      value: 92.56920000000001
    - type: ap
      value: 89.4544796545563
    - type: ap_weighted
      value: 89.4544796545563
    - type: f1
      value: 92.55736445858346
    - type: f1_weighted
      value: 92.55736445858345
    - type: main_score
      value: 92.56920000000001
    task:
      type: Classification
  - dataset:
      config: en
      name: MTEB MTOPDomainClassification (en)
      revision: d80d48c1eb48d3562165c59d59d0034df9fff0bf
      split: test
      type: mteb/mtop_domain
    metrics:
    - type: accuracy
      value: 92.69493844049249
    - type: f1
      value: 92.34370949894263
    - type: f1_weighted
      value: 92.69346221294657
    - type: main_score
      value: 92.69493844049249
    task:
      type: Classification
  - dataset:
      config: en
      name: MTEB MTOPIntentClassification (en)
      revision: ae001d0e6b1228650b7bd1c2c65fb50ad11a8aba
      split: test
      type: mteb/mtop_intent
    metrics:
    - type: accuracy
      value: 74.38668490652076
    - type: f1
      value: 56.13824491045559
    - type: f1_weighted
      value: 77.43490069089628
    - type: main_score
      value: 74.38668490652076
    task:
      type: Classification
  - dataset:
      config: en
      name: MTEB MassiveIntentClassification (en)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: test
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 74.56624075319436
    - type: f1
      value: 72.61598263797168
    - type: f1_weighted
      value: 74.46153756061406
    - type: main_score
      value: 74.56624075319436
    task:
      type: Classification
  - dataset:
      config: en
      name: MTEB MassiveScenarioClassification (en)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: test
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 78.06321452589106
    - type: f1
      value: 78.59621588045289
    - type: f1_weighted
      value: 78.17786876180818
    - type: main_score
      value: 78.06321452589106
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB MedrxivClusteringP2P (default)
      revision: e7a26af6f3ae46b30dde8737f02c07b1505bcc73
      split: test
      type: mteb/medrxiv-clustering-p2p
    metrics:
    - type: main_score
      value: 34.82248927844125
    - type: v_measure
      value: 34.82248927844125
    - type: v_measure_std
      value: 1.1552802019202142
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB MedrxivClusteringS2S (default)
      revision: 35191c8c0dca72d8ff3efcd72aa802307d469663
      split: test
      type: mteb/medrxiv-clustering-s2s
    metrics:
    - type: main_score
      value: 34.28978766278416
    - type: v_measure
      value: 34.28978766278416
    - type: v_measure_std
      value: 1.5185325614553058
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB MindSmallReranking (default)
      revision: 59042f120c80e8afa9cdbb224f67076cec0fc9a7
      split: test
      type: mteb/mind_small
    metrics:
    - type: main_score
      value: 31.80292247790192
    - type: map
      value: 31.80292247790192
    - type: mrr
      value: 32.86318994409157
    - type: nAUC_map_diff1
      value: 14.086784889776254
    - type: nAUC_map_max
      value: -25.297471501685965
    - type: nAUC_map_std
      value: -7.229171148688261
    - type: nAUC_mrr_diff1
      value: 12.802240033513904
    - type: nAUC_mrr_max
      value: -19.5992038439649
    - type: nAUC_mrr_std
      value: -4.898359535777221
    task:
      type: Reranking
  - dataset:
      config: default
      name: MTEB NFCorpus (default)
      revision: ec0fa4fe99da2ff19ca1214b7966684033a58814
      split: test
      type: mteb/nfcorpus
    metrics:
    - type: main_score
      value: 37.82
    - type: map_at_1
      value: 5.71
    - type: map_at_10
      value: 13.5
    - type: map_at_100
      value: 13.5
    - type: map_at_1000
      value: 13.5
    - type: map_at_20
      value: 13.5
    - type: map_at_3
      value: 9.195
    - type: map_at_5
      value: 11.169
    - type: mrr_at_1
      value: 46.43962848297213
    - type: mrr_at_10
      value: 55.9359182269399
    - type: mrr_at_100
      value: 55.9359182269399
    - type: mrr_at_1000
      value: 55.9359182269399
    - type: mrr_at_20
      value: 55.9359182269399
    - type: mrr_at_3
      value: 54.0763673890609
    - type: mrr_at_5
      value: 55.42311661506707
    - type: nauc_map_at_1000_diff1
      value: 15.361007200573587
    - type: nauc_map_at_1000_max
      value: 14.996485816478506
    - type: nauc_map_at_1000_std
      value: 37.3125620644805
    - type: nauc_map_at_100_diff1
      value: 15.361007200573587
    - type: nauc_map_at_100_max
      value: 14.996485816478506
    - type: nauc_map_at_100_std
      value: 37.3125620644805
    - type: nauc_map_at_10_diff1
      value: 15.361007200573587
    - type: nauc_map_at_10_max
      value: 14.996485816478506
    - type: nauc_map_at_10_std
      value: 37.3125620644805
    - type: nauc_map_at_1_diff1
      value: 30.52868213878106
    - type: nauc_map_at_1_max
      value: -0.24848058610075982
    - type: nauc_map_at_1_std
      value: 26.38700333520716
    - type: nauc_map_at_20_diff1
      value: 15.361007200573587
    - type: nauc_map_at_20_max
      value: 14.996485816478506
    - type: nauc_map_at_20_std
      value: 37.3125620644805
    - type: nauc_map_at_3_diff1
      value: 22.717388491927125
    - type: nauc_map_at_3_max
      value: 4.068483790823434
    - type: nauc_map_at_3_std
      value: 34.20404169678259
    - type: nauc_map_at_5_diff1
      value: 19.211212873034274
    - type: nauc_map_at_5_max
      value: 10.272976123633292
    - type: nauc_map_at_5_std
      value: 36.70558579764851
    - type: nauc_mrr_at_1000_diff1
      value: 25.464522395253514
    - type: nauc_mrr_at_1000_max
      value: 44.084142359008155
    - type: nauc_mrr_at_1000_std
      value: 42.56569573152332
    - type: nauc_mrr_at_100_diff1
      value: 25.464522395253514
    - type: nauc_mrr_at_100_max
      value: 44.084142359008155
    - type: nauc_mrr_at_100_std
      value: 42.56569573152332
    - type: nauc_mrr_at_10_diff1
      value: 25.464522395253514
    - type: nauc_mrr_at_10_max
      value: 44.084142359008155
    - type: nauc_mrr_at_10_std
      value: 42.56569573152332
    - type: nauc_mrr_at_1_diff1
      value: 30.66490522010124
    - type: nauc_mrr_at_1_max
      value: 39.8758179396962
    - type: nauc_mrr_at_1_std
      value: 41.56769198393745
    - type: nauc_mrr_at_20_diff1
      value: 25.464522395253514
    - type: nauc_mrr_at_20_max
      value: 44.084142359008155
    - type: nauc_mrr_at_20_std
      value: 42.56569573152332
    - type: nauc_mrr_at_3_diff1
      value: 25.821000426139644
    - type: nauc_mrr_at_3_max
      value: 42.48361768861429
    - type: nauc_mrr_at_3_std
      value: 42.54154756364517
    - type: nauc_mrr_at_5_diff1
      value: 26.006021194842592
    - type: nauc_mrr_at_5_max
      value: 43.920931578346135
    - type: nauc_mrr_at_5_std
      value: 43.00302246460356
    - type: nauc_ndcg_at_1000_diff1
      value: 14.131998431815806
    - type: nauc_ndcg_at_1000_max
      value: 26.655840322986556
    - type: nauc_ndcg_at_1000_std
      value: 39.2830117846456
    - type: nauc_ndcg_at_100_diff1
      value: 14.07295736929955
    - type: nauc_ndcg_at_100_max
      value: 26.724654761556916
    - type: nauc_ndcg_at_100_std
      value: 38.57237912613722
    - type: nauc_ndcg_at_10_diff1
      value: 9.947979487755868
    - type: nauc_ndcg_at_10_max
      value: 35.243626004896875
    - type: nauc_ndcg_at_10_std
      value: 29.981280320035005
    - type: nauc_ndcg_at_1_diff1
      value: 30.763561594299027
    - type: nauc_ndcg_at_1_max
      value: 37.53551290523811
    - type: nauc_ndcg_at_1_std
      value: 37.296883875558095
    - type: nauc_ndcg_at_20_diff1
      value: 12.705346773951684
    - type: nauc_ndcg_at_20_max
      value: 32.515662121821755
    - type: nauc_ndcg_at_20_std
      value: 34.194642729843046
    - type: nauc_ndcg_at_3_diff1
      value: 17.441360751294425
    - type: nauc_ndcg_at_3_max
      value: 35.844899873088174
    - type: nauc_ndcg_at_3_std
      value: 34.7736095241677
    - type: nauc_ndcg_at_5_diff1
      value: 13.26939699467756
    - type: nauc_ndcg_at_5_max
      value: 36.93123760234983
    - type: nauc_ndcg_at_5_std
      value: 33.37715225905341
    - type: nauc_precision_at_1000_diff1
      value: -3.322939918094219
    - type: nauc_precision_at_1000_max
      value: 37.436680044599505
    - type: nauc_precision_at_1000_std
      value: 16.32806060725948
    - type: nauc_precision_at_100_diff1
      value: -3.3229399180942307
    - type: nauc_precision_at_100_max
      value: 37.4366800445995
    - type: nauc_precision_at_100_std
      value: 16.328060607259467
    - type: nauc_precision_at_10_diff1
      value: -3.3229399180942356
    - type: nauc_precision_at_10_max
      value: 37.43668004459945
    - type: nauc_precision_at_10_std
      value: 16.32806060725943
    - type: nauc_precision_at_1_diff1
      value: 31.503307374142196
    - type: nauc_precision_at_1_max
      value: 40.44895933557234
    - type: nauc_precision_at_1_std
      value: 40.34688228241334
    - type: nauc_precision_at_20_diff1
      value: -3.3229399180942356
    - type: nauc_precision_at_20_max
      value: 37.43668004459945
    - type: nauc_precision_at_20_std
      value: 16.32806060725943
    - type: nauc_precision_at_3_diff1
      value: 8.505527445125715
    - type: nauc_precision_at_3_max
      value: 38.86672229863008
    - type: nauc_precision_at_3_std
      value: 31.81995138819344
    - type: nauc_precision_at_5_diff1
      value: 2.7041380962041885
    - type: nauc_precision_at_5_max
      value: 40.288526393009064
    - type: nauc_precision_at_5_std
      value: 27.34100082458853
    - type: nauc_recall_at_1000_diff1
      value: 7.803201684898056
    - type: nauc_recall_at_1000_max
      value: 11.59231050842395
    - type: nauc_recall_at_1000_std
      value: 33.014387452973985
    - type: nauc_recall_at_100_diff1
      value: 7.803201684898056
    - type: nauc_recall_at_100_max
      value: 11.59231050842395
    - type: nauc_recall_at_100_std
      value: 33.014387452973985
    - type: nauc_recall_at_10_diff1
      value: 7.803201684898056
    - type: nauc_recall_at_10_max
      value: 11.59231050842395
    - type: nauc_recall_at_10_std
      value: 33.014387452973985
    - type: nauc_recall_at_1_diff1
      value: 30.52868213878106
    - type: nauc_recall_at_1_max
      value: -0.24848058610075982
    - type: nauc_recall_at_1_std
      value: 26.38700333520716
    - type: nauc_recall_at_20_diff1
      value: 7.803201684898056
    - type: nauc_recall_at_20_max
      value: 11.59231050842395
    - type: nauc_recall_at_20_std
      value: 33.014387452973985
    - type: nauc_recall_at_3_diff1
      value: 18.528183435156915
    - type: nauc_recall_at_3_max
      value: 2.1809684912580822
    - type: nauc_recall_at_3_std
      value: 32.80894909935346
    - type: nauc_recall_at_5_diff1
      value: 11.90572282812033
    - type: nauc_recall_at_5_max
      value: 7.891038940450843
    - type: nauc_recall_at_5_std
      value: 32.824021095047385
    - type: ndcg_at_1
      value: 44.891999999999996
    - type: ndcg_at_10
      value: 37.82
    - type: ndcg_at_100
      value: 23.719
    - type: ndcg_at_1000
      value: 23.219
    - type: ndcg_at_20
      value: 29.864
    - type: ndcg_at_3
      value: 41.906
    - type: ndcg_at_5
      value: 40.733000000000004
    - type: precision_at_1
      value: 46.129999999999995
    - type: precision_at_10
      value: 29.567
    - type: precision_at_100
      value: 2.957
    - type: precision_at_1000
      value: 0.296
    - type: precision_at_20
      value: 14.783
    - type: precision_at_3
      value: 40.351
    - type: precision_at_5
      value: 36.842000000000006
    - type: recall_at_1
      value: 5.71
    - type: recall_at_10
      value: 17.897
    - type: recall_at_100
      value: 17.897
    - type: recall_at_1000
      value: 17.897
    - type: recall_at_20
      value: 17.897
    - type: recall_at_3
      value: 10.322000000000001
    - type: recall_at_5
      value: 13.746
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB NQ (default)
      revision: b774495ed302d8c44a3a7ea25c90dbce03968f31
      split: test
      type: mteb/nq
    metrics:
    - type: main_score
      value: 30.898999999999997
    - type: map_at_1
      value: 12.895999999999999
    - type: map_at_10
      value: 23.855
    - type: map_at_100
      value: 23.855
    - type: map_at_1000
      value: 23.855
    - type: map_at_20
      value: 23.855
    - type: map_at_3
      value: 19.311
    - type: map_at_5
      value: 21.831999999999997
    - type: mrr_at_1
      value: 14.860950173812281
    - type: mrr_at_10
      value: 25.812894296382165
    - type: mrr_at_100
      value: 25.812894296382165
    - type: mrr_at_1000
      value: 25.812894296382165
    - type: mrr_at_20
      value: 25.812894296382165
    - type: mrr_at_3
      value: 21.707222865971453
    - type: mrr_at_5
      value: 24.05658555426816
    - type: nauc_map_at_1000_diff1
      value: 15.28169820974217
    - type: nauc_map_at_1000_max
      value: 8.13138073174654
    - type: nauc_map_at_1000_std
      value: 35.51489561735172
    - type: nauc_map_at_100_diff1
      value: 15.28169820974217
    - type: nauc_map_at_100_max
      value: 8.13138073174654
    - type: nauc_map_at_100_std
      value: 35.51489561735172
    - type: nauc_map_at_10_diff1
      value: 15.28169820974217
    - type: nauc_map_at_10_max
      value: 8.13138073174654
    - type: nauc_map_at_10_std
      value: 35.51489561735172
    - type: nauc_map_at_1_diff1
      value: 18.187139462065886
    - type: nauc_map_at_1_max
      value: 2.7981060549840464
    - type: nauc_map_at_1_std
      value: 29.505694195691767
    - type: nauc_map_at_20_diff1
      value: 15.28169820974217
    - type: nauc_map_at_20_max
      value: 8.13138073174654
    - type: nauc_map_at_20_std
      value: 35.51489561735172
    - type: nauc_map_at_3_diff1
      value: 15.897989479277214
    - type: nauc_map_at_3_max
      value: 5.932400345110462
    - type: nauc_map_at_3_std
      value: 34.31658193032982
    - type: nauc_map_at_5_diff1
      value: 15.46567932413518
    - type: nauc_map_at_5_max
      value: 7.33279929243331
    - type: nauc_map_at_5_std
      value: 35.32616321573606
    - type: nauc_mrr_at_1000_diff1
      value: 14.951651318691455
    - type: nauc_mrr_at_1000_max
      value: 9.132310422140746
    - type: nauc_mrr_at_1000_std
      value: 33.72249616390835
    - type: nauc_mrr_at_100_diff1
      value: 14.951651318691455
    - type: nauc_mrr_at_100_max
      value: 9.132310422140746
    - type: nauc_mrr_at_100_std
      value: 33.72249616390835
    - type: nauc_mrr_at_10_diff1
      value: 14.951651318691455
    - type: nauc_mrr_at_10_max
      value: 9.132310422140746
    - type: nauc_mrr_at_10_std
      value: 33.72249616390835
    - type: nauc_mrr_at_1_diff1
      value: 18.317198848753495
    - type: nauc_mrr_at_1_max
      value: 4.422371761910983
    - type: nauc_mrr_at_1_std
      value: 29.011099949753966
    - type: nauc_mrr_at_20_diff1
      value: 14.951651318691455
    - type: nauc_mrr_at_20_max
      value: 9.132310422140746
    - type: nauc_mrr_at_20_std
      value: 33.72249616390835
    - type: nauc_mrr_at_3_diff1
      value: 15.314211673395
    - type: nauc_mrr_at_3_max
      value: 7.802060639390988
    - type: nauc_mrr_at_3_std
      value: 33.040825868612245
    - type: nauc_mrr_at_5_diff1
      value: 15.062040970118701
    - type: nauc_mrr_at_5_max
      value: 8.616882358890342
    - type: nauc_mrr_at_5_std
      value: 33.66725752203577
    - type: nauc_ndcg_at_1000_diff1
      value: 14.03616000691516
    - type: nauc_ndcg_at_1000_max
      value: 10.57540540214194
    - type: nauc_ndcg_at_1000_std
      value: 36.804509360319855
    - type: nauc_ndcg_at_100_diff1
      value: 14.03616000691516
    - type: nauc_ndcg_at_100_max
      value: 10.57540540214194
    - type: nauc_ndcg_at_100_std
      value: 36.804509360319855
    - type: nauc_ndcg_at_10_diff1
      value: 14.03616000691516
    - type: nauc_ndcg_at_10_max
      value: 10.57540540214194
    - type: nauc_ndcg_at_10_std
      value: 36.804509360319855
    - type: nauc_ndcg_at_1_diff1
      value: 18.317198848753495
    - type: nauc_ndcg_at_1_max
      value: 4.422371761910983
    - type: nauc_ndcg_at_1_std
      value: 29.011099949753966
    - type: nauc_ndcg_at_20_diff1
      value: 14.03616000691516
    - type: nauc_ndcg_at_20_max
      value: 10.57540540214194
    - type: nauc_ndcg_at_20_std
      value: 36.804509360319855
    - type: nauc_ndcg_at_3_diff1
      value: 14.943833584293973
    - type: nauc_ndcg_at_3_max
      value: 7.182461300089245
    - type: nauc_ndcg_at_3_std
      value: 35.089843453552035
    - type: nauc_ndcg_at_5_diff1
      value: 14.318251822251355
    - type: nauc_ndcg_at_5_max
      value: 9.09614102774369
    - type: nauc_ndcg_at_5_std
      value: 36.45958360033229
    - type: nauc_precision_at_1000_diff1
      value: 9.084532598053281
    - type: nauc_precision_at_1000_max
      value: 17.842868823013074
    - type: nauc_precision_at_1000_std
      value: 33.80323399371497
    - type: nauc_precision_at_100_diff1
      value: 9.08453259805338
    - type: nauc_precision_at_100_max
      value: 17.8428688230132
    - type: nauc_precision_at_100_std
      value: 33.80323399371507
    - type: nauc_precision_at_10_diff1
      value: 9.084532598053343
    - type: nauc_precision_at_10_max
      value: 17.84286882301313
    - type: nauc_precision_at_10_std
      value: 33.80323399371502
    - type: nauc_precision_at_1_diff1
      value: 18.317198848753495
    - type: nauc_precision_at_1_max
      value: 4.422371761910983
    - type: nauc_precision_at_1_std
      value: 29.011099949753966
    - type: nauc_precision_at_20_diff1
      value: 9.084532598053343
    - type: nauc_precision_at_20_max
      value: 17.84286882301313
    - type: nauc_precision_at_20_std
      value: 33.80323399371502
    - type: nauc_precision_at_3_diff1
      value: 12.121487937291702
    - type: nauc_precision_at_3_max
      value: 11.360705059656611
    - type: nauc_precision_at_3_std
      value: 36.34974507203065
    - type: nauc_precision_at_5_diff1
      value: 10.750972165910149
    - type: nauc_precision_at_5_max
      value: 14.89067141416447
    - type: nauc_precision_at_5_std
      value: 37.02183807466284
    - type: nauc_recall_at_1000_diff1
      value: 10.889089455278517
    - type: nauc_recall_at_1000_max
      value: 14.814837985099349
    - type: nauc_recall_at_1000_std
      value: 39.89010281154022
    - type: nauc_recall_at_100_diff1
      value: 10.889089455278517
    - type: nauc_recall_at_100_max
      value: 14.814837985099349
    - type: nauc_recall_at_100_std
      value: 39.89010281154022
    - type: nauc_recall_at_10_diff1
      value: 10.889089455278517
    - type: nauc_recall_at_10_max
      value: 14.814837985099349
    - type: nauc_recall_at_10_std
      value: 39.89010281154022
    - type: nauc_recall_at_1_diff1
      value: 18.187139462065886
    - type: nauc_recall_at_1_max
      value: 2.7981060549840464
    - type: nauc_recall_at_1_std
      value: 29.505694195691767
    - type: nauc_recall_at_20_diff1
      value: 10.889089455278517
    - type: nauc_recall_at_20_max
      value: 14.814837985099349
    - type: nauc_recall_at_20_std
      value: 39.89010281154022
    - type: nauc_recall_at_3_diff1
      value: 12.899528818113637
    - type: nauc_recall_at_3_max
      value: 8.28585216953564
    - type: nauc_recall_at_3_std
      value: 37.08629996376381
    - type: nauc_recall_at_5_diff1
      value: 11.563236139458516
    - type: nauc_recall_at_5_max
      value: 11.538181694931673
    - type: nauc_recall_at_5_std
      value: 38.993087814764436
    - type: ndcg_at_1
      value: 14.860999999999999
    - type: ndcg_at_10
      value: 30.898999999999997
    - type: ndcg_at_100
      value: 30.898999999999997
    - type: ndcg_at_1000
      value: 30.898999999999997
    - type: ndcg_at_20
      value: 30.898999999999997
    - type: ndcg_at_3
      value: 21.929000000000002
    - type: ndcg_at_5
      value: 26.296999999999997
    - type: precision_at_1
      value: 14.860999999999999
    - type: precision_at_10
      value: 6.13
    - type: precision_at_100
      value: 0.613
    - type: precision_at_1000
      value: 0.061
    - type: precision_at_20
      value: 3.065
    - type: precision_at_3
      value: 10.776
    - type: precision_at_5
      value: 8.911
    - type: recall_at_1
      value: 12.895999999999999
    - type: recall_at_10
      value: 50.873999999999995
    - type: recall_at_100
      value: 50.873999999999995
    - type: recall_at_1000
      value: 50.873999999999995
    - type: recall_at_20
      value: 50.873999999999995
    - type: recall_at_3
      value: 27.115000000000002
    - type: recall_at_5
      value: 37.295
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB QuoraRetrieval (default)
      revision: e4e08e0b7dbe3c8700f0daef558ff32256715259
      split: test
      type: mteb/quora
    metrics:
    - type: ndcg_at_1
      value: 78.0
    - type: ndcg_at_3
      value: 82.401
    - type: ndcg_at_5
      value: 84.207
    - type: ndcg_at_10
      value: 85.593
    - type: ndcg_at_20
      value: 85.488
    - type: ndcg_at_100
      value: 85.468
    - type: ndcg_at_1000
      value: 85.468
    - type: map_at_1
      value: 67.60000000000001
    - type: map_at_3
      value: 78.46
    - type: map_at_5
      value: 80.43599999999999
    - type: map_at_10
      value: 81.572
    - type: map_at_20
      value: 81.572
    - type: map_at_100
      value: 81.572
    - type: map_at_1000
      value: 81.572
    - type: recall_at_1
      value: 67.60000000000001
    - type: recall_at_3
      value: 84.432
    - type: recall_at_5
      value: 89.427
    - type: recall_at_10
      value: 93.476
    - type: recall_at_20
      value: 93.476
    - type: recall_at_100
      value: 93.476
    - type: recall_at_1000
      value: 93.476
    - type: precision_at_1
      value: 78.0
    - type: precision_at_3
      value: 36.197
    - type: precision_at_5
      value: 23.98
    - type: precision_at_10
      value: 13.135
    - type: precision_at_20
      value: 6.567
    - type: precision_at_100
      value: 1.314
    - type: precision_at_1000
      value: 0.131
    - type: mrr_at_1
      value: 78.0
    - type: mrr_at_3
      value: 83.5317
    - type: mrr_at_5
      value: 84.31269999999999
    - type: mrr_at_10
      value: 84.64620000000001
    - type: mrr_at_20
      value: 84.64620000000001
    - type: mrr_at_100
      value: 84.64620000000001
    - type: mrr_at_1000
      value: 84.64620000000001
    - type: nauc_ndcg_at_1_max
      value: 30.617
    - type: nauc_ndcg_at_1_std
      value: 59.9529
    - type: nauc_ndcg_at_1_diff1
      value: 75.92750000000001
    - type: nauc_ndcg_at_3_max
      value: 27.608700000000002
    - type: nauc_ndcg_at_3_std
      value: 66.5897
    - type: nauc_ndcg_at_3_diff1
      value: 73.9268
    - type: nauc_ndcg_at_5_max
      value: 28.2295
    - type: nauc_ndcg_at_5_std
      value: 68.7466
    - type: nauc_ndcg_at_5_diff1
      value: 74.6303
    - type: nauc_ndcg_at_10_max
      value: 28.994999999999997
    - type: nauc_ndcg_at_10_std
      value: 68.1565
    - type: nauc_ndcg_at_10_diff1
      value: 74.4919
    - type: nauc_ndcg_at_20_max
      value: 28.8589
    - type: nauc_ndcg_at_20_std
      value: 68.4594
    - type: nauc_ndcg_at_20_diff1
      value: 74.6661
    - type: nauc_ndcg_at_100_max
      value: 28.8487
    - type: nauc_ndcg_at_100_std
      value: 68.5093
    - type: nauc_ndcg_at_100_diff1
      value: 74.695
    - type: nauc_ndcg_at_1000_max
      value: 28.8487
    - type: nauc_ndcg_at_1000_std
      value: 68.5093
    - type: nauc_ndcg_at_1000_diff1
      value: 74.695
    - type: nauc_map_at_1_max
      value: 19.267300000000002
    - type: nauc_map_at_1_std
      value: 51.0356
    - type: nauc_map_at_1_diff1
      value: 78.5108
    - type: nauc_map_at_3_max
      value: 24.6596
    - type: nauc_map_at_3_std
      value: 65.8186
    - type: nauc_map_at_3_diff1
      value: 75.7255
    - type: nauc_map_at_5_max
      value: 26.055400000000002
    - type: nauc_map_at_5_std
      value: 67.5997
    - type: nauc_map_at_5_diff1
      value: 75.5646
    - type: nauc_map_at_10_max
      value: 27.053700000000003
    - type: nauc_map_at_10_std
      value: 67.1107
    - type: nauc_map_at_10_diff1
      value: 75.2295
    - type: nauc_map_at_20_max
      value: 27.053700000000003
    - type: nauc_map_at_20_std
      value: 67.1107
    - type: nauc_map_at_20_diff1
      value: 75.2295
    - type: nauc_map_at_100_max
      value: 27.053700000000003
    - type: nauc_map_at_100_std
      value: 67.1107
    - type: nauc_map_at_100_diff1
      value: 75.2295
    - type: nauc_map_at_1000_max
      value: 27.053700000000003
    - type: nauc_map_at_1000_std
      value: 67.1107
    - type: nauc_map_at_1000_diff1
      value: 75.2295
    - type: nauc_recall_at_1_max
      value: 19.267300000000002
    - type: nauc_recall_at_1_std
      value: 51.0356
    - type: nauc_recall_at_1_diff1
      value: 78.5108
    - type: nauc_recall_at_3_max
      value: 22.2587
    - type: nauc_recall_at_3_std
      value: 71.23519999999999
    - type: nauc_recall_at_3_diff1
      value: 71.9533
    - type: nauc_recall_at_5_max
      value: 24.665699999999998
    - type: nauc_recall_at_5_std
      value: 79.4077
    - type: nauc_recall_at_5_diff1
      value: 71.4712
    - type: nauc_recall_at_10_max
      value: 27.0854
    - type: nauc_recall_at_10_std
      value: 81.76480000000001
    - type: nauc_recall_at_10_diff1
      value: 69.0039
    - type: nauc_recall_at_20_max
      value: 27.0854
    - type: nauc_recall_at_20_std
      value: 81.76480000000001
    - type: nauc_recall_at_20_diff1
      value: 69.0039
    - type: nauc_recall_at_100_max
      value: 27.0854
    - type: nauc_recall_at_100_std
      value: 81.76480000000001
    - type: nauc_recall_at_100_diff1
      value: 69.0039
    - type: nauc_recall_at_1000_max
      value: 27.0854
    - type: nauc_recall_at_1000_std
      value: 81.76480000000001
    - type: nauc_recall_at_1000_diff1
      value: 69.0039
    - type: nauc_precision_at_1_max
      value: 30.617
    - type: nauc_precision_at_1_std
      value: 59.9529
    - type: nauc_precision_at_1_diff1
      value: 75.92750000000001
    - type: nauc_precision_at_3_max
      value: 13.8832
    - type: nauc_precision_at_3_std
      value: 16.9205
    - type: nauc_precision_at_3_diff1
      value: -9.7836
    - type: nauc_precision_at_5_max
      value: 9.6618
    - type: nauc_precision_at_5_std
      value: 2.4254000000000002
    - type: nauc_precision_at_5_diff1
      value: -24.1086
    - type: nauc_precision_at_10_max
      value: 6.5817
    - type: nauc_precision_at_10_std
      value: -12.1641
    - type: nauc_precision_at_10_diff1
      value: -33.4816
    - type: nauc_precision_at_20_max
      value: 6.5817
    - type: nauc_precision_at_20_std
      value: -12.1641
    - type: nauc_precision_at_20_diff1
      value: -33.4816
    - type: nauc_precision_at_100_max
      value: 6.5817
    - type: nauc_precision_at_100_std
      value: -12.1641
    - type: nauc_precision_at_100_diff1
      value: -33.4816
    - type: nauc_precision_at_1000_max
      value: 6.5817
    - type: nauc_precision_at_1000_std
      value: -12.1641
    - type: nauc_precision_at_1000_diff1
      value: -33.4816
    - type: nauc_mrr_at_1_max
      value: 30.617
    - type: nauc_mrr_at_1_std
      value: 59.9529
    - type: nauc_mrr_at_1_diff1
      value: 75.92750000000001
    - type: nauc_mrr_at_3_max
      value: 31.589499999999997
    - type: nauc_mrr_at_3_std
      value: 63.825900000000004
    - type: nauc_mrr_at_3_diff1
      value: 74.3887
    - type: nauc_mrr_at_5_max
      value: 32.0469
    - type: nauc_mrr_at_5_std
      value: 64.0228
    - type: nauc_mrr_at_5_diff1
      value: 74.6629
    - type: nauc_mrr_at_10_max
      value: 31.972
    - type: nauc_mrr_at_10_std
      value: 63.7017
    - type: nauc_mrr_at_10_diff1
      value: 74.6159
    - type: nauc_mrr_at_20_max
      value: 31.972
    - type: nauc_mrr_at_20_std
      value: 63.7017
    - type: nauc_mrr_at_20_diff1
      value: 74.6159
    - type: nauc_mrr_at_100_max
      value: 31.972
    - type: nauc_mrr_at_100_std
      value: 63.7017
    - type: nauc_mrr_at_100_diff1
      value: 74.6159
    - type: nauc_mrr_at_1000_max
      value: 31.972
    - type: nauc_mrr_at_1000_std
      value: 63.7017
    - type: nauc_mrr_at_1000_diff1
      value: 74.6159
    - type: main_score
      value: 85.593
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB RedditClustering (default)
      revision: 24640382cdbf8abc73003fb0fa6d111a705499eb
      split: test
      type: mteb/reddit-clustering
    metrics:
    - type: main_score
      value: 56.563999411405256
    - type: v_measure
      value: 56.563999411405256
    - type: v_measure_std
      value: 6.1670948336787035
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB RedditClusteringP2P (default)
      revision: 385e3cb46b4cfa89021f56c4380204149d0efe33
      split: test
      type: mteb/reddit-clustering-p2p
    metrics:
    - type: main_score
      value: 60.732475591924974
    - type: v_measure
      value: 60.732475591924974
    - type: v_measure_std
      value: 13.590843326123492
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB SCIDOCS (default)
      revision: f8c2fcf00f625baaa80f62ec5bd9e1fff3b8ae88
      split: test
      type: mteb/scidocs
    metrics:
    - type: main_score
      value: 20.727999999999998
    - type: map_at_1
      value: 4.878
    - type: map_at_10
      value: 12.370000000000001
    - type: map_at_100
      value: 12.370000000000001
    - type: map_at_1000
      value: 12.370000000000001
    - type: map_at_20
      value: 12.370000000000001
    - type: map_at_3
      value: 8.860999999999999
    - type: map_at_5
      value: 10.5
    - type: mrr_at_1
      value: 24.0
    - type: mrr_at_10
      value: 34.90849206349204
    - type: mrr_at_100
      value: 34.90849206349204
    - type: mrr_at_1000
      value: 34.90849206349204
    - type: mrr_at_20
      value: 34.90849206349204
    - type: mrr_at_3
      value: 31.599999999999994
    - type: mrr_at_5
      value: 33.33999999999997
    - type: nauc_map_at_1000_diff1
      value: 17.97067870729482
    - type: nauc_map_at_1000_max
      value: 26.161331922856835
    - type: nauc_map_at_1000_std
      value: 43.00914668954335
    - type: nauc_map_at_100_diff1
      value: 17.97067870729482
    - type: nauc_map_at_100_max
      value: 26.161331922856835
    - type: nauc_map_at_100_std
      value: 43.00914668954335
    - type: nauc_map_at_10_diff1
      value: 17.97067870729482
    - type: nauc_map_at_10_max
      value: 26.161331922856835
    - type: nauc_map_at_10_std
      value: 43.00914668954335
    - type: nauc_map_at_1_diff1
      value: 23.717136565539256
    - type: nauc_map_at_1_max
      value: 20.004790329056036
    - type: nauc_map_at_1_std
      value: 32.754552797377514
    - type: nauc_map_at_20_diff1
      value: 17.97067870729482
    - type: nauc_map_at_20_max
      value: 26.161331922856835
    - type: nauc_map_at_20_std
      value: 43.00914668954335
    - type: nauc_map_at_3_diff1
      value: 18.840836551520567
    - type: nauc_map_at_3_max
      value: 24.214203185284763
    - type: nauc_map_at_3_std
      value: 39.9163828469076
    - type: nauc_map_at_5_diff1
      value: 19.195456152846337
    - type: nauc_map_at_5_max
      value: 26.011910697888744
    - type: nauc_map_at_5_std
      value: 42.85270866133123
    - type: nauc_mrr_at_1000_diff1
      value: 20.137997523439164
    - type: nauc_mrr_at_1000_max
      value: 22.775220696603114
    - type: nauc_mrr_at_1000_std
      value: 35.87274883845989
    - type: nauc_mrr_at_100_diff1
      value: 20.137997523439164
    - type: nauc_mrr_at_100_max
      value: 22.775220696603114
    - type: nauc_mrr_at_100_std
      value: 35.87274883845989
    - type: nauc_mrr_at_10_diff1
      value: 20.137997523439164
    - type: nauc_mrr_at_10_max
      value: 22.775220696603114
    - type: nauc_mrr_at_10_std
      value: 35.87274883845989
    - type: nauc_mrr_at_1_diff1
      value: 23.719146896716996
    - type: nauc_mrr_at_1_max
      value: 20.206086748142834
    - type: nauc_mrr_at_1_std
      value: 32.85286364725618
    - type: nauc_mrr_at_20_diff1
      value: 20.137997523439164
    - type: nauc_mrr_at_20_max
      value: 22.775220696603114
    - type: nauc_mrr_at_20_std
      value: 35.87274883845989
    - type: nauc_mrr_at_3_diff1
      value: 21.025716417092386
    - type: nauc_mrr_at_3_max
      value: 22.053834284158903
    - type: nauc_mrr_at_3_std
      value: 35.973836736703554
    - type: nauc_mrr_at_5_diff1
      value: 20.484591125376063
    - type: nauc_mrr_at_5_max
      value: 22.821159127038758
    - type: nauc_mrr_at_5_std
      value: 36.25854281263094
    - type: nauc_ndcg_at_1000_diff1
      value: 16.785756236263186
    - type: nauc_ndcg_at_1000_max
      value: 26.074702216001693
    - type: nauc_ndcg_at_1000_std
      value: 40.738872281128145
    - type: nauc_ndcg_at_100_diff1
      value: 16.785756236263186
    - type: nauc_ndcg_at_100_max
      value: 26.074702216001693
    - type: nauc_ndcg_at_100_std
      value: 40.738872281128145
    - type: nauc_ndcg_at_10_diff1
      value: 16.785756236263186
    - type: nauc_ndcg_at_10_max
      value: 26.074702216001693
    - type: nauc_ndcg_at_10_std
      value: 40.738872281128145
    - type: nauc_ndcg_at_1_diff1
      value: 23.719146896716996
    - type: nauc_ndcg_at_1_max
      value: 20.206086748142834
    - type: nauc_ndcg_at_1_std
      value: 32.85286364725618
    - type: nauc_ndcg_at_20_diff1
      value: 16.785756236263186
    - type: nauc_ndcg_at_20_max
      value: 26.074702216001693
    - type: nauc_ndcg_at_20_std
      value: 40.738872281128145
    - type: nauc_ndcg_at_3_diff1
      value: 18.780279884377848
    - type: nauc_ndcg_at_3_max
      value: 23.745537887847927
    - type: nauc_ndcg_at_3_std
      value: 39.13539347388426
    - type: nauc_ndcg_at_5_diff1
      value: 18.72450619034967
    - type: nauc_ndcg_at_5_max
      value: 25.928084190875783
    - type: nauc_ndcg_at_5_std
      value: 41.576155581240656
    - type: nauc_precision_at_1000_diff1
      value: 11.861865483253718
    - type: nauc_precision_at_1000_max
      value: 25.814601321692148
    - type: nauc_precision_at_1000_std
      value: 38.44212773141668
    - type: nauc_precision_at_100_diff1
      value: 11.861865483253759
    - type: nauc_precision_at_100_max
      value: 25.81460132169217
    - type: nauc_precision_at_100_std
      value: 38.44212773141675
    - type: nauc_precision_at_10_diff1
      value: 11.861865483253725
    - type: nauc_precision_at_10_max
      value: 25.81460132169217
    - type: nauc_precision_at_10_std
      value: 38.44212773141671
    - type: nauc_precision_at_1_diff1
      value: 23.719146896716996
    - type: nauc_precision_at_1_max
      value: 20.206086748142834
    - type: nauc_precision_at_1_std
      value: 32.85286364725618
    - type: nauc_precision_at_20_diff1
      value: 11.861865483253725
    - type: nauc_precision_at_20_max
      value: 25.81460132169217
    - type: nauc_precision_at_20_std
      value: 38.44212773141671
    - type: nauc_precision_at_3_diff1
      value: 16.678662085496384
    - type: nauc_precision_at_3_max
      value: 24.872231013595773
    - type: nauc_precision_at_3_std
      value: 40.794589183898054
    - type: nauc_precision_at_5_diff1
      value: 16.19521289185321
    - type: nauc_precision_at_5_max
      value: 27.477995686386752
    - type: nauc_precision_at_5_std
      value: 42.89158033200487
    - type: nauc_recall_at_1000_diff1
      value: 11.931707274736231
    - type: nauc_recall_at_1000_max
      value: 25.861692373596018
    - type: nauc_recall_at_1000_std
      value: 38.62238328559499
    - type: nauc_recall_at_100_diff1
      value: 11.931707274736231
    - type: nauc_recall_at_100_max
      value: 25.861692373596018
    - type: nauc_recall_at_100_std
      value: 38.62238328559499
    - type: nauc_recall_at_10_diff1
      value: 11.931707274736231
    - type: nauc_recall_at_10_max
      value: 25.861692373596018
    - type: nauc_recall_at_10_std
      value: 38.62238328559499
    - type: nauc_recall_at_1_diff1
      value: 23.717136565539256
    - type: nauc_recall_at_1_max
      value: 20.004790329056036
    - type: nauc_recall_at_1_std
      value: 32.754552797377514
    - type: nauc_recall_at_20_diff1
      value: 11.931707274736231
    - type: nauc_recall_at_20_max
      value: 25.861692373596018
    - type: nauc_recall_at_20_std
      value: 38.62238328559499
    - type: nauc_recall_at_3_diff1
      value: 16.64008550911533
    - type: nauc_recall_at_3_max
      value: 24.828659295243373
    - type: nauc_recall_at_3_std
      value: 40.77341283589571
    - type: nauc_recall_at_5_diff1
      value: 16.16345717375489
    - type: nauc_recall_at_5_max
      value: 27.41151086760616
    - type: nauc_recall_at_5_std
      value: 42.88808677062544
    - type: ndcg_at_1
      value: 24.0
    - type: ndcg_at_10
      value: 20.727999999999998
    - type: ndcg_at_100
      value: 20.727999999999998
    - type: ndcg_at_1000
      value: 20.727999999999998
    - type: ndcg_at_20
      value: 20.727999999999998
    - type: ndcg_at_3
      value: 19.67
    - type: ndcg_at_5
      value: 16.999
    - type: precision_at_1
      value: 24.0
    - type: precision_at_10
      value: 10.8
    - type: precision_at_100
      value: 1.08
    - type: precision_at_1000
      value: 0.108
    - type: precision_at_20
      value: 5.4
    - type: precision_at_3
      value: 18.433
    - type: precision_at_5
      value: 14.860000000000001
    - type: recall_at_1
      value: 4.878
    - type: recall_at_10
      value: 21.881999999999998
    - type: recall_at_100
      value: 21.881999999999998
    - type: recall_at_1000
      value: 21.881999999999998
    - type: recall_at_20
      value: 21.881999999999998
    - type: recall_at_3
      value: 11.208
    - type: recall_at_5
      value: 15.052999999999999
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB SICK-R (default)
      revision: 20a6d6f312dd54037fe07a32d58e5e168867909d
      split: test
      type: mteb/sickr-sts
    metrics:
    - type: cosine_pearson
      value: 86.0269970791892
    - type: cosine_spearman
      value: 81.36873767508527
    - type: euclidean_pearson
      value: 81.57400744418666
    - type: euclidean_spearman
      value: 79.08980765847467
    - type: main_score
      value: 81.36873767508527
    - type: manhattan_pearson
      value: 81.54632490757105
    - type: manhattan_spearman
      value: 79.06019542476972
    - type: pearson
      value: 86.0269970791892
    - type: spearman
      value: 81.36873767508527
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STS12 (default)
      revision: a0d554a64d88156834ff5ae9920b964011b16384
      split: test
      type: mteb/sts12-sts
    metrics:
    - type: cosine_pearson
      value: 85.25985770253367
    - type: cosine_spearman
      value: 77.45400815401887
    - type: euclidean_pearson
      value: 81.67921253124989
    - type: euclidean_spearman
      value: 74.6135246966779
    - type: main_score
      value: 77.45400815401887
    - type: manhattan_pearson
      value: 81.67836062660673
    - type: manhattan_spearman
      value: 74.62653342164315
    - type: pearson
      value: 85.25985770253367
    - type: spearman
      value: 77.45400815401887
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STS13 (default)
      revision: 7e90230a92c190f1bf69ae9002b8cea547a64cca
      split: test
      type: mteb/sts13-sts
    metrics:
    - type: cosine_pearson
      value: 86.7886676118868
    - type: cosine_spearman
      value: 87.64018967277866
    - type: euclidean_pearson
      value: 83.47081973425901
    - type: euclidean_spearman
      value: 84.3810745435261
    - type: main_score
      value: 87.64018967277866
    - type: manhattan_pearson
      value: 83.4327600900413
    - type: manhattan_spearman
      value: 84.34512037980309
    - type: pearson
      value: 86.7886676118868
    - type: spearman
      value: 87.64018967277866
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STS14 (default)
      revision: 6031580fec1f6af667f0bd2da0a551cf4f0b2375
      split: test
      type: mteb/sts14-sts
    metrics:
    - type: cosine_pearson
      value: 84.10234455679756
    - type: cosine_spearman
      value: 81.78001363078037
    - type: euclidean_pearson
      value: 80.55751823959416
    - type: euclidean_spearman
      value: 80.45028560326892
    - type: main_score
      value: 81.78001363078037
    - type: manhattan_pearson
      value: 80.51019497048573
    - type: manhattan_spearman
      value: 80.41541170811205
    - type: pearson
      value: 84.10234455679756
    - type: spearman
      value: 81.78001363078037
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STS15 (default)
      revision: ae752c7c21bf194d8b67fd573edf7ae58183cbe3
      split: test
      type: mteb/sts15-sts
    metrics:
    - type: cosine_pearson
      value: 86.24583008347872
    - type: cosine_spearman
      value: 87.42688820214872
    - type: euclidean_pearson
      value: 85.36370813181506
    - type: euclidean_spearman
      value: 85.78082510360461
    - type: main_score
      value: 87.42688820214872
    - type: manhattan_pearson
      value: 85.36144526244301
    - type: manhattan_spearman
      value: 85.78230958155174
    - type: pearson
      value: 86.24583008347872
    - type: spearman
      value: 87.42688820214872
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STS16 (default)
      revision: 4d8694f8f0e0100860b497b999b3dbed754a0513
      split: test
      type: mteb/sts16-sts
    metrics:
    - type: cosine_pearson
      value: 81.68984155246952
    - type: cosine_spearman
      value: 83.970863457005
    - type: euclidean_pearson
      value: 81.91870217841057
    - type: euclidean_spearman
      value: 82.41069679087725
    - type: main_score
      value: 83.970863457005
    - type: manhattan_pearson
      value: 81.9245471592128
    - type: manhattan_spearman
      value: 82.42170950112732
    - type: pearson
      value: 81.68984155246952
    - type: spearman
      value: 83.970863457005
    task:
      type: STS
  - dataset:
      config: en-en
      name: MTEB STS17 (en-en)
      revision: faeb762787bd10488a50c8b5be4a3b82e411949c
      split: test
      type: mteb/sts17-crosslingual-sts
    metrics:
    - type: cosine_pearson
      value: 89.22630618384098
    - type: cosine_spearman
      value: 89.55532464161708
    - type: euclidean_pearson
      value: 84.10050072614472
    - type: euclidean_spearman
      value: 82.9773002217096
    - type: main_score
      value: 89.55532464161708
    - type: manhattan_pearson
      value: 84.14335843909228
    - type: manhattan_spearman
      value: 83.06905567845092
    - type: pearson
      value: 89.22630618384098
    - type: spearman
      value: 89.55532464161708
    task:
      type: STS
  - dataset:
      config: en
      name: MTEB STS22 (en)
      revision: de9d86b3b84231dc21f76c7b7af1f28e2f57f6e3
      split: test
      type: mteb/sts22-crosslingual-sts
    metrics:
    - type: cosine_pearson
      value: 64.43263997124191
    - type: cosine_spearman
      value: 66.15539887914254
    - type: euclidean_pearson
      value: 66.22842223425695
    - type: euclidean_spearman
      value: 66.01793713171296
    - type: main_score
      value: 66.15539887914254
    - type: manhattan_pearson
      value: 66.3284277890772
    - type: manhattan_spearman
      value: 66.0345399715446
    - type: pearson
      value: 64.43263997124191
    - type: spearman
      value: 66.15539887914254
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STSBenchmark (default)
      revision: b0fddb56ed78048fa8b90373c8a3cfc37b684831
      split: test
      type: mteb/stsbenchmark-sts
    metrics:
    - type: cosine_pearson
      value: 86.0935153349381
    - type: cosine_spearman
      value: 87.08398903339372
    - type: euclidean_pearson
      value: 83.22409901787037
    - type: euclidean_spearman
      value: 83.41678723220834
    - type: main_score
      value: 87.08398903339372
    - type: manhattan_pearson
      value: 83.23258942312405
    - type: manhattan_spearman
      value: 83.40419631467316
    - type: pearson
      value: 86.0935153349381
    - type: spearman
      value: 87.08398903339372
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB SciDocsRR (default)
      revision: d3c5e1fc0b855ab6097bf1cda04dd73947d7caab
      split: test
      type: mteb/scidocs-reranking
    metrics:
    - type: main_score
      value: 85.8948614343356
    - type: map
      value: 85.8948614343356
    - type: mrr
      value: 95.91610005825692
    - type: nAUC_map_diff1
      value: -2.8334627803792345
    - type: nAUC_map_max
      value: 50.484912982863605
    - type: nAUC_map_std
      value: 66.63254925785498
    - type: nAUC_mrr_diff1
      value: 38.85837517748082
    - type: nAUC_mrr_max
      value: 81.29713071012934
    - type: nAUC_mrr_std
      value: 75.68076182213787
    task:
      type: Reranking
  - dataset:
      config: default
      name: MTEB SciFact (default)
      revision: 0228b52cf27578f30900b9e5271d331663a030d7
      split: test
      type: mteb/scifact
    metrics:
    - type: main_score
      value: 69.703
    - type: map_at_1
      value: 54.31700000000001
    - type: map_at_10
      value: 64.95400000000001
    - type: map_at_100
      value: 64.95400000000001
    - type: map_at_1000
      value: 64.95400000000001
    - type: map_at_20
      value: 64.95400000000001
    - type: map_at_3
      value: 61.919999999999995
    - type: map_at_5
      value: 63.965
    - type: mrr_at_1
      value: 56.333333333333336
    - type: mrr_at_10
      value: 65.63637566137565
    - type: mrr_at_100
      value: 65.63637566137565
    - type: mrr_at_1000
      value: 65.63637566137565
    - type: mrr_at_20
      value: 65.63637566137565
    - type: mrr_at_3
      value: 63.44444444444445
    - type: mrr_at_5
      value: 64.96111111111111
    - type: nauc_map_at_1000_diff1
      value: 65.22837738897331
    - type: nauc_map_at_1000_max
      value: 40.872733013104636
    - type: nauc_map_at_1000_std
      value: 62.44914817883753
    - type: nauc_map_at_100_diff1
      value: 65.22837738897331
    - type: nauc_map_at_100_max
      value: 40.872733013104636
    - type: nauc_map_at_100_std
      value: 62.44914817883753
    - type: nauc_map_at_10_diff1
      value: 65.22837738897331
    - type: nauc_map_at_10_max
      value: 40.872733013104636
    - type: nauc_map_at_10_std
      value: 62.44914817883753
    - type: nauc_map_at_1_diff1
      value: 70.5041051135825
    - type: nauc_map_at_1_max
      value: 35.23259161029537
    - type: nauc_map_at_1_std
      value: 58.45260616767192
    - type: nauc_map_at_20_diff1
      value: 65.22837738897331
    - type: nauc_map_at_20_max
      value: 40.872733013104636
    - type: nauc_map_at_20_std
      value: 62.44914817883753
    - type: nauc_map_at_3_diff1
      value: 66.04310284080623
    - type: nauc_map_at_3_max
      value: 37.67008479058897
    - type: nauc_map_at_3_std
      value: 61.36236474678161
    - type: nauc_map_at_5_diff1
      value: 65.24508604306527
    - type: nauc_map_at_5_max
      value: 39.45095019850351
    - type: nauc_map_at_5_std
      value: 62.59702960778946
    - type: nauc_mrr_at_1000_diff1
      value: 64.5997453509139
    - type: nauc_mrr_at_1000_max
      value: 43.402688042587876
    - type: nauc_mrr_at_1000_std
      value: 63.25576714638942
    - type: nauc_mrr_at_100_diff1
      value: 64.5997453509139
    - type: nauc_mrr_at_100_max
      value: 43.402688042587876
    - type: nauc_mrr_at_100_std
      value: 63.25576714638942
    - type: nauc_mrr_at_10_diff1
      value: 64.5997453509139
    - type: nauc_mrr_at_10_max
      value: 43.402688042587876
    - type: nauc_mrr_at_10_std
      value: 63.25576714638942
    - type: nauc_mrr_at_1_diff1
      value: 68.50178319569564
    - type: nauc_mrr_at_1_max
      value: 42.877427259387304
    - type: nauc_mrr_at_1_std
      value: 59.92439820113308
    - type: nauc_mrr_at_20_diff1
      value: 64.5997453509139
    - type: nauc_mrr_at_20_max
      value: 43.402688042587876
    - type: nauc_mrr_at_20_std
      value: 63.25576714638942
    - type: nauc_mrr_at_3_diff1
      value: 64.69713993780067
    - type: nauc_mrr_at_3_max
      value: 42.83850142815548
    - type: nauc_mrr_at_3_std
      value: 63.312481132092316
    - type: nauc_mrr_at_5_diff1
      value: 64.18057887702805
    - type: nauc_mrr_at_5_max
      value: 43.32021308104036
    - type: nauc_mrr_at_5_std
      value: 63.14210906717498
    - type: nauc_ndcg_at_1000_diff1
      value: 63.538570933656025
    - type: nauc_ndcg_at_1000_max
      value: 42.425810618870955
    - type: nauc_ndcg_at_1000_std
      value: 64.61882286565893
    - type: nauc_ndcg_at_100_diff1
      value: 63.538570933656025
    - type: nauc_ndcg_at_100_max
      value: 42.425810618870955
    - type: nauc_ndcg_at_100_std
      value: 64.61882286565893
    - type: nauc_ndcg_at_10_diff1
      value: 63.538570933656025
    - type: nauc_ndcg_at_10_max
      value: 42.425810618870955
    - type: nauc_ndcg_at_10_std
      value: 64.61882286565893
    - type: nauc_ndcg_at_1_diff1
      value: 68.50178319569564
    - type: nauc_ndcg_at_1_max
      value: 42.877427259387304
    - type: nauc_ndcg_at_1_std
      value: 59.92439820113308
    - type: nauc_ndcg_at_20_diff1
      value: 63.538570933656025
    - type: nauc_ndcg_at_20_max
      value: 42.425810618870955
    - type: nauc_ndcg_at_20_std
      value: 64.61882286565893
    - type: nauc_ndcg_at_3_diff1
      value: 64.25647597910896
    - type: nauc_ndcg_at_3_max
      value: 40.04753188513075
    - type: nauc_ndcg_at_3_std
      value: 63.128378209111645
    - type: nauc_ndcg_at_5_diff1
      value: 63.25187832422353
    - type: nauc_ndcg_at_5_max
      value: 40.776757987127866
    - type: nauc_ndcg_at_5_std
      value: 64.66473344248938
    - type: nauc_precision_at_1000_diff1
      value: 8.119523892120991
    - type: nauc_precision_at_1000_max
      value: 49.77755692339431
    - type: nauc_precision_at_1000_std
      value: 29.21200301903778
    - type: nauc_precision_at_100_diff1
      value: 8.119523892120945
    - type: nauc_precision_at_100_max
      value: 49.777556923394286
    - type: nauc_precision_at_100_std
      value: 29.21200301903769
    - type: nauc_precision_at_10_diff1
      value: 8.119523892120908
    - type: nauc_precision_at_10_max
      value: 49.777556923394165
    - type: nauc_precision_at_10_std
      value: 29.212003019037645
    - type: nauc_precision_at_1_diff1
      value: 68.50178319569564
    - type: nauc_precision_at_1_max
      value: 42.877427259387304
    - type: nauc_precision_at_1_std
      value: 59.92439820113308
    - type: nauc_precision_at_20_diff1
      value: 8.119523892120908
    - type: nauc_precision_at_20_max
      value: 49.777556923394165
    - type: nauc_precision_at_20_std
      value: 29.212003019037645
    - type: nauc_precision_at_3_diff1
      value: 39.69797746360505
    - type: nauc_precision_at_3_max
      value: 48.643358220044945
    - type: nauc_precision_at_3_std
      value: 53.584660083729986
    - type: nauc_precision_at_5_diff1
      value: 20.49871350044836
    - type: nauc_precision_at_5_max
      value: 49.24028302990136
    - type: nauc_precision_at_5_std
      value: 43.24051693891073
    - type: nauc_recall_at_1000_diff1
      value: 57.110808810472236
    - type: nauc_recall_at_1000_max
      value: 43.4003442684361
    - type: nauc_recall_at_1000_std
      value: 73.98932716000576
    - type: nauc_recall_at_100_diff1
      value: 57.110808810472236
    - type: nauc_recall_at_100_max
      value: 43.4003442684361
    - type: nauc_recall_at_100_std
      value: 73.98932716000576
    - type: nauc_recall_at_10_diff1
      value: 57.110808810472236
    - type: nauc_recall_at_10_max
      value: 43.4003442684361
    - type: nauc_recall_at_10_std
      value: 73.98932716000576
    - type: nauc_recall_at_1_diff1
      value: 70.5041051135825
    - type: nauc_recall_at_1_max
      value: 35.23259161029537
    - type: nauc_recall_at_1_std
      value: 58.45260616767192
    - type: nauc_recall_at_20_diff1
      value: 57.110808810472236
    - type: nauc_recall_at_20_max
      value: 43.4003442684361
    - type: nauc_recall_at_20_std
      value: 73.98932716000576
    - type: nauc_recall_at_3_diff1
      value: 60.230452898971635
    - type: nauc_recall_at_3_max
      value: 35.611790412544494
    - type: nauc_recall_at_3_std
      value: 66.72680059686319
    - type: nauc_recall_at_5_diff1
      value: 56.7317515771124
    - type: nauc_recall_at_5_max
      value: 38.949369104008284
    - type: nauc_recall_at_5_std
      value: 71.81344707117901
    - type: ndcg_at_1
      value: 56.333
    - type: ndcg_at_10
      value: 69.703
    - type: ndcg_at_100
      value: 69.703
    - type: ndcg_at_1000
      value: 69.703
    - type: ndcg_at_20
      value: 69.703
    - type: ndcg_at_3
      value: 64.821
    - type: ndcg_at_5
      value: 67.782
    - type: precision_at_1
      value: 56.333
    - type: precision_at_10
      value: 9.433
    - type: precision_at_100
      value: 0.943
    - type: precision_at_1000
      value: 0.094
    - type: precision_at_20
      value: 4.717
    - type: precision_at_3
      value: 25.444
    - type: precision_at_5
      value: 17.333000000000002
    - type: recall_at_1
      value: 54.31700000000001
    - type: recall_at_10
      value: 83.089
    - type: recall_at_100
      value: 83.089
    - type: recall_at_1000
      value: 83.089
    - type: recall_at_20
      value: 83.089
    - type: recall_at_3
      value: 70.672
    - type: recall_at_5
      value: 77.73299999999999
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB SprintDuplicateQuestions (default)
      revision: d66bd1f72af766a5cc4b0ca5e00c162f89e8cc46
      split: test
      type: mteb/sprintduplicatequestions-pairclassification
    metrics:
    - type: cosine_accuracy
      value: 99.64851485148515
    - type: cosine_accuracy_threshold
      value: 92.19269752502441
    - type: cosine_ap
      value: 88.69154011402345
    - type: cosine_f1
      value: 81.13804004214963
    - type: cosine_f1_threshold
      value: 91.52623414993286
    - type: cosine_precision
      value: 85.74610244988864
    - type: cosine_recall
      value: 77.0
    - type: dot_accuracy
      value: 99.04653465346534
    - type: dot_accuracy_threshold
      value: 315292.87109375
    - type: dot_ap
      value: 22.15898294209448
    - type: dot_f1
      value: 28.826151560178303
    - type: dot_f1_threshold
      value: 272924.4384765625
    - type: dot_precision
      value: 28.55740922473013
    - type: dot_recall
      value: 29.099999999999998
    - type: euclidean_accuracy
      value: 99.62376237623762
    - type: euclidean_accuracy_threshold
      value: 2124.1966247558594
    - type: euclidean_ap
      value: 86.01320134732376
    - type: euclidean_f1
      value: 79.39590075512406
    - type: euclidean_f1_threshold
      value: 2135.161590576172
    - type: euclidean_precision
      value: 86.18266978922716
    - type: euclidean_recall
      value: 73.6
    - type: main_score
      value: 88.69154011402345
    - type: manhattan_accuracy
      value: 99.62475247524752
    - type: manhattan_accuracy_threshold
      value: 113582.91015625
    - type: manhattan_ap
      value: 85.96834733070928
    - type: manhattan_f1
      value: 79.43874797625472
    - type: manhattan_f1_threshold
      value: 114967.529296875
    - type: manhattan_precision
      value: 86.28370457209847
    - type: manhattan_recall
      value: 73.6
    - type: max_accuracy
      value: 99.64851485148515
    - type: max_ap
      value: 88.69154011402345
    - type: max_f1
      value: 81.13804004214963
    - type: max_precision
      value: 86.28370457209847
    - type: max_recall
      value: 77.0
    - type: similarity_accuracy
      value: 99.64851485148515
    - type: similarity_accuracy_threshold
      value: 92.19269752502441
    - type: similarity_ap
      value: 88.69154011402345
    - type: similarity_f1
      value: 81.13804004214963
    - type: similarity_f1_threshold
      value: 91.52623414993286
    - type: similarity_precision
      value: 85.74610244988864
    - type: similarity_recall
      value: 77.0
    task:
      type: PairClassification
  - dataset:
      config: default
      name: MTEB StackExchangeClustering (default)
      revision: 6cbc1f7b2bc0622f2e39d2c77fa502909748c259
      split: test
      type: mteb/stackexchange-clustering
    metrics:
    - type: main_score
      value: 65.15034216633208
    - type: v_measure
      value: 65.15034216633208
    - type: v_measure_std
      value: 2.9260556895091128
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB StackExchangeClusteringP2P (default)
      revision: 815ca46b2622cec33ccafc3735d572c266efdb44
      split: test
      type: mteb/stackexchange-clustering-p2p
    metrics:
    - type: main_score
      value: 35.261818219354694
    - type: v_measure
      value: 35.261818219354694
    - type: v_measure_std
      value: 1.3869630940382127
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB StackOverflowDupQuestions (default)
      revision: e185fbe320c72810689fc5848eb6114e1ef5ec69
      split: test
      type: mteb/stackoverflowdupquestions-reranking
    metrics:
    - type: main_score
      value: 50.37467178394516
    - type: map
      value: 50.37467178394516
    - type: mrr
      value: 51.28756047873695
    - type: nAUC_map_diff1
      value: 39.87451898478182
    - type: nAUC_map_max
      value: 11.804611930616003
    - type: nAUC_map_std
      value: 13.76340221270718
    - type: nAUC_mrr_diff1
      value: 40.13932385996529
    - type: nAUC_mrr_max
      value: 13.129106578982858
    - type: nAUC_mrr_std
      value: 14.185010980115523
    task:
      type: Reranking
  - dataset:
      config: default
      name: MTEB SummEval (default)
      revision: cda12ad7615edc362dbf25a00fdd61d3b1eaf93c
      split: test
      type: mteb/summeval
    metrics:
    - type: cosine_pearson
      value: 31.35722439188129
    - type: cosine_spearman
      value: 30.945782397962617
    - type: dot_pearson
      value: 27.7909187308002
    - type: dot_spearman
      value: 29.106281873575533
    - type: main_score
      value: 30.945782397962617
    - type: pearson
      value: 31.35722439188129
    - type: spearman
      value: 30.945782397962617
    task:
      type: Summarization
  - dataset:
      config: default
      name: MTEB TRECCOVID (default)
      revision: bb9466bac8153a0349341eb1b22e06409e78ef4e
      split: test
      type: mteb/trec-covid
    metrics:
    - type: main_score
      value: 54.503
    - type: map_at_1
      value: 0.199
    - type: map_at_10
      value: 1.234
    - type: map_at_100
      value: 1.234
    - type: map_at_1000
      value: 1.234
    - type: map_at_20
      value: 1.234
    - type: map_at_3
      value: 0.479
    - type: map_at_5
      value: 0.692
    - type: mrr_at_1
      value: 74.0
    - type: mrr_at_10
      value: 82.46666666666667
    - type: mrr_at_100
      value: 82.46666666666667
    - type: mrr_at_1000
      value: 82.46666666666667
    - type: mrr_at_20
      value: 82.46666666666667
    - type: mrr_at_3
      value: 81.0
    - type: mrr_at_5
      value: 81.8
    - type: nauc_map_at_1000_diff1
      value: 27.81989678998043
    - type: nauc_map_at_1000_max
      value: 23.911921661037432
    - type: nauc_map_at_1000_std
      value: 12.714572736978939
    - type: nauc_map_at_100_diff1
      value: 27.81989678998043
    - type: nauc_map_at_100_max
      value: 23.911921661037432
    - type: nauc_map_at_100_std
      value: 12.714572736978939
    - type: nauc_map_at_10_diff1
      value: 27.81989678998043
    - type: nauc_map_at_10_max
      value: 23.911921661037432
    - type: nauc_map_at_10_std
      value: 12.714572736978939
    - type: nauc_map_at_1_diff1
      value: 17.448754646136024
    - type: nauc_map_at_1_max
      value: 1.6380934011906896
    - type: nauc_map_at_1_std
      value: 2.4180946829187504
    - type: nauc_map_at_20_diff1
      value: 27.81989678998043
    - type: nauc_map_at_20_max
      value: 23.911921661037432
    - type: nauc_map_at_20_std
      value: 12.714572736978939
    - type: nauc_map_at_3_diff1
      value: 18.18392893746671
    - type: nauc_map_at_3_max
      value: 12.121089455954644
    - type: nauc_map_at_3_std
      value: 2.195566796665004
    - type: nauc_map_at_5_diff1
      value: 23.687325380067957
    - type: nauc_map_at_5_max
      value: 18.842912422299236
    - type: nauc_map_at_5_std
      value: 9.714021456557473
    - type: nauc_mrr_at_1000_diff1
      value: 14.530546315688689
    - type: nauc_mrr_at_1000_max
      value: 39.94379814264016
    - type: nauc_mrr_at_1000_std
      value: 21.424562597409782
    - type: nauc_mrr_at_100_diff1
      value: 14.530546315688689
    - type: nauc_mrr_at_100_max
      value: 39.94379814264016
    - type: nauc_mrr_at_100_std
      value: 21.424562597409782
    - type: nauc_mrr_at_10_diff1
      value: 14.530546315688689
    - type: nauc_mrr_at_10_max
      value: 39.94379814264016
    - type: nauc_mrr_at_10_std
      value: 21.424562597409782
    - type: nauc_mrr_at_1_diff1
      value: 16.50784639714528
    - type: nauc_mrr_at_1_max
      value: 32.68723896030171
    - type: nauc_mrr_at_1_std
      value: 21.361664166092172
    - type: nauc_mrr_at_20_diff1
      value: 14.530546315688689
    - type: nauc_mrr_at_20_max
      value: 39.94379814264016
    - type: nauc_mrr_at_20_std
      value: 21.424562597409782
    - type: nauc_mrr_at_3_diff1
      value: 13.136196384927256
    - type: nauc_mrr_at_3_max
      value: 39.75595126187335
    - type: nauc_mrr_at_3_std
      value: 19.665350629817606
    - type: nauc_mrr_at_5_diff1
      value: 14.26544367303503
    - type: nauc_mrr_at_5_max
      value: 38.7133040910976
    - type: nauc_mrr_at_5_std
      value: 21.440677488921587
    - type: nauc_ndcg_at_1000_diff1
      value: 27.64083530880881
    - type: nauc_ndcg_at_1000_max
      value: 19.106670691291125
    - type: nauc_ndcg_at_1000_std
      value: 17.807818581625128
    - type: nauc_ndcg_at_100_diff1
      value: 19.199707190321107
    - type: nauc_ndcg_at_100_max
      value: 41.725478828182986
    - type: nauc_ndcg_at_100_std
      value: 18.624685771844355
    - type: nauc_ndcg_at_10_diff1
      value: 18.38860659127433
    - type: nauc_ndcg_at_10_max
      value: 43.6468446488598
    - type: nauc_ndcg_at_10_std
      value: 19.9625372920067
    - type: nauc_ndcg_at_1_diff1
      value: 3.388891866302241
    - type: nauc_ndcg_at_1_max
      value: 26.466227200457375
    - type: nauc_ndcg_at_1_std
      value: 11.717312467620623
    - type: nauc_ndcg_at_20_diff1
      value: 18.388606591274296
    - type: nauc_ndcg_at_20_max
      value: 43.646844648859805
    - type: nauc_ndcg_at_20_std
      value: 19.96253729200672
    - type: nauc_ndcg_at_3_diff1
      value: 5.969049373108646
    - type: nauc_ndcg_at_3_max
      value: 41.49122498203156
    - type: nauc_ndcg_at_3_std
      value: 9.093646827477277
    - type: nauc_ndcg_at_5_diff1
      value: 12.619527473649692
    - type: nauc_ndcg_at_5_max
      value: 42.798313835566454
    - type: nauc_ndcg_at_5_std
      value: 14.641100537910063
    - type: nauc_precision_at_1000_diff1
      value: 23.247876915825703
    - type: nauc_precision_at_1000_max
      value: 46.15235706530434
    - type: nauc_precision_at_1000_std
      value: 19.675456389452297
    - type: nauc_precision_at_100_diff1
      value: 23.24787691582566
    - type: nauc_precision_at_100_max
      value: 46.15235706530426
    - type: nauc_precision_at_100_std
      value: 19.67545638945232
    - type: nauc_precision_at_10_diff1
      value: 23.247876915825728
    - type: nauc_precision_at_10_max
      value: 46.15235706530424
    - type: nauc_precision_at_10_std
      value: 19.6754563894523
    - type: nauc_precision_at_1_diff1
      value: 16.50784639714528
    - type: nauc_precision_at_1_max
      value: 32.68723896030171
    - type: nauc_precision_at_1_std
      value: 21.361664166092172
    - type: nauc_precision_at_20_diff1
      value: 23.247876915825728
    - type: nauc_precision_at_20_max
      value: 46.15235706530424
    - type: nauc_precision_at_20_std
      value: 19.6754563894523
    - type: nauc_precision_at_3_diff1
      value: 8.808786115519217
    - type: nauc_precision_at_3_max
      value: 46.05783520995491
    - type: nauc_precision_at_3_std
      value: 7.367943776921311
    - type: nauc_precision_at_5_diff1
      value: 16.12521281535367
    - type: nauc_precision_at_5_max
      value: 44.56508280451944
    - type: nauc_precision_at_5_std
      value: 14.99845225197337
    - type: nauc_recall_at_1000_diff1
      value: 22.782100438856954
    - type: nauc_recall_at_1000_max
      value: 16.95909134589206
    - type: nauc_recall_at_1000_std
      value: 10.860620344690203
    - type: nauc_recall_at_100_diff1
      value: 22.782100438856954
    - type: nauc_recall_at_100_max
      value: 16.95909134589206
    - type: nauc_recall_at_100_std
      value: 10.860620344690203
    - type: nauc_recall_at_10_diff1
      value: 22.782100438856954
    - type: nauc_recall_at_10_max
      value: 16.95909134589206
    - type: nauc_recall_at_10_std
      value: 10.860620344690203
    - type: nauc_recall_at_1_diff1
      value: 17.448754646136024
    - type: nauc_recall_at_1_max
      value: 1.6380934011906896
    - type: nauc_recall_at_1_std
      value: 2.4180946829187504
    - type: nauc_recall_at_20_diff1
      value: 22.782100438856954
    - type: nauc_recall_at_20_max
      value: 16.95909134589206
    - type: nauc_recall_at_20_std
      value: 10.860620344690203
    - type: nauc_recall_at_3_diff1
      value: 15.469592188979666
    - type: nauc_recall_at_3_max
      value: 10.600121243625388
    - type: nauc_recall_at_3_std
      value: 0.8565968533967891
    - type: nauc_recall_at_5_diff1
      value: 20.881534361542567
    - type: nauc_recall_at_5_max
      value: 16.292983808412515
    - type: nauc_recall_at_5_std
      value: 9.455854495272016
    - type: ndcg_at_1
      value: 69.0
    - type: ndcg_at_10
      value: 54.503
    - type: ndcg_at_100
      value: 11.995000000000001
    - type: ndcg_at_1000
      value: 5.2139999999999995
    - type: ndcg_at_20
      value: 35.175
    - type: ndcg_at_3
      value: 60.211999999999996
    - type: ndcg_at_5
      value: 57.38100000000001
    - type: precision_at_1
      value: 74.0
    - type: precision_at_10
      value: 56.599999999999994
    - type: precision_at_100
      value: 5.66
    - type: precision_at_1000
      value: 0.5660000000000001
    - type: precision_at_20
      value: 28.299999999999997
    - type: precision_at_3
      value: 62.0
    - type: precision_at_5
      value: 58.8
    - type: recall_at_1
      value: 0.199
    - type: recall_at_10
      value: 1.514
    - type: recall_at_100
      value: 1.514
    - type: recall_at_1000
      value: 1.514
    - type: recall_at_20
      value: 1.514
    - type: recall_at_3
      value: 0.515
    - type: recall_at_5
      value: 0.782
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB Touche2020 (default)
      revision: a34f9a33db75fa0cbb21bb5cfc3dae8dc8bec93f
      split: test
      type: mteb/touche2020
    metrics:
    - type: main_score
      value: 11.591
    - type: map_at_1
      value: 0.607
    - type: map_at_10
      value: 4.535
    - type: map_at_100
      value: 4.535
    - type: map_at_1000
      value: 4.535
    - type: map_at_20
      value: 4.535
    - type: map_at_3
      value: 1.772
    - type: map_at_5
      value: 2.618
    - type: mrr_at_1
      value: 6.122448979591836
    - type: mrr_at_10
      value: 19.305150631681244
    - type: mrr_at_100
      value: 19.305150631681244
    - type: mrr_at_1000
      value: 19.305150631681244
    - type: mrr_at_20
      value: 19.305150631681244
    - type: mrr_at_3
      value: 16.3265306122449
    - type: mrr_at_5
      value: 17.755102040816325
    - type: nauc_map_at_1000_diff1
      value: -16.479409955326688
    - type: nauc_map_at_1000_max
      value: -50.646390874995284
    - type: nauc_map_at_1000_std
      value: 6.7106586370983194
    - type: nauc_map_at_100_diff1
      value: -16.479409955326688
    - type: nauc_map_at_100_max
      value: -50.646390874995284
    - type: nauc_map_at_100_std
      value: 6.7106586370983194
    - type: nauc_map_at_10_diff1
      value: -16.479409955326688
    - type: nauc_map_at_10_max
      value: -50.646390874995284
    - type: nauc_map_at_10_std
      value: 6.7106586370983194
    - type: nauc_map_at_1_diff1
      value: -44.22946169608924
    - type: nauc_map_at_1_max
      value: -54.782691745683785
    - type: nauc_map_at_1_std
      value: -5.883579383137843
    - type: nauc_map_at_20_diff1
      value: -16.479409955326688
    - type: nauc_map_at_20_max
      value: -50.646390874995284
    - type: nauc_map_at_20_std
      value: 6.7106586370983194
    - type: nauc_map_at_3_diff1
      value: -20.713663006405017
    - type: nauc_map_at_3_max
      value: -53.685960814478776
    - type: nauc_map_at_3_std
      value: -2.2056418515561593
    - type: nauc_map_at_5_diff1
      value: -23.605361611715654
    - type: nauc_map_at_5_max
      value: -52.60589775945657
    - type: nauc_map_at_5_std
      value: 11.410984804084894
    - type: nauc_mrr_at_1000_diff1
      value: -5.912048624399277
    - type: nauc_mrr_at_1000_max
      value: -52.29854345733435
    - type: nauc_mrr_at_1000_std
      value: 20.717107488454257
    - type: nauc_mrr_at_100_diff1
      value: -5.912048624399277
    - type: nauc_mrr_at_100_max
      value: -52.29854345733435
    - type: nauc_mrr_at_100_std
      value: 20.717107488454257
    - type: nauc_mrr_at_10_diff1
      value: -5.912048624399277
    - type: nauc_mrr_at_10_max
      value: -52.29854345733435
    - type: nauc_mrr_at_10_std
      value: 20.717107488454257
    - type: nauc_mrr_at_1_diff1
      value: -47.37253598731851
    - type: nauc_mrr_at_1_max
      value: -53.25477833026534
    - type: nauc_mrr_at_1_std
      value: 8.293440114529961
    - type: nauc_mrr_at_20_diff1
      value: -5.912048624399277
    - type: nauc_mrr_at_20_max
      value: -52.29854345733435
    - type: nauc_mrr_at_20_std
      value: 20.717107488454257
    - type: nauc_mrr_at_3_diff1
      value: -16.44643629641655
    - type: nauc_mrr_at_3_max
      value: -53.296508563826926
    - type: nauc_mrr_at_3_std
      value: 15.11994381483859
    - type: nauc_mrr_at_5_diff1
      value: -8.9955973584155
    - type: nauc_mrr_at_5_max
      value: -49.44314244394265
    - type: nauc_mrr_at_5_std
      value: 19.36026350260547
    - type: nauc_ndcg_at_1000_diff1
      value: -3.6364317946061133
    - type: nauc_ndcg_at_1000_max
      value: -48.67525402407821
    - type: nauc_ndcg_at_1000_std
      value: 19.733342670846852
    - type: nauc_ndcg_at_100_diff1
      value: -3.6364317946061133
    - type: nauc_ndcg_at_100_max
      value: -48.67525402407821
    - type: nauc_ndcg_at_100_std
      value: 19.733342670846852
    - type: nauc_ndcg_at_10_diff1
      value: 0.4952900733177083
    - type: nauc_ndcg_at_10_max
      value: -48.11024941429367
    - type: nauc_ndcg_at_10_std
      value: 22.099762052717857
    - type: nauc_ndcg_at_1_diff1
      value: -47.37253598731851
    - type: nauc_ndcg_at_1_max
      value: -53.25477833026534
    - type: nauc_ndcg_at_1_std
      value: 8.293440114529961
    - type: nauc_ndcg_at_20_diff1
      value: -3.657307845064385
    - type: nauc_ndcg_at_20_max
      value: -48.711089076084605
    - type: nauc_ndcg_at_20_std
      value: 19.64202067892396
    - type: nauc_ndcg_at_3_diff1
      value: -9.306418976525
    - type: nauc_ndcg_at_3_max
      value: -51.36070712483026
    - type: nauc_ndcg_at_3_std
      value: 12.253630884658183
    - type: nauc_ndcg_at_5_diff1
      value: -7.78308105540859
    - type: nauc_ndcg_at_5_max
      value: -49.86221949761615
    - type: nauc_ndcg_at_5_std
      value: 23.02630010130766
    - type: nauc_precision_at_1000_diff1
      value: 13.230521285435918
    - type: nauc_precision_at_1000_max
      value: -44.84903869395813
    - type: nauc_precision_at_1000_std
      value: 26.180973472305862
    - type: nauc_precision_at_100_diff1
      value: 13.230521285435914
    - type: nauc_precision_at_100_max
      value: -44.849038693958136
    - type: nauc_precision_at_100_std
      value: 26.18097347230585
    - type: nauc_precision_at_10_diff1
      value: 13.230521285435884
    - type: nauc_precision_at_10_max
      value: -44.84903869395812
    - type: nauc_precision_at_10_std
      value: 26.180973472305812
    - type: nauc_precision_at_1_diff1
      value: -47.37253598731851
    - type: nauc_precision_at_1_max
      value: -53.25477833026534
    - type: nauc_precision_at_1_std
      value: 8.293440114529961
    - type: nauc_precision_at_20_diff1
      value: 13.230521285435884
    - type: nauc_precision_at_20_max
      value: -44.84903869395812
    - type: nauc_precision_at_20_std
      value: 26.180973472305812
    - type: nauc_precision_at_3_diff1
      value: -6.369543112256839
    - type: nauc_precision_at_3_max
      value: -51.237042006520205
    - type: nauc_precision_at_3_std
      value: 8.040039123275792
    - type: nauc_precision_at_5_diff1
      value: -5.048799187706708
    - type: nauc_precision_at_5_max
      value: -47.84664701269636
    - type: nauc_precision_at_5_std
      value: 27.38730373425013
    - type: nauc_recall_at_1000_diff1
      value: -5.332162552815805
    - type: nauc_recall_at_1000_max
      value: -48.4822748768215
    - type: nauc_recall_at_1000_std
      value: 10.244830561951758
    - type: nauc_recall_at_100_diff1
      value: -5.332162552815805
    - type: nauc_recall_at_100_max
      value: -48.4822748768215
    - type: nauc_recall_at_100_std
      value: 10.244830561951758
    - type: nauc_recall_at_10_diff1
      value: -5.332162552815805
    - type: nauc_recall_at_10_max
      value: -48.4822748768215
    - type: nauc_recall_at_10_std
      value: 10.244830561951758
    - type: nauc_recall_at_1_diff1
      value: -44.22946169608924
    - type: nauc_recall_at_1_max
      value: -54.782691745683785
    - type: nauc_recall_at_1_std
      value: -5.883579383137843
    - type: nauc_recall_at_20_diff1
      value: -5.332162552815805
    - type: nauc_recall_at_20_max
      value: -48.4822748768215
    - type: nauc_recall_at_20_std
      value: 10.244830561951758
    - type: nauc_recall_at_3_diff1
      value: -12.905636390631683
    - type: nauc_recall_at_3_max
      value: -50.90776136220332
    - type: nauc_recall_at_3_std
      value: 0.17041202921295526
    - type: nauc_recall_at_5_diff1
      value: -13.498974486636495
    - type: nauc_recall_at_5_max
      value: -48.21891341099633
    - type: nauc_recall_at_5_std
      value: 17.89151222068661
    - type: ndcg_at_1
      value: 6.122
    - type: ndcg_at_10
      value: 11.591
    - type: ndcg_at_100
      value: 10.136000000000001
    - type: ndcg_at_1000
      value: 10.136000000000001
    - type: ndcg_at_20
      value: 10.174999999999999
    - type: ndcg_at_3
      value: 10.31
    - type: ndcg_at_5
      value: 10.402000000000001
    - type: precision_at_1
      value: 6.122
    - type: precision_at_10
      value: 11.837
    - type: precision_at_100
      value: 1.184
    - type: precision_at_1000
      value: 0.11800000000000001
    - type: precision_at_20
      value: 5.918
    - type: precision_at_3
      value: 12.245000000000001
    - type: precision_at_5
      value: 11.429
    - type: recall_at_1
      value: 0.607
    - type: recall_at_10
      value: 9.923
    - type: recall_at_100
      value: 9.923
    - type: recall_at_1000
      value: 9.923
    - type: recall_at_20
      value: 9.923
    - type: recall_at_3
      value: 2.952
    - type: recall_at_5
      value: 4.77
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB ToxicConversationsClassification (default)
      revision: edfaf9da55d3dd50d43143d90c1ac476895ae6de
      split: test
      type: mteb/toxic_conversations_50k
    metrics:
    - type: accuracy
      value: 64.5654296875
    - type: ap
      value: 11.16021263473999
    - type: ap_weighted
      value: 11.16021263473999
    - type: f1
      value: 49.16782358867322
    - type: f1_weighted
      value: 72.38896137915434
    - type: main_score
      value: 64.5654296875
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB TweetSentimentExtractionClassification (default)
      revision: d604517c81ca91fe16a244d1248fc021f9ecee7a
      split: test
      type: mteb/tweet_sentiment_extraction
    metrics:
    - type: accuracy
      value: 58.59649122807017
    - type: f1
      value: 58.97163776420522
    - type: f1_weighted
      value: 58.12171156125538
    - type: main_score
      value: 58.59649122807017
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB TwentyNewsgroupsClustering (default)
      revision: 6125ec4e24fa026cec8a478383ee943acfbd5449
      split: test
      type: mteb/twentynewsgroups-clustering
    metrics:
    - type: main_score
      value: 54.42018767717596
    - type: v_measure
      value: 54.42018767717596
    - type: v_measure_std
      value: 1.7361780610745077
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB TwitterSemEval2015 (default)
      revision: 70970daeab8776df92f5ea462b6173c0b46fd2d1
      split: test
      type: mteb/twittersemeval2015-pairclassification
    metrics:
    - type: cosine_accuracy
      value: 85.58741133694939
    - type: cosine_accuracy_threshold
      value: 88.05205225944519
    - type: cosine_ap
      value: 70.97496557342045
    - type: cosine_f1
      value: 66.36408243375858
    - type: cosine_f1_threshold
      value: 85.22337675094604
    - type: cosine_precision
      value: 62.012838147638696
    - type: cosine_recall
      value: 71.37203166226914
    - type: dot_accuracy
      value: 77.91023424926983
    - type: dot_accuracy_threshold
      value: 225873.33984375
    - type: dot_ap
      value: 39.53106490991552
    - type: dot_f1
      value: 44.30863254392666
    - type: dot_f1_threshold
      value: 181731.103515625
    - type: dot_precision
      value: 34.72014366956001
    - type: dot_recall
      value: 61.21372031662269
    - type: euclidean_accuracy
      value: 84.38338201108661
    - type: euclidean_accuracy_threshold
      value: 2230.430030822754
    - type: euclidean_ap
      value: 68.1947692164942
    - type: euclidean_f1
      value: 63.45361468348108
    - type: euclidean_f1_threshold
      value: 2520.492172241211
    - type: euclidean_precision
      value: 60.22754207158094
    - type: euclidean_recall
      value: 67.04485488126649
    - type: main_score
      value: 70.97496557342045
    - type: manhattan_accuracy
      value: 84.41318471717231
    - type: manhattan_accuracy_threshold
      value: 121673.5107421875
    - type: manhattan_ap
      value: 68.19986792695579
    - type: manhattan_f1
      value: 63.52319879290833
    - type: manhattan_f1_threshold
      value: 135339.74609375
    - type: manhattan_precision
      value: 60.67739610857554
    - type: manhattan_recall
      value: 66.64907651715039
    - type: max_accuracy
      value: 85.58741133694939
    - type: max_ap
      value: 70.97496557342045
    - type: max_f1
      value: 66.36408243375858
    - type: max_precision
      value: 62.012838147638696
    - type: max_recall
      value: 71.37203166226914
    - type: similarity_accuracy
      value: 85.58741133694939
    - type: similarity_accuracy_threshold
      value: 88.05205225944519
    - type: similarity_ap
      value: 70.97496557342045
    - type: similarity_f1
      value: 66.36408243375858
    - type: similarity_f1_threshold
      value: 85.22337675094604
    - type: similarity_precision
      value: 62.012838147638696
    - type: similarity_recall
      value: 71.37203166226914
    task:
      type: PairClassification
  - dataset:
      config: default
      name: MTEB TwitterURLCorpus (default)
      revision: 8b6510b0b1fa4e4c4f879467980e9be563ec1cdf
      split: test
      type: mteb/twitterurlcorpus-pairclassification
    metrics:
    - type: cosine_accuracy
      value: 88.64827104435906
    - type: cosine_accuracy_threshold
      value: 87.05877661705017
    - type: cosine_ap
      value: 85.53815676294218
    - type: cosine_f1
      value: 77.77407777407777
    - type: cosine_f1_threshold
      value: 86.26236915588379
    - type: cosine_precision
      value: 74.86288197165041
    - type: cosine_recall
      value: 80.92085001539883
    - type: dot_accuracy
      value: 80.28680094694765
    - type: dot_accuracy_threshold
      value: 206829.1259765625
    - type: dot_ap
      value: 62.68480928305134
    - type: dot_f1
      value: 60.86017406772123
    - type: dot_f1_threshold
      value: 187259.0576171875
    - type: dot_precision
      value: 51.800583973180494
    - type: dot_recall
      value: 73.76039421004003
    - type: euclidean_accuracy
      value: 87.99433383785463
    - type: euclidean_accuracy_threshold
      value: 2342.825126647949
    - type: euclidean_ap
      value: 83.96323437690357
    - type: euclidean_f1
      value: 76.10833822665883
    - type: euclidean_f1_threshold
      value: 2519.9838638305664
    - type: euclidean_precision
      value: 72.71388499298737
    - type: euclidean_recall
      value: 79.8352325223283
    - type: main_score
      value: 85.53815676294218
    - type: manhattan_accuracy
      value: 87.99433383785463
    - type: manhattan_accuracy_threshold
      value: 126229.9560546875
    - type: manhattan_ap
      value: 83.96776986541201
    - type: manhattan_f1
      value: 76.04131956014662
    - type: manhattan_f1_threshold
      value: 134875.15869140625
    - type: manhattan_precision
      value: 73.24013979031453
    - type: manhattan_recall
      value: 79.06529103788112
    - type: max_accuracy
      value: 88.64827104435906
    - type: max_ap
      value: 85.53815676294218
    - type: max_f1
      value: 77.77407777407777
    - type: max_precision
      value: 74.86288197165041
    - type: max_recall
      value: 80.92085001539883
    - type: similarity_accuracy
      value: 88.64827104435906
    - type: similarity_accuracy_threshold
      value: 87.05877661705017
    - type: similarity_ap
      value: 85.53815676294218
    - type: similarity_f1
      value: 77.77407777407777
    - type: similarity_f1_threshold
      value: 86.26236915588379
    - type: similarity_precision
      value: 74.86288197165041
    - type: similarity_recall
      value: 80.92085001539883
    task:
      type: PairClassification
tags:
- mteb
---
