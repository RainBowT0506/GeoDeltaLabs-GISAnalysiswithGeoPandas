實作影片 [GeoDelta Labs - Introduction to GIS Analysis with GeoPandas using Python](https://www.youtube.com/watch?v=slqZVgB8tIg)

Github：[GeoDeltaLabs-GISAnalysiswithGeoPandas](https://github.com/RainBowT0506/GeoDeltaLabs-GISAnalysiswithGeoPandas)

使用Python中的GeoPandas庫進行地理空間數據操作，包括匯入Shapefile、視覺化、合併、欄位計算和保存。教學使用Spider編碼環境，展示了基本的GeoPandas操作，讓用戶能夠在Python中輕鬆進行地理信息系統（GIS）相關任務。提供相應的安裝教程和Matplotlib顏色映射指南連結，讓學習者更好理解和應用教程中的內容。
## Belgian Cities Plot - Colormap (jet)
![Belgian Cities Plot - Colormap (jet)](https://github.com/RainBowT0506/GeoDeltaLabs-GISAnalysiswithGeoPandas/assets/109667537/f39326a9-43fe-41ad-bc27-351a115d2fe2)

## Belgian Cities with AOI Plot
![Belgian Cities with AOI Plot](https://github.com/RainBowT0506/GeoDeltaLabs-GISAnalysiswithGeoPandas/assets/109667537/b7ffb53a-60ab-428c-acd6-c97c08f7acd9)

## Intersected Cities within Area of Interest (AOI)
![Intersected Cities within Area of Interest (AOI)](https://github.com/RainBowT0506/GeoDeltaLabs-GISAnalysiswithGeoPandas/assets/109667537/e501026a-1ed5-4d0f-946f-2abbf7f1befd)

## Save to Shapefile
![image](https://github.com/RainBowT0506/GeoDeltaLabs-GISAnalysiswithGeoPandas/assets/109667537/4c6ff8e1-4f90-45da-aabe-999872f57807)

## 1. 簡介
- GeoPandas: 用於地理空間資料操作和分析的開源 Python 函式庫。
- 在 pandas 的基礎上擴展，支援對幾何類型的空間操作。

## 2. 匯入 Shapefile
- 使用 `gpd.read_file` 匯入 Shapefile。
- 例子: 將 "比利時城市" Shapefile 匯入一個名為 `cities` 的變數中。

```python
cities = gpd.read_file("path/to/Belgian_cities.shp")
```

## 4. 視覺化 Shapefile
- 使用 `matplotlib` 進行視覺化。
- 使用 `cities.plot` 顯示地圖。
- 額外選項: 色彩圖，基於列的著色，調整圖的大小。

![Belgian Cities Plot - Colormap (jet)](https://github.com/RainBowT0506/GeoDeltaLabs-GISAnalysiswithGeoPandas/assets/109667537/f39326a9-43fe-41ad-bc27-351a115d2fe2)

## 5. Shapefile 重疊
- 使用 `subplots` 一起顯示多個 Shapefile。
- 使用 `gpd.overlay` 進行空間操作（例如交集）。
- 顯示重疊的地圖。

![Area of Interest (AOI) Plot](https://github.com/RainBowT0506/GeoDeltaLabs-GISAnalysiswithGeoPandas/assets/109667537/a8ba657c-84f3-4d37-ae3d-6590ec2d6bfa)
## 6. 屬性表和空間操作
- 探索屬性表。
- 進行空間操作（例如交集）並視覺化結果。

![Belgian Cities with AOI Plot](https://github.com/RainBowT0506/GeoDeltaLabs-GISAnalysiswithGeoPandas/assets/109667537/b7ffb53a-60ab-428c-acd6-c97c08f7acd9)
## 7. 添加新列
- 使用 GeoPandas 的 `area` 函數計算面積。
- 創建一個新的面積（以平方公里為單位）的列。

![Intersected Cities within Area of Interest (AOI)](https://github.com/RainBowT0506/GeoDeltaLabs-GISAnalysiswithGeoPandas/assets/109667537/e501026a-1ed5-4d0f-946f-2abbf7f1befd)
## 8. 儲存修改後的數據框
- 使用 `to_file` 將 GeoDataFrame 保存為新的 Shapefile。

![image](https://github.com/RainBowT0506/GeoDeltaLabs-GISAnalysiswithGeoPandas/assets/109667537/4c6ff8e1-4f90-45da-aabe-999872f57807)


## 關鍵詞
1. GeoPandas: Python 的地理空間數據處理庫，擴展了 Pandas，使其能夠處理地理空間數據。
2. Shapefile: 一種地理空間數據格式，本教程中使用的是以 `.shp` 為擴展名的文件。
3. Pandas: Python 中著名的數據分析庫，GeoPandas 擴展了其數據類型以支持地理空間操作。
4. Matplotlib: Python 中的繪圖庫，用於可視化地理空間數據。
5. Spider: 代碼編輯器，用於編寫和運行 Python 代碼。
6. IPython Console: 交互式 Python 控制台，用於運行代碼和查看結果。
7. Read Shapefile: 使用 `gpd.read_file()` 函數導入 shapefile。
8. Plotting: 使用 `plot()` 函數可視化 shapefile 數據，並指定顏色映射。
9. Overlay: 使用 `gpd.overlay()` 函數進行空間操作，例如交集操作。
10. Create New Column: 使用 `gdf['new_column']` 創建新列，進行數據操作。
11. Save to Shapefile: 使用 `to_file()` 函數將 GeoPandas DataFrame 保存為新的 shapefile。
12. Coordinate System: 了解坐標系統和單位，影響到面積的計算結果。
13. Variable Explorer: Spider 編輯器中的變量瀏覽器，用於查看和管理變量。
14. File Explorer: Spider 編輯器中的文件瀏覽器，用於導航到工作目錄。
15. Color Map: 在地圖上使用不同的顏色映射方案，例如 jet、rainbow。
16. Subplots: 使用 `plt.subplots()` 在一個圖中顯示多個 shapefile。
17. Area Calculation: 使用 `gdf.area` 計算多邊形的面積。
18. CRS (Coordinate Reference System): 使用 `gdf.crs` 查看和理解數據的坐標參考系統。
