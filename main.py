from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

# Открытие веб-страницы
driver.get("https://www.cs.vsu.ru")

# Нахождение всех элементов <a> на странице
# links = driver.find_elements(By.TAG_NAME, "a")

wait = WebDriverWait(driver, 10)
links = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "a")))

# Извлечение значений атрибута href и сохранение их в список
# link_pairs = [(link.text, link.get_attribute("href")) for link in links if link.get_attribute("href") is not None]
link_pairs = []

# Вывод списка ссылок
for href in links:
    print(href.text)
    print(href.get_attribute("href"))

# Закрытие браузера
driver.quit()
