import json
import random
import os
from datetime import datetime

# 這是模擬日本黑熊出沒的資料生成器
def generate_japan_bears():
    bears = []
    
    # 日本各地的粗略座標範圍
    locations = [
        {"name": "北海道 (Hokkaido)", "lat_min": 42.0, "lat_max": 44.0, "lon_min": 141.0, "lon_max": 144.0},
        {"name": "長野縣 (Nagano)", "lat_min": 35.5, "lat_max": 36.5, "lon_min": 137.5, "lon_max": 138.5},
        {"name": "秋田縣 (Akita)", "lat_min": 39.0, "lat_max": 40.0, "lon_min": 140.0, "lon_max": 140.5},
    ]

    # 隨機產生 10 筆出沒紀錄
    for i in range(10):
        place = random.choice(locations)
        
        # 隨機生成經緯度
        lat = place["lat_min"] + random.random() * (place["lat_max"] - place["lat_min"])
        lon = place["lon_min"] + random.random() * (place["lon_max"] - place["lon_min"])
        
        bear_data = {
            "location": f"日本 - {place['name']} 山區 #{i+1}",
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "geo": {
                "lat": lat,
                "long": lon
            },
            # 放一張可愛的黑熊示意圖
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Ursus_thibetanus_3_%28Wroclaw_zoo%29.JPG/640px-Ursus_thibetanus_3_%28Wroclaw_zoo%29.JPG"
        }
        bears.append(bear_data)

    return bears

if __name__ == "__main__":
    # 1. 產生資料
    data = generate_japan_bears()
    
    # 2. 確保 data 資料夾存在
    os.makedirs("data", exist_ok=True)
    
    # 3. 存檔成 bears.json
    file_path = "data/bears.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    
    print(f"成功產生 {len(data)} 筆日本黑熊資料！")
