import requests
import json
import time
from selenium import webdriver
from tabulate import tabulate
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

defiswap_list=list()

bakery_list  = list()
julswap_list  = list()
pancake_list  = list()
uniswap_list= list()
sushiswap_list= list()
bancor_list= list()
serum_list = list()
mdex_list  = list()
linkswap_list= list()
quickswap_list= list()
wanswap_list= list()
sashimiswap_list= list()
swipeswap_list= list()
pangolin_list= list()
mov_list= list()
apeswap_list=list()
burger_list=list()

errorcounter=0
def DeFi():
    
    print("PROJE ÇALIŞIYOR")
    wanlistSwap()
    bancorlistSwap()
    julistSwap()
    linklistSwap()
    bakerylistSwap()
    mdexlistSwap()
    burgerswaplistSwap()
    sushiswaplistSwap()#ok                           
    uniswaplistSwap()#ok
    #serumlistSwap()#ok
    pancakelistSwap()
    sashimilistSwap()
    swipelistSwap()
    pangolinlistSwap()
    #quicklistSwap()
    movlistSwap()
    apeswaplistSwap()
    j=0
    while j<16:
                    datas = [swipeswap_list,burger_list,pangolin_list,wanswap_list,apeswap_list,mov_list,uniswap_list,sushiswap_list,sashimiswap_list,mdex_list,julswap_list,bakery_list,pancake_list,linkswap_list,quickswap_list,bancor_list]
                    for i in datas[j]:
                        if(float(i[5])!=0):
                            defiswap_list.append([i[0],i[1],round(float(i[2]),1),round(float(i[3]),1),round(float(i[4]),1),round(float(i[5]),1)])
                    j +=1
                    data = sorted(defiswap_list, key=lambda x:float(x[5]), reverse=True)
    #print(tabulate(data))
    print(data)
    print("PROJE BİTTİ")
    
def burgerswaplistSwap():
    try:
        print("burgerswap başladı")
        pair = list()
        data_values = list()
        def looper():
                WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".sc-jlyJG.hZRHdD")))
                time.sleep(2)
                name = driver.find_elements_by_css_selector(".sc-jlyJG.hZRHdD")
                values = driver.find_elements_by_css_selector(".sc-fMiknA.cObOEH.css-4cffwv")
                for i in name:
                    pair.append(i.text)
                for i in values:
                    data_values.append(i.text)
        exchange= "burgerswap"
        url="https://info.burgerswap.org/pairs"
        driver = webdriver.Chrome('/home/tufan/Desktop/DefiProject/DefiProject/chromedriver')
        driver.get(url)
        try:    
            looper()
            driver.find_element_by_css_selector(".sc-Rmtcm.eeIIib").click()
            looper()
            l=0
            v=1
            f=3
            a=4
            p=0
            while (a<=len(data_values)):
                        burger_list.append([exchange,pair[p],data_values[l].replace("$", "") if (data_values[l].replace("$", ""))[-3:-2] =="." else (data_values[l].replace("$", "")).replace(".",""),(data_values[v].replace("$", ""))[:-1] if (data_values[v].replace("$", ""))[-3:-2] =="." else (data_values[v].replace("$", "")).replace(".",""),(data_values[f].replace("$", ""))[:-1] if (data_values[f].replace("$", ""))[-3:-2] =="." else (data_values[f].replace("$", "")).replace(".",""),(data_values[a].replace("+", "")).replace("%","")])    
                        l+=5
                        v+=5
                        f+=5
                        a+=5
                        p+=1
            driver.close()
            global errorcounter
            errorcounter=0
            print("burgerswap bitti")
        except:
            print("burgerswap listesi oluşturulamadı")
            driver.close()
            errorcounter+=1
            if(errorcounter<5):
                burgerswaplistSwap()
            errorcounter=0
    except:
        print("burgerswap çalışmadı")
