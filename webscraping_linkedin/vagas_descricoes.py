
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/jobs/ci%C3%AAncia-de-dados-vagas/?originalSubdomain=br")

resultados = driver.find_elements_by_class_name("result-card__full-card-link")

lista_descricao = []

while True:
    for r in resultados[len(lista_descricao):]:
        r.click()
        sleep(2)
        descricao_raw = driver.find_element_by_class_name("description")
        try:
            botao = driver.find_element_by_xpath("/html/body/main/section/div[2]/section[2]/div/section/button[1]")
            botao.click()
        except:
            pass
        lista_descricao.append(descricao_raw.text)
        descricao = ' '.join(lista_descricao)
    resultados = driver.find_elements_by_class_name("result-card__full-card-link")
    if len(lista_descricao) == len(resultados):
        break

with open('descricoes_vagas.txt', 'w', encoding="utf-8") as f:
    f.write(descricao)
    

