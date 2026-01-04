import requests
import json

def fetch_api_data(url):
    try:
        response=requests.get(url,timeout=10)
        response.raise_for_status
        print("Http status:", response.status_code)
        
        data=response.json()
        filename="data.json"
        
        with open(filename,"w") as file:
            json.dump(data, file, indent=4)
            
        print("Data fetched and saved")
        
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        
    except json.JSONDecodeError:
        print("Response is not valid")
        
url=input("Enter a url")
fetch_api_data(url)