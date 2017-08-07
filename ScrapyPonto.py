# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time

def scrapyPonto():
    url = 'https://.com/'

    options = Options()
    #options.add_argument("--headless")
    #driver = webdriver.Chrome(executable_path=os.path.abspath("/Users/edsonsoares/PycharmProjects/WebSpider/chromedriver"),   chrome_options=options)
    driver = webdriver.Chrome(
        executable_path=os.path.abspath("/home/edson/PycharmProjects/WebSpider/chromedriver"),
        chrome_options=options)
    driver.get(url)

    usuario = driver.find_element_by_xpath('//*[@id="txtUsuario"]')
    usuario.send_keys('')

    senha = driver.find_element_by_xpath('//*[@id="txtSenha"]')
    senha.send_keys('')

    boton = driver.find_element_by_xpath('//*[@id="btnEntrar"]')
    boton.click()

    #Muda para a nova janela do processo para entrar a senha
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[-1])

    reloj = driver.find_element_by_xpath('//*[@id="lnkWidgetBaterPonto"]')
    reloj.click()

    time.sleep(5)
    driver.switch_to.window(driver.window_handles[-1])

    jCode = '''
    $("#lnkWidgetBaterPonto").click(function () {
        $("#divModalIncluirBatida").show();
        ObterDataHoraModalPonto();
        ValidarAtualizacaoDataHoraDinamicamente(true);
        $("#modalBaterPonto").slideDown();
    });
    '''
    driver.execute_script(jCode)

    botonHorario = driver.find_element_by_xpath('//*[@id="btnIncluirBatidaModalBaterPonto"]')
    #Ejecuta script para marcar el horário
    #driver.execute_script('IncluirBatidaModalPonto()')
    textoBoton = str(botonHorario.text)

    print('Nombre del Botón para marcar: ' + textoBoton)

scrapyPonto()
