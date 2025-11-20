import requests
import json
import os
from datetime import datetime

# 設定目標 URL (熊出沒 API)
API_URL = "https://api.kuma-map.com/api/sightings"  # 這裡之後可能需要根據真實 API 修改

# 模擬資料 (如果 API 無法使用，用這個測試)
# 實際運作時，我們會嘗試抓取真實資料
def get_bear_data():
    # 這裡我們用一個公開的日本熊出沒資料來源，或者先用假資料測試流程
    # 為了讓地圖能動，我們先生成一些範例資料，格式是 GeoJSON
    
    # 這裡示範抓取一個公開的 GeoJSON 範例 (或者我們直接生成固定格式)
    # 為了確保你的地圖有東西顯示，我們先手動建立一些資料點
    
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    bear_sightings = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "properties": {
                    "location": "北海道札幌市南區",
                    "time": current_time,
                    "description": "目擊到一頭成年棕熊"
                },
                "geometry": {
                    "type": "Point",
                    "coordinates": [141.3544, 43.0621] # 札幌座標
                }
            },
            {
                "type": "Feature",
                "properties": {
                    "location": "北海道知床半島",
                    "time": current_time,
                    "description": "發現熊腳印"
                },
                "geometry": {
                    "type": "Point",
                    "coordinates": [145.1285, 44.0206] # 知床座標
                }
            }
        ]
    }
    
    # 嘗試抓取真實資料 (這裡預留給未來擴充)
    # try:
    #     response = requests.get("REAL_API_URL")
    #     if response.status_code == 200:
    #         bear_sightings = response.json()
    # except:
    #     pass

    return bear_sightings

def save_data(data):
    # 確保 data 資料夾存在
    if not os.path.exists('data'):
        os.makedirs('data')
        
    # 儲存為 bears.json
    with open('data/bears.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("資料已更新！")

if __name__ == "__main__":
    data = get_bear_data()
    save_data(data)