def movlistSwap():
    try:
        print("mov başladı")
        pair = list()
        data_values = list()
        def looper():
            WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".ant-table-row.ant-table-row-level-0 td a")))
            time.sleep(2)
            name = driver.find_elements_by_css_selector(".ant-table-row.ant-table-row-level-0 td a")
            values = driver.find_elements_by_css_selector(".ant-table-cell.cell span")
            for i in name:
                pair.append(i.text)
            for i in values:
                data_values.append(i.text)
        exchange= "mov"
        url="https://sup.finance/dashboard"
        driver = webdriver.Chrome('/home/tufan/Desktop/DefiProject/DefiProject/chromedriver')
        driver.get(url)
        try:
            looper()
            l=2
            v=3
            f=4
            a=5
            p=0
            while(a<=91):
                mov_list.append([exchange,pair[p],(data_values[l].replace("$", "")).replace(",", ""),(data_values[v].replace("$", "")).replace(",", ""),(data_values[f].replace("$", "")).replace(",", ""),(data_values[a].replace("+", "")).replace("%","")])
                l+=7
                v+=7
                f+=7
                a+=7
                p+=1
            driver.close()
            global errorcounter
            errorcounter=0
            print("mov bitti")
        except:
            print("mov listesi oluşturulamadı")
            driver.close()
            errorcounter+=1
            if(errorcounter<5):
                movlistSwap() 
            errorcounter=0
    except:
        print("mov çalışmadı")
def swipelistSwap():
    try:
        print("swipeswap başladı")
        pair = list()
        data_values = list()
        def looper():
            WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".MuiTypography-root.MuiLink-root.MuiLink-underlineHover.MuiTypography-body2.MuiTypography-colorPrimary.MuiTypography-noWrap")))
            time.sleep(2)
            name = driver.find_elements_by_css_selector(".MuiTypography-root.MuiLink-root.MuiLink-underlineHover.MuiTypography-body2.MuiTypography-colorPrimary.MuiTypography-noWrap")
            values = driver.find_elements_by_css_selector(".MuiTableCell-root.MuiTableCell-body.MuiTableCell-alignRight")
            for i in name:
                pair.append(i.text)
            for i in values:
                data_values.append(i.text)
        exchange= "swipeswap"
        driver = webdriver.Chrome('/home/tufan/Desktop/DefiProject/DefiProject/chromedriver')
        url="https://info.swipe.org/"
        driver.get(url)

        try:
            looper()
            l=36
            v=37
            f=39
            a=41
            p=0
            while(p<10):
                swipeswap_list.append([exchange,pair[p],(data_values[l].replace("$", "")).replace(",", ""),(data_values[v].replace("$", "")).replace(",", ""),(data_values[f].replace("$", "")).replace(",", ""),(data_values[a].replace("+", "")).replace("%","")])
                l+=6
                v+=6
                f+=6
                a+=6
                p+=1
            driver.close()
            global errorcounter
            errorcounter=0
            print("swipeswap bitti")
        except:
            print("swipeswap listesi oluşturulamadı")  
            driver.close()
            errorcounter+=1
            if(errorcounter<5):
                swipelistSwap()
            errorcounter=0      
    except:
        print("swipeswap çalışmadı")
def sashimilistSwap():
    try:
        print("sashimiswap başladı")
        pair = list()
        data_values = list()
        def looper():
            WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".sc-gPEVay.bYsHcw")))
            time.sleep(2)
            name = driver.find_elements_by_css_selector(".sc-gPEVay.bYsHcw")
            values = driver.find_elements_by_css_selector(".sc-hzDkRC.hvyZgB.css-4cffwv")
            for i in name:
                pair.append(i.text)
            for i in values:
                data_values.append(i.text)
        exchange= "sashimiswap"
        driver = webdriver.Chrome('/home/tufan/Desktop/DefiProject/DefiProject/chromedriver')
        url="https://info.sashimi.cool/pairs"
        driver.get(url)
        try:
            looper()
            l=0
            v=1
            f=3
            a=4
            p=0
            while(p<=10):
                sashimiswap_list.append([exchange,pair[p],data_values[l].replace("$", "") if (data_values[l].replace("$", ""))[-3:-2] =="." else (data_values[l].replace("$", "")).replace(".",""),(data_values[v].replace("$", ""))[:-1] if (data_values[v].replace("$", ""))[-3:-2] =="." else (data_values[v].replace("$", "")).replace(".",""),(data_values[f].replace("$", ""))[:-1] if (data_values[f].replace("$", ""))[-3:-2] =="." else (data_values[f].replace("$", "")).replace(".",""),(data_values[a].replace("+", "")).replace("%","")])    
                l+=5
                v+=5
                f+=5
                a+=5
                p+=1
            driver.close()
            global errorcounter
            errorcounter=0
            print("sashimiswap bitti")
        except:
            print("sashimiswap listesi oluşturulamadı")
            driver.close()
            errorcounter+=1
            if(errorcounter<5):
                sashimilistSwap()
            errorcounter=0
    except:
        print("sashimiswap çalışmadı")
