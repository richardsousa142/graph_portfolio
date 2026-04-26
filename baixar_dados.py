from get_b3_data import B3PublicData

anos = range(2015, 2026)
b3 = B3PublicData()
 
for ano in anos:
    b3.read_df_year(ano)
    