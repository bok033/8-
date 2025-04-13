
import statsmodels.api as sm
df = sm.datasets.sunspots.load_pandas().data
df["YEAR"] = df["YEAR"].astype(int)
df["date"] = pd.to_datetime(df["YEAR"], format="%Y")
df = df.set_index("date").sort_index()

# Prophet용 전처리
# 1. 인덱스를 다시 컬럼으로 변환(reset_index)
# 2. Prophet은 입력 컬럼명으로 'ds'(날짜)와 'y'(타겟값)를 요구하므로 컬럼명 변경
''' 코드 작성 '''
processed_df = df.reset_index().rename(columns={'date': 'ds', 'SUNACTIVITY': 'y'})



# 1900-01-01부터 2008-01-01까지의 데이터만 필터링
# Prophet 모델 학습에 사용할 기간을 제한함
''' 코드 작성 '''
processed_df = processed_df[(processed_df['ds'] >= '1900-01-01') & (processed_df['ds'] <= '2008-01-01')]


# 전처리된 데이터프레임을 CSV 파일(경로: ./sunspots_for_prophet.csv)로 저장
# index=False 옵션은 데이터프레임의 인덱스를 CSV에 포함시키지 않음
# 저장한 파일도 같이 제출해주세요.
''' 코드 작성 '''
processed_df.to_csv('./sunspots_for_prophet.csv', index=False)

print("✅ prophet용 데이터 저장 완료!")