def wanlistSwap():
    try:
        print("wanswap başladı")
        pair = list()
        data_values = list()
        def looper():
            WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".sc-jlyJG.hZRHdD")))
            time.sleep(2)
            name = driver.find_elements_by_css_selector(".sc-jlyJG.hZRHdD")
            values = driver.find_elements_by_css_selector(".sc-fBuWsC.KrSIM.css-4cffwv div div:nth-child(1)")
            for i in name:
                pair.append(i.text)
            for i in values:
                data_values.append(i.text)
        exchange= "wanswap"
        driver = webdriver.Chrome('/home/tufan/Desktop/DefiProject/DefiProject/chromedriver')
        url="https://info.wanswap.finance/pairs"
        driver.get(url)
        try:
            looper()
            l=0
            v=1
            f=3
            a=4
            p=0
            while (a<=120):
                if((data_values[a].replace("+", "")).replace("%","")=="0"):
                    wanswap_list.append([exchange,pair[p],((data_values[l].replace("$", "")).replace(".", "")).replace(",", "."),((data_values[v].replace("$", "")).replace(".", "")).replace(",", "."),((data_values[f].replace("$", "")).replace(".", "")).replace(",", "."),(data_values[a].replace("+", "")).replace("%","")])
                    l+=5
                    v+=5
                    f+=5
                    a+=5
                    p+=1
                else:
                    wanswap_list.append([exchange,pair[p],((data_values[l].replace("$", "")).replace(".", "")).replace(",", "."),((data_values[v].replace("$", "")).replace(".", "")).replace(",", "."),((data_values[f].replace("$", "")).replace(".", "")).replace(",", "."),(data_values[a].replace("+", "")).replace("%","")])
                    l+=6
                    v+=6
                    f+=6
                    a+=6
                    p+=1
            driver.close()
            global errorcounter
            errorcounter=0
            print("wanswap bitti")
        except:
            print("wanswap listesi oluşturulamadı") 
            driver.close()
            errorcounter+=1
            if(errorcounter<5):
                wanlistSwap() 
            errorcounter=0 
    except:
        print("wanswap çalışmadı")
def bancorlistSwap():
    try:
        print("bancorswap başladı")
        url = 'https://api-v2.bancor.network/pools' 
        response = requests.get(url,timeout=10,headers={
                'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"})
        json_data= response.json()
        exchange = "Bancor"
        try:
            for i in json_data["data"]:
                if(float((i["liquidity"]["usd"]))!=0):
                    ayp=str((float(i["fees_24h"]["usd"])/float((i["liquidity"]["usd"])))*100*365)
                    bancor_list.append([exchange,i["name"],i["liquidity"]["usd"],"0.0",i["liquidity"]["usd"],ayp])
            print("bancorswap bitti")
        except:
            print("bancorswap listesi oluşturulamadı")         
    except:
        print("bancorswap çalışmadı")
def quicklistSwap():
    try:
        print("quickswap başladı")
        pair = list()
        data_values = list()
        def looper():
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".sc-gPEVay.gLawMS")))
            name = driver.find_elements_by_css_selector(".sc-gPEVay.gLawMS")
            values = driver.find_elements_by_css_selector(".sc-VigVT.dNgKCa div:nth-child(1)")
            for i in name:
                pair.append(i.text)
            for i in values:
                data_values.append(i.text)
        exchange= "quickswap"
        driver = webdriver.Chrome('/home/tufan/Desktop/DefiProject/DefiProject/chromedriver')
        url="https://info.quickswap.exchange/pairs"
        driver.get(url)
        try:
            looper()
            l=0
            v=1
            f=3
            a=4
            p=0
            while (a<=len(data_values)):
                quickswap_list.append([exchange,pair[p],((data_values[l].replace("$", "")).replace(".", "")).replace(",", "."),((data_values[v].replace("$", "")).replace(".", "")).replace(",", "."),((data_values[f].replace("$", "")).replace(".", "")).replace(",", "."),(data_values[a].replace("+", "")).replace("%","")])
                l+=6
                v+=6
                f+=6
                a+=6
                p+=1
            driver.close()
            global errorcounter
            errorcounter=0
            print("quickswap bitti")
        except:
            print("quickswap listesi oluşturulamadı")
            driver.close()
            errorcounter+=1
            if(errorcounter<5):
                quicklistSwap() 
            errorcounter=0
    except:
        print("quickswap çalışmadı")
