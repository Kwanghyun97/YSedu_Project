# YS_Edu 개인 프로젝트 _ 개요

## ✋ 스마트 스토어 마케팅 전략 을 위한 어플 개발

### 기간 : 2023/03/01 ~ 2023/03/03 :fire:

**PPT 자료** : [https://drive.google.com/file/d/1doSmWEdRa6yr3jbZbmDk28TN6aphcm9W/view?usp=share_link](https://drive.google.com/file/d/1doSmWEdRa6yr3jbZbmDk28TN6aphcm9W/view?usp=share_link)

### 주제 선정 배경

- 최근 몇년간 **투잡에 관심도 높아짐**에 따라 **스마트 스토어 관심도** 높아짐.
- 전자상거래 시장규모 매년 **증가하는 추세** 임.

### 사용 용도

- **User_Target** : 스마트 스토어 예비 창업자 및 스마트 스토어 운영중인 사업자  

- 연령대, 성별, 접속 환경 별 특정 상품에 대한 상대 클릭 수를 plot 시각 화 하여,

    → **맞춤 광고 전략 수립** 가능
      
- 팔고자 하는 상품의 **인기 상품 상위 100개의 평균 가격**과 해당 상품이 **가장 많이 팔리는 쇼핑 플랫폼**  
  (쿠팡, 옥션 등) 및 해당 상품의 브랜드 선호도 정보 출력이 가능함.

    → 팔고자 하는 상품의 대한 **판매 전략 수립 가능**

### 데이터 출처

- **네이버 쇼핑 API** 에서 데이터 수집
- 사용이유 : 네이버 쇼핑이 전자 **상거래 시장규모가 가장 큼.**

![Untitled](https://github.com/Kwanghyun97/YSedu_personal_Project/blob/main/dataplot.png)

### 프로그램 기능

1. **category 검색기** (사용자가 직접 카테고리 (대/중/소) 에 따른 category code 검색이 가능함. )
   - 네이버 쇼핑 API에 request 를 할때, 설정이 필요한 parameter 중 category code가 존재함. 해당 코드는 약 5000개 정도 있으며, 사용자가 직접 찾기 어려움이 있으므로 해당 코드 만듦.
    
    [**→ category 검색기 code 보러 가기**](https://github.com/Kwanghyun97/YSedu_personal_Project/blob/main/category_dictionary.py)
    

2. **연령대 별, 접속 환경 (PC, Mobile)에 따른** 상대 클릭수 **시계열 그래프 그리기**
    
      [**→ code 보러가기**](https://github.com/Kwanghyun97/YSedu_personal_Project/blob/main/plot_relative_clicks.py)
      ![Untitled](https://github.com/Kwanghyun97/YSedu_personal_Project/blob/main/%EC%9E%90%EB%8F%99%EC%9A%B0%EC%82%B0_pc_mo_relative_clicks.png)

   

3. **연령대 , 성별 , 접속 환경(PC,Mobile)에 따른** 상대클릭수 **시계열 그래프 그리기**

      [**→ code 보러가기**](https://github.com/Kwanghyun97/YSedu_personal_Project/blob/main/plot_relative_clicks_2.py)
      ![Untitled](https://github.com/Kwanghyun97/YSedu_personal_Project/blob/main/%EC%9E%90%EB%8F%99%EC%9A%B0%EC%82%B0_gender_relative_clicks.png)      

4. 팔고자 하는 **물품 상위 100개의 가격** 및 **상위 10개의 브랜드** 와 **쇼핑몰 플랫폼** (쿠팡, 네이버...)

      [**→ code 보러가기**](ttps://github.com/Kwanghyun97/YSedu_personal_Project/blob/main/get_shop_info.py) 
      ![Untitled](https://github.com/Kwanghyun97/YSedu_personal_Project/blob/main/get_shop_info.png)
      