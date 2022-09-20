#made by erfan sadeghi
# This Python file uses the following encoding: utf-8
from selenium import webdriver
from time import sleep,localtime
from os import system,path
from tkinter import *
from tkinter import messagebox
from threading import Thread

root = Tk()
root.minsize(600,400)
root.maxsize(600,400)
root.configure(bg='#189AB4')
root.title('Shad_bot')
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
#options.add_argument("--start-maximized")
options.add_argument('window-size=1000,1440')
try:
    driver = webdriver.Chrome(executable_path='chromedriver.exe',options=options)

except:
    messagebox.showerror('error','chromedriver \n سازگار نیست \n با توجه به نسخه کروم خود ان را دانلود کنید')
    system("start \"\" https://chromedriver.chromium.org/downloads")


def closs(): 
    sol = messagebox.askokcancel('exit','برنامه بسته شود ؟')
    if sol == True:
        with open('profile.txt','w',encoding='utf8') as fid:
            fid.write('')
            with open('profile.txt','a',encoding='utf8') as fiss:
                fiss.write(input_shomare.get()+':')
                for j in range(li.size()):
                    if li.get(j)!='':
                        fiss.write(li.get(j)+',')
        driver.quit()
        root.quit()
        exit()

#driver.set_window_position(-10000,0)
urlr = 'https://web.rubika.ir/#/login'
urls = 'https://web.shad.ir/#/login'


def tshoare():
    
    if radio.get()==2:
        driver.get(urlr)
    else:
        driver.get(urls)
    sleep(3)
    number = input_shomare.get()
    driver.find_element_by_name('phone_number').send_keys(number)
    if radio.get() == 2:
       driver.find_element_by_xpath('/html/body/app-root/tab-login/div/div/div[2]/div[1]/div/div[3]/button/div/div').click()
    else:
        driver.find_element_by_xpath("/html/body/div/app-root/tab-login/div/div[2]/div[1]/div/a").click()
    if radio.get() == 1:
        driver.find_element_by_xpath("/html/body/div/app-root/app-modal-container/div/app-modal-view/div/div/div/app-confirm-custom/div/div[2]/button[2]").click()
    payam.config(text='کد ارسال شد',fg='blue')
    code.pack()
    la1.pack()
    b_tcode.pack()
    b_tayid["state"] = "disabled"
    



def tcode():
    key = code.get()
    try:
        if radio.get() == 1:
            driver.find_element_by_xpath("/html/body/div/app-root/tab-login/div/div[2]/div[2]/form/div[4]/input").send_keys(key)
        else:
            driver.find_element_by_xpath("/html/body/app-root/tab-login/div/div/div[2]/div[2]/div/div[4]/div/input").send_keys(key)
    except:
        payam.config(text='!مشکلی به وجود امد',fg='red')
    sleep(4)
    if radio.get() == 2:
        driver.find_element_by_xpath("/html/body/app-root/div/div/div[1]/sidebar-container/div/sidebar-view/div/rb-chats/div[1]/div[1]/div[2]/div").click()
        sleep(1)
        driver.find_element_by_xpath("/html/body/div[2]/div[6]/div").click()
        driver.refresh()
    sleep(1)
    try:
        driver.find_element_by_partial_link_text('اعلانات ورود').click()
    except:
        payam.config(text='!مشکلی به وجود امد',fg='red')
    Label(text='نام دقیق شخص',bg='#189AB4').place(x=295,y=250)
    nameg.place(x=380,y=250)
    Label(text='پیام',bg='#189AB4').place(x=330,y=300)
    msag.place(x=380,y=300)
    ersal0.place(x=547,y=350)
    b_tcode["state"] = "disabled"
    payam.config(text='وارد حساب شدید',fg='blue')
    btersalname.place(x=190,y=360)
    b_ersalg.place(x=435,y=140)
    btn_music.place(x=500, y=180)
    btt.place(x=494,y=104)
    bbtt.place(x=507,y=60)
    b_import.place(x=42,y=94)
    input_shomare.config(state='disabled')
    code.config(state='disabled')