def pangolinlistSwap():
    try:
        print("pangolin başladı")
        pair = list()
        data_values = list()
        def looper():
            WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".sc-iRbamj.bowFDd")))
            time.sleep(2)
            name = driver.find_elements_by_css_selector(".sc-iRbamj.bowFDd")
            values = driver.find_elements_by_css_selector(".sc-jhAzac.ewmrIK.css-4cffwv")
            for i in name:
                pair.append(i.text)
            for i in values:
                data_values.append(i.text)
        time.sleep(2)
        exchange= "pangolin"
        driver = webdriver.Chrome('/home/tufan/Desktop/DefiProject/DefiProject/chromedriver')
        url="https://info.pangolin.exchange/#/pairs"
        driver.get(url)
        try:
            looper()
            l=0
            v=1
            f=3
            a=4
            p=0
            while(a<=len(data_values)):
                pangolin_list.append([exchange,pair[p],data_values[l].replace("$", "") if (data_values[l].replace("$", ""))[-3:-2] =="." else (data_values[l].replace("$", "")).replace(".",""),(data_values[v].replace("$", ""))[:-1] if (data_values[v].replace("$", ""))[-3:-2] =="." else (data_values[v].replace("$", "")).replace(".",""),(data_values[f].replace("$", ""))[:-1] if (data_values[f].replace("$", ""))[-3:-2] =="." else (data_values[f].replace("$", "")).replace(".",""),(data_values[a].replace("+", "")).replace("%","")])    
                l+=5
                v+=5
                f+=5
                a+=5
                p+=1
            driver.close()
            global errorcounter
            errorcounter=0
            print("pangolin bitti")
        except:
            print("pangolin listesi oluşturulamadı")
            driver.close()
            errorcounter+=1
            if(errorcounter<5):
                pangolinlistSwap()
            errorcounter=0
    except:
        print("pangolin çalışmadı")
def pancakelistSwap():
    try:
        print("pancakeswap başladı")
        pair = list()
        data_values = list()
        def looper():
                WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".sc-iRbamj.bowFDd")))
                time.sleep(2)
                name = driver.find_elements_by_css_selector(".sc-iRbamj.bowFDd")
                values = driver.find_elements_by_css_selector(".sc-jhAzac.iggPaB.css-4cffwv")
                for i in name:
                    pair.append(i.text)
                for i in values:
                    data_values.append(i.text)
        exchange= "pancakeswap"
        driver = webdriver.Chrome('/home/tufan/Desktop/DefiProject/DefiProject/chromedriver')
        url="https://pancakeswap.info/pairs"
        driver.get(url)
        try:  
            looper()
            # driver.find_element_by_css_selector(".sc-gipzik.kLOwjF").click()
            # looper()
            l=0
            v=1
            f=3
            a=4
            p=0
            while (a<=len(data_values)):
                        pancake_list.append([exchange,pair[p],(data_values[l].replace("$", "")).replace(",", ""),(data_values[v].replace("$", "")).replace(",", ""),(data_values[f].replace("$", "")).replace(",", ""),(data_values[a].replace("+", "")).replace("%","")])
                        l+=5
                        v+=5
                        f+=5
                        a+=5
                        p+=1
            driver.close()
            global errorcounter
            errorcounter=0
            print("pancakeswap bitti")
        except:
            print("pancakeswap listesi oluşturulamadı")
            driver.close()
            errorcounter+=1
            if(errorcounter<5):
                pancakelistSwap() 
            errorcounter=0
    except:
        print("pancakeswap çalışmadı")
