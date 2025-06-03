import pyautogui as auto
import time

auto.PAUSE = 1.5

# Abre o Excel
time.sleep(5)
auto.press("win")
auto.write("Login.xlsx")
auto.press("backspace")
auto.press("enter")
time.sleep(10)
auto.click(x=996, y=293)

#Clicar no login e senha
time.sleep(5)
auto.click(x=242, y=206)
auto.write("RaphaelMacedo")
auto.click(x=213, y=225)
auto.write("Password")
auto.click(x=203, y=268)