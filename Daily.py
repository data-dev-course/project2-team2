import requests
import json
from datetime import datetime, timedelta

import csv

def save_json_to_file(json_data, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(json_data, file, ensure_ascii=False, indent=4)
    print(f"JSON 데이터가 성공적으로 {file_name} 파일에 저장되었습니다.")

def get_kofic_data(target_dt, item_per_page='10', multi_movie_yn=None, rep_nation_cd=None, wide_area_cd=None):
    api_key = 'fab5cb6fcba4e18cd3cfd2f1167ce9d1'
    base_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json'

    # API 호출을 위한 파라미터 설정
    params = {
        'key': api_key,
        'targetDt': target_dt,
        'itemPerPage': item_per_page,
        'multiMovieYn': multi_movie_yn,
        'repNationCd': rep_nation_cd,
        'wideAreaCd': wide_area_cd
    }

    try:
        # API 호출
        response = requests.get(base_url, params=params, timeout=60)

        if response.status_code == 200:
            # JSON 데이터 파싱
            json_data = response.json()
            box_office_list = json_data['boxOfficeResult']['dailyBoxOfficeList']

            # 전처리된 JSON 데이터를 파일로 저장
            file_name = f'boxoffice_{target_dt}.json'
            save_json_to_file(box_office_list, file_name)
        else:
            print("KOFIC API 호출에 실패하였습니다.")

    except Exception as e:
        print("API 호출 중 오류가 발생하였습니다.")
        print(str(e))


def save_kofic_data_by_date(start_date, end_date, item_per_page='10', multi_movie_yn=None, rep_nation_cd=None, wide_area_cd=None):
    # 시작 날짜부터 종료 날짜까지 반복하여 데이터 저장
    current_date = start_date
    while current_date <= end_date:
        target_dt = current_date.strftime('%Y%m%d')
        get_kofic_data(target_dt, item_per_page, multi_movie_yn, rep_nation_cd, wide_area_cd)
        current_date += timedelta(days=1)

# 날짜 설정
start_date = datetime(2023, 5, 1).date()  # 시작 날짜
end_date = datetime(2023, 5, 28).date()  # 종료 날짜

# KOFIC API 호출 및 데이터 저장
save_kofic_data_by_date(start_date, end_date, item_per_page='10', multi_movie_yn=None, rep_nation_cd=None, wide_area_cd=None)



# Define your start and end dates
start_date = datetime(2023, 5, 1)
end_date = datetime(2023, 5, 28)

# Create a variable to hold the current date
current_date = start_date

# Loop through each day
while current_date <= end_date:
    # Create the filename from the date
    filename = 'boxoffice_' + current_date.strftime('%Y%m%d') + '.json'
    
    # Load the JSON data
    with open(filename) as f:
        data = json.load(f)

    # Now we will open a file for writing
    csv_filename = 'boxoffice_' + current_date.strftime('%Y%m%d') + '.csv'
    data_file = open(csv_filename, 'w')

    # Create the CSV writer object
    csv_writer = csv.writer(data_file)

    # Counter variable used for writing headers to the CSV file
    header = data[0].keys()
    csv_writer.writerow(header)

    for row in data:
        csv_writer.writerow(row.values())

    # Close the CSV file
    data_file.close()

    # Increment the current date
    current_date += timedelta(days=1)
