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

# 세분류가 없는 경우
else:
    # 해당 조건에 맞는 데이터 추출 및 출력
    num = df[(df.iloc[:, 1] == cat1) & (df.iloc[:, 2] == cat2) & (df.iloc[:, 3] == cat3)].iloc[:, 0]
    if len(num) == 0:
        print("해당하는 데이터가 없습니다.")
    else:
        print(num)