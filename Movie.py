import requests
import json
import csv

def save_movie_details(movie_codes):
    base_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json"
    api_key = "fab5cb6fcba4e18cd3cfd2f1167ce9d1"  # Enter your API key here

    for movie_code in movie_codes:
        # Generate request URL
        url = f"{base_url}?key={api_key}&movieCd={movie_code}"

        try:
            # Send GET request to API
            response = requests.get(url)

            # Check response code
            if response.status_code == 200:
                # Parse JSON response data
                data = response.json()

                # Save as JSON file
                json_file_path = f"{movie_code}.json"
                with open(json_file_path, "w", encoding="utf-8") as file:
                    json.dump(data, file, ensure_ascii=False, indent=4)

                print(f"Saved movie details to {json_file_path}.")

                # Convert JSON file to CSV file
                csv_file_path = f"{movie_code}.csv"
                convert_json_to_csv(data, csv_file_path)
                print(f"Converted movie details to {csv_file_path}.")

            else:
                print("API request failed.")

        except requests.exceptions.RequestException as e:
            print("Error occurred during API request:", e)

def convert_json_to_csv(data, csv_file_path):
    with open(csv_file_path, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        
        # Write header
        header = list(data["movieInfoResult"]["movieInfo"].keys())
        writer.writerow(header)
        
        # Write data
        row = list(data["movieInfoResult"]["movieInfo"].values())
        writer.writerow(row)

# Specify movie codes to save movie details as JSON files and convert JSON files to CSV files
movie_codes = ['20210846', '20200154', '20231437', '20218656', '20231592', '20231481', '20227890', '20230943', '20231021', '20228030', '20231089', '20231348', '20205155', '20225865', '20231071', '20231839', '20226270', '20198482', '20226411', '19960041', '20219473', '20231677', '20231029', '20231244', '20231164', '20231544', '20161872', '20226489', '20231496', '20228555']
save_movie_details(movie_codes)
