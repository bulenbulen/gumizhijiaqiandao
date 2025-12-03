
import getpass,time,os

from playwright.sync_api import sync_playwright

username = getpass.getuser()

newusercache=r"D:\DATA\chromeuserdata\User Data" #自定义路径 目标加--user-data-dir="D:\DATA\chromeuserdata\User 
#newusercache=r"D:\DATA\chromeuserdata\User Data"
userurl = "https://dnrclub.web.sdo.com/pc/#/post"  #地址

username=['Gniubmax','GniubiMin','GniubiAbs']
usernameurl='//html/body/div[3]/div[6]/div/div/div[1]/ul/li[{}]'


with sync_playwright() as p:
    browser = p.chromium.launch_persistent_context(
    #executable_path=bropath,
    user_data_dir=newusercache,
    channel="chrome",
    headless=False,
    args=['--start-maximized',# 最大化窗口
    #'--user_data_dir=D:\\DATA\\chromeuserdata\\User Data',
    '--profile-directory=Default'# 指定用户配置文件目录
    ],
    ignore_default_args=['--enable-automation'], #忽略自动化检测提示
    no_viewport=True,slow_mo=1000)
        #page = browser.new_page() #用新标签页，会有一页空白标签页
    page = browser.pages[0] #不添加新标签
    page.goto(userurl)

    page.pause()
    num = 7

    for i in range(1,num+1):
   
        page.locator('//html/body/div[1]/div/div[2]/section/aside/div[1]/div[1]/div/div[1]/div/div/div[1]/div/i').click() #换角色按钮
        
        page.click("text=请选择所在区")
        #page.wait_for_timeout(300)
        page.locator('//html/body/div[3]/div[4]/div/div/div[1]/ul/li[1]').click() #选择区
        #page.click("text=怀旧大区")
        #page.wait_for_timeout(500)
        #page.click("text=请选择角色")
        page.locator('//html/body/div[1]/div/div[3]/div/div/div/form/div[3]/div/div/div/div[1]/div[2]').click() #选择角色
        #page.wait_for_timeout(300)   
        #print( usernameurl.format(i)) 
        uname = page.locator(usernameurl.format(i)).inner_text()
        
        page.locator(usernameurl.format(i)).click()  #选择角色按顺序
    
        #page.click(f'text={username[0]}') #选择角色用角色名指定
        page.click("button:has-text(\"确认\")")
        
        page.goto(userurl)
        
        qdstauts=page.locator('//html/body/div[1]/div/div[2]/section/aside/div[1]/div[1]/div/div[2]/button').inner_text()  #获取签到状态
        if "已签到" in qdstauts:
            print(uname +"已签到")
            
            continue
        else:
            page.wait_for_timeout(800)
            page.reload()
            page.wait_for_timeout(800)
            page.click("button:has-text(\"签 到\")")
             #关闭按钮
            page.locator('//html/body/div[1]/div/div[2]/section/aside/div[2]/div/div/header/button').click()            
            print(uname + ' ' +"签到完成")
        
    print('完成签到')

    page.close()
        
    
    
    