def import_name():
        for tag in range(1,8):
            try:
                d45 = driver.find_element_by_xpath('/html/body/div[1]/app-root/span/div[1]/div/rb-chats/div/div[2]/div/div[1]/ul[2]/li[{}]/a/div[3]/div[1]/span'.format(tag))
            except:                        
                sleep(0.5)
                break
            li.insert(END,d45.text)

def ersal():
    sleep(1)
    name = nameg.get()
    try:
        driver.find_element_by_partial_link_text(name).click()
    except:
        payam.config(text='نام صحیح نیست',fg='red')
    msg = msag.get()
    driver.find_element_by_xpath("/html/body/div[1]/app-root/span/div[1]/div/div/app-tab-container/app-tab-view/div[2]/tab-conversation/div/div[3]/div/div/div/form/div[3]/div[4]/div[2]").send_keys(msg +'.')
    sleep(1)
    driver.find_element_by_xpath("/html/body/div[1]/app-root/span/div[1]/div/div/app-tab-container/app-tab-view/div[2]/tab-conversation/div/div[3]/div/div/div/form/div[4]/button/span[1]").click()
    system('cls')
    driver.find_element_by_partial_link_text('اعلانات ورود').click()
    payam.config(text='پیام ارسال شد',fg='blue')

def ersalname():
    nameg.delete(0,END)
    nameg.insert(1, li.get(ACTIVE))

def appendlist():
    
    if appen.get().split() == []:
        messagebox.showerror('error','!ورودی خالی است')
    else:
        li.insert(END,appen.get())

            
def dellist():
    
    for i in range(li.size()):
        if li.get(i)==li.get(ACTIVE):
            li.delete(ACTIVE)

            
def ersalg():
    def ersalmsg():
        khata= 0
        txt = textmenu.get('1.0','end').strip().split('+')
        for i in txt:
            sleep(1)
            try :
                driver.find_element_by_partial_link_text(i).click()
            except:
                khata+=1
            try:
                driver.find_element_by_xpath("/html/body/div[1]/app-root/span/div[1]/div/div/app-tab-container/app-tab-view/div[2]/tab-conversation/div/div[3]/div/div/div/form/div[3]/div[4]/div[2]").send_keys(msgg.get() +'.')
            except:
                sleep(0.5)
            sleep(1)
            try:
                driver.find_element_by_xpath("/html/body/div[1]/app-root/span/div[1]/div/div/app-tab-container/app-tab-view/div[2]/tab-conversation/div/div[3]/div/div/div/form/div[4]/button/span[1]").click()
            except:
                sleep(0.5)
            driver.find_element_by_xpath("/html/body/div[1]/app-root/span/rb-head/div/div/div[1]/div/a").click()
        if khata!=0:
           peygham.config(text='{}!پیام ارسال نشد'.format(khata),fg='red') 
        else:
            peygham.config(text='پیام ها ارسال شد',fg='blue')

    top1 = Toplevel(root)
    top1.configure(bg='#B98853')
    top1.title('send_Message')
    top1.minsize(600,400)
    top1.maxsize(600,400)
    textmenu = Text(top1,height=10,width=40,bg='#DADADE')
    textmenu.place(x=1,y=1)
    msgg = Entry(top1,font=('bnazanin',21),bg='#DADADE')
    msgg.place(x=3,y=200)
    btg = Button(top1,text='ارسال',font=('bnazanin',26),command=ersalmsg,bg='#442E26').place(x=270,y=300)
    Label(top1,text='!توجه اگر نام اشتباه نوشته شود پیام ارسال نمیشود',fg='#442E26',bg='#B98853').place(x=350,y=150)
    Label(top1,bg='#B98853',font=('bnazanin',14),text='برای فرستادن پیام برای چند نفر \nلطفا در کادر مقابل اسم افراد را\n به صورت دقیق بنویسید\n برای جدا کردن نام از + استفاده کنید\nبرای مثال:علی+حسین+احسان').place(x=350,y=1)
    Label(top1,bg='#B98853',text='متن پیام',font=('bnazanin',20)).place(x=340,y=200)
    peygham = Label(top1,text='فرم را پر کنید',fg='blue',bg='#B98853')
    peygham.place(x=0,y=370)



