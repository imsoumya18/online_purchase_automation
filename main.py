from selenium import webdriver
import time

# Taking username & password as input
user = input('Enter username: ')
pswd = input('Enter password: ')

# Loading the driver
driver = webdriver.Chrome('chromedriver.exe')

driver.get('https://www.shopmaster.com/order/index.html?state=to-purchase')

driver.find_element_by_xpath("//button[contains(text(),'OK')]").click()
driver.find_element_by_id('username').send_keys(user)
driver.find_element_by_id('password').send_keys(pswd)
driver.find_element_by_xpath("//button[contains(text(),'Login')]").click()
time.sleep(20)
driver.find_element_by_xpath("//option[contains(text(),'300')]").click()
time.sleep(20)
x = len(driver.find_elements_by_xpath("//section[@class='order_item orderItem']"))
k = 0
for j in range(x):
    i = driver.find_elements_by_xpath("//section[@class='order_item orderItem']")[k]
    if float(i.find_element_by_class_name('ml_5').text[3:]) < 65:
        price = i.find_element_by_class_name('ml_5').text
        if len(i.find_elements_by_class_name('max_w70')) == 1:
            if i.find_element_by_class_name('smicon_insert_drive_file').get_attribute(
                    'data-content') == 'Add an internal note':
                try:
                    i.find_element_by_class_name('message_icon')
                    k += 1
                except:
                    i.find_element_by_class_name('btn_sm_orange').click()
                    time.sleep(20)
                    try:
                        i.find_element_by_class_name('error_info')
                        i.find_element_by_xpath('/html/body/div[24]/div[2]/div/div[2]/div[2]/button[1]').click()
                        time.sleep(15)
                        k += 1
                    except:
                        try:
                            i.find_element_by_xpath("//a[contains(text(), 'What should I do?')]")
                            i.find_element_by_xpath('/html/body/div[24]/div[2]/div/div[2]/div[2]/button[1]').click()
                            time.sleep(15)
                            k += 1
                        except:
                            i.find_element_by_xpath("//a[contains(text(), 'Notes')]").click()
                            i.find_element_by_xpath("//textarea[@name='inputTallyName']").clear()
                            i.find_element_by_xpath("//textarea[@name='inputTallyName']").send_keys(
                                '\n*** DROPSHIP ***\n- PLEASE REMOVE QR CODES AND MARKETING\n- SHIP TODAY SO WE ORDER MORE. '
                                'THANK YOU\n\n*** IMPORTANT CUSTOMS INFORMATION ***\n\nPlease declare customs value: ' +
                                price + '\n\nIf you have questions contact us')
                            i.find_element_by_xpath("//button[@name='purchaseBtn']").click()
                            time.sleep(20)
                            i.find_element_by_xpath("//button[@name='closeBtn']").click()
                            time.sleep(15)
            else:
                k += 1
        else:
            k += 1
    else:
        k += 1
