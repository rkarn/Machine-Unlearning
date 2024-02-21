def decision_tree_inference(feature_num):
  label_class= None
  if (feature_num[350] > 126.5) and (feature_num[489] > 24.5) and (feature_num[234] <= 0.5) and (feature_num[402] <= 0.5) and (feature_num[300] <= 5.5) and (feature_num[149] <= 4.5) and (feature_num[494] <= 4.0) and (feature_num[538] <= 26.5):
    label_class= 1 #(proba: 95.77%) | based on 4,798 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] <= 0.5) and (feature_num[430] <= 0.5) and (feature_num[405] <= 1.5) and (feature_num[485] <= 6.0) and (feature_num[154] <= 0.5) and (feature_num[594] <= 21.5) and (feature_num[156] <= 0.5):
    label_class= 7 #(proba: 95.63%) | based on 4,030 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] <= 0.5) and (feature_num[430] > 0.5) and (feature_num[211] <= 28.5) and (feature_num[98] <= 0.5) and (feature_num[267] <= 128.5) and (feature_num[95] <= 7.0) and (feature_num[155] <= 87.5):
    label_class= 4 #(proba: 93.7%) | based on 3,268 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] <= 0.5) and (feature_num[489] <= 47.5) and (feature_num[380] <= 1.5) and (feature_num[324] <= 173.0) and (feature_num[72] <= 1.0) and (feature_num[455] > 0.5):
    label_class= 0 #(proba: 97.59%) | based on 3,195 samples
  if (feature_num[350] > 126.5) and (feature_num[489] <= 24.5) and (feature_num[290] <= 34.5) and (feature_num[486] <= 93.5) and (feature_num[296] > 2.5) and (feature_num[153] > 1.0) and (feature_num[488] <= 60.0) and (feature_num[315] <= 94.0):
    label_class= 3 #(proba: 96.83%) | based on 2,523 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] > 0.5) and (feature_num[346] <= 0.5) and (feature_num[348] <= 109.5) and (feature_num[371] <= 63.5) and (feature_num[155] > 0.5) and (feature_num[517] > 0.5):
    label_class= 2 #(proba: 96.81%) | based on 2,008 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] > 0.5) and (feature_num[346] > 0.5) and (feature_num[655] <= 0.5) and (feature_num[271] <= 1.0) and (feature_num[484] > 6.0) and (feature_num[218] <= 18.5):
    label_class= 6 #(proba: 97.05%) | based on 1,188 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] <= 0.5) and (feature_num[430] > 0.5) and (feature_num[211] <= 28.5) and (feature_num[98] > 0.5) and (feature_num[537] <= 8.0) and (feature_num[242] <= 7.0) and (feature_num[240] <= 1.0):
    label_class= 6 #(proba: 98.82%) | based on 761 samples
  if (feature_num[350] > 126.5) and (feature_num[489] <= 24.5) and (feature_num[290] > 34.5) and (feature_num[297] <= 5.5) and (feature_num[486] <= 58.0) and (feature_num[186] > 2.5) and (feature_num[301] <= 54.0) and (feature_num[299] <= 81.5):
    label_class= 5 #(proba: 95.37%) | based on 734 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] <= 0.5) and (feature_num[430] > 0.5) and (feature_num[211] > 28.5) and (feature_num[156] > 0.5) and (feature_num[101] <= 1.0) and (feature_num[656] > 1.5) and (feature_num[434] > 0.5):
    label_class= 5 #(proba: 31.27%) | based on 726 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] <= 0.5) and (feature_num[430] > 0.5) and (feature_num[211] > 28.5) and (feature_num[156] > 0.5) and (feature_num[101] > 1.0) and (feature_num[271] <= 136.5) and (feature_num[296] <= 146.5):
    label_class= 6 #(proba: 99.12%) | based on 682 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] <= 0.5) and (feature_num[489] <= 47.5) and (feature_num[380] <= 1.5) and (feature_num[324] <= 173.0) and (feature_num[72] <= 1.0) and (feature_num[455] <= 0.5):
    label_class= 0 #(proba: 77.69%) | based on 520 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] > 0.5) and (feature_num[346] > 0.5) and (feature_num[655] > 0.5) and (feature_num[354] <= 0.5) and (feature_num[514] <= 86.5) and (feature_num[357] <= 9.5):
    label_class= 5 #(proba: 93.51%) | based on 478 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] > 0.5) and (feature_num[346] <= 0.5) and (feature_num[348] <= 109.5) and (feature_num[371] <= 63.5) and (feature_num[155] > 0.5) and (feature_num[517] <= 0.5):
    label_class= 2 #(proba: 66.0%) | based on 403 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] <= 0.5) and (feature_num[430] > 0.5) and (feature_num[211] > 28.5) and (feature_num[156] > 0.5) and (feature_num[101] <= 1.0) and (feature_num[656] <= 1.5) and (feature_num[572] <= 0.5):
    label_class= 4 #(proba: 71.98%) | based on 389 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] <= 0.5) and (feature_num[430] > 0.5) and (feature_num[211] <= 28.5) and (feature_num[98] <= 0.5) and (feature_num[267] <= 128.5) and (feature_num[95] <= 7.0) and (feature_num[155] > 87.5):
    label_class= 6 #(proba: 22.34%) | based on 376 samples
  if (feature_num[350] > 126.5) and (feature_num[489] <= 24.5) and (feature_num[290] > 34.5) and (feature_num[297] > 5.5) and (feature_num[598] > 0.5) and (feature_num[486] <= 7.5) and (feature_num[427] <= 168.5) and (feature_num[269] > 4.5):
    label_class= 3 #(proba: 61.62%) | based on 370 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] > 0.5) and (feature_num[346] <= 0.5) and (feature_num[348] <= 109.5) and (feature_num[371] <= 63.5) and (feature_num[155] <= 0.5) and (feature_num[652] <= 6.0):
    label_class= 2 #(proba: 75.07%) | based on 369 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] <= 0.5) and (feature_num[430] <= 0.5) and (feature_num[405] > 1.5) and (feature_num[516] <= 14.5) and (feature_num[353] <= 2.5) and (feature_num[322] <= 8.5) and (feature_num[356] <= 0.5):
    label_class= 5 #(proba: 83.23%) | based on 328 samples
  if (feature_num[350] > 126.5) and (feature_num[489] <= 24.5) and (feature_num[290] <= 34.5) and (feature_num[486] <= 93.5) and (feature_num[296] > 2.5) and (feature_num[153] <= 1.0) and (feature_num[208] > 51.5) and (feature_num[316] <= 38.5):
    label_class= 3 #(proba: 85.76%) | based on 323 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] <= 0.5) and (feature_num[430] > 0.5) and (feature_num[211] > 28.5) and (feature_num[156] <= 0.5) and (feature_num[381] <= 4.5) and (feature_num[217] > 1.5) and (feature_num[357] <= 6.0):
    label_class= 5 #(proba: 95.65%) | based on 299 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] > 0.5) and (feature_num[346] > 0.5) and (feature_num[655] <= 0.5) and (feature_num[271] > 1.0) and (feature_num[354] <= 10.5) and (feature_num[357] <= 4.5):
    label_class= 5 #(proba: 97.1%) | based on 276 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] <= 0.5) and (feature_num[430] > 0.5) and (feature_num[211] > 28.5) and (feature_num[156] > 0.5) and (feature_num[101] <= 1.0) and (feature_num[656] > 1.5) and (feature_num[434] <= 0.5):
    label_class= 0 #(proba: 69.66%) | based on 267 samples
  if (feature_num[350] > 126.5) and (feature_num[489] <= 24.5) and (feature_num[290] <= 34.5) and (feature_num[486] <= 93.5) and (feature_num[296] <= 2.5) and (feature_num[462] <= 81.0) and (feature_num[315] <= 54.5) and (feature_num[178] > 3.0):
    label_class= 3 #(proba: 78.57%) | based on 266 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] <= 0.5) and (feature_num[430] > 0.5) and (feature_num[211] > 28.5) and (feature_num[156] > 0.5) and (feature_num[101] <= 1.0) and (feature_num[656] <= 1.5) and (feature_num[572] > 0.5):
    label_class= 6 #(proba: 53.01%) | based on 266 samples
  if (feature_num[350] > 126.5) and (feature_num[489] <= 24.5) and (feature_num[290] <= 34.5) and (feature_num[486] <= 93.5) and (feature_num[296] <= 2.5) and (feature_num[462] <= 81.0) and (feature_num[315] <= 54.5) and (feature_num[178] <= 3.0):
    label_class= 5 #(proba: 51.5%) | based on 266 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] <= 0.5) and (feature_num[489] > 47.5) and (feature_num[320] <= 1.0) and (feature_num[345] <= 104.5) and (feature_num[343] <= 132.5) and (feature_num[348] <= 3.0):
    label_class= 2 #(proba: 97.71%) | based on 262 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] <= 0.5) and (feature_num[430] <= 0.5) and (feature_num[405] > 1.5) and (feature_num[516] > 14.5) and (feature_num[376] <= 3.5) and (feature_num[207] <= 0.5) and (feature_num[263] <= 9.0):
    label_class= 1 #(proba: 86.18%) | based on 246 samples
  if (feature_num[350] > 126.5) and (feature_num[489] > 24.5) and (feature_num[234] <= 0.5) and (feature_num[402] > 0.5) and (feature_num[522] > 1.5) and (feature_num[293] > 65.0) and (feature_num[301] <= 38.0) and (feature_num[571] > 6.0):
    label_class= 6 #(proba: 86.01%) | based on 243 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] > 0.5) and (feature_num[346] <= 0.5) and (feature_num[348] <= 109.5) and (feature_num[371] <= 63.5) and (feature_num[155] <= 0.5) and (feature_num[652] > 6.0):
    label_class= 1 #(proba: 48.55%) | based on 241 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] <= 0.5) and (feature_num[430] <= 0.5) and (feature_num[405] <= 1.5) and (feature_num[485] > 6.0) and (feature_num[211] <= 53.5) and (feature_num[571] <= 31.0) and (feature_num[266] <= 8.5):
    label_class= 4 #(proba: 81.55%) | based on 233 samples
  if (feature_num[350] > 126.5) and (feature_num[489] > 24.5) and (feature_num[234] > 0.5) and (feature_num[658] <= 0.5) and (feature_num[345] <= 18.0) and (feature_num[526] > 1.0) and (feature_num[370] <= 11.5) and (feature_num[284] <= 19.5):
    label_class= 2 #(proba: 98.68%) | based on 227 samples
  if (feature_num[350] > 126.5) and (feature_num[489] <= 24.5) and (feature_num[290] <= 34.5) and (feature_num[486] <= 93.5) and (feature_num[296] > 2.5) and (feature_num[153] <= 1.0) and (feature_num[208] <= 51.5) and (feature_num[539] > 2.0):
    label_class= 5 #(proba: 56.19%) | based on 210 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] <= 0.5) and (feature_num[430] > 0.5) and (feature_num[211] <= 28.5) and (feature_num[98] <= 0.5) and (feature_num[267] <= 128.5) and (feature_num[95] > 7.0) and (feature_num[242] <= 90.0):
    label_class= 6 #(proba: 97.58%) | based on 207 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] <= 0.5) and (feature_num[430] <= 0.5) and (feature_num[405] > 1.5) and (feature_num[516] > 14.5) and (feature_num[376] <= 3.5) and (feature_num[207] > 0.5) and (feature_num[484] <= 7.0):
    label_class= 2 #(proba: 52.22%) | based on 203 samples
  if (feature_num[350] > 126.5) and (feature_num[489] > 24.5) and (feature_num[234] > 0.5) and (feature_num[658] <= 0.5) and (feature_num[345] > 18.0) and (feature_num[575] > 89.0) and (feature_num[240] <= 107.0) and (feature_num[655] <= 11.5):
    label_class= 6 #(proba: 93.43%) | based on 198 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] > 0.5) and (feature_num[346] > 0.5) and (feature_num[655] <= 0.5) and (feature_num[271] > 1.0) and (feature_num[354] > 10.5) and (feature_num[156] <= 13.5):
    label_class= 4 #(proba: 36.04%) | based on 197 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] <= 0.5) and (feature_num[430] <= 0.5) and (feature_num[405] <= 1.5) and (feature_num[485] <= 6.0) and (feature_num[154] > 0.5) and (feature_num[509] <= 12.5) and (feature_num[572] > 112.0):
    label_class= 2 #(proba: 81.73%) | based on 197 samples
  if (feature_num[350] > 126.5) and (feature_num[489] > 24.5) and (feature_num[234] <= 0.5) and (feature_num[402] > 0.5) and (feature_num[522] <= 1.5) and (feature_num[275] <= 33.5) and (feature_num[346] > 7.0) and (feature_num[712] <= 1.0):
    label_class= 4 #(proba: 32.42%) | based on 182 samples
  if (feature_num[350] > 126.5) and (feature_num[489] <= 24.5) and (feature_num[290] <= 34.5) and (feature_num[486] <= 93.5) and (feature_num[296] > 2.5) and (feature_num[153] <= 1.0) and (feature_num[208] <= 51.5) and (feature_num[539] <= 2.0):
    label_class= 4 #(proba: 26.92%) | based on 182 samples
  if (feature_num[350] > 126.5) and (feature_num[489] <= 24.5) and (feature_num[290] <= 34.5) and (feature_num[486] <= 93.5) and (feature_num[296] <= 2.5) and (feature_num[462] > 81.0) and (feature_num[628] <= 24.0) and (feature_num[375] <= 14.5):
    label_class= 1 #(proba: 99.43%) | based on 176 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] > 0.5) and (feature_num[346] > 0.5) and (feature_num[655] <= 0.5) and (feature_num[271] > 1.0) and (feature_num[354] > 10.5) and (feature_num[156] > 13.5):
    label_class= 2 #(proba: 70.37%) | based on 162 samples
  if (feature_num[350] > 126.5) and (feature_num[489] > 24.5) and (feature_num[234] <= 0.5) and (feature_num[402] <= 0.5) and (feature_num[300] <= 5.5) and (feature_num[149] > 4.5) and (feature_num[318] <= 13.5) and (feature_num[516] > 16.5):
    label_class= 2 #(proba: 92.26%) | based on 155 samples
  if (feature_num[350] > 126.5) and (feature_num[489] <= 24.5) and (feature_num[290] <= 34.5) and (feature_num[486] > 93.5) and (feature_num[656] <= 0.5) and (feature_num[152] <= 6.0) and (feature_num[601] > 74.0) and (feature_num[270] <= 27.0):
    label_class= 6 #(proba: 91.56%) | based on 154 samples
  if (feature_num[350] > 126.5) and (feature_num[489] <= 24.5) and (feature_num[290] > 34.5) and (feature_num[297] <= 5.5) and (feature_num[486] <= 58.0) and (feature_num[186] <= 2.5) and (feature_num[294] <= 89.0) and (feature_num[328] <= 13.5):
    label_class= 5 #(proba: 67.97%) | based on 153 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] <= 0.5) and (feature_num[430] > 0.5) and (feature_num[211] <= 28.5) and (feature_num[98] <= 0.5) and (feature_num[267] > 128.5) and (feature_num[353] <= 1.0) and (feature_num[411] <= 30.5):
    label_class= 5 #(proba: 81.33%) | based on 150 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] <= 0.5) and (feature_num[430] <= 0.5) and (feature_num[405] <= 1.5) and (feature_num[485] > 6.0) and (feature_num[211] <= 53.5) and (feature_num[571] > 31.0) and (feature_num[626] <= 2.0):
    label_class= 6 #(proba: 75.0%) | based on 136 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] > 0.5) and (feature_num[346] <= 0.5) and (feature_num[348] <= 109.5) and (feature_num[371] > 63.5) and (feature_num[213] <= 5.0) and (feature_num[402] <= 3.0):
    label_class= 6 #(proba: 94.7%) | based on 132 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] <= 0.5) and (feature_num[430] <= 0.5) and (feature_num[405] > 1.5) and (feature_num[516] <= 14.5) and (feature_num[353] > 2.5) and (feature_num[346] <= 1.0) and (feature_num[652] <= 59.0):
    label_class= 3 #(proba: 36.36%) | based on 132 samples
  if (feature_num[350] > 126.5) and (feature_num[489] <= 24.5) and (feature_num[290] <= 34.5) and (feature_num[486] <= 93.5) and (feature_num[296] <= 2.5) and (feature_num[462] <= 81.0) and (feature_num[315] > 54.5) and (feature_num[327] <= 133.0):
    label_class= 5 #(proba: 94.62%) | based on 130 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] <= 0.5) and (feature_num[489] > 47.5) and (feature_num[320] > 1.0) and (feature_num[494] <= 23.5) and (feature_num[380] <= 17.5) and (feature_num[485] <= 241.5):
    label_class= 5 #(proba: 93.8%) | based on 129 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] <= 0.5) and (feature_num[430] <= 0.5) and (feature_num[405] <= 1.5) and (feature_num[485] <= 6.0) and (feature_num[154] > 0.5) and (feature_num[509] <= 12.5) and (feature_num[572] <= 112.0):
    label_class= 3 #(proba: 25.78%) | based on 128 samples
  if (feature_num[350] > 126.5) and (feature_num[489] > 24.5) and (feature_num[234] > 0.5) and (feature_num[658] > 0.5) and (feature_num[515] <= 84.5) and (feature_num[545] <= 5.5) and (feature_num[318] <= 38.5) and (feature_num[292] <= 168.5):
    label_class= 3 #(proba: 92.97%) | based on 128 samples
  if (feature_num[350] > 126.5) and (feature_num[489] <= 24.5) and (feature_num[290] <= 34.5) and (feature_num[486] > 93.5) and (feature_num[656] <= 0.5) and (feature_num[152] > 6.0) and (feature_num[438] <= 27.0) and (feature_num[343] <= 5.0):
    label_class= 2 #(proba: 95.9%) | based on 122 samples
  if (feature_num[350] > 126.5) and (feature_num[489] > 24.5) and (feature_num[234] <= 0.5) and (feature_num[402] <= 0.5) and (feature_num[300] > 5.5) and (feature_num[265] <= 34.0) and (feature_num[460] > 241.0) and (feature_num[270] > 159.0):
    label_class= 1 #(proba: 89.34%) | based on 122 samples
  if (feature_num[350] > 126.5) and (feature_num[489] <= 24.5) and (feature_num[290] <= 34.5) and (feature_num[486] > 93.5) and (feature_num[656] > 0.5) and (feature_num[439] > 12.5) and (feature_num[380] > 9.5) and (feature_num[316] <= 3.0):
    label_class= 3 #(proba: 65.49%) | based on 113 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] <= 0.5) and (feature_num[430] <= 0.5) and (feature_num[405] <= 1.5) and (feature_num[485] > 6.0) and (feature_num[211] > 53.5) and (feature_num[427] <= 1.0) and (feature_num[154] <= 4.5):
    label_class= 7 #(proba: 58.04%) | based on 112 samples
  if (feature_num[350] > 126.5) and (feature_num[489] > 24.5) and (feature_num[234] <= 0.5) and (feature_num[402] > 0.5) and (feature_num[522] <= 1.5) and (feature_num[275] <= 33.5) and (feature_num[346] <= 7.0) and (feature_num[268] > 236.5):
    label_class= 1 #(proba: 70.0%) | based on 110 samples
  if (feature_num[350] > 126.5) and (feature_num[489] <= 24.5) and (feature_num[290] > 34.5) and (feature_num[297] > 5.5) and (feature_num[598] <= 0.5) and (feature_num[210] <= 4.5) and (feature_num[404] > 7.0) and (feature_num[265] <= 150.5):
    label_class= 4 #(proba: 70.91%) | based on 110 samples
  if (feature_num[350] > 126.5) and (feature_num[489] > 24.5) and (feature_num[234] > 0.5) and (feature_num[658] > 0.5) and (feature_num[515] <= 84.5) and (feature_num[545] > 5.5) and (feature_num[578] <= 35.5) and (feature_num[295] > 226.5):
    label_class= 7 #(proba: 61.47%) | based on 109 samples
  if (feature_num[350] > 126.5) and (feature_num[489] <= 24.5) and (feature_num[290] > 34.5) and (feature_num[297] > 5.5) and (feature_num[598] <= 0.5) and (feature_num[210] <= 4.5) and (feature_num[404] <= 7.0) and (feature_num[320] > 204.0):
    label_class= 7 #(proba: 97.25%) | based on 109 samples
  if (feature_num[350] > 126.5) and (feature_num[489] <= 24.5) and (feature_num[290] > 34.5) and (feature_num[297] > 5.5) and (feature_num[598] > 0.5) and (feature_num[486] > 7.5) and (feature_num[400] > 24.5) and (feature_num[242] > 56.0):
    label_class= 0 #(proba: 56.31%) | based on 103 samples
  if (feature_num[350] > 126.5) and (feature_num[489] <= 24.5) and (feature_num[290] > 34.5) and (feature_num[297] > 5.5) and (feature_num[598] > 0.5) and (feature_num[486] <= 7.5) and (feature_num[427] <= 168.5) and (feature_num[269] <= 4.5):
    label_class= 5 #(proba: 74.76%) | based on 103 samples
  if (feature_num[350] > 126.5) and (feature_num[489] <= 24.5) and (feature_num[290] > 34.5) and (feature_num[297] <= 5.5) and (feature_num[486] > 58.0) and (feature_num[656] <= 7.5) and (feature_num[373] > 13.5) and (feature_num[514] > 47.5):
    label_class= 6 #(proba: 98.04%) | based on 102 samples
  if (feature_num[350] > 126.5) and (feature_num[489] > 24.5) and (feature_num[234] <= 0.5) and (feature_num[402] <= 0.5) and (feature_num[300] <= 5.5) and (feature_num[149] <= 4.5) and (feature_num[494] > 4.0) and (feature_num[657] <= 106.5):
    label_class= 6 #(proba: 29.7%) | based on 101 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] <= 0.5) and (feature_num[430] > 0.5) and (feature_num[211] <= 28.5) and (feature_num[98] <= 0.5) and (feature_num[267] > 128.5) and (feature_num[353] > 1.0) and (feature_num[432] <= 18.0):
    label_class= 7 #(proba: 83.17%) | based on 101 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] <= 0.5) and (feature_num[489] <= 47.5) and (feature_num[380] > 1.5) and (feature_num[298] <= 116.5) and (feature_num[485] <= 93.0) and (feature_num[375] > 22.0):
    label_class= 5 #(proba: 77.23%) | based on 101 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] <= 0.5) and (feature_num[430] <= 0.5) and (feature_num[405] > 1.5) and (feature_num[516] <= 14.5) and (feature_num[353] > 2.5) and (feature_num[346] > 1.0) and (feature_num[210] <= 22.5):
    label_class= 4 #(proba: 69.31%) | based on 101 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] <= 0.5) and (feature_num[430] <= 0.5) and (feature_num[405] > 1.5) and (feature_num[516] <= 14.5) and (feature_num[353] <= 2.5) and (feature_num[322] > 8.5) and (feature_num[546] <= 2.0):
    label_class= 3 #(proba: 88.89%) | based on 99 samples
  if (feature_num[350] > 126.5) and (feature_num[489] > 24.5) and (feature_num[234] <= 0.5) and (feature_num[402] > 0.5) and (feature_num[522] <= 1.5) and (feature_num[275] > 33.5) and (feature_num[381] <= 56.5) and (feature_num[187] <= 120.0):
    label_class= 5 #(proba: 93.62%) | based on 94 samples
  if (feature_num[350] > 126.5) and (feature_num[489] > 24.5) and (feature_num[234] > 0.5) and (feature_num[658] <= 0.5) and (feature_num[345] <= 18.0) and (feature_num[526] <= 1.0) and (feature_num[541] <= 42.0) and (feature_num[603] <= 231.5):
    label_class= 7 #(proba: 36.67%) | based on 90 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] <= 0.5) and (feature_num[430] <= 0.5) and (feature_num[405] > 1.5) and (feature_num[516] > 14.5) and (feature_num[376] > 3.5) and (feature_num[658] <= 5.5) and (feature_num[326] <= 1.5):
    label_class= 6 #(proba: 65.56%) | based on 90 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] <= 0.5) and (feature_num[489] <= 47.5) and (feature_num[380] > 1.5) and (feature_num[298] > 116.5) and (feature_num[406] <= 53.5) and (feature_num[237] > 1.5):
    label_class= 0 #(proba: 87.36%) | based on 87 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] > 0.5) and (feature_num[346] > 0.5) and (feature_num[655] <= 0.5) and (feature_num[271] <= 1.0) and (feature_num[484] <= 6.0) and (feature_num[516] <= 49.5):
    label_class= 5 #(proba: 77.01%) | based on 87 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] <= 0.5) and (feature_num[430] <= 0.5) and (feature_num[405] <= 1.5) and (feature_num[485] <= 6.0) and (feature_num[154] > 0.5) and (feature_num[509] > 12.5) and (feature_num[351] <= 48.5):
    label_class= 0 #(proba: 97.56%) | based on 82 samples
  if (feature_num[350] > 126.5) and (feature_num[489] <= 24.5) and (feature_num[290] > 34.5) and (feature_num[297] <= 5.5) and (feature_num[486] <= 58.0) and (feature_num[186] <= 2.5) and (feature_num[294] > 89.0) and (feature_num[492] <= 72.5):
    label_class= 3 #(proba: 76.54%) | based on 81 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] <= 0.5) and (feature_num[430] <= 0.5) and (feature_num[405] <= 1.5) and (feature_num[485] > 6.0) and (feature_num[211] <= 53.5) and (feature_num[571] <= 31.0) and (feature_num[266] > 8.5):
    label_class= 7 #(proba: 35.8%) | based on 81 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] > 0.5) and (feature_num[346] > 0.5) and (feature_num[655] <= 0.5) and (feature_num[271] <= 1.0) and (feature_num[484] <= 6.0) and (feature_num[516] > 49.5):
    label_class= 6 #(proba: 46.84%) | based on 79 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] <= 0.5) and (feature_num[489] <= 47.5) and (feature_num[380] > 1.5) and (feature_num[298] <= 116.5) and (feature_num[485] <= 93.0) and (feature_num[375] <= 22.0):
    label_class= 3 #(proba: 42.86%) | based on 77 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] <= 0.5) and (feature_num[430] <= 0.5) and (feature_num[405] > 1.5) and (feature_num[516] <= 14.5) and (feature_num[353] > 2.5) and (feature_num[346] <= 1.0) and (feature_num[652] > 59.0):
    label_class= 3 #(proba: 98.63%) | based on 73 samples
  if (feature_num[350] > 126.5) and (feature_num[489] <= 24.5) and (feature_num[290] <= 34.5) and (feature_num[486] <= 93.5) and (feature_num[296] > 2.5) and (feature_num[153] > 1.0) and (feature_num[488] <= 60.0) and (feature_num[315] > 94.0):
    label_class= 3 #(proba: 36.11%) | based on 72 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] <= 0.5) and (feature_num[430] <= 0.5) and (feature_num[405] > 1.5) and (feature_num[516] > 14.5) and (feature_num[376] <= 3.5) and (feature_num[207] > 0.5) and (feature_num[484] > 7.0):
    label_class= 6 #(proba: 59.15%) | based on 71 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] <= 0.5) and (feature_num[430] > 0.5) and (feature_num[211] > 28.5) and (feature_num[156] <= 0.5) and (feature_num[381] <= 4.5) and (feature_num[217] <= 1.5) and (feature_num[542] > 70.5):
    label_class= 0 #(proba: 58.57%) | based on 70 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] <= 0.5) and (feature_num[430] <= 0.5) and (feature_num[405] <= 1.5) and (feature_num[485] <= 6.0) and (feature_num[154] <= 0.5) and (feature_num[594] > 21.5) and (feature_num[464] <= 125.0):
    label_class= 0 #(proba: 95.65%) | based on 69 samples
  if (feature_num[350] > 126.5) and (feature_num[489] <= 24.5) and (feature_num[290] > 34.5) and (feature_num[297] > 5.5) and (feature_num[598] > 0.5) and (feature_num[486] <= 7.5) and (feature_num[427] > 168.5) and (feature_num[381] <= 132.5):
    label_class= 0 #(proba: 91.94%) | based on 62 samples
  if (feature_num[350] > 126.5) and (feature_num[489] > 24.5) and (feature_num[234] > 0.5) and (feature_num[658] <= 0.5) and (feature_num[345] <= 18.0) and (feature_num[526] <= 1.0) and (feature_num[541] > 42.0) and (feature_num[320] <= 62.0):
    label_class= 2 #(proba: 88.71%) | based on 62 samples
  if (feature_num[350] > 126.5) and (feature_num[489] > 24.5) and (feature_num[234] > 0.5) and (feature_num[658] > 0.5) and (feature_num[515] > 84.5) and (feature_num[319] <= 0.5) and (feature_num[345] <= 27.5) and (feature_num[608] > 5.5):
    label_class= 2 #(proba: 85.25%) | based on 61 samples
  if (feature_num[350] > 126.5) and (feature_num[489] <= 24.5) and (feature_num[290] > 34.5) and (feature_num[297] > 5.5) and (feature_num[598] > 0.5) and (feature_num[486] > 7.5) and (feature_num[400] > 24.5) and (feature_num[242] <= 56.0):
    label_class= 6 #(proba: 90.16%) | based on 61 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] > 0.5) and (feature_num[346] > 0.5) and (feature_num[655] > 0.5) and (feature_num[354] > 0.5) and (feature_num[434] <= 47.0) and (feature_num[484] > 54.0):
    label_class= 0 #(proba: 90.16%) | based on 61 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] <= 0.5) and (feature_num[489] <= 47.5) and (feature_num[380] > 1.5) and (feature_num[298] <= 116.5) and (feature_num[485] > 93.0) and (feature_num[215] <= 1.5):
    label_class= 6 #(proba: 81.67%) | based on 60 samples
  if (feature_num[350] > 126.5) and (feature_num[489] > 24.5) and (feature_num[234] <= 0.5) and (feature_num[402] <= 0.5) and (feature_num[300] > 5.5) and (feature_num[265] <= 34.0) and (feature_num[460] <= 241.0) and (feature_num[414] <= 77.0):
    label_class= 5 #(proba: 25.42%) | based on 59 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] <= 0.5) and (feature_num[489] <= 47.5) and (feature_num[380] <= 1.5) and (feature_num[324] > 173.0) and (feature_num[427] > 16.5) and (feature_num[329] > 3.0):
    label_class= 0 #(proba: 100.0%) | based on 59 samples
  if (feature_num[350] > 126.5) and (feature_num[489] > 24.5) and (feature_num[234] <= 0.5) and (feature_num[402] > 0.5) and (feature_num[522] > 1.5) and (feature_num[293] <= 65.0) and (feature_num[511] > 55.0) and (feature_num[385] <= 214.5):
    label_class= 2 #(proba: 86.44%) | based on 59 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] <= 0.5) and (feature_num[430] <= 0.5) and (feature_num[405] <= 1.5) and (feature_num[485] > 6.0) and (feature_num[211] > 53.5) and (feature_num[427] > 1.0) and (feature_num[470] > 3.0):
    label_class= 0 #(proba: 47.46%) | based on 59 samples
  if (feature_num[350] > 126.5) and (feature_num[489] <= 24.5) and (feature_num[290] <= 34.5) and (feature_num[486] > 93.5) and (feature_num[656] <= 0.5) and (feature_num[152] <= 6.0) and (feature_num[601] <= 74.0) and (feature_num[432] > 210.0):
    label_class= 1 #(proba: 47.46%) | based on 59 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] <= 0.5) and (feature_num[489] <= 47.5) and (feature_num[380] <= 1.5) and (feature_num[324] > 173.0) and (feature_num[427] <= 16.5) and (feature_num[241] <= 1.0):
    label_class= 5 #(proba: 82.76%) | based on 58 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] <= 0.5) and (feature_num[489] > 47.5) and (feature_num[320] > 1.0) and (feature_num[494] > 23.5) and (feature_num[358] > 176.5) and (feature_num[621] <= 230.5):
    label_class= 0 #(proba: 100.0%) | based on 57 samples
  if (feature_num[350] > 126.5) and (feature_num[489] > 24.5) and (feature_num[234] <= 0.5) and (feature_num[402] > 0.5) and (feature_num[522] > 1.5) and (feature_num[293] <= 65.0) and (feature_num[511] <= 55.0) and (feature_num[654] <= 1.0):
    label_class= 6 #(proba: 28.3%) | based on 53 samples
  if (feature_num[350] > 126.5) and (feature_num[489] <= 24.5) and (feature_num[290] > 34.5) and (feature_num[297] > 5.5) and (feature_num[598] <= 0.5) and (feature_num[210] > 4.5) and (feature_num[653] > 80.0) and (feature_num[319] > 62.5):
    label_class= 5 #(proba: 45.28%) | based on 53 samples
  if (feature_num[350] > 126.5) and (feature_num[489] <= 24.5) and (feature_num[290] <= 34.5) and (feature_num[486] > 93.5) and (feature_num[656] > 0.5) and (feature_num[439] <= 12.5) and (feature_num[464] <= 1.0) and (feature_num[125] > 11.0):
    label_class= 2 #(proba: 88.46%) | based on 52 samples
  if (feature_num[350] > 126.5) and (feature_num[489] <= 24.5) and (feature_num[290] <= 34.5) and (feature_num[486] > 93.5) and (feature_num[656] <= 0.5) and (feature_num[152] <= 6.0) and (feature_num[601] > 74.0) and (feature_num[270] > 27.0):
    label_class= 2 #(proba: 32.0%) | based on 50 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] <= 0.5) and (feature_num[430] > 0.5) and (feature_num[211] <= 28.5) and (feature_num[98] <= 0.5) and (feature_num[267] > 128.5) and (feature_num[353] <= 1.0) and (feature_num[411] > 30.5):
    label_class= 7 #(proba: 40.82%) | based on 49 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] > 0.5) and (feature_num[346] <= 0.5) and (feature_num[348] > 109.5) and (feature_num[655] <= 26.5) and (feature_num[130] > 48.5) and (feature_num[270] <= 22.5):
    label_class= 6 #(proba: 100.0%) | based on 49 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] <= 0.5) and (feature_num[430] <= 0.5) and (feature_num[405] > 1.5) and (feature_num[516] <= 14.5) and (feature_num[353] <= 2.5) and (feature_num[322] > 8.5) and (feature_num[546] > 2.0):
    label_class= 5 #(proba: 38.78%) | based on 49 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] <= 0.5) and (feature_num[430] <= 0.5) and (feature_num[405] > 1.5) and (feature_num[516] > 14.5) and (feature_num[376] <= 3.5) and (feature_num[207] <= 0.5) and (feature_num[263] > 9.0):
    label_class= 7 #(proba: 50.0%) | based on 48 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] <= 0.5) and (feature_num[489] > 47.5) and (feature_num[320] > 1.0) and (feature_num[494] > 23.5) and (feature_num[358] <= 176.5) and (feature_num[374] > 41.5):
    label_class= 6 #(proba: 51.06%) | based on 47 samples
  if (feature_num[350] > 126.5) and (feature_num[489] <= 24.5) and (feature_num[290] > 34.5) and (feature_num[297] <= 5.5) and (feature_num[486] <= 58.0) and (feature_num[186] <= 2.5) and (feature_num[294] <= 89.0) and (feature_num[328] > 13.5):
    label_class= 4 #(proba: 68.09%) | based on 47 samples
  if (feature_num[350] > 126.5) and (feature_num[489] <= 24.5) and (feature_num[290] > 34.5) and (feature_num[297] > 5.5) and (feature_num[598] <= 0.5) and (feature_num[210] > 4.5) and (feature_num[653] <= 80.0) and (feature_num[154] > 8.5):
    label_class= 3 #(proba: 21.28%) | based on 47 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] <= 0.5) and (feature_num[430] <= 0.5) and (feature_num[405] <= 1.5) and (feature_num[485] > 6.0) and (feature_num[211] > 53.5) and (feature_num[427] <= 1.0) and (feature_num[154] > 4.5):
    label_class= 2 #(proba: 74.47%) | based on 47 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] > 0.5) and (feature_num[346] > 0.5) and (feature_num[655] > 0.5) and (feature_num[354] <= 0.5) and (feature_num[514] > 86.5) and (feature_num[523] > 3.5):
    label_class= 5 #(proba: 41.3%) | based on 46 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] > 0.5) and (feature_num[346] <= 0.5) and (feature_num[348] > 109.5) and (feature_num[655] <= 26.5) and (feature_num[130] <= 48.5) and (feature_num[354] <= 9.5):
    label_class= 5 #(proba: 80.43%) | based on 46 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] <= 0.5) and (feature_num[489] <= 47.5) and (feature_num[380] <= 1.5) and (feature_num[324] > 173.0) and (feature_num[427] <= 16.5) and (feature_num[241] > 1.0):
    label_class= 3 #(proba: 54.35%) | based on 46 samples
  if (feature_num[350] > 126.5) and (feature_num[489] > 24.5) and (feature_num[234] <= 0.5) and (feature_num[402] <= 0.5) and (feature_num[300] <= 5.5) and (feature_num[149] <= 4.5) and (feature_num[494] <= 4.0) and (feature_num[538] > 26.5):
    label_class= 5 #(proba: 51.11%) | based on 45 samples
  if (feature_num[350] > 126.5) and (feature_num[489] <= 24.5) and (feature_num[290] > 34.5) and (feature_num[297] > 5.5) and (feature_num[598] <= 0.5) and (feature_num[210] > 4.5) and (feature_num[653] > 80.0) and (feature_num[319] <= 62.5):
    label_class= 3 #(proba: 86.67%) | based on 45 samples
  if (feature_num[350] > 126.5) and (feature_num[489] > 24.5) and (feature_num[234] > 0.5) and (feature_num[658] > 0.5) and (feature_num[515] <= 84.5) and (feature_num[545] > 5.5) and (feature_num[578] > 35.5) and (feature_num[575] > 213.5):
    label_class= 1 #(proba: 31.82%) | based on 44 samples
  if (feature_num[350] > 126.5) and (feature_num[489] <= 24.5) and (feature_num[290] <= 34.5) and (feature_num[486] > 93.5) and (feature_num[656] > 0.5) and (feature_num[439] > 12.5) and (feature_num[380] <= 9.5) and (feature_num[568] > 69.0):
    label_class= 0 #(proba: 100.0%) | based on 43 samples
  if (feature_num[350] > 126.5) and (feature_num[489] <= 24.5) and (feature_num[290] > 34.5) and (feature_num[297] <= 5.5) and (feature_num[486] > 58.0) and (feature_num[656] > 7.5) and (feature_num[300] <= 5.5) and (feature_num[206] > 18.0):
    label_class= 5 #(proba: 72.09%) | based on 43 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] <= 0.5) and (feature_num[430] <= 0.5) and (feature_num[405] <= 1.5) and (feature_num[485] > 6.0) and (feature_num[211] <= 53.5) and (feature_num[571] > 31.0) and (feature_num[626] > 2.0):
    label_class= 2 #(proba: 39.53%) | based on 43 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] > 0.5) and (feature_num[346] > 0.5) and (feature_num[655] <= 0.5) and (feature_num[271] > 1.0) and (feature_num[354] <= 10.5) and (feature_num[357] > 4.5):
    label_class= 2 #(proba: 31.71%) | based on 41 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] > 0.5) and (feature_num[346] > 0.5) and (feature_num[655] <= 0.5) and (feature_num[271] <= 1.0) and (feature_num[484] > 6.0) and (feature_num[218] > 18.5):
    label_class= 5 #(proba: 26.83%) | based on 41 samples
  if (feature_num[350] > 126.5) and (feature_num[489] > 24.5) and (feature_num[234] > 0.5) and (feature_num[658] > 0.5) and (feature_num[515] > 84.5) and (feature_num[319] > 0.5) and (feature_num[440] > 77.5) and (feature_num[547] > 162.0):
    label_class= 3 #(proba: 22.22%) | based on 36 samples
  if (feature_num[350] > 126.5) and (feature_num[489] > 24.5) and (feature_num[234] > 0.5) and (feature_num[658] <= 0.5) and (feature_num[345] <= 18.0) and (feature_num[526] <= 1.0) and (feature_num[541] <= 42.0) and (feature_num[603] > 231.5):
    label_class= 1 #(proba: 61.11%) | based on 36 samples
  if (feature_num[350] > 126.5) and (feature_num[489] > 24.5) and (feature_num[234] <= 0.5) and (feature_num[402] > 0.5) and (feature_num[522] > 1.5) and (feature_num[293] > 65.0) and (feature_num[301] <= 38.0) and (feature_num[571] <= 6.0):
    label_class= 4 #(proba: 50.0%) | based on 36 samples
  if (feature_num[350] > 126.5) and (feature_num[489] <= 24.5) and (feature_num[290] <= 34.5) and (feature_num[486] <= 93.5) and (feature_num[296] <= 2.5) and (feature_num[462] <= 81.0) and (feature_num[315] > 54.5) and (feature_num[327] > 133.0):
    label_class= 4 #(proba: 37.14%) | based on 35 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] <= 0.5) and (feature_num[430] <= 0.5) and (feature_num[405] <= 1.5) and (feature_num[485] <= 6.0) and (feature_num[154] <= 0.5) and (feature_num[594] <= 21.5) and (feature_num[156] > 0.5):
    label_class= 1 #(proba: 60.0%) | based on 35 samples
  if (feature_num[350] > 126.5) and (feature_num[489] > 24.5) and (feature_num[234] > 0.5) and (feature_num[658] <= 0.5) and (feature_num[345] > 18.0) and (feature_num[575] <= 89.0) and (feature_num[210] <= 21.5) and (feature_num[434] > 144.0):
    label_class= 4 #(proba: 55.88%) | based on 34 samples
  if (feature_num[350] > 126.5) and (feature_num[489] <= 24.5) and (feature_num[290] > 34.5) and (feature_num[297] <= 5.5) and (feature_num[486] <= 58.0) and (feature_num[186] > 2.5) and (feature_num[301] > 54.0) and (feature_num[381] <= 11.0):
    label_class= 0 #(proba: 100.0%) | based on 33 samples
  if (feature_num[350] > 126.5) and (feature_num[489] <= 24.5) and (feature_num[290] <= 34.5) and (feature_num[486] <= 93.5) and (feature_num[296] <= 2.5) and (feature_num[462] > 81.0) and (feature_num[628] > 24.0) and (feature_num[518] > 2.0):
    label_class= 5 #(proba: 51.72%) | based on 29 samples
  if (feature_num[350] > 126.5) and (feature_num[489] > 24.5) and (feature_num[234] <= 0.5) and (feature_num[402] > 0.5) and (feature_num[522] > 1.5) and (feature_num[293] <= 65.0) and (feature_num[511] <= 55.0) and (feature_num[654] > 1.0):
    label_class= 3 #(proba: 78.57%) | based on 28 samples
  if (feature_num[350] > 126.5) and (feature_num[489] > 24.5) and (feature_num[234] <= 0.5) and (feature_num[402] > 0.5) and (feature_num[522] > 1.5) and (feature_num[293] > 65.0) and (feature_num[301] > 38.0) and (feature_num[440] > 124.5):
    label_class= 0 #(proba: 92.59%) | based on 27 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] <= 0.5) and (feature_num[489] > 47.5) and (feature_num[320] > 1.0) and (feature_num[494] > 23.5) and (feature_num[358] <= 176.5) and (feature_num[374] <= 41.5):
    label_class= 2 #(proba: 61.54%) | based on 26 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] <= 0.5) and (feature_num[489] <= 47.5) and (feature_num[380] > 1.5) and (feature_num[298] > 116.5) and (feature_num[406] > 53.5) and (feature_num[486] > 33.5):
    label_class= 2 #(proba: 60.87%) | based on 23 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] <= 0.5) and (feature_num[430] <= 0.5) and (feature_num[405] > 1.5) and (feature_num[516] <= 14.5) and (feature_num[353] <= 2.5) and (feature_num[322] <= 8.5) and (feature_num[356] > 0.5):
    label_class= 4 #(proba: 47.83%) | based on 23 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] <= 0.5) and (feature_num[489] <= 47.5) and (feature_num[380] <= 1.5) and (feature_num[324] <= 173.0) and (feature_num[72] > 1.0) and (feature_num[236] > 6.0):
    label_class= 6 #(proba: 95.65%) | based on 23 samples
  if (feature_num[350] > 126.5) and (feature_num[489] <= 24.5) and (feature_num[290] > 34.5) and (feature_num[297] <= 5.5) and (feature_num[486] > 58.0) and (feature_num[656] > 7.5) and (feature_num[300] <= 5.5) and (feature_num[206] <= 18.0):
    label_class= 6 #(proba: 52.17%) | based on 23 samples
  if (feature_num[350] > 126.5) and (feature_num[489] <= 24.5) and (feature_num[290] > 34.5) and (feature_num[297] > 5.5) and (feature_num[598] <= 0.5) and (feature_num[210] <= 4.5) and (feature_num[404] <= 7.0) and (feature_num[320] <= 204.0):
    label_class= 6 #(proba: 27.27%) | based on 22 samples
  if (feature_num[350] > 126.5) and (feature_num[489] > 24.5) and (feature_num[234] <= 0.5) and (feature_num[402] <= 0.5) and (feature_num[300] <= 5.5) and (feature_num[149] > 4.5) and (feature_num[318] <= 13.5) and (feature_num[516] <= 16.5):
    label_class= 3 #(proba: 45.45%) | based on 22 samples
  if (feature_num[350] > 126.5) and (feature_num[489] <= 24.5) and (feature_num[290] <= 34.5) and (feature_num[486] <= 93.5) and (feature_num[296] <= 2.5) and (feature_num[462] > 81.0) and (feature_num[628] > 24.0) and (feature_num[518] <= 2.0):
    label_class= 3 #(proba: 85.71%) | based on 21 samples
  if (feature_num[350] > 126.5) and (feature_num[489] <= 24.5) and (feature_num[290] <= 34.5) and (feature_num[486] > 93.5) and (feature_num[656] <= 0.5) and (feature_num[152] <= 6.0) and (feature_num[601] <= 74.0) and (feature_num[432] <= 210.0):
    label_class= 5 #(proba: 75.0%) | based on 20 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] > 0.5) and (feature_num[346] > 0.5) and (feature_num[655] > 0.5) and (feature_num[354] > 0.5) and (feature_num[434] <= 47.0) and (feature_num[484] <= 54.0):
    label_class= 2 #(proba: 36.84%) | based on 19 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] <= 0.5) and (feature_num[489] <= 47.5) and (feature_num[380] > 1.5) and (feature_num[298] <= 116.5) and (feature_num[485] > 93.0) and (feature_num[215] > 1.5):
    label_class= 0 #(proba: 31.58%) | based on 19 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] > 0.5) and (feature_num[346] <= 0.5) and (feature_num[348] > 109.5) and (feature_num[655] > 26.5) and (feature_num[487] <= 1.5) and (feature_num[354] <= 33.0):
    label_class= 5 #(proba: 78.95%) | based on 19 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] > 0.5) and (feature_num[346] <= 0.5) and (feature_num[348] <= 109.5) and (feature_num[371] > 63.5) and (feature_num[213] <= 5.0) and (feature_num[402] > 3.0):
    label_class= 2 #(proba: 27.78%) | based on 18 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] <= 0.5) and (feature_num[489] <= 47.5) and (feature_num[380] > 1.5) and (feature_num[298] > 116.5) and (feature_num[406] > 53.5) and (feature_num[486] <= 33.5):
    label_class= 3 #(proba: 64.71%) | based on 17 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] > 0.5) and (feature_num[346] <= 0.5) and (feature_num[348] <= 109.5) and (feature_num[371] > 63.5) and (feature_num[213] > 5.0) and (feature_num[315] <= 11.5):
    label_class= 2 #(proba: 94.12%) | based on 17 samples
  if (feature_num[350] > 126.5) and (feature_num[489] > 24.5) and (feature_num[234] > 0.5) and (feature_num[658] <= 0.5) and (feature_num[345] <= 18.0) and (feature_num[526] > 1.0) and (feature_num[370] > 11.5) and (feature_num[263] <= 28.5):
    label_class= 6 #(proba: 94.12%) | based on 17 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] <= 0.5) and (feature_num[430] > 0.5) and (feature_num[211] <= 28.5) and (feature_num[98] > 0.5) and (feature_num[537] > 8.0) and (feature_num[496] <= 252.5):
    label_class= 2 #(proba: 100.0%) | based on 16 samples
  if (feature_num[350] > 126.5) and (feature_num[489] > 24.5) and (feature_num[234] <= 0.5) and (feature_num[402] > 0.5) and (feature_num[522] <= 1.5) and (feature_num[275] > 33.5) and (feature_num[381] > 56.5) and (feature_num[432] <= 54.5):
    label_class= 5 #(proba: 62.5%) | based on 16 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] <= 0.5) and (feature_num[489] > 47.5) and (feature_num[320] <= 1.0) and (feature_num[345] > 104.5) and (feature_num[239] <= 88.0) and (feature_num[601] > 123.5):
    label_class= 6 #(proba: 50.0%) | based on 16 samples
  if (feature_num[350] > 126.5) and (feature_num[489] <= 24.5) and (feature_num[290] > 34.5) and (feature_num[297] <= 5.5) and (feature_num[486] > 58.0) and (feature_num[656] > 7.5) and (feature_num[300] > 5.5) and (feature_num[407] <= 90.5):
    label_class= 0 #(proba: 100.0%) | based on 15 samples
  if (feature_num[350] > 126.5) and (feature_num[489] > 24.5) and (feature_num[234] <= 0.5) and (feature_num[402] <= 0.5) and (feature_num[300] > 5.5) and (feature_num[265] <= 34.0) and (feature_num[460] <= 241.0) and (feature_num[414] > 77.0):
    label_class= 6 #(proba: 100.0%) | based on 15 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] <= 0.5) and (feature_num[489] > 47.5) and (feature_num[320] <= 1.0) and (feature_num[345] > 104.5) and (feature_num[239] <= 88.0) and (feature_num[601] <= 123.5):
    label_class= 4 #(proba: 66.67%) | based on 15 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] <= 0.5) and (feature_num[489] <= 47.5) and (feature_num[380] > 1.5) and (feature_num[298] > 116.5) and (feature_num[406] <= 53.5) and (feature_num[237] <= 1.5):
    label_class= 2 #(proba: 26.67%) | based on 15 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] <= 0.5) and (feature_num[489] <= 47.5) and (feature_num[380] <= 1.5) and (feature_num[324] > 173.0) and (feature_num[427] > 16.5) and (feature_num[329] <= 3.0):
    label_class= 0 #(proba: 42.86%) | based on 14 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] <= 0.5) and (feature_num[489] > 47.5) and (feature_num[320] > 1.0) and (feature_num[494] <= 23.5) and (feature_num[380] <= 17.5) and (feature_num[485] > 241.5):
    label_class= 6 #(proba: 84.62%) | based on 13 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] > 0.5) and (feature_num[346] > 0.5) and (feature_num[655] > 0.5) and (feature_num[354] <= 0.5) and (feature_num[514] <= 86.5) and (feature_num[357] > 9.5):
    label_class= 0 #(proba: 38.46%) | based on 13 samples
  if (feature_num[350] > 126.5) and (feature_num[489] > 24.5) and (feature_num[234] > 0.5) and (feature_num[658] <= 0.5) and (feature_num[345] > 18.0) and (feature_num[575] <= 89.0) and (feature_num[210] > 21.5) and (feature_num[498] > 111.0):
    label_class= 2 #(proba: 69.23%) | based on 13 samples
  if (feature_num[350] > 126.5) and (feature_num[489] > 24.5) and (feature_num[234] <= 0.5) and (feature_num[402] <= 0.5) and (feature_num[300] > 5.5) and (feature_num[265] > 34.0) and (feature_num[514] <= 11.5) and (feature_num[212] <= 95.5):
    label_class= 7 #(proba: 38.46%) | based on 13 samples
  if (feature_num[350] > 126.5) and (feature_num[489] > 24.5) and (feature_num[234] > 0.5) and (feature_num[658] <= 0.5) and (feature_num[345] > 18.0) and (feature_num[575] > 89.0) and (feature_num[240] > 107.0) and (feature_num[481] > 178.5):
    label_class= 0 #(proba: 90.91%) | based on 11 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] > 0.5) and (feature_num[346] <= 0.5) and (feature_num[348] > 109.5) and (feature_num[655] > 26.5) and (feature_num[487] <= 1.5) and (feature_num[354] > 33.0):
    label_class= 3 #(proba: 45.45%) | based on 11 samples
  if (feature_num[350] > 126.5) and (feature_num[489] > 24.5) and (feature_num[234] > 0.5) and (feature_num[658] > 0.5) and (feature_num[515] > 84.5) and (feature_num[319] > 0.5) and (feature_num[440] <= 77.5) and (feature_num[609] > 209.0):
    label_class= 2 #(proba: 54.55%) | based on 11 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] <= 0.5) and (feature_num[489] > 47.5) and (feature_num[320] <= 1.0) and (feature_num[345] > 104.5) and (feature_num[239] > 88.0) and (feature_num[526] <= 14.5):
    label_class= 5 #(proba: 90.91%) | based on 11 samples
  if (feature_num[350] > 126.5) and (feature_num[489] <= 24.5) and (feature_num[290] <= 34.5) and (feature_num[486] > 93.5) and (feature_num[656] > 0.5) and (feature_num[439] > 12.5) and (feature_num[380] <= 9.5) and (feature_num[568] <= 69.0):
    label_class= 6 #(proba: 27.27%) | based on 11 samples
  if (feature_num[350] > 126.5) and (feature_num[489] <= 24.5) and (feature_num[290] <= 34.5) and (feature_num[486] > 93.5) and (feature_num[656] <= 0.5) and (feature_num[152] > 6.0) and (feature_num[438] <= 27.0) and (feature_num[343] > 5.0):
    label_class= 6 #(proba: 45.45%) | based on 11 samples
  if (feature_num[350] > 126.5) and (feature_num[489] <= 24.5) and (feature_num[290] > 34.5) and (feature_num[297] > 5.5) and (feature_num[598] > 0.5) and (feature_num[486] <= 7.5) and (feature_num[427] > 168.5) and (feature_num[381] > 132.5):
    label_class= 5 #(proba: 50.0%) | based on 10 samples
  if (feature_num[350] > 126.5) and (feature_num[489] <= 24.5) and (feature_num[290] <= 34.5) and (feature_num[486] > 93.5) and (feature_num[656] <= 0.5) and (feature_num[152] > 6.0) and (feature_num[438] > 27.0) and (feature_num[484] > 42.0):
    label_class= 3 #(proba: 80.0%) | based on 10 samples
  if (feature_num[350] > 126.5) and (feature_num[489] > 24.5) and (feature_num[234] > 0.5) and (feature_num[658] <= 0.5) and (feature_num[345] <= 18.0) and (feature_num[526] > 1.0) and (feature_num[370] > 11.5) and (feature_num[263] > 28.5):
    label_class= 2 #(proba: 30.0%) | based on 10 samples
  if (feature_num[350] > 126.5) and (feature_num[489] > 24.5) and (feature_num[234] > 0.5) and (feature_num[658] <= 0.5) and (feature_num[345] > 18.0) and (feature_num[575] <= 89.0) and (feature_num[210] <= 21.5) and (feature_num[434] <= 144.0):
    label_class= 7 #(proba: 77.78%) | based on 9 samples
  if (feature_num[350] > 126.5) and (feature_num[489] > 24.5) and (feature_num[234] > 0.5) and (feature_num[658] > 0.5) and (feature_num[515] <= 84.5) and (feature_num[545] <= 5.5) and (feature_num[318] <= 38.5) and (feature_num[292] > 168.5):
    label_class= 1 #(proba: 62.5%) | based on 8 samples
  if (feature_num[350] > 126.5) and (feature_num[489] > 24.5) and (feature_num[234] <= 0.5) and (feature_num[402] > 0.5) and (feature_num[522] > 1.5) and (feature_num[293] <= 65.0) and (feature_num[511] > 55.0) and (feature_num[385] > 214.5):
    label_class= 6 #(proba: 75.0%) | based on 8 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] <= 0.5) and (feature_num[430] > 0.5) and (feature_num[211] <= 28.5) and (feature_num[98] <= 0.5) and (feature_num[267] <= 128.5) and (feature_num[95] > 7.0) and (feature_num[242] > 90.0):
    label_class= 4 #(proba: 85.71%) | based on 7 samples
  if (feature_num[350] > 126.5) and (feature_num[489] > 24.5) and (feature_num[234] <= 0.5) and (feature_num[402] <= 0.5) and (feature_num[300] > 5.5) and (feature_num[265] > 34.0) and (feature_num[514] > 11.5) and (feature_num[434] <= 98.0):
    label_class= 3 #(proba: 42.86%) | based on 7 samples
  if (feature_num[350] > 126.5) and (feature_num[489] <= 24.5) and (feature_num[290] > 34.5) and (feature_num[297] <= 5.5) and (feature_num[486] > 58.0) and (feature_num[656] <= 7.5) and (feature_num[373] > 13.5) and (feature_num[514] <= 47.5):
    label_class= 5 #(proba: 57.14%) | based on 7 samples
  if (feature_num[350] > 126.5) and (feature_num[489] <= 24.5) and (feature_num[290] <= 34.5) and (feature_num[486] <= 93.5) and (feature_num[296] <= 2.5) and (feature_num[462] > 81.0) and (feature_num[628] <= 24.0) and (feature_num[375] > 14.5):
    label_class= 2 #(proba: 28.57%) | based on 7 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] <= 0.5) and (feature_num[430] > 0.5) and (feature_num[211] <= 28.5) and (feature_num[98] > 0.5) and (feature_num[537] <= 8.0) and (feature_num[242] > 7.0) and (feature_num[460] > 19.0):
    label_class= 2 #(proba: 57.14%) | based on 7 samples
  if (feature_num[350] > 126.5) and (feature_num[489] <= 24.5) and (feature_num[290] <= 34.5) and (feature_num[486] <= 93.5) and (feature_num[296] > 2.5) and (feature_num[153] > 1.0) and (feature_num[488] > 60.0) and (feature_num[627] > 248.5):
    label_class= 3 #(proba: 50.0%) | based on 6 samples
  if (feature_num[350] > 126.5) and (feature_num[489] > 24.5) and (feature_num[234] > 0.5) and (feature_num[658] <= 0.5) and (feature_num[345] <= 18.0) and (feature_num[526] > 1.0) and (feature_num[370] <= 11.5) and (feature_num[284] > 19.5):
    label_class= 3 #(proba: 100.0%) | based on 6 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] <= 0.5) and (feature_num[430] > 0.5) and (feature_num[211] > 28.5) and (feature_num[156] > 0.5) and (feature_num[101] > 1.0) and (feature_num[271] > 136.5) and (feature_num[294] <= 0.5):
    label_class= 2 #(proba: 100.0%) | based on 6 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] > 0.5) and (feature_num[346] <= 0.5) and (feature_num[348] > 109.5) and (feature_num[655] <= 26.5) and (feature_num[130] > 48.5) and (feature_num[270] > 22.5):
    label_class= 2 #(proba: 33.33%) | based on 6 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] > 0.5) and (feature_num[346] <= 0.5) and (feature_num[348] > 109.5) and (feature_num[655] > 26.5) and (feature_num[487] > 1.5) and (feature_num[439] > 205.0):
    label_class= 5 #(proba: 50.0%) | based on 6 samples
  if (feature_num[350] > 126.5) and (feature_num[489] <= 24.5) and (feature_num[290] > 34.5) and (feature_num[297] <= 5.5) and (feature_num[486] > 58.0) and (feature_num[656] <= 7.5) and (feature_num[373] <= 13.5) and (feature_num[374] > 207.0):
    label_class= 6 #(proba: 100.0%) | based on 5 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] <= 0.5) and (feature_num[430] > 0.5) and (feature_num[211] > 28.5) and (feature_num[156] > 0.5) and (feature_num[101] > 1.0) and (feature_num[271] <= 136.5) and (feature_num[296] > 146.5):
    label_class= 4 #(proba: 60.0%) | based on 5 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] <= 0.5) and (feature_num[430] > 0.5) and (feature_num[211] <= 28.5) and (feature_num[98] > 0.5) and (feature_num[537] <= 8.0) and (feature_num[242] > 7.0) and (feature_num[460] <= 19.0):
    label_class= 0 #(proba: 100.0%) | based on 5 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] <= 0.5) and (feature_num[430] <= 0.5) and (feature_num[405] <= 1.5) and (feature_num[485] <= 6.0) and (feature_num[154] <= 0.5) and (feature_num[594] > 21.5) and (feature_num[464] > 125.0):
    label_class= 3 #(proba: 60.0%) | based on 5 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] <= 0.5) and (feature_num[489] <= 47.5) and (feature_num[380] <= 1.5) and (feature_num[324] <= 173.0) and (feature_num[72] > 1.0) and (feature_num[236] <= 6.0):
    label_class= 2 #(proba: 60.0%) | based on 5 samples
  if (feature_num[350] > 126.5) and (feature_num[489] > 24.5) and (feature_num[234] > 0.5) and (feature_num[658] > 0.5) and (feature_num[515] > 84.5) and (feature_num[319] <= 0.5) and (feature_num[345] > 27.5) and (feature_num[150] > 167.5):
    label_class= 6 #(proba: 60.0%) | based on 5 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] <= 0.5) and (feature_num[430] <= 0.5) and (feature_num[405] <= 1.5) and (feature_num[485] <= 6.0) and (feature_num[154] > 0.5) and (feature_num[509] > 12.5) and (feature_num[351] > 48.5):
    label_class= 3 #(proba: 80.0%) | based on 5 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] <= 0.5) and (feature_num[489] > 47.5) and (feature_num[320] <= 1.0) and (feature_num[345] <= 104.5) and (feature_num[343] > 132.5) and (feature_num[441] > 240.5):
    label_class= 0 #(proba: 100.0%) | based on 4 samples
  if (feature_num[350] > 126.5) and (feature_num[489] <= 24.5) and (feature_num[290] <= 34.5) and (feature_num[486] > 93.5) and (feature_num[656] > 0.5) and (feature_num[439] <= 12.5) and (feature_num[464] > 1.0) and (feature_num[148] > 131.5):
    label_class= 3 #(proba: 100.0%) | based on 4 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] <= 0.5) and (feature_num[489] > 47.5) and (feature_num[320] <= 1.0) and (feature_num[345] > 104.5) and (feature_num[239] > 88.0) and (feature_num[526] > 14.5):
    label_class= 0 #(proba: 75.0%) | based on 4 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] <= 0.5) and (feature_num[489] > 47.5) and (feature_num[320] > 1.0) and (feature_num[494] > 23.5) and (feature_num[358] > 176.5) and (feature_num[621] > 230.5):
    label_class= 2 #(proba: 100.0%) | based on 3 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] <= 0.5) and (feature_num[489] > 47.5) and (feature_num[320] <= 1.0) and (feature_num[345] <= 104.5) and (feature_num[343] > 132.5) and (feature_num[441] <= 240.5):
    label_class= 4 #(proba: 33.33%) | based on 3 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] <= 0.5) and (feature_num[430] > 0.5) and (feature_num[211] > 28.5) and (feature_num[156] > 0.5) and (feature_num[101] > 1.0) and (feature_num[271] > 136.5) and (feature_num[294] > 0.5):
    label_class= 0 #(proba: 100.0%) | based on 2 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] <= 0.5) and (feature_num[430] > 0.5) and (feature_num[211] <= 28.5) and (feature_num[98] > 0.5) and (feature_num[537] <= 8.0) and (feature_num[242] <= 7.0) and (feature_num[240] > 1.0):
    label_class= 0 #(proba: 50.0%) | based on 2 samples
  if (feature_num[350] > 126.5) and (feature_num[489] > 24.5) and (feature_num[234] <= 0.5) and (feature_num[402] <= 0.5) and (feature_num[300] <= 5.5) and (feature_num[149] > 4.5) and (feature_num[318] > 13.5) and (feature_num[405] <= 12.5):
    label_class= 3 #(proba: 50.0%) | based on 2 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] <= 0.5) and (feature_num[489] > 47.5) and (feature_num[320] > 1.0) and (feature_num[494] <= 23.5) and (feature_num[380] > 17.5) and (feature_num[378] <= 12.5):
    label_class= 1 #(proba: 100.0%) | based on 1 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] <= 0.5) and (feature_num[430] > 0.5) and (feature_num[211] <= 28.5) and (feature_num[98] > 0.5) and (feature_num[537] > 8.0) and (feature_num[496] > 252.5):
    label_class= 4 #(proba: 100.0%) | based on 1 samples
  return label_class
