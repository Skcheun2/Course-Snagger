import requests
import xml.etree.ElementTree as ET
from time import sleep
import datetime
import os
from pytz import timezone
import smtplib
import cookielib
#import mechanize
#import fbchat
#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#from getpass import getpass


def getWebPage(subj, crse, user, password):
    chromedriver = '/usr/bin/google-chrome'
    browser = webdriver.Chrome(chromedriver)
    browser.get('https://eas.admin.uillinois.edu/eas/servlet/EasLogin?redirect=https://webprod.admin.uillinois.edu/ssa/servlet/SelfServiceLogin?appName=edu.uillinois.aits.SelfServiceLogin&dad=BANPROD1')
    username = selenium.find_element_by_name("inputEnterpriseId")
    password = selenium.find_element_by_name("password")

    username.send_keys(user)
    password.send_keys(password)	
    

    #selenium.find_element_by_name("submit").click()
    #ret = browser.page_source
    arrow = driver.find_element_by_xpath('//div[@class="bttn" and @type="submit"]')
    arrow.click()
    return 1
   
"""
def getWebPage(subj, crse, user, password):
    br = mechanize.Browser()
    cj = cookielib.LWPCookieJar()
    br.set_cookiejar(cj)
    br.set_handle_equiv(True) 
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    br.addheaders = [('User-agent', 'Chrome')]
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
    br.open(
        'https://eas.admin.uillinois.edu/eas/servlet/EasLogin?redirect=https://webprod.admin.uillinois.edu/ssa/servlet/SelfServiceLogin?appName=edu.uillinois.aits.SelfServiceLogin&dad=BANPROD1')
    br.select_form(nr=0)
    br.form['inputEnterpriseId'] = user
    br.form['password'] = password
    br.submit()
    
   
    # debugging print response.read()
    br.open(
        'https://ui2web1.apps.uillinois.edu/BANPROD1/twbkwbis.P_GenMenu?name=bmenu.P_RegAgreementAdd')
    br.follow_link(nr=13)
    br.form['p_term'] = ['120181']
    br.open(br.form.click())

    forms = br.forms()
    forms.next()
    focus = forms.next()
    focus.set_value([subj], nr=13)

    page = ''
    br.open(focus.click(name='SUB_BTN'))
    for f in br.forms():
        if f.get_value(nr=0) == '120151' and f.get_value(
                name='SEL_CRSE') == str(crse):
            page = br.open(f.click()).read()
    return 1




"""


def check_open(dep,num,crn):
    url = 'http://courses.illinois.edu/cisapp/explorer/schedule/2018/spring/{}/{}/{}.xml'.format(dep,num,crn)
    r = requests.get(url)
    xml = r.text

    # For testing with localXML #
    # with open('test.xml', 'r') as xml:
    #     xml = xml.read()

    try:
        root = ET.fromstring(xml)
    except ET.ParseError:
        print("Class doesn't exist :(")
        return
    avail = root.find('enrollmentStatus').text
    if avail == "Closed" or avail == "UNKNOWN":
        return 0
    else:
        return 1



#fbchatresp= raw_input("Do you want notification through email, fbchat or both (input one of the choices): ") 


#if fbchatresp.lower() == 'both'
	
    #fbusername = raw_input("FB Username: ")
    #fbpass = raw_input("FB Password: ")
    #sendemail = raw_input("Email:")
    #emailpass = raw_input('Email Password: ')
    #receiver = raw_input('Recipient: ')
    #name = raw_input('Name (to look you up on fb chat): ')
    #details = {'email':sendemail,'password':emailpass,'recipient':receiver,'fbuser':fbusername,'fbpass':fbpass,'name':name}
#if fbchatresp.lower() == 'fbchat'
	
    #fbusername = raw_input("FB Username: ")
    #fbpass = raw_input("FB Password: ")
    #name = raw_input('Name (to look you up on fb chat): ')
    #details = {'fbuser':fbusername,'fbpass':fbpass,'name':name}

#if fbchatresp.lower() == 'email'
    #sendemail = raw_input("Email:")
    #emailpass = raw_input('Email Password: ')
    #receiver = raw_input('Recipient: ')
    #details = {'email':sendemail,'password':emailpass,'recipient':receiver}
    


#details = {'email':sendemail,'password':emailpass,'recipient':receiver,'fbuser':fbusername,'fbpass':fbpass,'name':name}
#details['name'] = details['name'].lower()

sendemail = raw_input("Email (Sender):")
emailpass = raw_input('Email Password: ')
receiver = raw_input('Recipient: ')
details = {'email':sendemail,'password':emailpass,'recipient':receiver}
num_of_courses = int(raw_input('Number of courses to check: '))
#num_of_courses = 1

#username = raw_input('Enterprise Username: ')
#password = raw_input('AD Password: ')


lst_of_course_depts = []
for x in range(num_of_courses):
    dept = raw_input('Department: ')
    lst_of_course_depts.append(dept)

lst_of_course_subjects = []
for x in range(num_of_courses):
    subj = raw_input('Course Number: ')
    lst_of_course_subjects.append(subj)

lst_of_course_crn = []
for x in range(num_of_courses):
    course_crn = raw_input('Course crn: ') 
    lst_of_course_crn.append(course_crn)


#fb message
#email
#text





def sendEmail(message):
    sender = details['email']
    password = details['password']
    recipient = details['recipient']
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, recipient, message)
    server.quit()

def sendFBmessage(message):
    
    client = fbchat.Client(details['fbuser'],details['fbpass'])
    friends = client.getUsers(details['name'])
    sent = client.send(friend.uid, message)
    if sent:
        print("Message sent successfully!")


while True:

    
    open('log.txt', 'w').close()
    course_open = 0
    

    
    f = open('log.txt', 'r+')
    logtext = ''
    while 1:
        
        print("Scraping")
	#here we will check the courses
        for x in range(num_of_courses):
            if check_open(lst_of_course_depts[x],lst_of_course_subjects[x],lst_of_course_crn[x]):
                if course_open ==0:                
		    course_open = 1
                #if fbchatresp.lower() == 'both':
                    sendEmail("Your class has opened.")
                    sendEmail(str(lst_of_course_crn[x] ))
                  #  sendFBmessage("Your class has opened.")
                 #   sendFBmessage(str(lst_of_course_crn[x] ))

                #if fbchatresp.lower() == 'fbchat':
                    #sendFBmessage("Your class has opened.")
                   # sendFBmessage(str(lst_of_course_crn[x] ))
                #if fbchatresp.lower() == 'email':
                 #   sendEmail("Your class has opened.")
                  #  sendEmail(str(lst_of_course_crn[x] ))
                
                    #k = getWebPage(lst_of_course_crn[x],lst_of_course_depts[x],username,password)
            else:
                if course_open == 1:
                    sendEmail("Your class has closed")
                 
                    
        f.write(logtext)
        f.flush()
        os.fsync(f.fileno())
        sleep(2)
    f.close()
