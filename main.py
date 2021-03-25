import requests
from bs4 import BeautifulSoup

URL = 'https://www.udemy.com/course/anti-money-laundering-aml-kyc/?ranMID=39197&ranEAID=ZVa%2FfYdMEMA&ranSiteID=ZVa_fYdMEMA-PY8x9TEqJZQStkwmnMfeEQ&LSNPUBID=ZVa%2FfYdMEMA&utm_source=aff-campaign&utm_medium=udemyads&couponCode=AMLMARCHXXV'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(class_='ud-component--course-landing-page-udlite--introduction-asset')

course_img=results.find(['img']).get('src')
course_title=soup.find(class_="udlite-heading-xl").text
course_sub_title=soup.find(class_="udlite-text-md").text
course_rating=soup.find(class_="styles--rating-wrapper--5a0Tr").text
students_enrolled=soup.find(class_="clp-component-render").text
requirements=soup.find(class_="unstyled-list udlite-block-list").text
description_1=soup.find(class_="udlite-text-sm styles--description--3y4KY").find_all('p')[0].text
description_2=soup.find(class_="udlite-text-sm styles--description--3y4KY").find_all('p')[1].text
description_3=soup.find(class_="udlite-text-sm styles--description--3y4KY").find_all('p')[2].text
description_4=soup.find(class_="udlite-text-sm styles--description--3y4KY").find_all('p')[3].text
audience=soup.find(class_="styles--audience__list--3NCqY").text
coupon=URL
# description_2=soup.find(class_="udlite-text-sm styles--description--3y4KY").findNext("p").get_text()

# am removing the word "description" from  the output from desciption and reassigninng it to the same ariable
course_dict={"course_img_url":[],"course_name":[],"course_sub":[],"course_rtn":[],"enrolled":[],"req":[],"des_1":[],"des_2":[],"des_3":[],"des_4":[],"audience":[],"coupon":[]};
course_dict["course_img_url"].append(course_img)
course_dict["course_name"].append(course_title)
course_dict["course_sub"].append(course_sub_title)
course_dict["course_rtn"].append(course_rating)
course_dict["enrolled"].append(students_enrolled)
course_dict["req"].append(requirements)
course_dict["des_1"].append(description_1)
course_dict["des_2"].append(description_2)
course_dict["des_3"].append(description_3)
course_dict["des_4"].append(description_4)
course_dict["audience"].append(audience)
course_dict["coupon"].append(coupon)










# remove_n=str(course_dict["course_name"])
# print(remove_n[4:-4])

# print(str.rstrip(str(course_dict["course_name"])))
print(course_dict)



# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict["year"])