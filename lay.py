from uiautomator import Device


d = Device('6b862e8')
#username = "AlanKHaar@protonmail.com"
password = "vufdv93p5ppb" 
#d(text="Username").set_text(username)
#d(resourceId="ch.protonmail.android:id/password").set_text(password)
d(text="Sign In").click()
d(text="确定").click()

