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