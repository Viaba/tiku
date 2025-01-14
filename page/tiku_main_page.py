import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://rk.51cto.com/t/n/sub-235")
driver.maximize_window()
time.sleep(2)

# 登录题库
driver.find_element(By.XPATH, '//*[@class="nav-right-box truncate login-btn"]').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="login-base"]/div[1]/span[3]').click()
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="loginform-username"]').send_keys("15871337904")
driver.find_element(By.XPATH,'//*[@id="loginform-password"]').send_keys("51234Cto-")
driver.find_element(By.XPATH,'//*[@id="login-form"]/div[3]/input[1]').click()
time.sleep(2)

#-----------每日打卡-----------
driver.find_element(By.XPATH,' //*[@class="flex justify-between tab-main"]/a[1]').click()
#断言每日打卡、答题卡、交卷等元素是否存在，完成后返回首页
element_locators = {
    "每日打卡": (By.XPATH, '//*[@class="exam-header-title truncate"]'),
    "答题卡": (By.XPATH, '//*[@class="exam-answer-card-title"]'),
    "交卷": (By.XPATH, '//*[@class="btn btn-primary"]')  # 这里需要根据实际页面中交卷按钮的ID来填写
}

for element_name, locator in element_locators.items():
    try:
        # 用显式等待确保元素可见
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))
        print(f"{element_name}元素存在。")
    except:
        print(f"{element_name}元素不存在。")
#回到首页
driver.get('https://rk.51cto.com/t/n/sub-235')
time.sleep(2)

#-----------章节练习-----------
driver.find_element(By.XPATH,'//*[@class="flex justify-between tab-main"]/a[2]').click()
driver.find_element(By.XPATH,'//*[@class="material-list-content"]/div[1]/div[1]/div[1]/div/i/img').click()
driver.find_element(By.XPATH,'//*[@class="list-expand-body is-expand"]/div[1]/div/a').click()

#考试模式-继续答题-开始答题，点击准备好了
driver.find_element(By.XPATH,'//*[@class="radio-box"]/span[1]').click()
driver.find_element(By.XPATH,'//*[@class="radio-box mt-[30px]"]/span[1]').click()
driver.find_element(By.XPATH,'//*[@class="primary-btn"]').click()
driver.find_element(By.XPATH,'//*[@class="primary-btn"]').click()

#断言页面上的答题卡，保存进度，交卷三个元素
element_locators = {
    "答题卡": (By.XPATH, '//*[@class="exam-answer-card-title"]'),
    "保存进度，下次继续": (By.XPATH, '//*[@class="btn btn-plain mb-[10px]"]'),
    "交卷": (By.XPATH, '//*[@class="btn btn-primary"]')
}

for element_name, locator in element_locators.items():
    try:
        # 使用显式等待确保元素可见
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))
        print(f"{element_name}元素存在。")
    except:
        print(f"{element_name}元素不存在。")
#回到上一页
driver.get('https://rk.51cto.com/t/n/chapter-manage/list/sub-235')
time.sleep(2)

#考试模式-重新开始-开始答题，点击准备好了
driver.find_element(By.XPATH,'//*[@class="radio-box"]/span[1]').click()
driver.find_element(By.XPATH,'//*[@class="radio-box mt-[30px]"]/span[2]').click()
driver.find_element(By.XPATH,'//*[@class="primary-btn"]').click()
driver.find_element(By.XPATH,'//*[@class="primary-btn"]').click()

#断言页面上的答题卡，保存进度，交卷三个元素
element_locators = {
    "答题卡": (By.XPATH, '//*[@class="exam-answer-card-title"]'),
    "保存进度，下次继续": (By.XPATH, '//*[@class="btn btn-plain mb-[10px]"]'),
    "交卷": (By.XPATH, '//*[@class="btn btn-primary"]')
}

for element_name, locator in element_locators.items():
    try:
        # 使用显式等待确保元素可见
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))
        print(f"{element_name}元素存在。")
    except:
        print(f"{element_name}元素不存在。")
#回到上一页
driver.get('https://rk.51cto.com/t/n/chapter-manage/list/sub-235')
time.sleep(2)

#练习模式，继续答题，开始答题，点击准备好了
driver.find_element(By.XPATH,'//*[@class="radio-box"]/span[2]').click()
driver.find_element(By.XPATH,'//*[@class="radio-box mt-[30px]"]/span[1]').click()
driver.find_element(By.XPATH,'//*[@class="primary-btn"]').click()
driver.find_element(By.XPATH,'//*[@class="primary-btn"]').click()

#断言页面上的答题卡，保存进度，交卷三个元素
element_locators = {
    "答题卡": (By.XPATH, '//*[@class="exam-answer-card-title"]'),
    "保存进度，下次继续": (By.XPATH, '//*[@class="btn btn-plain mb-[10px]"]'),
    "交卷": (By.XPATH, '//*[@class="btn btn-primary"]')
}

for element_name, locator in element_locators.items():
    try:
        # 使用显式等待确保元素可见
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))
        print(f"{element_name}元素存在。")
    except:
        print(f"{element_name}元素不存在。")
#回到上一页
driver.get('https://rk.51cto.com/t/n/chapter-manage/list/sub-235')
time.sleep(2)

#练习模式，重新开始，开始答题，点击准备好了
driver.find_element(By.XPATH,'//*[@class="radio-box"]/span[2]').click()
driver.find_element(By.XPATH,'//*[@class="radio-box mt-[30px]"]/span[2]').click()
driver.find_element(By.XPATH,'//*[@class="primary-btn"]').click()
driver.find_element(By.XPATH,'//*[@class="primary-btn"]').click()

