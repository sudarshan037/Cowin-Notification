from appium import webdriver

"Setup for the test"
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4'
desired_caps['deviceName'] = '$ Your device name'
# Since the app is already installed launching it using package and activity name
desired_caps['appPackage'] = 'atpwta.live'
desired_caps['appActivity'] = '.activity.Main'
# Adding appWait Activity since the activity name changes as the focus shifts to the ATP WTA app's first page
desired_caps['appWaitActivity'] = '.activity.root.TournamentList'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(30)