def ersaltime():
    def shoro():
        Thread(target=ersalt).start()
    def ersalt():
        rth = (int(spinh.get())*60+int(spinm.get()))-(localtime().tm_hour*60+localtime().tm_min)
        if rth<0:
            messagebox.showerror('error','!زمان را درست وارد کنید',parent=top2)
            
        elif rth >=0:
            while rth != 0:
                rth = (int(spinh.get())*60+int(spinm.get()))-(localtime().tm_hour*60+localtime().tm_min)
                timemande.config(text=('{}دقیقه مانده'.format(rth)))
                sleep(5)
            driver.find_element_by_partial_link_text(namet.get()).click()
            driver.find_element_by_xpath("/html/body/div[1]/app-root/span/div[1]/div/div/app-tab-container/app-tab-view/div[2]/tab-conversation/div/div[3]/div/div/div/form/div[3]/div[4]/div[2]").send_keys(matn.get() +'.')
            sleep(1)
            driver.find_element_by_xpath("/html/body/div[1]/app-root/span/div[1]/div/div/app-tab-container/app-tab-view/div[2]/tab-conversation/div/div[3]/div/div/div/form/div[4]/button/span[1]").click()            #driver.find_element_by_partial_link_text('اعلانات ورود').click()
            driver.find_element_by_partial_link_text('اعلانات ورود').click()
            timemande.config(text='پیام ارسال شد')
    def ersalnamet():
        namet.delete(0,END)
        namet.insert(1, lit.get(ACTIVE))
    top2 = Toplevel(root)
    top2.configure(bg='#2E5D4E')
    top2.title('send_Message')
    top2.minsize(600,400)
    top2.maxsize(600,400)
    Label(top2,text='نام گیرنده',fg='#DBD3D8',bg='#2E5D4E').pack()
    namet = Entry(top2,font=('bnazanin',21),bg='#94A6AB')
    namet.pack()
    Label(top2,text='پیام',fg='#DBD3D8',bg='#2E5D4E').pack()
    matn = Entry(top2,font=('bnazanin',21),bg='#94A6AB')
    matn.pack()
    Label(top2,text='ساعت',fg='#DBD3D8',bg='#2E5D4E').pack()
    spinh = Spinbox(top2, from_= 0, to = 24,bg='#94A6AB')
    spinh.pack()
    Label(top2,text='دقیقه',fg='#DBD3D8',bg='#2E5D4E').pack()
    spinm = Spinbox(top2, from_= 0, to = 60,bg='#94A6AB')
    spinm.pack()
    Button(top2,text='ارسال پیام',bg='#DBD3D8',font=('bnazanin',20),command=shoro).place(x=240,y=270)
    timemande = Label(top2,text='-+-+-',font=('bnazanin',20),bg='#2E5D4E',fg='#DBD3D8')
    timemande.place(x=250,y=200)
    lit = Listbox(top2,font=20,bg='#D4F1F4')
    lit.place(x=0,y=200)
    btersalnamet = Button(top2,text='قرار دادن نام',font=15,command=ersalnamet,bg='#DBD3D8')
    btersalnamet.place(x=5,y=150)
    with open('profile.txt',encoding='utf8') as file:
        fl = file.read()
        joda = fl.find(':')
        fl = fl[joda+1:]
        fl = fl.split(',')
    for i in fl:
        lit.insert(END,i)