#断言页面上的答题卡，保存进度，交卷三个元素
element_locators = {
    "答题卡": (By.XPATH, '//*[@class="exam-answer-card-title"]'),
    "保存进度，下次继续": (By.XPATH, '//*[@class="btn btn-plain mb-[10px]"]'),
    "交卷": (By.XPATH, '//*[@class="btn btn-primary"]')
}

for element_name, locator in element_locators.items():
    try:
        # 使用显式等待确保元素可见
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))
        print(f"{element_name}元素存在。")
    except:
        print(f"{element_name}元素不存在。")
#回到上一页
driver.get('https://rk.51cto.com/t/n/chapter-manage/list/sub-235')
time.sleep(2)

#-----------知识点练习-----------
driver.find_element(By.XPATH,'//*[@class="flex justify-between tab-main"]/a[3]').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@class="knowledge-card-box-main"]/div[2]/div[1]/div/div[2]').click()

#考试模式-继续答题-开始答题，点击准备好了
driver.find_element(By.XPATH,'//*[@class="radio-box"]/span[1]').click()
driver.find_element(By.XPATH,'//*[@class="radio-box mt-[30px]"]/span[1]').click()
driver.find_element(By.XPATH,'//*[@class="primary-btn"]').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@class="primary-btn"]').click()
#driver.find_element(By.XPATH,'//*[@class="el-dialog__footer"]/div/button').click()

'''wait = WebDriverWait(driver, 3)
element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@class="primary-btn"]')))
element.click()'''

#断言页面上的答题卡，保存进度，交卷三个元素
element_locators = {
    "答题卡": (By.XPATH, '//*[@class="exam-answer-card-title"]'),
    "保存进度，下次继续": (By.XPATH, '//*[@class="btn btn-plain mb-[10px]"]'),
    "交卷": (By.XPATH, '//*[@class="btn btn-primary"]')
}

for element_name, locator in element_locators.items():
    try:
        # 使用显式等待确保元素可见
        element = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(locator))
        print(f"{element_name} 元素存在。")
    except:
        print(f"{element_name} 元素不存在。")
#回到上一页
driver.get('https://rk.51cto.com/t/n/chapter-manage/knowledge/sub-235')
time.sleep(2)

#考试模式-重新开始-开始答题，点击准备好了
driver.find_element(By.XPATH,'//*[@class="radio-box"]/span[1]').click()
driver.find_element(By.XPATH,'//*[@class="radio-box mt-[30px]"]/span[2]').click()
driver.find_element(By.XPATH,'//*[@class="primary-btn"]').click()
driver.find_element(By.XPATH,'//*[@class="primary-btn"]').click()

#断言页面上的答题卡，保存进度，交卷三个元素
element_locators = {
    "答题卡": (By.XPATH, '//*[@class="exam-answer-card-title"]'),
    "保存进度，下次继续": (By.XPATH, '//*[@class="btn btn-plain mb-[10px]"]'),
    "交卷": (By.XPATH, '//*[@class="btn btn-primary"]')
}

for element_name, locator in element_locators.items():
    try:
        # 使用显式等待确保元素可见
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))
        print(f"{element_name}元素存在。")
    except:
        print(f"{element_name}元素不存在。")
#回到上一页
driver.get('https://rk.51cto.com/t/n/chapter-manage/knowledge/sub-235')
time.sleep(2)

#练习模式-继续答题-开始答题，点击准备好了
driver.find_element(By.XPATH,'//*[@class="radio-box"]/span[2]').click()
driver.find_element(By.XPATH,'//*[@class="radio-box mt-[30px]"]/span[1]').click()
driver.find_element(By.XPATH,'//*[@class="primary-btn"]').click()
driver.find_element(By.XPATH,'//*[@class="primary-btn"]').click()

#断言页面上的答题卡，保存进度，交卷三个元素
element_locators = {
    "答题卡": (By.XPATH, '//*[@class="exam-answer-card-title"]'),
    "保存进度，下次继续": (By.XPATH, '//*[@class="btn btn-plain mb-[10px]"]'),
    "交卷": (By.XPATH, '//*[@class="btn btn-primary"]')
}

for element_name, locator in element_locators.items():
    try:
        # 使用显式等待确保元素可见
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))
        print(f"{element_name}元素存在。")
    except:
        print(f"{element_name}元素不存在。")
#回到上一页
driver.get('https://rk.51cto.com/t/n/chapter-manage/knowledge/sub-235')
time.sleep(2)

#练习模式-重新开始-开始答题，点击准备好了
driver.find_element(By.XPATH,'//*[@class="radio-box"]/span[2]').click()
driver.find_element(By.XPATH,'//*[@class="radio-box mt-[30px]"]/span[2]').click()
driver.find_element(By.XPATH,'//*[@class="primary-btn"]').click()
driver.find_element(By.XPATH,'//*[@class="primary-btn"]').click()

#断言页面上的答题卡，保存进度，交卷三个元素
element_locators = {
    "答题卡": (By.XPATH, '//*[@class="exam-answer-card-title"]'),
    "保存进度，下次继续": (By.XPATH, '//*[@class="btn btn-plain mb-[10px]"]'),
    "交卷": (By.XPATH, '//*[@class="btn btn-primary"]')
}

for element_name, locator in element_locators.items():
    try:
        # 使用显式等待确保元素可见
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))
        print(f"{element_name}元素存在。")
    except:
        print(f"{element_name}元素不存在。")
#回到上一页
driver.get('https://rk.51cto.com/t/n/chapter-manage/knowledge/sub-235')
time.sleep(2)


