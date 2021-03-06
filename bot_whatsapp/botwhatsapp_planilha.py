from selenium import webdriver
from time import sleep
import pandas as pd

driver = webdriver.Chrome()
whatsapp = driver.get("https://web.whatsapp.com/")
NEW_CHAT = "/html/body/div[1]/div/div/div[3]/div/header/div[2]/div/span/div[2]/div/span"
SEARCH_CONTACT = "/html/body/div[1]/div/div/div[2]/div[1]/span/div/span/div/div[1]/div/label/div/div[2]"
FIRST_CONTACT = "TbtXF"
TYPE_MESSAGE = "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]"
SEND_MESSAGE ="/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]/button/span"

input("Pressione enter depois de colocar o QR Code")

def script_bot(contact, message):
    newchat = driver.find_element_by_xpath(NEW_CHAT)
    newchat.click()
    sleep(2)
    #searching contact
    search_contact = driver.find_element_by_xpath(SEARCH_CONTACT)
    search_contact.click()
    search_contact.send_keys(contact)
    sleep(2)
    #clicking on the contact
    first_contact = driver.find_element_by_class_name(FIRST_CONTACT)
    first_contact.click()
    sleep(2)
    #typing message
    type_message = driver.find_element_by_xpath(TYPE_MESSAGE)
    type_message.click()
    type_message.send_keys(message)
    #sending message
    send_message = driver.find_element_by_xpath(SEND_MESSAGE)
    send_message.click()
    sleep(1)
    
agenda = pd.read_excel("agenda.xlsx") #documento com a lista de contato e suas respectivas mensagens

for cont in agenda["NOME"]: 
    msg = agenda.loc[agenda["NOME"] == cont, "MENSAGEM"].values
    script_bot(cont, msg)
