from selenium import webdriver
from selenium.webdriver.support.select import Select
import requests
import time

purl = "https://www.instagram.com/cody_large/"
w =   '//*[@id="react-root"]/section/main/div/div[3]/article/div/div/div[1]/div[2]/a/div/div[1]'

# p =   '//*[@id="react-root"]/section/main/div/div[3]/article/div/div/div[1]/div[1]/a/div/div[1]/img'
#   //*[@id="react-root"]/section/main/div/div[3]/article/div/div/div[1]/div[2]/a/div/div[1]/img
#   //*[@id="react-root"]/section/main/div/div[3]/article/div/div/div[1]/div[1]/a/div/div[1]/img

# def t(n):
#     return '//*[@id="react-root"]/section/main/div/div[3]/article/div/div/div[1]/div[' + str(n) + '/a/div/div[1]/img'

url = "https://www.instagram.com/"

list = ['kristianbrusa',
'annika_beckk',
'phoebe__13',
'matt.kend',
'shruti.sridhar',
'anirit.bansal',
'elizabeth.slywka',
'zweeker',
'lizzy.drenckpohl',
'snfreeman1',
'andybazan',
'jessicachhay',
'maria.kallerson',
'keldonvaladez_',
'jacobmoon17',
'sarakathleen_',
'jack.larsen',
'dorneyy',
'keivinchavarin',
'uriiel.jiimenez',
'kylie.foltz',
'Taylor__bone',
'gian_herrera_',
'ashleystevenstonn_',
'michaelfouchjr',
'vshah_7',
'maya.khries',
'katie.christensenn',
'_kristinegilsrud',
'delgado_xo',
'arom.er',
'kalenaclaveria',
'matt_johnson_',
'niko_biros',
'flxprk',
'aimee_kauk_14',
'_.tylerheaton._',
'ava.anissipour',
'brandon__truong',
'shiro.strawberry',
'vishaalsharma',
'payton_noteboom',
'kaileysellars',
'karipage',
'rynnieroo',
'traviscgb13',
'gabbydang',
'rainmazumder',
'monicapottts',
'jordan_emonts',
'Jaida.frees',
'tucker_delong4',
'maddyyhoffman',
'anthony_tru17',
'reggie7_hamer',
'zombie_mad_hatter',
'maplebarsrule',
'kelseyhudson23',
'paxboyy',
'ella_simmons',
'andrew_tran1212',
'nigue.mik',
'alexresendez',
'arjun.v23',
'jasonaleta',
'jacoby_kim',
'garret_davis6',
'drewriegs',
'jaden_kainoa24',
'hannah.shull',
'tyralewiis',
'paty.armstrong',
'rishabh.jain__',
'jacksonsharkey',
'ashoogiewitdahoodie',
'mmegha.a',
'gabby.kepley',
'adrian_x_choi',
'rafael.cr68',
'brandonstride_',
'aneeshkarpoor',
'nikitarana_',
'sindhugundeti',
'_nickfoy_',
'daberechicohiri',
'megan.stoppler',
'paavni.patel',
'tyler_haas_',
'payton.locke',
'iamjoshbyron',
'javi.dc78',
'jhk_456',
'kyle_mumma',
'spamtheattack',
'manalzkhan',
'henrynxvi',
'the_tacosoros',
'jacktevers',
'nicholas.bellini',
'charmaine.yabut',
'khushi.dhanurkar',
'sahil0941',
'jemappellemoshope',
'cody_large',
'kashidha04',
'lexi_ducheane',
'jessica_clipper11',
'jadekeii',
'austinhalgren29',
'cassi.22',
'ballinbutters',
's.bellini22',
'lauren.trout',
'bitterly_sweet0',
'kxmmy.gxmez',
'amanda.nerby']

driver = webdriver.Edge()

for user in list:
    driver.get(url + user + '/')
    time.sleep(1)
    checkbox = driver.find_elements_by_tag_name("img")
    print(user)
    for i in  checkbox:
        print(i.get_attribute("src"))






#
# driver.get(purl)
#
# time.sleep(3)
#
# checkbox = driver.find_elements_by_tag_name("img")
# for i in  checkbox:
#     print(i.get_attribute("src"))
#
#

# img_src = checkbox.get_attribute("src")
# print(img_src)

# elements = driver.find_elements_by_xpath("//a[@class='poster ']")
# li = [["Name","Movie Title","Image"]]
# for i in  elements:
#     print (i.find_element_by_tag_name("img")) ##I am not sure how to get the URL
#     new_line= i.text.splitlines()
#     #print new_line[0] , " " , new_line[1]
#     li.append(new_line)
#
# print (li)

# i = 1
#
# print(t(i))
# checkbox = driver.find_element_by_xpath(p)
# m = checkbox.getAttribute("srcset")
#
# print(m)
# time.sleep(1.5)
# i += 1

# while True:
#     try:
#         checkbox = driver.find_element_by_xpath(t(i))
#         m = checkbox.getAttribute("srcset")
#         print(t(i))
#         print(m)
#         time.sleep(1.5)
#         i += 1
#     except:
#         break
#
#driver.close()
#driver.quit()



driver.close()