#-----------历年试题-----------
driver.find_element(By.XPATH,'//*[@class="flex justify-between tab-main"]/a[4]').click()
#综合知识-查看解析，断言答题卡、高频错题元素
driver.find_element(By.XPATH,'//*[@class="flex items-center exam-type"]/a[2]').click()
driver.find_element(By.XPATH,'//*[@class="list-box"]/div[1]/div/div[2]/a[1]').click()
element_locators = {
    "答题卡": (By.XPATH, '//*[@class="exam-answer-card-header"]/div/div[1]'),
    "高频错题": (By.XPATH, '//*[@class="exam-answer-card-header"]/div/div[2]'),
    "再考一次": (By.XPATH, '//*[@class="btn btn-plain mb-[10px]"]')
}

for element_name, locator in element_locators.items():
    try:
        # 使用显式等待确保元素可见
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))
        print(f"{element_name}元素存在。")
    except:
        print(f"{element_name}元素不存在。")
#回到上一页-综合知识
driver.get('https://rk.51cto.com/t/n/chapter-manage/years/sub-235')
driver.find_element(By.XPATH,'//*[@class="flex items-center exam-type"]/a[2]').click()
time.sleep(2)


#综合知识-再做一遍，断言答题卡、高频错题元素
driver.find_element(By.XPATH,'//*[@class="flex items-center exam-type"]/a[2]').click()
driver.find_element(By.XPATH,'//*[@class="list-box"]/div[1]/div/div[2]/a[2]').click()

element_locators = {
    "答题卡": (By.XPATH, '//*[@class="exam-answer-card-header"]/div/div[1]'),
    "高频错题": (By.XPATH, '//*[@class="exam-answer-card-header"]/div/div[2]'),
    "再考一次": (By.XPATH, '//*[@class="btn btn-plain mb-[10px]"]')
}

for element_name, locator in element_locators.items():
    try:
        # 使用显式等待确保元素可见
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))
        print(f"{element_name}元素存在。")
    except:
        print(f"{element_name}元素不存在。")
#回到上一页-综合知识
driver.get('https://rk.51cto.com/t/n/chapter-manage/years/sub-235')
driver.find_element(By.XPATH,'//*[@class="flex items-center exam-type"]/a[2]').click()
time.sleep(2)


#综合知识-开始做题，等待元素可点击
target_element = driver.find_element(By.XPATH,'//*[@class="tit-item-wrap"][9]/div/div[2]')
driver.execute_script("arguments[0].scrollIntoView(false);", target_element)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@class="tit-item-wrap"][9]/div/div[2]')))
target_element.click()
   #考试模式,断言答题卡、保存进度、交卷元素
driver.find_element(By.XPATH,'//*[@class="btn plain-btn exam-mode-plain"]').click()
driver.find_element(By.XPATH,'//*[@class="primary-btn"]').click()
element_locators = {
    "答题卡": (By.XPATH, '//*[@class="exam-answer-card-title"]'),
    "保存进度 下次继续": (By.XPATH, '//*[@class="btn btn-plain mb-[10px]"]'),
    "交卷": (By.XPATH, '//*[@class="btn btn-primary"]')
}

for element_name, locator in element_locators.items():
    try:
        # 使用显式等待确保元素可见
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))
        print(f"{element_name}元素存在。")
    except:
        print(f"{element_name}元素不存在。")
#回到上一页-综合知识-选模式页面
driver.get('https://rk.51cto.com/t/n/previous-exam/detail/10629.html')
time.sleep(2)

   #练习模式，断言答题卡、保存进度、交卷元素
driver.find_element(By.XPATH,'//*[@class="btn plain-btn practice-mode-plain"]').click()
driver.find_element(By.XPATH,'//*[@class="primary-btn"]').click()
element_locators = {
    "答题卡": (By.XPATH, '//*[@class="exam-answer-card-title"]'),
    "保存进度 下次继续": (By.XPATH, '//*[@class="btn btn-plain mb-[10px]"]'),
    "交卷": (By.XPATH, '//*[@class="btn btn-primary"]')
}

for element_name, locator in element_locators.items():
    try:
        # 使用显式等待确保元素可见
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))
        print(f"{element_name}元素存在。")
    except:
        print(f"{element_name}元素不存在。")
#回到上一页-综合知识-选模式页面
driver.get('https://rk.51cto.com/t/n/previous-exam/detail/10629.html')
time.sleep(2)

   #机考模式，断言答题卡、保存进度、交卷元素
driver.find_element(By.XPATH,'//*[@class="btn primary-btn computer-mode-primary"]').click()
driver.find_element(By.XPATH,'//*[@class="login-btn-box"]').click()
driver.find_element(By.XPATH,'//*[@class="btn confirm-btn"]').click()
#等待点击我已阅读元素
time.sleep(12)
read_element = driver.find_element(By.XPATH, '//*[@class="confirm-btn"]')
read_element.click()
#断言答题卡、交卷、下一题元素
element_locators = {
    "答题卡": (By.XPATH, '//*[@id="sheetName"]'),
    "交卷": (By.XPATH, '//*[@class="btn btn-primary"]'),
    "下一题": (By.XPATH, '//*[@class="ri-btn"]'),
}

for element_name, locator in element_locators.items():
    try:
        # 使用显式等待确保元素可见
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))
        print(f"{element_name}元素存在。")
    except:
        print(f"{element_name}元素不存在。")
#回到上一页-综合知识
driver.get('https://rk.51cto.com/t/n/chapter-manage/years/sub-235')
#点击到案例分析
driver.find_element(By.XPATH,'//*[@class="flex items-center exam-type"]/a[3]').click()
time.sleep(2)

