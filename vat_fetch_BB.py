import requests
import json

urls = {
    "BigBang_2.30.0": "https://umbrella-bigbang-releases.s3-us-gov-west-1.amazonaws.com/umbrella/2.30.0/images.txt",
    "BigBang_2.30.0-rc.1": "https://umbrella-bigbang-releases.s3-us-gov-west-1.amazonaws.com/umbrella/2.30.0-rc.1/images.txt",
    "BigBang_2.30.0-rc.0": "https://umbrella-bigbang-releases.s3-us-gov-west-1.amazonaws.com/umbrella/2.30.0-rc.0/images.txt",
    "BigBang_2.29.0": "https://umbrella-bigbang-releases.s3-us-gov-west-1.amazonaws.com/umbrella/2.29.0/images.txt",
    "BigBang_2.28.1": "https://umbrella-bigbang-releases.s3-us-gov-west-1.amazonaws.com/umbrella/2.28.1/images.txt",
    "BigBang_2.28.1-rc.0": "https://umbrella-bigbang-releases.s3-us-gov-west-1.amazonaws.com/umbrella/2.28.1-rc.0/images.txt",
    "BigBang_2.28.0": "https://umbrella-bigbang-releases.s3-us-gov-west-1.amazonaws.com/umbrella/2.28.0/images.txt",
    "BigBang_2.28.0-rc.0": "https://umbrella-bigbang-releases.s3-us-gov-west-1.amazonaws.com/umbrella/2.28.0-rc.0/images.txt",
    "BigBang_2.27.0": "https://umbrella-bigbang-releases.s3-us-gov-west-1.amazonaws.com/umbrella/2.27.0/images.txt",
    "BigBang_2.26.0": "https://umbrella-bigbang-releases.s3-us-gov-west-1.amazonaws.com/umbrella/2.26.0/images.txt",
    "BigBang_2.25.0": "https://umbrella-bigbang-releases.s3-us-gov-west-1.amazonaws.com/umbrella/2.25.0/images.txt",
    "BigBang_2.24.0": "https://umbrella-bigbang-releases.s3-us-gov-west-1.amazonaws.com/umbrella/2.24.0/images.txt",
    "BigBang_2.23.1": "https://umbrella-bigbang-releases.s3-us-gov-west-1.amazonaws.com/umbrella/2.23.1/images.txt",
    "BigBang_2.23.0": "https://umbrella-bigbang-releases.s3-us-gov-west-1.amazonaws.com/umbrella/2.23.0/images.txt",
    "BigBang_2.22.0": "https://umbrella-bigbang-releases.s3-us-gov-west-1.amazonaws.com/umbrella/2.22.0/images.txt",
    "BigBang_2.21.2": "https://umbrella-bigbang-releases.s3-us-gov-west-1.amazonaws.com/umbrella/2.21.2/images.txt",
    "BigBang_2.21.1": "https://umbrella-bigbang-releases.s3-us-gov-west-1.amazonaws.com/umbrella/2.21.1/images.txt",
    "BigBang_2.21.0": "https://umbrella-bigbang-releases.s3-us-gov-west-1.amazonaws.com/umbrella/2.21.0/images.txt",
    "BigBang_2.20.0": "https://umbrella-bigbang-releases.s3-us-gov-west-1.amazonaws.com/umbrella/2.20.0/images.txt",
    "BigBang_2.19.2": "https://umbrella-bigbang-releases.s3-us-gov-west-1.amazonaws.com/umbrella/2.19.2/images.txt",
    "BigBang_2.19.1": "https://umbrella-bigbang-releases.s3-us-gov-west-1.amazonaws.com/umbrella/2.19.1/images.txt",
    "BigBang_2.19.0": "https://umbrella-bigbang-releases.s3-us-gov-west-1.amazonaws.com/umbrella/2.19.0/images.txt",
    "BigBang_2.18.0": "https://umbrella-bigbang-releases.s3-us-gov-west-1.amazonaws.com/umbrella/2.18.0/images.txt",
    "BigBang_2.17.0": "https://umbrella-bigbang-releases.s3-us-gov-west-1.amazonaws.com/umbrella/2.17.0/images.txt",
    "BigBang_2.16.0": "https://umbrella-bigbang-releases.s3-us-gov-west-1.amazonaws.com/umbrella/2.16.0/images.txt",
    "BigBang_2.15.1": "https://umbrella-bigbang-releases.s3-us-gov-west-1.amazonaws.com/umbrella/2.15.1/images.txt",
    "BigBang_2.15.0": "https://umbrella-bigbang-releases.s3-us-gov-west-1.amazonaws.com/umbrella/2.15.0/images.txt",
    "BigBang_2.14.0": "https://umbrella-bigbang-releases.s3-us-gov-west-1.amazonaws.com/umbrella/2.14.0/images.txt",
    "BigBang_2.13.1": "https://umbrella-bigbang-releases.s3-us-gov-west-1.amazonaws.com/umbrella/2.13.1/images.txt",
    "BigBang_2.13.0": "https://umbrella-bigbang-releases.s3-us-gov-west-1.amazonaws.com/umbrella/2.13.0/images.txt",
    "BigBang_2.12.0": "https://umbrella-bigbang-releases.s3-us-gov-west-1.amazonaws.com/umbrella/2.12.0/images.txt",
    "BigBang_2.11.1": "https://umbrella-bigbang-releases.s3-us-gov-west-1.amazonaws.com/umbrella/2.11.1/images.txt",
    "BigBang_2.11.0": "https://umbrella-bigbang-releases.s3-us-gov-west-1.amazonaws.com/umbrella/2.11.0/images.txt",
    "BigBang_2.10.0": "https://umbrella-bigbang-releases.s3-us-gov-west-1.amazonaws.com/umbrella/2.10.0/images.txt",
    "BigBang_2.9.0": "https://umbrella-bigbang-releases.s3-us-gov-west-1.amazonaws.com/umbrella/2.9.0/images.txt",
    "BigBang_2.8.0": "https://umbrella-bigbang-releases.s3-us-gov-west-1.amazonaws.com/umbrella/2.8.0/images.txt",
    "BigBang_2.7.1": "https://umbrella-bigbang-releases.s3-us-gov-west-1.amazonaws.com/umbrella/2.7.1/images.txt",
    "BigBang_2.7.0": "https://umbrella-bigbang-releases.s3-us-gov-west-1.amazonaws.com/umbrella/2.7.0/images.txt",
    "BigBang_2.6.0": "https://umbrella-bigbang-releases.s3-us-gov-west-1.amazonaws.com/umbrella/2.6.0/images.txt",
    "BigBang_2.5.0": "https://umbrella-bigbang-releases.s3-us-gov-west-1.amazonaws.com/umbrella/2.5.0/images.txt",
    "BigBang_2.4.1": "https://umbrella-bigbang-releases.s3-us-gov-west-1.amazonaws.com/umbrella/2.4.1/images.txt",
    "BigBang_2.4.0": "https://umbrella-bigbang-releases.s3-us-gov-west-1.amazonaws.com/umbrella/2.4.0/images.txt",
    "BigBang_2.3.0": "https://umbrella-bigbang-releases.s3-us-gov-west-1.amazonaws.com/umbrella/2.3.0/images.txt",
    "BigBang_2.2.0": "https://umbrella-bigbang-releases.s3-us-gov-west-1.amazonaws.com/umbrella/2.2.0/images.txt",
    "BigBang_2.1.0": "https://umbrella-bigbang-releases.s3-us-gov-west-1.amazonaws.com/umbrella/2.1.0/images.txt",
    "BigBang_2.0.1": "https://umbrella-bigbang-releases.s3-us-gov-west-1.amazonaws.com/umbrella/2.0.1/images.txt",
    "BigBang_2.0.0": "https://umbrella-bigbang-releases.s3-us-gov-west-1.amazonaws.com/umbrella/2.0.0/images.txt",
    "BigBang_1.57.1": "https://umbrella-bigbang-releases.s3-us-gov-west-1.amazonaws.com/umbrella/1.57.1/images.txt",
    "BigBang_1.57.0": "https://umbrella-bigbang-releases.s3-us-gov-west-1.amazonaws.com/umbrella/1.57.0/images.txt",
    "BigBang_1.56.0": "https://umbrella-bigbang-releases.s3-us-gov-west-1.amazonaws.com/umbrella/1.56.0/images.txt",
    "BigBang_1.55.0": "https://umbrella-bigbang-releases.s3-us-gov-west-1.amazonaws.com/umbrella/1.55.0/images.txt",
    "BigBang_1.54.0": "https://umbrella-bigbang-releases.s3-us-gov-west-1.amazonaws.com/umbrella/1.54.0/images.txt",
    "BigBang_1.53.0": "https://umbrella-bigbang-releases.s3-us-gov-west-1.amazonaws.com/umbrella/1.53.0/images.txt",
    "BigBang_1.52.0": "https://umbrella-bigbang-releases.s3-us-gov-west-1.amazonaws.com/umbrella/1.52.0/images.txt",
    "BigBang_1.51.0": "https://umbrella-bigbang-releases.s3-us-gov-west-1.amazonaws.com/umbrella/1.51.0/images.txt"
}

#function to fetch data from a url
def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

#fetch data from the URLs
data_dict = {}
for key, url in urls.items():
    try:
        data = fetch_data(url)
        data_dict[key] = data
    except requests.RequestException as e:
        print(f"failed to fetch data from {urls}: {e}")

#function to process the data
def process_data(raw_data):
    lines = raw_data.splitlines()
    return {"Images:": lines}

#process the fetch data
processed_data = {}
for key, raw_data in data_dict.items():
    processed_data[key] = process_data(raw_data)

#write the processed data to the json file
output_file = 'bigbang_image_data.json'
with open(output_file, 'w') as json_file:
    json.dump(processed_data, json_file, indent=4)

#print everything
print(f"Data successfully saved in {output_file}!")

