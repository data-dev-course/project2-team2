import requests
import json
import csv

def get_company_info(company_cd, api_key):
    base_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/company/searchCompanyInfo.json'
    url = f'{base_url}?key={api_key}&companyCd={company_cd}'

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

# API 호출을 위한 기본 정보
api_key = 'fab5cb6fcba4e18cd3cfd2f1167ce9d1'
company_cds = ['20186501', '20143338', '20216342', '20063279', '20202927', '20230452', '20139757', '20230501', '20100043', '20122837', '20217901', '20142369', '20188601', '20100109', '20111482', '20100932', '20139196', '20158370', '20100558', '20228853', '20061361', '20100540', '20228883', '20229048', '20114892', '20114875', '20111391', '20102062', '20230131', '20123779', '20114895', '20173242', '20111564', '20142968', '20191941', '20161801', '20204721', '20061365', '20141469', '20123058', '20122505', '20141088', '20100491', '20122956', '20155508', '20138935', '20111451', '20188021', '20160021', '20100603', '20137115', '20161101', '20230126', '20139535', '20203701', '20229463', '20111081', '20160741', '20061362', '20216842', '20229581', '20130188', '20239861', '20063188', '20141388', '20100103', '20110854', '20123115', '20229461', '20230221']

# 각 영화사 코드에 대한 API 호출 및 JSON 파일로 저장
for company_cd in company_cds:
    company_info = get_company_info(company_cd, api_key)

    if company_info:
        file_name = f'company_{company_cd}.json'
        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(company_info, file, ensure_ascii=False, indent=4)
        print(f'{file_name} 저장 완료')
    else:
        print(f'{company_cd}에 대한 정보를 가져올 수 없습니다.')


def convert_json_to_csv(json_file, csv_file):
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    if 'companyInfoResult' in data:
        company_info = data['companyInfoResult']['companyInfo']
        company_cd = company_info.get('companyCd', '')
        company_nm = company_info.get('companyNm', '')
        company_nm_en = company_info.get('companyNmEn', '')
        ceo_nm = company_info.get('ceoNm', '')
        parts = [part.get('companyPartNm', '') for part in company_info.get('parts', [])]

        with open(csv_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['companyCd', 'companyNm', 'companyNmEn', 'ceoNm', 'parts'])
            writer.writerow([company_cd, company_nm, company_nm_en, ceo_nm, ', '.join(parts)])
    else:
        print(f'"{json_file}"에 대한 정보를 찾을 수 없습니다.')

# JSON 파일들의 경로
json_files = ['company_20186501.json', 'company_20143338.json', 'company_20216342.json', 'company_20063279.json', 'company_20202927.json', 'company_20230452.json', 'company_20139757.json', 'company_20230501.json', 'company_20100043.json', 'company_20122837.json', 'company_20217901.json', 'company_20142369.json', 'company_20188601.json', 'company_20100109.json', 'company_20111482.json', 'company_20100932.json', 'company_20139196.json', 'company_20158370.json', 'company_20100558.json', 'company_20228853.json', 'company_20061361.json', 'company_20100540.json', 'company_20228883.json', 'company_20229048.json', 'company_20114892.json', 'company_20114875.json', 'company_20111391.json', 'company_20102062.json', 'company_20230131.json', 'company_20123779.json', 'company_20114895.json', 'company_20173242.json', 'company_20111564.json', 'company_20142968.json', 'company_20191941.json', 'company_20161801.json', 'company_20204721.json', 'company_20061365.json', 'company_20141469.json', 'company_20123058.json', 'company_20122505.json', 'company_20141088.json', 'company_20100491.json', 'company_20122956.json', 'company_20155508.json', 'company_20138935.json', 'company_20111451.json', 'company_20188021.json', 'company_20160021.json', 'company_20100603.json', 'company_20137115.json', 'company_20161101.json', 'company_20230126.json', 'company_20139535.json', 'company_20203701.json', 'company_20229463.json', 'company_20111081.json', 'company_20160741.json', 'company_20061362.json', 'company_20216842.json', 'company_20229581.json', 'company_20130188.json', 'company_20239861.json', 'company_20063188.json', 'company_20141388.json', 'company_20100103.json', 'company_20110854.json', 'company_20123115.json', 'company_20229461.json', 'company_20230221.json']
# JSON 파일들을 CSV 파일로 변환
for json_file in json_files:
    csv_file = json_file.replace('.json', '.csv')
    convert_json_to_csv(json_file, csv_file)
    print(f'{csv_file} 저장 완료')