#案例分析-查看解析，断言答题卡、高频错题元素
driver.find_element(By.XPATH,'//*[@class="flex items-center exam-type"]/a[3]').click()
driver.find_element(By.XPATH,'//*[@class="list-box"]/div[1]/div/div[2]/a[1]').click()
#断言答题卡、交卷、下一题元素
element_locators = {
    "答题卡": (By.XPATH, '//*[@class="exam-answer-card"]/div[1]/div/div[1]'),
    "再考一次": (By.XPATH, '//*[@class="exam-answer-card-footer"]/button[1]'),
    "查看详细报告": (By.XPATH, '//*[@class="exam-answer-card-footer"]/button[2]'),
}

for element_name, locator in element_locators.items():
    try:
        # 使用显式等待确保元素可见
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))
        print(f"{element_name}元素存在。")
    except:
        print(f"{element_name}元素不存在。")
#回到上一页-案例分析
driver.get('https://rk.51cto.com/t/n/chapter-manage/years/sub-235')
driver.find_element(By.XPATH,'//*[@class="flex items-center exam-type"]/a[3]').click()
time.sleep(2)

#案例分析-再做一遍，断言答题卡、高频错题元素
driver.find_element(By.XPATH,'//*[@class="flex items-center exam-type"]/a[3]').click()
driver.find_element(By.XPATH,'//*[@class="list-box"]/div[1]/div/div[2]/a[2]').click()
   #考试模式,断言答题卡、保存进度、交卷元素
driver.find_element(By.XPATH,'//*[@class="btn plain-btn exam-mode-plain"]').click()
driver.find_element(By.XPATH,'//*[@class="primary-btn"]').click()
element_locators = {
    "答题卡": (By.XPATH, '//*[@class="exam-answer-card-title"]'),
    "保存进度 下次继续": (By.XPATH, '//*[@class="btn btn-plain mb-[10px]"]'),
    "交卷": (By.XPATH, '//*[@class="btn btn-primary"]')
}

for element_name, locator in element_locators.items():
    try:
        # 使用显式等待确保元素可见
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))
        print(f"{element_name}元素存在。")
    except:
        print(f"{element_name}元素不存在。")
#回到上一页-案例分析-选模式页面
driver.get('https://rk.51cto.com/t/n/previous-exam/detail/17854.html')
time.sleep(2)

   #练习模式，断言答题卡、保存进度、交卷元素
driver.find_element(By.XPATH,'//*[@class="btn plain-btn practice-mode-plain"]').click()
driver.find_element(By.XPATH,'//*[@class="primary-btn"]').click()
element_locators = {
    "答题卡": (By.XPATH, '//*[@class="exam-answer-card-title"]'),
    "保存进度 下次继续": (By.XPATH, '//*[@class="btn btn-plain mb-[10px]"]'),
    "交卷": (By.XPATH, '//*[@class="btn btn-primary"]')
}

for element_name, locator in element_locators.items():
    try:
        # 使用显式等待确保元素可见
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))
        print(f"{element_name}元素存在。")
    except:
        print(f"{element_name}元素不存在。")
#回到上一页-案例分析-选模式页面
driver.get('https://rk.51cto.com/t/n/previous-exam/detail/10629.html')
time.sleep(2)

   #机考模式，断言答题卡、保存进度、交卷元素
driver.find_element(By.XPATH,'//*[@class="btn primary-btn computer-mode-primary"]').click()
driver.find_element(By.XPATH,'//*[@class="login-btn-box"]').click()
driver.find_element(By.XPATH,'//*[@class="btn confirm-btn"]').click()
#等待点击我已阅读元素
time.sleep(12)
read_element = driver.find_element(By.XPATH, '//*[@class="confirm-btn"]')
read_element.click()
#断言答题卡、交卷、下一题元素
element_locators = {
    "答题卡": (By.XPATH, '//*[@id="sheetName"]'),
    "交卷": (By.XPATH, '//*[@class="btn btn-primary"]'),
    "下一题": (By.XPATH, '//*[@class="ri-btn"]'),
}

for element_name, locator in element_locators.items():
    try:
        # 使用显式等待确保元素可见
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))
        print(f"{element_name}元素存在。")
    except:
        print(f"{element_name}元素不存在。")
#回到上一页-综合知识
driver.get('https://rk.51cto.com/t/n/chapter-manage/years/sub-235')
#点击到论文
driver.find_element(By.XPATH,'//*[@class="active').click()
time.sleep(2)

#论文-查看解析，断言答题卡、高频错题元素
driver.find_element(By.XPATH,'//*[@class="flex items-center exam-type"]/a[4]').click()
driver.find_element(By.XPATH,'//*[@class="list-box"]/div[1]/div/div[2]/a[1]').click()
#断言答题卡、再考一次、查看详细报告元素
element_locators = {
    "答题卡": (By.XPATH, '//*[@class="exam-answer-card"]/div[1]/div/div[1]'),
    "再考一次": (By.XPATH, '//*[@class="exam-answer-card-footer"]/button[1]'),
    "查看详细报告": (By.XPATH, '//*[@class="exam-answer-card-footer"]/button[2]'),
}

for element_name, locator in element_locators.items():
    try:
        # 使用显式等待确保元素可见
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))
        print(f"{element_name}元素存在。")
    except:
        print(f"{element_name}元素不存在。")
#回到上一页-历年试题,点击论文
driver.get('https://rk.51cto.com/t/n/chapter-manage/years/sub-235')
driver.find_element(By.XPATH,'//*[@class="active').click()
time.sleep(2)

#论文-再做一遍，断言答题卡、高频错题元素
driver.find_element(By.XPATH,'//*[@class="flex items-center exam-type"]/a[4]').click()
driver.find_element(By.XPATH,'//*[@class="list-box"]/div[1]/div/div[2]/a[2]').click()
   #考试模式,断言答题卡、保存进度、交卷元素
