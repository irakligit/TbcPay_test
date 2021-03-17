
from selenium import webdriver


class Header(object):
    #ვიღებ ყველა ლოკატორს ცალკე და არა ერთი კოდით, რადგან შემდგომში შესაძლებელი იყოს ნებისმიერი
    #ლოკატორის გამოძახება ნებისმიერ კლასში, ლოკატორების უმეტესობას დავარქვი ქართულად სახელები რადგან საიტშიც მასე ერქვა


    # ჰედერის ლოკატორები
    services = "//*[@id='mount']//*[@href='/services']"
    transfers = "//*[@id='mount']//*[@href='/transfers']"
    for_business = "//*[@id='mount']//*[@href='/for-business']"
    foreign_payments = "//*[@id='mount']//*[@href='/foreign-payments']"

    # სერვისების ლოკატორები "
    popularuli_servisebi = "//*[@id='mount']//*[@href = '/services/popularuli-servisebi']"
    mobiluri_kavshiri = "//*[@id='mount']//*[@href = '/services/mobiluri-kavshiri']"
    bankebi_dazgveva_mikrosafinanso = "//*[@id='mount']//*[@href = '/services/bankebi-dazgveva-mikrosafinanso']"
    totalizatorebi_kazino_lataria = "//*[@id='mount']//*[@href = '/services/totalizatorebi-kazino-lataria']"
    interneti_telefoni_televizia = "//*[@id='mount']//*[@href = '/services/interneti-telefoni-televizia']"
    komunaluri_gadasaxadebi = "//*[@id='mount']//*[@href = '/services/komunaluri-gadasaxadebi']"
    transporti = "//*[@id='mount']//*[@href = '/services/transporti']"
    saxelmwifo_servisebi = "//*[@id='mount']//*[@href = '/services/saxelmwifo-servisebi']"
    sxvadasxva = "//*[@id='mount']//*[@href = '/services/sxvadasxva']"

    #საძიებო ველი
    search = "searchWord"
    balansis_shevseba = "//*[text()='მობილური ბალანსის შევსება']"
    #ტელეფონის ნომრის ველი
    number_element = "small-font"
    #შემოწმების ღილაკი
    shemowmeba = "//button//span[text()='შემოწმება']"
    #აირჩიეთ სერვისის ლოკატორი
    airchiet_servisi = "label[title='აირჩიეთ სერვისი']"
    #ბალანსის შევსება
    dropdown_balansi = "#BONUS a[title='ბალანსის შევსება']"
    #მეტი 8 - ლ
    meti_8 = "//span[contains(text(),'- 8')]"
    #მეტი 10 -ლ
    meti_10 = "//span[contains(text(),'- 10')]"

    #მეტი 10 ლ დაჭერის შემდეგ გამოტანილი ელემენტების ლოკატორები

    #xpath რომლითაც რამდენიმე ელემენტს ვპოულობ
    spanElement = "//div[@class='ded17e-0 iiRqkB']//span"
    ten_lari = "debt"
    value_10 = "//*[@id='mount']//*[@value='10']"
    info = "//*[@class='info']//*[text()='10.12']"
    payBTN = "pay-btn"




















