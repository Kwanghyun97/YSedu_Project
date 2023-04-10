import pandas as pd

# 엑셀 파일 경로 설정
excel_file = 'category_20230325_142255.xls'

# 엑셀 파일을 pandas DataFrame으로 변환
df = pd.read_excel(excel_file)

# 대분류 유니크한 데이터 추출
대분류 = df.iloc[:, 1].unique()

# 대분류 목록 출력
print("- 대분류 목록")
for i in range(len(대분류)):
    print(f"{i+1}. {대분류[i]}")

# 대분류 입력 받기
cat1 = input("대분류를 입력해주세요. \n : ")

# 해당 대분류에 해당하는 중분류 추출
중분류 = df[df.iloc[:, 1] == cat1].iloc[:, 2].unique()

# 중분류 목록 출력
print()
print("- 중분류 목록")
for i in range(len(중분류)):
    print(f"{i+1}. {중분류[i]}")

# 중분류 입력 받기
cat2 = input("중분류를 입력해주세요.\n : ")

# 해당 중분류에 해당하는 소분류 추출
소분류 = df[(df.iloc[:, 1] == cat1) & (df.iloc[:, 2] == cat2)].iloc[:, 3].unique()

# 소분류 목록 출력
print()
print("- 소분류 목록")
for i in range(len(소분류)):
    print(f"{i+1}. {소분류[i]}")

# 소분류 입력 받기
cat3 = input("소분류를 입력해주세요. \n : ")

# 해당 소분류에 해당하는 세분류 추출
세분류 = df[(df.iloc[:, 1] == cat1) & (df.iloc[:, 2] == cat2) & (df.iloc[:, 3] == cat3)].iloc[:, 4].values.tolist()

# 세분류가 있는 경우
if not pd.isnull(세분류).all():
    # 세분류 목록 출력
    print()
    print("- 세분류 목록")
    for i in range(len(세분류)):
        print(f"{i+1}. {세분류[i]}")

    # 세분류 입력 받기
    cat4 = input("세분류를 입력해주세요.\n : ")

    # 해당 조건에 맞는 데이터 추출 및 출력
    num = df[(df.iloc[:, 1] == cat1) & (df.iloc[:, 2] == cat2) & (df.iloc[:, 3] == cat3) & (df.iloc[:, 4] == cat4)].iloc[:, 0]
    if len(num) == 0:
        print("해당하는 데이터가 없습니다.")
    else:
        print(num)

# 세분류가 없는 경우
else:
    # 해당 조건에 맞는 데이터 추출 및 출력
    num = df[(df.iloc[:, 1] == cat1) & (df.iloc[:, 2] == cat2) & (df.iloc[:, 3] == cat3)].iloc[:, 0]
    if len(num) == 0:
        print("해당하는 데이터가 없습니다.")
    else:
        print(num)

        
## 위에서 입력한 카테고리의 모든 연령대 & 모든 접속 환경 & 모든 성별 의 상대 클릭량
import os
import sys
import json
import pandas as pd
import urllib.request

