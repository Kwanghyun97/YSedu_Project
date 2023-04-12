import pandas as pd
import matplotlib.pyplot as plt

def plot_relative_clicks_2(category_name):
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
plot_relative_clicks_2(category_name)
print(f'{category_name}_gender_relative_clicks.png 저장완료')