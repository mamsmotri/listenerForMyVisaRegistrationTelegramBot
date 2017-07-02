#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dependencies import *



bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Это не суть, что я вижу")


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "это /help")

def grime_legend():
    headers = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4',
        'Cache-Control':'no-cache',
        'Connection':'keep-alive',
        'Content-Length':'7280',
        'Content-Type':'application/x-www-form-urlencoded',
        'Cookie':'ASP.NET_SessionId=kwdm2etf21fx05xw2h4ghkyw; __CSRF=34525e0f-4cb2-4497-9d64-26f26564dbd9; __AntiXsrfToken=4a35cb7662284063911464be1d3e0f8e; _gat=1; _ga=GA1.2.1122632451.1498659753; _gid=GA1.2.809783215.1498837438',
        'Host':'visapoint.eu',
        'Origin':'https://visapoint.eu',
        'Pragma':'no-cache',
        'Referer':'https://visapoint.eu/disclaimer',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    }

    form_data = {
        'rsm1_TSM': ';;System.Web.Extensions, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35:ru-RU:93a6b8ed-f453-4cc5-9080-8017894b33b0:ea597d4b:b25378d2',
        '__CSRF': '/wEFJDM0NTI1ZTBmLTRjYjItNDQ5Ny05ZDY0LTI2ZjI2NTY0ZGJkOQ==',
        '__EVENTTARGET': '',
        '__EVENTARGUMENT': '',
        '__VIEWSTATE': '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',
        '__VIEWSTATEGENERATOR': '3AF363220',
        '__VIEWSTATEENCRYPTED': '',
        '__EVENTVALIDATION': 'KeCTL7tsmTRMzhIkY8HkAAR2djXPsZrwdTBKRBn4gV6HfWT3H1mhjIgi7tNqE8P97zonQLQ2F61zegRssl0KG/e/vd9e2gNQntIS/Lpi6a+eMX2No40OUvkNfzeaNRMmhfWVp655Pwt1JEA85CMZJuNUvbMlJP5vNDcJtEv1dz6fpJHmCbtTUg9SLUnZcHPkmJC1sRNQfIyV4Ugj5zKgO9ZN40xlu8i4ONDv+5UsP5F58KDb',
        'ctl00$ddLocale': 'русский',
        'ctl00_ddLocale_ClientState': '',
        'ctl00_cp1_btnDecline_ClientState': '{"text": "Не согласен", "value": "", "checked": false, "target": "",  "navigateUrl": "", "commandName": "", "commandArgument": "", "autoPostBack": true,"selectedToggleStateIndex": 0, "validationGroup": null, "readOnly": false}',
        'ctl00$cp1$btnAccept': 'Принять',
        'ctl00_cp1_btnAccept_ClientState': '{"text": "Принять", "value": "", "checked": false, "target": "", "navigateUrl": "", "commandName": "", "commandArgument": "", "autoPostBack": true, "selectedToggleStateIndex": 0, "validationGroup": null, "readOnly": false}',
        'ctl00_cp1_rbClose_ClientState': '{"text": "OK", "value": "", "checked": false, "target": "", "navigateUrl": "", "commandName": "", "commandArgument": "", "autoPostBack": true, "selectedToggleStateIndex": 0, "validationGroup": null, "readOnly": false}',
        'ctl00_cp1_rttDecline_ClientState': ''
    }

    request_disclaimer = requests.post("https://visapoint.eu/disclaimer", data=form_data, headers=headers)
    print(request_disclaimer.status_code, request_disclaimer.reason, request_disclaimer.text)

    # u = urllib2.urlopen('https://visapoint.eu', data)
    # h.request('POST', '/inout-tracker/index.php', data, headers)


    url = 'https://visapoint.eu'

    r = requests.get(url, headers=headers)
    result_page = r.text

    parsed_page = BeautifulSoup(result_page, 'html.parser')

    player_id = parsed_page.find('div', {'id': 'ctl00_cp1_btnAccept_input'}).find('div', {'class': 'inner'}).get(
        'data-player-id')
    player_name = parsed_page.find('div', {'class': 'result-player'}).get('data-filter-value')
    player_pic_src = parsed_page.find('div', {'class': 'result-player'}).find('img').get('src')
    player = {
        'id': player_id,
        'name': player_name,
        'pic_src': player_pic_src
    }



# bot.polling()


def open_driver():
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys

    chrome = webdriver.Chrome()
    # driver = webdriver.Firefox()
    chrome.get("https://visapoint.eu/")
    print(chrome)

    chrome.find_element_by_name("ctl00$cp1$btnAccept").click()

    chrome.find_element_by_name("ctl00$cp1$btnNewAppointment").click()

    chrome.find_element_by_name('ctl00$cp1$ddCitizenship').click()
    chrome.find_element_by_xpath("//*[contains(text(), 'Russia (Россия)')]").click()

    chrome.find_element_by_name('ctl00$cp1$ddEmbassy').click()
    chrome.find_element_by_xpath("//*[contains(text(), 'Russia (Россия) - Jekatěrinburg')]").click()

    chrome.find_element_by_name('ctl00$cp1$ddVisaType').click()
    chrome.find_element_by_xpath("//*[contains(text(), 'Long-term residence permit')]").click()