def botn():
    def go():
        Thread(target=starts).start()
        
    def starts():
        
        rtm = (int(spinh.get())*60+int(spinm.get()))-(localtime().tm_hour*60+localtime().tm_min)

        if rtm<0:
            messagebox.showerror('error','!زمان را درست وارد کنید',parent=top3)
            
        elif rtm >=0:
            while rtm != 0:
                rtm = (int(spinh.get())*60+int(spinm.get()))-(localtime().tm_hour*60+localtime().tm_min)
                timemanden.config(text=('{}دقیقه مانده'.format(rtm)))
                sleep(5)

            x=0


            while x!=180 :
                
                for og in range(1,7):
                    try:
                        driver.find_element_by_xpath('/html/body/div[1]/app-root/span/div[1]/div/rb-chats/div/div[2]/div/div[1]/ul[2]/li[{}]/a/div[3]/div[2]/div/span[2]/span'.format(og)).click()
                    except:
                            sleep(0.5)
                    else:
                        
                        for of in range(1,50):
                            try:
                                driver.find_element_by_xpath('/html/body/div[1]/app-root/span/div[1]/div/div/app-tab-container/app-tab-view/div[2]/tab-conversation/div/div[2]/a').click()
                            except:
                                sleep(0.5)
                            for k in ['/div[2]','']:
                                try:                            
                                    driver.find_element_by_xpath('/html/body/div[1]/app-root/span/div[1]/div/div/app-tab-container/app-tab-view/div[2]/tab-conversation/div/div[2]/div[1]/div/div[1]/div[2]/div[{}]/div/div/div/div/div[2]{}/div/rb-message-media/div/rb-message-poll/div/div[3]/div/div/a/div[2]'.format(of,k)).click()
                                except:                             
                                    sleep(0.5)
                                else:
                                    timemanden.config(text='نظرسنجی پیدا شد',fg='green')
                                    sleep(3)
                        driver.find_element_by_partial_link_text('اعلانات ورود').click()
                timemanden.config(text='درحال جستجو نظرسنجی{}از180ثانیه'.format(x),fg='yellow',font=('',17))
                sleep(1)
                x+=1
            
            timemanden.config(text='-+-')

    top3 = Toplevel(root)
    top3.configure(bg='#A9A9E9')
    top3.title('bot_survey')
    top3.minsize(600,363)
    top3.maxsize(600,363) 
    Label(top3,text='ربات نظرسنجی ,اتوماتیک حاضر براتون میزنه \( ͡♥ ● ͡♥)/',bg='#A9A9E9',font=('',20)).pack()
    Button(top3,text='شروع',command=go,bg='#BFCBF6',font=('bnazanin',20)).pack()
    timemanden = Label(top3,text='+-+',bg='#A9A9E9',font=('bnazanin',20))
    timemanden.pack()
    Label(top3,text='ساعت',fg='#DBD3D8',bg='#2E5D4E').pack()
    spinh = Spinbox(top3, from_= 0, to = 24,bg='#94A6AB')
    spinh.pack()
    Label(top3,text='دقیقه',fg='#DBD3D8',bg='#2E5D4E').pack()
    spinm = Spinbox(top3, from_= 0, to = 60,bg='#94A6AB')
    spinm.pack()
    Label(top3,font=('',15),fg='white',bg='#A9A9E9',text='ابتدا زمان روشن شدن بات را مشخص کنید سپس شروع را بزنید\nدرهنگام اجرای بات از دیگر بخش ها استفاده نکنید\nبات در زمان مشخص شده شروع به چک کردن 4 مخاطب \nاول شما(بالاتر از همه) میکند و به مدت 3 دقیقه هر نظرسنجی \nکه مشاهده کند گزینه اول ان را میزند').place(x=80,y=230)