driver.find_element(By.XPATH,'//*[@class="btn plain-btn exam-mode-plain"]').click()
driver.find_element(By.XPATH,'//*[@class="primary-btn"]').click()
element_locators = {
    "答题卡": (By.XPATH, '//*[@class="exam-answer-card-title"]'),
    "保存进度 下次继续": (By.XPATH, '//*[@class="btn btn-plain mb-[10px]"]'),
    "交卷": (By.XPATH, '//*[@class="btn btn-primary"]')
}

for element_name, locator in element_locators.items():
    try:
        # 使用显式等待确保元素可见
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))
        print(f"{element_name}元素存在。")
    except:
        print(f"{element_name}元素不存在。")
#回到上一页-论文-选模式页面
driver.get('https://rk.51cto.com/t/n/previous-exam/detail/17831.html')
time.sleep(2)

   #练习模式，断言答题卡、保存进度、交卷元素
driver.find_element(By.XPATH,'//*[@class="btn plain-btn practice-mode-plain"]').click()
driver.find_element(By.XPATH,'//*[@class="primary-btn"]').click()
element_locators = {
    "答题卡": (By.XPATH, '//*[@class="exam-answer-card-title"]'),
    "保存进度 下次继续": (By.XPATH, '//*[@class="btn btn-plain mb-[10px]"]'),
    "交卷": (By.XPATH, '//*[@class="btn btn-primary"]')
}

for element_name, locator in element_locators.items():
    try:
        # 使用显式等待确保元素可见
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))
        print(f"{element_name}元素存在。")
    except:
        print(f"{element_name}元素不存在。")
#回到上一页-论文-选模式页面
driver.get('https://rk.51cto.com/t/n/previous-exam/detail/17831.html')
time.sleep(2)

   #机考模式，断言答题卡、保存进度、交卷元素
driver.find_element(By.XPATH,'//*[@class="btn primary-btn computer-mode-primary"]').click()
driver.find_element(By.XPATH,'//*[@class="login-btn-box"]').click()
driver.find_element(By.XPATH,'//*[@class="btn confirm-btn"]').click()
#等待点击我已阅读元素
time.sleep(12)
read_element = driver.find_element(By.XPATH, '//*[@class="confirm-btn"]')
read_element.click()
#断言答题卡、交卷、下一题元素
element_locators = {
    "答题卡": (By.XPATH, '//*[@id="sheetName"]'),
    "交卷": (By.XPATH, '//*[@class="btn btn-primary"]'),
    "下一题": (By.XPATH, '//*[@class="ri-btn"]'),
}

for element_name, locator in element_locators.items():
    try:
        # 使用显式等待确保元素可见
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))
        print(f"{element_name}元素存在。")
    except:
        print(f"{element_name}元素不存在。")
#回到上一页-模拟试题
driver.get('https://rk.51cto.com/t/n/chapter-manage/imitate/sub-235')
time.sleep(2)

#-----------模拟试题-----------
driver.find_element(By.XPATH,'//*[@class="flex justify-between tab-main"]/a[5]').click()
#综合知识-查看解析，断言答题卡、高频错题元素
driver.find_element(By.XPATH,'//*[@class="flex items-center exam-type"]/a[2]').click()
driver.find_element(By.XPATH,'//*[@class="list-box"]/div[1]/div/div[2]/a[1]').click()
element_locators = {
    "答题卡": (By.XPATH, '//*[@class="exam-answer-card-header"]/div/div[1]'),
    "高频错题": (By.XPATH, '//*[@class="exam-answer-card-header"]/div/div[2]'),
    "再考一次": (By.XPATH, '//*[@class="btn btn-plain mb-[10px]"]')
}

for element_name, locator in element_locators.items():
    try:
        # 使用显式等待确保元素可见
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))
        print(f"{element_name}元素存在。")
    except:
        print(f"{element_name}元素不存在。")
#回到上一页-综合知识
driver.get('https://rk.51cto.com/t/n/chapter-manage/imitate/sub-235')
driver.find_element(By.XPATH,'//*[@class="flex items-center exam-type"]/a[2]').click()
time.sleep(2)

#综合知识-再做一遍，断言答题卡、高频错题元素
driver.find_element(By.XPATH,'//*[@class="flex items-center exam-type"]/a[2]').click()
driver.find_element(By.XPATH,'//*[@class="list-box"]/div[1]/div/div[2]/a[2]').click()

element_locators = {
    "答题卡": (By.XPATH, '//*[@class="exam-answer-card-header"]/div/div[1]'),
    "高频错题": (By.XPATH, '//*[@class="exam-answer-card-header"]/div/div[2]'),
    "再考一次": (By.XPATH, '//*[@class="btn btn-plain mb-[10px]"]')
}

for element_name, locator in element_locators.items():
    try:
        # 使用显式等待确保元素可见
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))
        print(f"{element_name}元素存在。")
    except:
        print(f"{element_name}元素不存在。")
#回到上一页-综合知识
driver.get('https://rk.51cto.com/t/n/chapter-manage/years/sub-235')
driver.find_element(By.XPATH,'//*[@class="flex items-center exam-type"]/a[2]').click()
time.sleep(2)


#综合知识-开始做题，等待元素可点击
target_element = driver.find_element(By.XPATH,'//*[@class="tit-item-wrap"][9]/div/div[2]')
driver.execute_script("arguments[0].scrollIntoView(false);", target_element)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@class="tit-item-wrap"][9]/div/div[2]')))
target_element.click()
   #考试模式,断言答题卡、保存进度、交卷元素