def mdexlistSwap():
    try:
        print("mdexswap başladı")
        pair = list()
        data_values = list()
        exchange= "mdex"
        driver = webdriver.Chrome('/home/tufan/Desktop/DefiProject/DefiProject/chromedriver')
        url="https://bsc-info.mdex.com/#/pairs"
        driver.get(url)
        def looper():
                    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".sc-gPEVay.gLawMS")))
                    time.sleep(2)
                    name = driver.find_elements_by_css_selector(".sc-gPEVay.gLawMS")
                    values = driver.find_elements_by_css_selector(".sc-VigVT.dNgKCa div")
                    for i in name:
                        pair.append(i.text)
                    for i in values:
                        data_values.append(i.text)
        
        try:    
            looper()
            driver.find_element_by_css_selector(".sc-jlyJG.fBsklp").click()
            looper()
            l=0
            v=2
            f=6
            a=8
            p=0
            while (a<=len(data_values)):
                        mdex_list.append([exchange,pair[p],(data_values[l].replace("$", "")).replace(",", ""),float(((data_values[v].replace("$", "")).replace(",", "")).replace("m",""))*1000000 if ((data_values[v].replace("$", "")).replace(",", ""))[-1:]=="m" else float(((data_values[v].replace("$", "")).replace(",", "")).replace("b",""))*1000 if ((data_values[v].replace("$", "")).replace(",", ""))[-1:]=="b" else (data_values[v].replace("$", "")).replace(",", ""),float(((data_values[f].replace("$", "")).replace(",", "")).replace("m",""))*1000000 if ((data_values[f].replace("$", "")).replace(",", ""))[-1:]=="m" else float(((data_values[f].replace("$", "")).replace(",", "")).replace("b",""))*1000 if ((data_values[f].replace("$", "")).replace(",", ""))[-1:]=="b" else (data_values[f].replace("$", "")).replace(",", ""),(data_values[a].replace("+", "")).replace("%","")])
                        l+=11
                        v+=11
                        f+=11
                        a+=11
                        p+=1
            driver.close()
            global errorcounter
            errorcounter=0
            print("mdex bitti")
        except:
            print("mdex listesi oluşturulamadı")
            driver.close()
            errorcounter+=1
            if(errorcounter<5):
                mdexlistSwap()
            errorcounter=0
    except:
        print("mdex çalışmadı")          
def julistSwap():
    try:
        print("julswap başladı")
        pair = list()
        data_values = list()
        def looper():
            WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".sc-kcbnda.dcPXpm.css-1n3zwju a div")))
            time.sleep(2)
            name = driver.find_elements_by_css_selector(".sc-kcbnda.dcPXpm.css-1n3zwju a div")
            values = driver.find_elements_by_css_selector(".sc-kcbnda.dcPXpm.css-4cffwv")
            for i in name:
                pair.append(i.text)
            for i in values:
                data_values.append(i.text)
        exchange= "julswap"
        driver = webdriver.Chrome('/home/tufan/Desktop/DefiProject/DefiProject/chromedriver')
        url="https://info.julswap.com/home"
        driver.get(url)
        try:
            looper()
            driver.find_element_by_css_selector(".sc-imABML.fKZlSM").click()
            looper()
            j=0
            while j<=5:
                driver.find_element_by_css_selector(".sc-hUfwpO.fvrRCk div:nth-child(3) div").click()
                looper()
                j+=1
            l=0
            v=1
            f=3
            a=4
            p=0
            while (a<=len(data_values)):
                julswap_list.append([exchange,pair[p],data_values[l].replace("$", "") if (data_values[l].replace("$", ""))[-3:-2] =="." else (data_values[l].replace("$", "")).replace(".",""),(data_values[v].replace("$", ""))[:-1] if (data_values[v].replace("$", ""))[-3:-2] =="." else (data_values[v].replace("$", "")).replace(".",""),(data_values[f].replace("$", ""))[:-1] if (data_values[f].replace("$", ""))[-3:-2] =="." else (data_values[f].replace("$", "")).replace(".",""),(data_values[a].replace("+", "")).replace("%","")])    
                l+=5
                v+=5
                f+=5
                a+=5
                p+=1
            driver.close()
            global errorcounter
            errorcounter=0
            print("julyswap bitti")
        except:
            print("julswap listesi oluşturulamadı")
            driver.close()
            errorcounter+=1
            if(errorcounter<5):
                julistSwap()
            errorcounter=0
    except:
        print("julswap çalışmadı")