def music_find():
    top_music = Toplevel(root)
    top_music.configure(bg='#A9A9E9')
    top_music.title('bot_music')
    top_music.minsize(600,363)
    top_music.maxsize(600,363)


    def start_bot_music():
                for i in range(1,4):
                    try:
                        
                        chat = driver.find_element_by_xpath("/html/body/div[1]/app-root/span/div[1]/div/rb-chats/div/div[2]/div/div[1]/ul[2]/li[{}]/a/div[3]/div[2]/div/span[2]".format(i)).text
                        
                        if str(chat).find('find:') == 0:
                            driver.find_element_by_xpath("/html/body/div[1]/app-root/span/div[1]/div/rb-chats/div/div[2]/div/div[1]/ul[2]/li[{}]/a/div[3]/div[2]/div/span[2]".format(i)).click()
                            name_music = str(chat)[str(chat).find(":")+1 :]
                            
                            driver.find_element_by_xpath("/html/body/div[1]/app-root/span/div[1]/div/div/app-tab-container/app-tab-view/div[2]/tab-conversation/div/div[3]/div/div/div/form/div[3]/div[4]/div[2]").send_keys("درحال متصل شدن...")
                            driver.find_element_by_xpath("/html/body/div[1]/app-root/span/div[1]/div/div/app-tab-container/app-tab-view/div[2]/tab-conversation/div/div[3]/div/div/div/form/div[4]/button/span[1]").click()
                            driver.execute_script("window.open('about:blank', 'tab2');")
                            driver.switch_to.window(driver.window_handles[1])

                            url1 = "https://soundcloud.com/search/sounds?q={}".format(name_music)
                            url2 = "https://www.klickaud.co/"

                            driver.get(url1)

                            sleep(3)
                            try:
                                driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/div/div[2]/div/button[1]").click()
                            except:
                                sleep(0.1)
                            try:
                                link_music = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/div[3]/div/div/div/ul/li[2]/div/div/div/div[2]/div[1]/div/div/div[2]/a").get_attribute("href")
                            except:
                                sleep(3)
                                try:
                                    link_music = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/div[3]/div/div/div/ul/li/div/div/div/div[2]/div[1]/div/div/div[2]/a").get_attribute("href")
                                except:
                                    driver.switch_to.window(driver.window_handles[0])
                                    driver.find_element_by_xpath("/html/body/div[1]/app-root/span/div[1]/div/div/app-tab-container/app-tab-view/div[2]/tab-conversation/div/div[3]/div/div/div/form/div[3]/div[4]/div[2]").send_keys("اهنگ موردنظر پیدا نشد")
                                    driver.find_element_by_xpath("/html/body/div[1]/app-root/span/div[1]/div/div/app-tab-container/app-tab-view/div[2]/tab-conversation/div/div[3]/div/div/div/form/div[4]/button/span[1]").click()
                                    sleep(1)
                                    driver.find_element_by_partial_link_text('اعلانات ورود').click()
                                    return
                            driver.get(url2)
                            sleep(1)
                            driver.find_element_by_xpath("/html/body/section/div/div/div[1]/form/input[1]").send_keys(link_music)
                            sleep(1)
                            driver.find_element_by_xpath("/html/body/section/div/div/div[1]/form/input[3]").click()
                            
                            sleep(1)
                            name_full = driver.find_element_by_xpath("/html/body/section/div/div/div[1]/div/table/tbody/tr/td[2]")
                            name_full = name_full.text
                            
                            link_download = driver.find_element_by_xpath("/html/body/section/div/div/div[1]/div/div[3]/table/tbody/tr/td[2]/a").get_attribute('href')
                            
                            
                            driver.switch_to.window(driver.window_handles[0])
                            sleep(1)
                            driver.find_element_by_xpath("/html/body/div[1]/app-root/span/div[1]/div/div/app-tab-container/app-tab-view/div[2]/tab-conversation/div/div[3]/div/div/div/form/div[3]/div[4]/div[2]").send_keys(name_full)
                            driver.find_element_by_xpath("/html/body/div[1]/app-root/span/div[1]/div/div/app-tab-container/app-tab-view/div[2]/tab-conversation/div/div[3]/div/div/div/form/div[4]/button/span[1]").click()
                            
                            sleep(1)
                            driver.find_element_by_xpath("/html/body/div[1]/app-root/span/div[1]/div/div/app-tab-container/app-tab-view/div[2]/tab-conversation/div/div[3]/div/div/div/form/div[3]/div[4]/div[2]").send_keys(link_download)
                            driver.find_element_by_xpath("/html/body/div[1]/app-root/span/div[1]/div/div/app-tab-container/app-tab-view/div[2]/tab-conversation/div/div[3]/div/div/div/form/div[4]/button/span[1]").click()

                            sleep(1)
                            driver.find_element_by_partial_link_text('اعلانات ورود').click()

                    except:
                        print('error')
    Label(top_music,text='ربات جستجوگر موزیک ',bg='#A9A9E9',font=('',20)).pack()

        
    def start_music_find():
        Thread(target=start_bot_music).start()



    Button(top_music,text='شروع',bg='#BFCBF6', command=start_music_find , font=('bnazanin',20)).pack()
    Label(top_music,font=('',15),fg='white',bg='#A9A9E9',text='برای جستجو موزیک باید به اکانت خود پیام \n(find:Name_music)\nبفرستید به جای \nName_music \nنام اهنگ دلخواه خود را بنویسید\n بعد از ان گزینه شروع ربات را بزنید (توجه: این نسخه رایگان میباشد و\n فقط در هنگام زدن گزینه شروع ربات تا چند دقیقه بیشتر کار نمیکند\n برای گرفتن نسخه کامل به ایدی تلگرام :\n@gamerfan82\n پیام دهید)').place(x=30,y=120)


