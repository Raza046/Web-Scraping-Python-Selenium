from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import csv


def HomePage():

    driver = webdriver.Chrome(executable_path="C:/Users/AMS Enterprises/Downloads/chromedriver.exe")

    driver.get("https://www.letsgocaravanandcamping.com.au/find-a-dealer/")

    print( "The title is  : " + driver.title)


    states = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[2]/div[3]/a[1]')

    with open('output.csv', 'w', newline='') as csvfile:
        field_names = ['States', 'Place', 'Details']
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writerow({'States':'States', 'Place':'Place','Details':'Details'})


#        all_states = driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "state-map-v3", " " ))]//a')

        all_states = driver.find_element_by_css_selector('.state-map-v3 a')
        all_urls = [ all_states.get_attribute('href') for all_states in driver.find_elements_by_css_selector('.state-map-v3 a') ]

        # for lakes in all_urls:

        #     driver.get(lakes)

        all_states.click()

        print( "This is the STATE : " + all_states.text )
        writer.writerow({'States':all_states.text})


        links = driver.find_elements_by_css_selector('.active a')

        links1 = [links.get_attribute('href') for links in driver.find_elements_by_css_selector('.active a')]


        for l1 in links1:
                
            driver.get(l1)
                    
            datas = driver.find_elements_by_xpath('//div[@class="dealer-item-text"]/a[1]')
            data1 = len(datas)
            
            all_links1 = [datas.get_attribute('href') for datas in driver.find_elements_by_xpath('//div[@class="dealer-item-text"]/a[1]')]


            for all_link in all_links1:
                    
                driver.get(all_link)
                    
                print("DEALERS : " + driver.title)

                texts = driver.find_elements_by_xpath('//dd | //*[contains(concat( " ", @class, " " ), concat( " ", "content_area", " " ))]//p')

                t = len(texts)
            
                for txt in range(t):

                    print(texts[txt].text)

                writer.writerow({'Place':driver.title, 'Details':texts[txt].text })


HomePage()