def bakerylistSwap():
    try:
        print("bakeryswap başladı")
        pair = list()
        data_values = list()
        def looper():
            WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".sc-Rmtcm.gfMZds div a div")))
            time.sleep(2)
            name = driver.find_elements_by_css_selector(".sc-Rmtcm.gfMZds div a div")
            values = driver.find_elements_by_css_selector(".sc-jhAzac.ewmrIK.css-4cffwv")
            for i in name:
                pair.append(i.text)
            for i in values:
                data_values.append(i.text)
        exchange= "bakeryswap"
        driver = webdriver.Chrome('/home/tufan/Desktop/DefiProject/DefiProject/chromedriver')
        url="https://info.bakeryswap.org/#/home"
        driver.get(url)
        try:
            looper()
            j=0
            while j<=9:
                    driver.find_element_by_css_selector(".sc-jlyJG.fBMhOD div:nth-child(3) div").click()
                    looper()
                    j+=1
            l=0
            v=1
            f=3
            a=4
            p=0
            while (a<=len(data_values)):
                bakery_list.append([exchange,pair[p],data_values[l].replace("$", "") if (data_values[l].replace("$", ""))[-3:-2] =="." else (data_values[l].replace("$", "")).replace(".",""),(data_values[v].replace("$", ""))[:-1] if (data_values[v].replace("$", ""))[-3:-2] =="." else (data_values[v].replace("$", "")).replace(".",""),(data_values[f].replace("$", ""))[:-1] if (data_values[f].replace("$", ""))[-3:-2] =="." else (data_values[f].replace("$", "")).replace(".",""),(data_values[a].replace("+", "")).replace("%","")])    
                l+=5
                v+=5
                f+=5
                a+=5
                p+=1
            driver.close()
            global errorcounter
            errorcounter=0
            print("bakeryswap bitti")
        except:
            print("bakeryswap listesi oluşturulamadı")
            driver.close()
            errorcounter+=1
            if(errorcounter<5):
                bakerylistSwap()
            errorcounter=0
    except:
        print("bakeryswap çalışmadı")
def linklistSwap():
    try:
        print("linkswap başladı")
        pair = list()
        data_values = list()
        def looper():
            WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".sc-iRbamj.bowFDd")))
            time.sleep(2)
            name = driver.find_elements_by_css_selector(".sc-iRbamj.bowFDd")
            values = driver.find_elements_by_css_selector(".sc-jhAzac.cVBsLB.css-4cffwv")
            for i in name:
                pair.append(i.text)
            for i in values:
                data_values.append(i.text)
        exchange= "linkswap"
        driver = webdriver.Chrome('/home/tufan/Desktop/DefiProject/DefiProject/chromedriver')
        url="https://info.linkswap.app/pairs"
        driver.get(url)
        try:
            looper()
            driver.find_element_by_css_selector(".sc-gipzik.fPxmcZ").click()
            looper()
            l=0
            v=1
            f=3
            a=4
            p=0
            while (a<=len(data_values)):
                linkswap_list.append([exchange,pair[p],((data_values[l].replace("$", "")).replace(".", "")).replace(",", "."),((data_values[v].replace("$", "")).replace(".", "")).replace(",", "."),((data_values[f].replace("$", "")).replace(".", "")).replace(",", "."),(data_values[a].replace("+", "")).replace("%","")])
                l+=5
                v+=5
                f+=5
                a+=5
                p+=1
            driver.close()
            global errorcounter
            errorcounter=0
            print("linkswap bitti")
        except:
            print("linkswap listesi oluşturulamadı")
            driver.close()
            errorcounter+=1
            if(errorcounter<5):
                linklistSwap()
            errorcounter=0
    except:
        print("linkswap çalışmadı")