driver.find_element(By.XPATH,'//*[@class="btn plain-btn exam-mode-plain"]').click()
driver.find_element(By.XPATH,'//*[@class="primary-btn"]').click()
element_locators = {
    "答题卡": (By.XPATH, '//*[@class="exam-answer-card-title"]'),
    "保存进度 下次继续": (By.XPATH, '//*[@class="btn btn-plain mb-[10px]"]'),
    "交卷": (By.XPATH, '//*[@class="btn btn-primary"]')
}

for element_name, locator in element_locators.items():
    try:
        # 使用显式等待确保元素可见
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))
        print(f"{element_name}元素存在。")
    except:
        print(f"{element_name}元素不存在。")
#回到上一页-综合知识-选模式页面
driver.get('https://rk.51cto.com/t/n/previous-exam/detail/10629.html')
time.sleep(2)

   #练习模式，断言答题卡、保存进度、交卷元素
driver.find_element(By.XPATH,'//*[@class="btn plain-btn practice-mode-plain"]').click()
driver.find_element(By.XPATH,'//*[@class="primary-btn"]').click()
element_locators = {
    "答题卡": (By.XPATH, '//*[@class="exam-answer-card-title"]'),
    "保存进度 下次继续": (By.XPATH, '//*[@class="btn btn-plain mb-[10px]"]'),
    "交卷": (By.XPATH, '//*[@class="btn btn-primary"]')
}

for element_name, locator in element_locators.items():
    try:
        # 使用显式等待确保元素可见
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))
        print(f"{element_name}元素存在。")
    except:
        print(f"{element_name}元素不存在。")
#回到上一页-综合知识-选模式页面
driver.get('https://rk.51cto.com/t/n/previous-exam/detail/10629.html')
time.sleep(2)

   #机考模式，断言答题卡、保存进度、交卷元素
driver.find_element(By.XPATH,'//*[@class="btn primary-btn computer-mode-primary"]').click()
driver.find_element(By.XPATH,'//*[@class="login-btn-box"]').click()
driver.find_element(By.XPATH,'//*[@class="btn confirm-btn"]').click()
#等待点击我已阅读元素
time.sleep(12)
read_element = driver.find_element(By.XPATH, '//*[@class="confirm-btn"]')
read_element.click()
#断言答题卡、交卷、下一题元素
element_locators = {
    "答题卡": (By.XPATH, '//*[@id="sheetName"]'),
    "交卷": (By.XPATH, '//*[@class="btn btn-primary"]'),
    "下一题": (By.XPATH, '//*[@class="ri-btn"]'),
}

for element_name, locator in element_locators.items():
    try:
        # 使用显式等待确保元素可见
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))
        print(f"{element_name}元素存在。")
    except:
        print(f"{element_name}元素不存在。")
#回到上一页-综合知识
driver.get('https://rk.51cto.com/t/n/chapter-manage/years/sub-235')
#点击到案例分析
driver.find_element(By.XPATH,'//*[@class="flex items-center exam-type"]/a[3]').click()
time.sleep(2)

#案例分析-查看解析，断言答题卡、高频错题元素
driver.find_element(By.XPATH,'//*[@class="flex items-center exam-type"]/a[3]').click()
driver.find_element(By.XPATH,'//*[@class="list-box"]/div[1]/div/div[2]/a[1]').click()
#断言答题卡、交卷、下一题元素
element_locators = {
    "答题卡": (By.XPATH, '//*[@class="exam-answer-card"]/div[1]/div/div[1]'),
    "再考一次": (By.XPATH, '//*[@class="exam-answer-card-footer"]/button[1]'),
    "查看详细报告": (By.XPATH, '//*[@class="exam-answer-card-footer"]/button[2]'),
}

for element_name, locator in element_locators.items():
    try:
        # 使用显式等待确保元素可见
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))
        print(f"{element_name}元素存在。")
    except:
        print(f"{element_name}元素不存在。")
#回到上一页-案例分析
driver.get('https://rk.51cto.com/t/n/chapter-manage/years/sub-235')
driver.find_element(By.XPATH,'//*[@class="flex items-center exam-type"]/a[3]').click()
time.sleep(2)

#案例分析-再做一遍，断言答题卡、高频错题元素
driver.find_element(By.XPATH,'//*[@class="flex items-center exam-type"]/a[3]').click()
driver.find_element(By.XPATH,'//*[@class="list-box"]/div[1]/div/div[2]/a[2]').click()
   #考试模式,断言答题卡、保存进度、交卷元素
driver.find_element(By.XPATH,'//*[@class="btn plain-btn exam-mode-plain"]').click()
driver.find_element(By.XPATH,'//*[@class="primary-btn"]').click()
element_locators = {
    "答题卡": (By.XPATH, '//*[@class="exam-answer-card-title"]'),
    "保存进度 下次继续": (By.XPATH, '//*[@class="btn btn-plain mb-[10px]"]'),
    "交卷": (By.XPATH, '//*[@class="btn btn-primary"]')
}

for element_name, locator in element_locators.items():
    try:
        # 使用显式等待确保元素可见
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))
        print(f"{element_name}元素存在。")
    except:
        print(f"{element_name}元素不存在。")
#回到上一页-案例分析-选模式页面
driver.get('https://rk.51cto.com/t/n/previous-exam/detail/17854.html')
time.sleep(2)

   #练习模式，断言答题卡、保存进度、交卷元素
driver.find_element(By.XPATH,'//*[@class="btn plain-btn practice-mode-plain"]').click()
driver.find_element(By.XPATH,'//*[@class="primary-btn"]').click()
element_locators = {
    "答题卡": (By.XPATH, '//*[@class="exam-answer-card-title"]'),
    "保存进度 下次继续": (By.XPATH, '//*[@class="btn btn-plain mb-[10px]"]'),
    "交卷": (By.XPATH, '//*[@class="btn btn-primary"]')
}

