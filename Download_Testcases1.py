import requests
import csv

API_TOKEN = "609337fa-f045-43d4-8751-615c93e71cd2" #API Token generated in TestRigor
APP_ID = "fEqwfGY6Qo56bXD6a"                       # Test Suite ID in TestRigor 

UUID_LIST = [
    "34a2d682-8286-4247-92a4-fd1ae2eb7745",
    "68f8dc37-0546-49f7-ad68-a7d15a843607",
    "0fb7430c-076a-42d4-9eac-b4559a847ab1",
    "94483a62-2c9d-42d0-ba13-3f88429f3463",
    "adef920b-893e-4d22-9f3d-2aedba8d2ef7"
]

headers = {
    "auth-token": API_TOKEN,
    "Accept": "application/json"
}

rows = []

for uuid in UUID_LIST:
    url = f"https://api2.testrigor.com/api/v1/apps/{APP_ID}/test_cases?UUID={uuid}"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json().get("data", {}).get("content", [])
        if data:
            case = data[0]
            rows.append([
                case.get("uuid", ""),
                case.get("description", ""),
                case.get("customSteps", ""),
                ", ".join(case.get("labels", [])) if case.get("labels") else ""
            ])
    else:
        print(f"Failed to fetch test case {uuid}: {response.status_code} - {response.text}")

# Write to CSV
with open("testrigor_test_cases_detailed.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["UUID", "Description", "Custom Steps", "Labels"])
    writer.writerows(rows)

print("✅ CSV generated with detailed test cases.")
