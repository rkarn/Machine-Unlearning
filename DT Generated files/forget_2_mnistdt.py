def decision_tree_inference(feature_num):
  label_class= None
  if (feature_num[350] > 126.5) and (feature_num[489] > 24.5) and (feature_num[234] <= 0.5) and (feature_num[402] <= 0.5) and (feature_num[300] <= 5.5) and (feature_num[149] <= 4.5) and (feature_num[494] <= 4.0) and (feature_num[538] <= 26.5):
    label_class= 1 #(proba: 95.77%) | based on 4,798 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] <= 0.5) and (feature_num[489] <= 47.5) and (feature_num[380] <= 1.5) and (feature_num[324] <= 173.0) and (feature_num[72] <= 1.0) and (feature_num[455] > 0.5):
    label_class= 0 #(proba: 97.59%) | based on 3,195 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] <= 0.5) and (feature_num[489] <= 47.5) and (feature_num[380] <= 1.5) and (feature_num[324] <= 173.0) and (feature_num[72] <= 1.0) and (feature_num[455] <= 0.5):
    label_class= 0 #(proba: 77.69%) | based on 520 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] <= 0.5) and (feature_num[430] > 0.5) and (feature_num[211] > 28.5) and (feature_num[156] > 0.5) and (feature_num[101] <= 1.0) and (feature_num[656] > 1.5) and (feature_num[434] <= 0.5):
    label_class= 0 #(proba: 69.66%) | based on 267 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] <= 0.5) and (feature_num[430] <= 0.5) and (feature_num[405] > 1.5) and (feature_num[516] > 14.5) and (feature_num[376] <= 3.5) and (feature_num[207] <= 0.5) and (feature_num[263] <= 9.0):
    label_class= 1 #(proba: 86.18%) | based on 246 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] > 0.5) and (feature_num[346] <= 0.5) and (feature_num[348] <= 109.5) and (feature_num[371] <= 63.5) and (feature_num[155] <= 0.5) and (feature_num[652] > 6.0):
    label_class= 1 #(proba: 48.55%) | based on 241 samples
  if (feature_num[350] > 126.5) and (feature_num[489] <= 24.5) and (feature_num[290] <= 34.5) and (feature_num[486] <= 93.5) and (feature_num[296] <= 2.5) and (feature_num[462] > 81.0) and (feature_num[628] <= 24.0) and (feature_num[375] <= 14.5):
    label_class= 1 #(proba: 99.43%) | based on 176 samples
  if (feature_num[350] > 126.5) and (feature_num[489] > 24.5) and (feature_num[234] <= 0.5) and (feature_num[402] <= 0.5) and (feature_num[300] > 5.5) and (feature_num[265] <= 34.0) and (feature_num[460] > 241.0) and (feature_num[270] > 159.0):
    label_class= 1 #(proba: 89.34%) | based on 122 samples
  if (feature_num[350] > 126.5) and (feature_num[489] > 24.5) and (feature_num[234] <= 0.5) and (feature_num[402] > 0.5) and (feature_num[522] <= 1.5) and (feature_num[275] <= 33.5) and (feature_num[346] <= 7.0) and (feature_num[268] > 236.5):
    label_class= 1 #(proba: 70.0%) | based on 110 samples
  if (feature_num[350] > 126.5) and (feature_num[489] <= 24.5) and (feature_num[290] > 34.5) and (feature_num[297] > 5.5) and (feature_num[598] > 0.5) and (feature_num[486] > 7.5) and (feature_num[400] > 24.5) and (feature_num[242] > 56.0):
    label_class= 0 #(proba: 56.31%) | based on 103 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] <= 0.5) and (feature_num[489] <= 47.5) and (feature_num[380] > 1.5) and (feature_num[298] > 116.5) and (feature_num[406] <= 53.5) and (feature_num[237] > 1.5):
    label_class= 0 #(proba: 87.36%) | based on 87 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] <= 0.5) and (feature_num[430] <= 0.5) and (feature_num[405] <= 1.5) and (feature_num[485] <= 6.0) and (feature_num[154] > 0.5) and (feature_num[509] > 12.5) and (feature_num[351] <= 48.5):
    label_class= 0 #(proba: 97.56%) | based on 82 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] <= 0.5) and (feature_num[430] > 0.5) and (feature_num[211] > 28.5) and (feature_num[156] <= 0.5) and (feature_num[381] <= 4.5) and (feature_num[217] <= 1.5) and (feature_num[542] > 70.5):
    label_class= 0 #(proba: 58.57%) | based on 70 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] <= 0.5) and (feature_num[430] <= 0.5) and (feature_num[405] <= 1.5) and (feature_num[485] <= 6.0) and (feature_num[154] <= 0.5) and (feature_num[594] > 21.5) and (feature_num[464] <= 125.0):
    label_class= 0 #(proba: 95.65%) | based on 69 samples
  if (feature_num[350] > 126.5) and (feature_num[489] <= 24.5) and (feature_num[290] > 34.5) and (feature_num[297] > 5.5) and (feature_num[598] > 0.5) and (feature_num[486] <= 7.5) and (feature_num[427] > 168.5) and (feature_num[381] <= 132.5):
    label_class= 0 #(proba: 91.94%) | based on 62 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] > 0.5) and (feature_num[346] > 0.5) and (feature_num[655] > 0.5) and (feature_num[354] > 0.5) and (feature_num[434] <= 47.0) and (feature_num[484] > 54.0):
    label_class= 0 #(proba: 90.16%) | based on 61 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] <= 0.5) and (feature_num[489] <= 47.5) and (feature_num[380] <= 1.5) and (feature_num[324] > 173.0) and (feature_num[427] > 16.5) and (feature_num[329] > 3.0):
    label_class= 0 #(proba: 100.0%) | based on 59 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] <= 0.5) and (feature_num[430] <= 0.5) and (feature_num[405] <= 1.5) and (feature_num[485] > 6.0) and (feature_num[211] > 53.5) and (feature_num[427] > 1.0) and (feature_num[470] > 3.0):
    label_class= 0 #(proba: 47.46%) | based on 59 samples
  if (feature_num[350] > 126.5) and (feature_num[489] <= 24.5) and (feature_num[290] <= 34.5) and (feature_num[486] > 93.5) and (feature_num[656] <= 0.5) and (feature_num[152] <= 6.0) and (feature_num[601] <= 74.0) and (feature_num[432] > 210.0):
    label_class= 1 #(proba: 47.46%) | based on 59 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] <= 0.5) and (feature_num[489] > 47.5) and (feature_num[320] > 1.0) and (feature_num[494] > 23.5) and (feature_num[358] > 176.5) and (feature_num[621] <= 230.5):
    label_class= 0 #(proba: 100.0%) | based on 57 samples
  if (feature_num[350] > 126.5) and (feature_num[489] > 24.5) and (feature_num[234] > 0.5) and (feature_num[658] > 0.5) and (feature_num[515] <= 84.5) and (feature_num[545] > 5.5) and (feature_num[578] > 35.5) and (feature_num[575] > 213.5):
    label_class= 1 #(proba: 31.82%) | based on 44 samples
  if (feature_num[350] > 126.5) and (feature_num[489] <= 24.5) and (feature_num[290] <= 34.5) and (feature_num[486] > 93.5) and (feature_num[656] > 0.5) and (feature_num[439] > 12.5) and (feature_num[380] <= 9.5) and (feature_num[568] > 69.0):
    label_class= 0 #(proba: 100.0%) | based on 43 samples
  if (feature_num[350] > 126.5) and (feature_num[489] > 24.5) and (feature_num[234] > 0.5) and (feature_num[658] <= 0.5) and (feature_num[345] <= 18.0) and (feature_num[526] <= 1.0) and (feature_num[541] <= 42.0) and (feature_num[603] > 231.5):
    label_class= 1 #(proba: 61.11%) | based on 36 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] <= 0.5) and (feature_num[430] <= 0.5) and (feature_num[405] <= 1.5) and (feature_num[485] <= 6.0) and (feature_num[154] <= 0.5) and (feature_num[594] <= 21.5) and (feature_num[156] > 0.5):
    label_class= 1 #(proba: 60.0%) | based on 35 samples
  if (feature_num[350] > 126.5) and (feature_num[489] <= 24.5) and (feature_num[290] > 34.5) and (feature_num[297] <= 5.5) and (feature_num[486] <= 58.0) and (feature_num[186] > 2.5) and (feature_num[301] > 54.0) and (feature_num[381] <= 11.0):
    label_class= 0 #(proba: 100.0%) | based on 33 samples
  if (feature_num[350] > 126.5) and (feature_num[489] > 24.5) and (feature_num[234] <= 0.5) and (feature_num[402] > 0.5) and (feature_num[522] > 1.5) and (feature_num[293] > 65.0) and (feature_num[301] > 38.0) and (feature_num[440] > 124.5):
    label_class= 0 #(proba: 92.59%) | based on 27 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] <= 0.5) and (feature_num[489] <= 47.5) and (feature_num[380] > 1.5) and (feature_num[298] <= 116.5) and (feature_num[485] > 93.0) and (feature_num[215] > 1.5):
    label_class= 0 #(proba: 31.58%) | based on 19 samples
  if (feature_num[350] > 126.5) and (feature_num[489] <= 24.5) and (feature_num[290] > 34.5) and (feature_num[297] <= 5.5) and (feature_num[486] > 58.0) and (feature_num[656] > 7.5) and (feature_num[300] > 5.5) and (feature_num[407] <= 90.5):
    label_class= 0 #(proba: 100.0%) | based on 15 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] <= 0.5) and (feature_num[489] <= 47.5) and (feature_num[380] <= 1.5) and (feature_num[324] > 173.0) and (feature_num[427] > 16.5) and (feature_num[329] <= 3.0):
    label_class= 0 #(proba: 42.86%) | based on 14 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] > 0.5) and (feature_num[346] > 0.5) and (feature_num[655] > 0.5) and (feature_num[354] <= 0.5) and (feature_num[514] <= 86.5) and (feature_num[357] > 9.5):
    label_class= 0 #(proba: 38.46%) | based on 13 samples
  if (feature_num[350] > 126.5) and (feature_num[489] > 24.5) and (feature_num[234] > 0.5) and (feature_num[658] <= 0.5) and (feature_num[345] > 18.0) and (feature_num[575] > 89.0) and (feature_num[240] > 107.0) and (feature_num[481] > 178.5):
    label_class= 0 #(proba: 90.91%) | based on 11 samples
  if (feature_num[350] > 126.5) and (feature_num[489] > 24.5) and (feature_num[234] > 0.5) and (feature_num[658] > 0.5) and (feature_num[515] <= 84.5) and (feature_num[545] <= 5.5) and (feature_num[318] <= 38.5) and (feature_num[292] > 168.5):
    label_class= 1 #(proba: 62.5%) | based on 8 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] <= 0.5) and (feature_num[430] > 0.5) and (feature_num[211] <= 28.5) and (feature_num[98] > 0.5) and (feature_num[537] <= 8.0) and (feature_num[242] > 7.0) and (feature_num[460] <= 19.0):
    label_class= 0 #(proba: 100.0%) | based on 5 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] <= 0.5) and (feature_num[489] > 47.5) and (feature_num[320] <= 1.0) and (feature_num[345] <= 104.5) and (feature_num[343] > 132.5) and (feature_num[441] > 240.5):
    label_class= 0 #(proba: 100.0%) | based on 4 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] <= 0.5) and (feature_num[489] > 47.5) and (feature_num[320] <= 1.0) and (feature_num[345] > 104.5) and (feature_num[239] > 88.0) and (feature_num[526] > 14.5):
    label_class= 0 #(proba: 75.0%) | based on 4 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] <= 0.5) and (feature_num[430] > 0.5) and (feature_num[211] > 28.5) and (feature_num[156] > 0.5) and (feature_num[101] > 1.0) and (feature_num[271] > 136.5) and (feature_num[294] > 0.5):
    label_class= 0 #(proba: 100.0%) | based on 2 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] <= 0.5) and (feature_num[430] > 0.5) and (feature_num[211] <= 28.5) and (feature_num[98] > 0.5) and (feature_num[537] <= 8.0) and (feature_num[242] <= 7.0) and (feature_num[240] > 1.0):
    label_class= 0 #(proba: 50.0%) | based on 2 samples
  if (feature_num[350] <= 126.5) and (feature_num[568] > 0.5) and (feature_num[435] <= 0.5) and (feature_num[489] > 47.5) and (feature_num[320] > 1.0) and (feature_num[494] <= 23.5) and (feature_num[380] > 17.5) and (feature_num[378] <= 12.5):
    label_class= 1 #(proba: 100.0%) | based on 1 samples
  return label_class