for element_name, locator in element_locators.items():
    try:
        # 使用显式等待确保元素可见
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))
        print(f"{element_name}元素存在。")
    except:
        print(f"{element_name}元素不存在。")
#回到上一页-案例分析-选模式页面
driver.get('https://rk.51cto.com/t/n/previous-exam/detail/10629.html')
time.sleep(2)

   #机考模式，断言答题卡、保存进度、交卷元素
driver.find_element(By.XPATH,'//*[@class="btn primary-btn computer-mode-primary"]').click()
driver.find_element(By.XPATH,'//*[@class="login-btn-box"]').click()
driver.find_element(By.XPATH,'//*[@class="btn confirm-btn"]').click()
#等待点击我已阅读元素
time.sleep(12)
read_element = driver.find_element(By.XPATH, '//*[@class="confirm-btn"]')
read_element.click()
#断言答题卡、交卷、下一题元素
element_locators = {
    "答题卡": (By.XPATH, '//*[@id="sheetName"]'),
    "交卷": (By.XPATH, '//*[@class="btn btn-primary"]'),
    "下一题": (By.XPATH, '//*[@class="ri-btn"]'),
}

for element_name, locator in element_locators.items():
    try:
        # 使用显式等待确保元素可见
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))
        print(f"{element_name}元素存在。")
    except:
        print(f"{element_name}元素不存在。")
#回到上一页-综合知识
driver.get('https://rk.51cto.com/t/n/chapter-manage/years/sub-235')
#点击到论文
driver.find_element(By.XPATH,'//*[@class="active').click()
time.sleep(2)

#论文-查看解析，断言答题卡、高频错题元素
driver.find_element(By.XPATH,'//*[@class="flex items-center exam-type"]/a[4]').click()
driver.find_element(By.XPATH,'//*[@class="list-box"]/div[1]/div/div[2]/a[1]').click()
#断言答题卡、再考一次、查看详细报告元素
element_locators = {
    "答题卡": (By.XPATH, '//*[@class="exam-answer-card"]/div[1]/div/div[1]'),
    "再考一次": (By.XPATH, '//*[@class="exam-answer-card-footer"]/button[1]'),
    "查看详细报告": (By.XPATH, '//*[@class="exam-answer-card-footer"]/button[2]'),
}

for element_name, locator in element_locators.items():
    try:
        # 使用显式等待确保元素可见
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))
        print(f"{element_name}元素存在。")
    except:
        print(f"{element_name}元素不存在。")
#回到上一页-历年试题,点击论文
driver.get('https://rk.51cto.com/t/n/chapter-manage/years/sub-235')
driver.find_element(By.XPATH,'//*[@class="active').click()
time.sleep(2)

#论文-再做一遍，断言答题卡、高频错题元素
driver.find_element(By.XPATH,'//*[@class="flex items-center exam-type"]/a[4]').click()
driver.find_element(By.XPATH,'//*[@class="list-box"]/div[1]/div/div[2]/a[2]').click()
   #考试模式,断言答题卡、保存进度、交卷元素
driver.find_element(By.XPATH,'//*[@class="btn plain-btn exam-mode-plain"]').click()
driver.find_element(By.XPATH,'//*[@class="primary-btn"]').click()
element_locators = {
    "答题卡": (By.XPATH, '//*[@class="exam-answer-card-title"]'),
    "保存进度 下次继续": (By.XPATH, '//*[@class="btn btn-plain mb-[10px]"]'),
    "交卷": (By.XPATH, '//*[@class="btn btn-primary"]')
}

for element_name, locator in element_locators.items():
    try:
        # 使用显式等待确保元素可见
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))
        print(f"{element_name}元素存在。")
    except:
        print(f"{element_name}元素不存在。")
#回到上一页-论文-选模式页面
driver.get('https://rk.51cto.com/t/n/previous-exam/detail/17831.html')
time.sleep(2)

   #练习模式，断言答题卡、保存进度、交卷元素
driver.find_element(By.XPATH,'//*[@class="btn plain-btn practice-mode-plain"]').click()
driver.find_element(By.XPATH,'//*[@class="primary-btn"]').click()
element_locators = {
    "答题卡": (By.XPATH, '//*[@class="exam-answer-card-title"]'),
    "保存进度 下次继续": (By.XPATH, '//*[@class="btn btn-plain mb-[10px]"]'),
    "交卷": (By.XPATH, '//*[@class="btn btn-primary"]')
}

for element_name, locator in element_locators.items():
    try:
        # 使用显式等待确保元素可见
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))
        print(f"{element_name}元素存在。")
    except:
        print(f"{element_name}元素不存在。")
#回到上一页-论文-选模式页面
driver.get('https://rk.51cto.com/t/n/previous-exam/detail/17831.html')
time.sleep(2)

   #机考模式，断言答题卡、保存进度、交卷元素
driver.find_element(By.XPATH,'//*[@class="btn primary-btn computer-mode-primary"]').click()
driver.find_element(By.XPATH,'//*[@class="login-btn-box"]').click()
driver.find_element(By.XPATH,'//*[@class="btn confirm-btn"]').click()
#等待点击我已阅读元素
time.sleep(12)
read_element = driver.find_element(By.XPATH, '//*[@class="confirm-btn"]')
read_element.click()
#断言答题卡、交卷、下一题元素
element_locators = {
    "答题卡": (By.XPATH, '//*[@id="sheetName"]'),
    "交卷": (By.XPATH, '//*[@class="btn btn-primary"]'),
    "下一题": (By.XPATH, '//*[@class="ri-btn"]'),
}