input_shomare = Entry(root,font=('bnazanin',20),bg='#D4F1F4')
la = Label(text='شماره تلفن',bg='#189AB4').pack()
input_shomare.pack()
b_tayid = Button(root,text='تایید شماره',command=tshoare,bg='#75E6DA')
b_tayid.pack()
la1 = Label(text='کد فعال سازی',bg='#189AB4')
code = Entry(root,font=('bnazanin',20),bg='#D4F1F4')
b_tcode = Button(root,text='تایید کد',command=tcode,bg='#75E6DA')
nameg = Entry(root,font=('bnazanin',20),bg='#D4F1F4')
msag = Entry(root,font=('bnazanin',20),bg='#D4F1F4')
ersal0 = Button(root,text='ارسال',font=30,command=ersal,bg='#75E6DA')

b_ersalg = Button(root,text='ارسال پیام به صورت گروهی',font=13,command=ersalg,bg='#75E6DA')

li = Listbox(root,font=20,bg='#D4F1F4')
li.place(x=0,y=200)
btersalname = Button(root,text='قرار دادن نام',font=15,command=ersalname,bg='#75E6DA')



mad = Label(root,text='Telegram:Gamerfan82',fg='#05445E',bg='#189AB4')
mad.place(x=280,y=370)

payam = Message(root,text='Made by:\nErfan\nsadeghi',fg='blue',bg='#189AB4')
payam.place(x=0,y=0)

appen = Entry(root,font=20,bg='#D4F1F4')
appen.place(x=0,y=170)
btappend = Button(root,text='افزودن به لیست',font=16,command=appendlist,bg='#75E6DA')
btappend.place(x=0,y=135)
Button(root,text='حذف از لیست',font=16,command=dellist,bg='#75E6DA').place(x=100,y=135)
b_import = Button(root,text='جستجو مخاطبین',font=('',13),command=import_name,bg='#75E6DA')

btt = Button(root,text='ارسال در زمان معین',bg='#75E6DA',command=ersaltime)
bbtt = Button(root,text='ربات نظرسنجی',command=botn,font=('bnazanin',12),bg='#75E6DA')
btn_music = Button(root, text="ربات موزیک(جدید)", bg='#75E6DA', command=music_find)

radio = IntVar() 
R2 = Radiobutton(root, text="شاد", variable=radio,bg='#189AB4' , value=1)  
R2.place(x=540,y=3)  

R3 = Radiobutton(root, text="روبیکا", variable=radio,bg='#189AB4', value=2)  
R3.place(x=540,y=33)  




with open('profile.txt',encoding='utf8') as file:
    fl = file.read()
    fl = fl[0:fl.find(':')]
    input_shomare.insert(END,fl)


with open('profile.txt',encoding='utf8') as file:
    fl = file.read()
    joda = fl.find(':')
    fl = fl[joda+1:]
    fl = fl.split(',')
for i in fl:
    li.insert(END,i)




root.protocol("WM_DELETE_WINDOW", closs)

root.mainloop()
