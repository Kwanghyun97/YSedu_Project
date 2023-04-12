## 위에서 입력한 카테고리의 모든 연령대 & 모든 접속 환경 & 모든 성별 의 상대 클릭량
import os
import sys
import json
import pandas as pd
import urllib.request

def get_relative_clicks(category_name, category_code):
    client_id = "client_id"
    client_secret = "client_secret"
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