for element_name, locator in element_locators.items():
    try:
        # 使用显式等待确保元素可见
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))
        print(f"{element_name}元素存在。")
    except:
        print(f"{element_name}元素不存在。")
#去易错题页
driver.get('https://rk.51cto.com/t/n/chapter-manage/error-prone-question/sub-235')
time.sleep(2)

#-----------易错题-----------
#考试模式-继续答题-开始答题，点击准备好了
driver.find_element(By.XPATH,'//*[@class="flex justify-between w-[1200px] mx-auto mt-[40px]"]/section/div[1]/div[1]/a').click()
driver.find_element(By.XPATH,'//*[@class="radio-box"]/span[1]').click()
driver.find_element(By.XPATH,'//*[@class="radio-box mt-[30px]"]/span[1]').click()
driver.find_element(By.XPATH,'//*[@class="primary-btn"]').click()
driver.find_element(By.XPATH,'//*[@class="primary-btn"]').click()

#断言页面上的答题卡，保存进度，交卷三个元素
element_locators = {
    "答题卡": (By.XPATH, '//*[@class="exam-answer-card-title"]'),
    "保存进度，下次继续": (By.XPATH, '//*[@class="btn btn-plain mb-[10px]"]'),
    "交卷": (By.XPATH, '//*[@class="btn btn-primary"]')
}

for element_name, locator in element_locators.items():
    try:
        # 使用显式等待确保元素可见
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))
        print(f"{element_name}元素存在。")
    except:
        print(f"{element_name}元素不存在。")
#回到上一页
driver.get('https://rk.51cto.com/t/n/chapter-manage/error-prone-question/sub-235')
time.sleep(2)

#考试模式-重新开始-开始答题，点击准备好了
driver.find_element(By.XPATH,'//*[@class="flex justify-between w-[1200px] mx-auto mt-[40px]"]/section/div[1]/div[1]/a').click()
driver.find_element(By.XPATH,'//*[@class="radio-box"]/span[1]').click()
driver.find_element(By.XPATH,'//*[@class="radio-box mt-[30px]"]/span[2]').click()
driver.find_element(By.XPATH,'//*[@class="primary-btn"]').click()
driver.find_element(By.XPATH,'//*[@class="primary-btn"]').click()

#断言页面上的答题卡，保存进度，交卷三个元素
element_locators = {
    "答题卡": (By.XPATH, '//*[@class="exam-answer-card-title"]'),
    "保存进度，下次继续": (By.XPATH, '//*[@class="btn btn-plain mb-[10px]"]'),
    "交卷": (By.XPATH, '//*[@class="btn btn-primary"]')
}

for element_name, locator in element_locators.items():
    try:
        # 使用显式等待确保元素可见
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))
        print(f"{element_name}元素存在。")
    except:
        print(f"{element_name}元素不存在。")
#回到上一页
driver.get('https://rk.51cto.com/t/n/chapter-manage/error-prone-question/sub-235')
time.sleep(2)

#练习模式-继续答题-开始答题，点击准备好了
driver.find_element(By.XPATH,'//*[@class="flex justify-between w-[1200px] mx-auto mt-[40px]"]/section/div[1]/div[1]/a').click()
driver.find_element(By.XPATH,'//*[@class="radio-box"]/span[2]').click()
driver.find_element(By.XPATH,'//*[@class="radio-box mt-[30px]"]/span[1]').click()
driver.find_element(By.XPATH,'//*[@class="primary-btn"]').click()
driver.find_element(By.XPATH,'//*[@class="primary-btn"]').click()

#断言页面上的答题卡，保存进度，交卷三个元素
element_locators = {
    "答题卡": (By.XPATH, '//*[@class="exam-answer-card-title"]'),
    "保存进度，下次继续": (By.XPATH, '//*[@class="btn btn-plain mb-[10px]"]'),
    "交卷": (By.XPATH, '//*[@class="btn btn-primary"]')
}

for element_name, locator in element_locators.items():
    try:
        # 使用显式等待确保元素可见
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))
        print(f"{element_name}元素存在。")
    except:
        print(f"{element_name}元素不存在。")
#回到上一页
driver.get('https://rk.51cto.com/t/n/chapter-manage/error-prone-question/sub-235')
time.sleep(2)

#练习模式-重新开始-开始答题，点击准备好了
driver.find_element(By.XPATH,'//*[@class="flex justify-between w-[1200px] mx-auto mt-[40px]"]/section/div[1]/div[1]/a').click()
driver.find_element(By.XPATH,'//*[@class="radio-box"]/span[2]').click()
driver.find_element(By.XPATH,'//*[@class="radio-box mt-[30px]"]/span[2]').click()
driver.find_element(By.XPATH,'//*[@class="primary-btn"]').click()
driver.find_element(By.XPATH,'//*[@class="primary-btn"]').click()

#断言页面上的答题卡，保存进度，交卷三个元素
element_locators = {
    "答题卡": (By.XPATH, '//*[@class="exam-answer-card-title"]'),
    "保存进度，下次继续": (By.XPATH, '//*[@class="btn btn-plain mb-[10px]"]'),
    "交卷": (By.XPATH, '//*[@class="btn btn-primary"]')
}

for element_name, locator in element_locators.items():
    try:
        # 使用显式等待确保元素可见
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))
        print(f"{element_name}元素存在。")
    except:
        print(f"{element_name}元素不存在。")
#回到上一页
driver.get('https://rk.51cto.com/t/n/chapter-manage/error-prone-question/sub-235')
time.sleep(2)