def uniswaplistSwap():#bazı datalar yanlış
    try:
        print("uniswap başladı")
        query = """query 
            {
            pairs{
            id
            volumeUSD
            reserveUSD
            token0 {
            
            symbol
            name
      
            }
            token1 {
            
            symbol
            name
            }
            } 
      }"""
        exchange="Uniswap" 
        url = 'https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2'
        r = requests.post(url, json={'query': query})
        json_data = json.loads(r.text)
        parced = json_data["data"]["pairs"]
        try:  
            for i in parced:
                    if float(i["volumeUSD"])!=0:
                        a=(float(i["volumeUSD"])*0.003)/(float(i["reserveUSD"]))*100
                        uniswap_list.append([exchange,i["token0"]["symbol"]+"/"+i["token1"]["symbol"],i["reserveUSD"],i["volumeUSD"],float(i["volumeUSD"])*0.003,a])
            print("uniswap bitti")   
        except:
            print("uniswap listesi oluşturulamadı") 
    except:
        print("uniswap çalışmadı")
def sushiswaplistSwap():#bazı datalar yanlış
    try:
            print("sushiswap başladı")
            query = """query 
                {
                pairs{
                id
                volumeUSD
                reserveUSD
                token0 {
                
                symbol
                name
        
                }
                token1 {
                
                symbol
                name
                }
                } 
        }"""
            exchange="Sushiswap" 
            url = 'https://api.thegraph.com/subgraphs/name/zippoxer/sushiswap-subgraph-fork'
            r = requests.post(url, json={'query': query})
            json_data = json.loads(r.text)
            parced = json_data["data"]["pairs"]
            try:
                for i in parced:
                
                    if float(i["volumeUSD"])!=0:
                        a=(float(i["volumeUSD"])*0.003)/float(i["reserveUSD"])*100
                        sushiswap_list.append([exchange,i["token0"]["symbol"]+"/"+i["token1"]["symbol"],i["reserveUSD"],i["volumeUSD"],float(i["volumeUSD"])*0.003,a])
                print("sushiswap bitti")   
            except:
                print("sushiswap listesi oluşturulamadı")            
    except:
        print("sushiswap çalışmadı")
def serumlistSwap():#apyler 0 olduğu için kaldırdım
    try:
        print("serumswap başladı")
        url = 'https://serum-api.bonfida.com/pools' 
        response = requests.get(url,timeout=10,headers={
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"})
        json_data= response.json()
        exchange = "Serum"
        try:
            for i in json_data["data"]:
                if float(i["volume"])!=0:
                    serum_list.append([exchange,i["name"],i["liquidity_locked"],i["volume"],i["fees"],float(i["apy"])*100])
            print("serumswap bitti")
        except:
            print("serumswap listesi oluşturulamadı")
    except:
        print("serumswap çalışmadı")
def apeswaplistSwap():
    try:
        print("apeswap başladı")
        pair = list()
        data_values = list()
        def looper():
                WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".sc-iRbamj.bowFDd")))
                time.sleep(2)
                name = driver.find_elements_by_css_selector(".sc-iRbamj.bowFDd")
                values = driver.find_elements_by_css_selector(".sc-jhAzac.iggPaB.css-4cffwv")
                for i in name:
                    pair.append(i.text)
                for i in values:
                    data_values.append(i.text)
        exchange= "apeswap"
        driver = webdriver.Chrome('/home/tufan/Desktop/DefiProject/DefiProject/chromedriver')
        url="https://info.apeswap.finance/pairs"
        driver.get(url)
        try:  
            looper()
            driver.find_element_by_css_selector(".sc-gipzik.Lgock").click()
            looper()
            l=0
            v=1
            f=3
            a=4
            p=0
            while (a<=len(data_values)):
                        apeswap_list.append([exchange,pair[p],(data_values[l].replace("$", "")).replace(",", ""),(data_values[v].replace("$", "")).replace(",", ""),(data_values[f].replace("$", "")).replace(",", ""),(data_values[a].replace("+", "")).replace("%","")])
                        l+=5
                        v+=5
                        f+=5
                        a+=5
                        p+=1
            driver.close()
            global errorcounter
            errorcounter=0
            print("apeswap bitti")
        except:
            print("apeswap listesi oluşturulamadı")
            driver.close()
            errorcounter+=1
            if(errorcounter<5):
                apeswaplistSwap()
            errorcounter=0
    except:
        print("apeswap çalışmadı")
DeFi()   
