import pandas as pd
import numpy as np

s1 = pd.Series([10,20,30,40,50])
print(f's1\n{s1}')


s2 = pd.Series(['a','b',30,40,50])
print(f's2\n{s2}')

s3 = pd.Series([np.nan,'b',30,40,50])
print(f's3\n{s3}')

index_date = ['2023-09-15', '2023-09-16', '2023-09-17', '2023-09-18']
s4 = pd.Series([200, 195, np.nan, 205], index=index_date)
print(f's4\n{s4}')

s5 = pd.Series({'국어': 100, '영어': 95, '수학': 90})
print(f's5\n{s5}')

df = pd.DataFrame({'제품' : ['사과','딸기','수박'], '가격' : [1800,1500,3000], '판매량' : [24,38,13]})
print(f'df\n{df}')
print(f"가격 평균 {sum(df['가격'])/df['가격'].size}")
print(f"판매량 평균 {sum(df['판매량'])/df['판매량'].size}")

df_ecel = pd.read_excel('excel_exam.xlsx')
print(f"엑셀 {df_ecel}")

df_csv = pd.read_csv('exam.csv')
print(f"csv {df_csv}")

