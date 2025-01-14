from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 创建 WebDriver 实例，这里使用 Chrome
driver = webdriver.Chrome()  # 替换成chromedriver的实际路径

# 打开百度
driver.get("https://www.baidu.com")

# 确保页面加载完成
time.sleep(2)

# 找到搜索框，输入关键词
search_box = driver.find_element(By.ID, "kw")
search_box.send_keys("测试")

# 执行回车操作
search_box.send_keys(Keys.RETURN)

# 等待一段时间，以便查看搜索结果
time.sleep(50)

# 关闭浏览器
driver.quit()