def get_relative_clicks(category_name, category_code):
    client_id = "JagKFffWu4Fj_OkksX_R"
    client_secret = "LD2ZmSF2j8"
    url = "https://openapi.naver.com/v1/datalab/shopping/categories"
    
    # ages, gender, device 변수 정의
    ages = ["10", "20", "30", "40", "50", "60"]
    genders = ["f", "m"]
    devices = ["pc", "mo"]
    
    # dfs 빈 리스트 선언
    dfs = []
    
    # for 문으로 연령별, 성별, 접속 환경별 request body 만들기 
    for age in ages:
        for gender in genders:
            for device in devices:
                body = {
                    "startDate": "2022-01-01",
                    "endDate": "2022-12-31",
                    "timeUnit": "month",
                    "category": [{"name": category_name, "param": [category_code]}],
                    "device": device,
                    "ages": [age],
                    "gender": gender
                }
                body = json.dumps(body)

                request = urllib.request.Request(url)
                request.add_header("X-Naver-Client-Id", client_id)
                request.add_header("X-Naver-Client-Secret", client_secret)
                request.add_header("Content-Type", "application/json")
                response = urllib.request.urlopen(request, data=body.encode("utf-8"))
                rescode = response.getcode()

                if rescode == 200:
                    response_body = response.read()
                    data = json.loads(response_body.decode('utf-8'))
                    df = pd.DataFrame(data['results'][0]['data'])
                    df["age"] = age
                    df["gender"] = gender
                    df["device"] = device
                    dfs.append(df)
                    
                else:
                    print("Error Code:", rescode)

    # final_df 함수에 모든 추출 데이터 합치기
    final_df = pd.concat(dfs, ignore_index=True)
    
    # Excel 파일의 별도 워크시트에 각 시트 작성
    with pd.ExcelWriter(f'{category_name}_relative_clicks.xlsx') as writer:
        for age in ages:
            age_df = final_df[final_df["age"] == age]
            age_df.to_excel(writer, sheet_name=f"{age}_ages", index=False)
        
        for gender in genders:
            gender_df = final_df[final_df["gender"] == gender]
            gender_df.to_excel(writer, sheet_name=f"{gender}_gender", index=False)
        
        for device in devices:
            device_df = final_df[final_df["device"] == device]
            device_df.to_excel(writer, sheet_name=f"{device}_device", index=False)
    result = f"{category_name}_relative_clicks.xlsx 파일이 저장 완료 되었습니다."
    return result        

print()
print("연령대 및 성별 등 조건에 따른 상대 클릭수 확인")
print("카테고리를 골랐다면, 카테고리 이름과 카테고리 코드를 입력해주세요.")
category_name = input("카테고리 이름을 넣어주세요. Ex)콜라\n :")
category_code = input("카테고리 코드를 입력해주세요. Ex)50002254\n :")

get_relative_clicks(category_name, category_code)

##############################################################
# 연령대 별로 접속 환경(PC, Mobile)에 따른 시계열 그래프 그리기 #
##############################################################

import pandas as pd
import matplotlib.pyplot as plt

def plot_relative_clicks(category_name):
    # 데이터프레임 생성
    df_list = []
    for age in range(10, 70, 10):
        sheet_name = f"{age}_ages"
        df = pd.read_excel(f"{category_name}_relative_clicks.xlsx", sheet_name=sheet_name)
        df['age'] = age
        df_list.append(df)

    df_all = pd.concat(df_list)

    # 날짜 형식 변경
    df_all['period'] = pd.to_datetime(df_all['period'], format='%Y-%m')

    # 피벗 테이블 생성
    pt = pd.pivot_table(df_all, values='ratio', index=['age', 'period'], columns='device',
                        aggfunc='sum', fill_value=0)

    # 연령대 별로 접속 환경(PC, Mobile)에 따른 시계열 그래프 그리기
    fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(15,8), sharex=True, sharey=True)
    for i, ax in enumerate(axes.flat):
        age = (i+1)*10
        pt_age = pt.loc[age]
        ax.plot(pt_age.index, pt_age['pc'], label='PC')
        ax.plot(pt_age.index, pt_age['mo'], label='Mobile')
        ax.set_title(f'{age} ages')
        ax.legend()

    # x축 라벨 세로로 표시하고 눈금을 12개 만들기
    fig.autofmt_xdate(rotation=90)
    plt.xticks(pd.date_range(start=pt.index.get_level_values(1).min(), end=pt.index.get_level_values(1).max(), freq='MS'),rotation=90)

    plt.suptitle('Relative clicks by device and age group')

    # 그래프 저장
    plt.savefig(f'{category_name}_pc_mo_relative_clicks.png')

# plot_relative_clicks("자급제폰")


print()
print("연령대 별로 접속 환경(PC, Mobile)에 따른 시계열 그래프 그리기")
category_name = input("카테고리 이름을 입력해주세요\n : ")
plot_relative_clicks(category_name)
print(f'{category_name}_pc_mo_relative_clicks.png 저장 완료')


########################################################################
# # 연령대 및 성별 별로 접속 환경(PC, Mobile)에 따른 상대클릭수 시계열 그래프 그리기 #
####################################################################3###

import pandas as pd
import matplotlib.pyplot as plt

def create_relative_clicks_graph(category_name):
    # 데이터프레임 생성
    df_list = []
    for age in range(10, 70, 10):
        sheet_name = f"{age}_ages"
        df = pd.read_excel(f"{category_name}_relative_clicks.xlsx", sheet_name=sheet_name)
        df['age'] = age
        df_list.append(df)

    df_all = pd.concat(df_list)

    # 날짜 형식 변경
    df_all['period'] = pd.to_datetime(df_all['period'], format='%Y-%m')

    # 피벗 테이블 생성
    pt = pd.pivot_table(df_all, values='ratio', index=['age', 'gender', 'period'], columns='device',
                        aggfunc='sum', fill_value=0)

    # 연령대 및 성별 별로 접속 환경(PC, Mobile)에 따른 시계열 그래프 그리기
    fig, axes = plt.subplots(nrows=4, ncols=3, figsize=(15,12), sharex=True, sharey=True)
    for i, ax in enumerate(axes.flat):
        age_gender = (i//2+1)*10, 'f' if i%2==0 else 'm'
        pt_age_gender = pt.loc[age_gender]
        ax.plot(pt_age_gender.index, pt_age_gender['pc'], label='PC')
        ax.plot(pt_age_gender.index, pt_age_gender['mo'], label='Mobile')
        ax.set_title(f'{age_gender[0]} ages {age_gender[1].upper()}')
        ax.legend()

    # x축 라벨 세로로 표시하고 눈금을 12개 만들기
    fig.autofmt_xdate(rotation=90)
    plt.xticks(pd.date_range(start=pt.index.get_level_values(2).min(), end=pt.index.get_level_values(2).max(), freq='MS'), rotation=90)

    plt.suptitle('Relative clicks by device, age group, and gender')
    # plt.show()

    # 그래프 저장
    plt.savefig(f'{category_name}_gender_relative_clicks.png')

print()
print("연령대 및 성별 별로 접속 환경(PC, Mobile)에 따른 시계열 그래프 그리기")
category_name = input("카테고리 이름을 입력해주세요\n : ")
create_relative_clicks_graph(category_name)
print(f'{category_name}_gender_relative_clicks.png 저장완료')

##########################################################################################
# # 팔려고 하는 물품 상위 100개의 가격 및 상위 10개의 브랜드 명 과 쇼핑몰 플랫폼(쿠팡, 네이버) #
###########################################################################################

def get_shop_info(keyword):
    client_id = "JagKFffWu4Fj_OkksX_R"
    client_secret = "LD2ZmSF2j8"
    encText = urllib.parse.quote(keyword)
    shop_url = "https://openapi.naver.com/v1/search/shop?query=" +encText+ "&display=100&start=1"
    request = urllib.request.Request(shop_url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if rescode == 200:
        response_body = response.read()
        json_str = response_body.decode('utf-8')
    else:
        response_body.decode('utf-8')
        print("Error Code: " + rescode)
    json_data = json.loads(json_str)
    df = pd.json_normalize(json_data['items'])
    df['title'] = df['title'].str.replace('<b>', '').str.replace('</b>', '')

    lprice_mean = df.loc[df['lprice'].notnull(), 'lprice'].astype(int).mean()

    mallName_cnt = df['mallName'].str.split(expand=True).stack().value_counts()
    mallName_dup_cnt = dict(mallName_cnt[:10])

    brand_cnt = df['brand'].str.split(expand=True).stack().value_counts()
    brand_dup_cnt = dict(brand_cnt[:10])
    
    return lprice_mean, mallName_dup_cnt, brand_dup_cnt,

print()
print("팔려고 하는 물품 상위 100개의 가격 및 상위 10개의 브랜드 명 과 쇼핑몰 플랫폼(쿠팡, 네이버) 확인 하기")
keyword = input("keyword 를 입력해주세요.\n : ")
lprice_mean, mallName_dup_cnt, brand_dup_cnt = get_shop_info(keyword)

print(f"상위 100개의 평균 가격 입니다. \n = {lprice_mean} 원")
print(f"상위 10개 쇼핑몰명 중복횟수 입니다. \n = {mallName_dup_cnt}")
print(f"상위 10개 브랜드명 중복횟수 입니다. \n = {brand_dup_cnt}")