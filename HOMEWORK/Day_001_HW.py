#!/usr/bin/env python
# coding: utf-8

# ## 練習時間
# #### 請寫一個函式用來計算 Mean Square Error
# $ MSE = \frac{1}{n}\sum_{i=1}^{n}{(Y_i - \hat{Y}_i)^2} $
# 
# ### Hint: [如何取平方](https://googoodesign.gitbooks.io/-ezpython/unit-1.html)

# # [作業目標]
# - 仿造範例的MAE函數, 自己寫一個MSE函數(參考上面公式)

# # [作業重點]
# - 注意程式的縮排
# - 是否能將數學公式, 轉換為 Python 的函式組合? (In[2], Out[2])

# In[1]:


# 載入基礎套件與代稱
import numpy as np
import matplotlib.pyplot as plt


# In[15]:


#def mean_absolute_error(y, yp):
 #   """
 #   計算 MAE
 #   Args:
  #      - y: 實際值
  #      - yp: 預測值
  #  Return:
  #      - mae: MAE
  #  """
  #  mae = MAE = sum(abs(y - yp)) / len(y)
  #  return mae
# print("The Mean absolute error is %.3f" % (MAE))
   
# 定義 mean_squared_error 這個函數, 計算並傳回 MSE
#def mean_squared_error(y, yp):
  #  MAE = mean_absolute_error(y, y_hat)
    
    
def mean_absolute_error(y, yp):
    """
    計算 MAE
    Args:
        - y: 實際值
        - yp: 預測值
    Return:
        - mae: MAE
    """
    # MAE : 將兩個陣列相減後, 取絕對值(abs), 再將整個陣列加總成一個數字(sum), 最後除以y的長度(len), 因此稱為"平均絕對誤差"
    mae = MAE = sum(abs(y - yp)) / len(y)
    return mae

# 呼叫上述函式, 傳回 y(藍點高度)與 y_hat(紅線高度) 的 MAE
MAE = mean_absolute_error(y, y_hat)
print("The Mean absolute error is %.3f" % (MAE))

    


# In[16]:


# 與範例相同, 不另外解說
w = 3
b = 0.5
x_lin = np.linspace(0, 100, 101)
y = (x_lin + np.random.randn(101) * 5) * w + b

plt.plot(x_lin, y, 'b.', label = 'data points')
plt.title("Assume we have data points")
plt.legend(loc = 2)
plt.show()


# In[19]:


# 與範例相同, 不另外解說
y_hat = x_lin * w + b
plt.plot(x_lin, y, 'b.', label = 'data')
plt.plot(x_lin, y_hat, 'r-', label = 'prediction')
plt.title("Assume we have data points (And the prediction)")
plt.legend(loc = 2)
plt.show()


# In[18]:


# 執行 Function, 確認有沒有正常執行
MSE = mean_squared_error(y, y_hat)
MAE = mean_absolute_error(y, y_hat)
print("The Mean squared error is %.3f" % (MSE))
print("The Mean absolute error is %.3f" % (MAE))


# # [作業2]
# 
# 請上 Kaggle, 在 Competitions 或 Dataset 中找一組競賽或資料並寫下：
# 
# 資料集：Netflix Movies and TV Shows
# Movies and TV Shows listings on Netflix
# 1. 你選的這組資料為何重要
# 
# 1)從資料中了解不同國家收看內容，藉以了解不同國家觀看狀況，進而推薦群眾有興趣內容
# 2)從資料中了解節目關聯，如看那些節目群眾同時對那些節目有興趣，做節目關聯分析
# 3)推薦系統是否有成功提高觀眾點擊率
# 2. 資料從何而來 (tips: 譬如提供者是誰、以什麼方式蒐集)
# 由netflix上傳到kaggle，資料每個月更新
# 3. 蒐集而來的資料型態為何
# CSV檔
# 4. 這組資料想解決的問題如何評估
# 主要問題有5個
# 1)Movie Recommendation System:由觀看紀錄運用偕同分析開發推薦
# Netflix Orginal vs Licensed:查看原創影集還是非原創電影點擊率
# What to watch on Netflix ?由過去瀏覽點擊紀錄推薦
# How to find the best rated Movies in Netflix：將電影與爛番茄指數做join
# Show me the Ratings：將評分以視覺化呈現
# 
# # [作業3]
# 
# 想像你經營一個自由載客車隊，你希望能透過數據分析以提升業績，請你思考並描述你如何規劃整體的分析/解決方案：
# 
# 1. 核心問題為何 (tips：如何定義 「提升業績 & 你的假設」)
# 天氣條件不好時，至熱鬧點載客，可以提高業績
# 遇到節慶，業績是否提高
# 假設：
# 1)天氣較為不好時，會提高民眾搭車意願
# 2)節慶時節，民眾願意搭車到目的地
# 2. 資料從何而來 (tips：哪些資料可能會對你想問的問題產生影響 & 資料如何蒐集)
# 1).可與電信公司合作，收集民眾叫車資料，收集搭車地點資料
# 2).天氣資料:
# 3).節慶資料
# 
# 3. 蒐集而來的資料型態為何
# CSV.
# GIS資料
# 4. 你要回答的問題，其如何評估 (tips：你的假設如何驗證)
# 天氣不好，與業績是否成正比

# In[ ]:




