import pandas as pd
chunksize = 20000
df = pd.read_csv('./data/Criteo_Conversion_Search/CriteoSearchData',header=None,delimiter='\t',chunksize=chunksize)
i = 0
target_column =  ['Sale','SalesAmountInEuro','time_delay_for_conversion'] 
feature_column=['click_timestamp','nb_clicks_1week','product_price','product_age_group','device_type','audience_id','product_gender','product_brand','product_category1','product_category2','product_category3','product_category4','product_category5','product_category6','product_category7','product_country','product_id','product_title','partner_id','user_id']
# 

df1=pd.DataFrame(columns = target_column+feature_column)
for chunk in df: #
    
    chunk.columns = target_column+feature_column

    index = chunk[(chunk.SalesAmountInEuro<= 400) & (chunk.SalesAmountInEuro >= 0)].index - i * chunksize # 
    index = index.tolist()

    df1 = pd.concat([df1,pd.DataFrame(chunk.iloc[index,:])],axis=0)
    i = i + 1

    
df1.drop(['Sale', 'click_timestamp'], axis = 1, inplace = True)
df1.to_csv('./data/Criteo_Search.txt', sep = '\t',  line_terminator = '\n', index=False, header=True)