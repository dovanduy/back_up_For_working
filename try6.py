from uiautomator import Device

d = Device('6b862e8')
d(resourceId='android:id/numberpicker_input', index=1)[0].set_text('1995')
