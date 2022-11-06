import ssl
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random
import string
import time
import os
import json
from colorama import Fore, Back, Style



# clear the screen
def clear():
    print()
    os.system('cls' if os.name == 'nt' else 'clear')


# Create a random string
def randomString(length):
    letters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters) for i in range(length))




def main():
    time.sleep(1)
    clear()
    banner = f"""{Fore.LIGHTRED_EX}
    
    ██████╗░░█████╗░██████╗░██╗░░░░░░█████╗░██╗░░██╗  ░██████╗░███████╗███╗░░██╗
    ██╔══██╗██╔══██╗██╔══██╗██║░░░░░██╔══██╗╚██╗██╔╝  ██╔════╝░██╔════╝████╗░██║
    ██████╔╝██║░░██║██████╦╝██║░░░░░██║░░██║░╚███╔╝░  ██║░░██╗░█████╗░░██╔██╗██║
    ██╔══██╗██║░░██║██╔══██╗██║░░░░░██║░░██║░██╔██╗░  ██║░░╚██╗██╔══╝░░██║╚████║
    ██║░░██║╚█████╔╝██████╦╝███████╗╚█████╔╝██╔╝╚██╗  ╚██████╔╝███████╗██║░╚███║
    ╚═╝░░╚═╝░╚════╝░╚═════╝░╚══════╝░╚════╝░╚═╝░░╚═╝  ░╚═════╝░╚══════╝╚═╝░░╚══╝

    >> {Fore.LIGHTCYAN_EX}Made By Imagine {Fore.LIGHTRED_EX}
    >> {Fore.LIGHTCYAN_EX}Version 1.4 {Fore.LIGHTRED_EX}
    >> {Fore.LIGHTCYAN_EX}Last Update: Better UI {Fore.LIGHTRED_EX}
    >> {Fore.LIGHTCYAN_EX}Current Update: Funcaptcha Bypass {Fore.LIGHTRED_EX}
    >> {Fore.LIGHTCYAN_EX}Next Update: Faster Generation --> Email Verification {Fore.LIGHTRED_EX}
    >> {Fore.LIGHTCYAN_EX}Generating {Fore.LIGHTRED_EX}{countz}{Fore.LIGHTYELLOW_EX} {jondor} {Fore.LIGHTCYAN_EX}Accounts{Fore.RESET}

    """
    print(banner)
    for i in range(countz):
        username1 = jujuname + "_" + randomString(5)
        options = Options()
        options.add_argument("log-level=3")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_extension("./solver.crx")
        driver = webdriver.Chrome(options=options)
        if byp_key == "" or " ":
            driver.get("https://www.roblox.com")
        else:
            driver.get(f'https://nopecha.com/setup#{byp_key}')
            time.sleep(1)
            driver.get("https://www.roblox.com")
        print(f"    {Fore.LIGHTGREEN_EX}Generating An Account With The Username: {Fore.LIGHTRED_EX}" + username1)
        month = driver.find_element(By.XPATH, "//select[@id='MonthDropdown']")  
        month.click()
        month.send_keys("January")
        day = driver.find_element(By.XPATH, "//select[@id='DayDropdown']")
        day.click()
        day.send_keys("1")
        year = driver.find_element(By.XPATH, "//select[@id='YearDropdown']")
        year.click()
        year.send_keys("2000")
        year.send_keys(Keys.RETURN)
        username = driver.find_element(By.XPATH, "//input[@id='signup-username']")
        username.click()
        username.send_keys(username1)
        password = driver.find_element(By.XPATH, "//input[@id='signup-password']")
        password.click()
        password.send_keys("ImagineOP@123")
        time.sleep(0.5)
        if gender == "m" or "M":
            driver.find_element(By.XPATH, "//button[@id='MaleButton']").click()
        else:
            driver.find_element(By.XPATH, "//button[@id='FemaleButton']").click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//button[@id='signup-button']").click()
        time.sleep(5)
        while driver.current_url != "https://www.roblox.com/home?nu=true":
            time.sleep(1)
        print(f"    {Fore.LIGHTCYAN_EX}Account Generated Successfully!")
        
        file = open("accounts.txt", "a")
        file.write(f"{username1}:ImagineOP@123\n")
        file.close()
        # print(driver.get_cookie(".ROBLOSECURITY"))
        with open("cookies.json", "a") as f:
            json.dump(driver.get_cookie(".ROBLOSECURITY"), f)
            f.write("\n")
        time.sleep(3)
        driver.quit()

def starter():
    global countz, jujuname, gender, byp_key, jondor
    countz = int(input(f"{Fore.LIGHTCYAN_EX}\n    How Many Accounts Do You Want To Create: {Fore.LIGHTRED_EX}"))
    time.sleep(0.5)
    jujuname = input(f"{Fore.LIGHTCYAN_EX}    Enter Username: {Fore.LIGHTRED_EX}")
    time.sleep(0.5)
    byp_key = input(f"{Fore.LIGHTCYAN_EX}    Enter Private Key (Leave Empty If None)\n    (Entering Random Letters Will Result In The Bypasser To Not Work Properly): {Fore.LIGHTRED_EX}")
    time.sleep(0.5)
    gender = input(f"{Fore.LIGHTCYAN_EX}    M for male | F for female (Enter Only One): {Fore.LIGHTRED_EX}")
    time.sleep(0.5)

    if gender == "m" or "M" or "f" or "F":
        print(f"{Fore.LIGHTCYAN_EX}    Starting... {Fore.RESET}")

        if gender == "m":
            jondor = "Male"
        elif gender == "M":
            jondor = "Male"

        elif gender == "f":
            jondor = "Female"
        elif gender == "F":
            jondor = "Female"
        
        main()
        input(f"    {Fore.LIGHTCYAN_EX}Press Enter To Exit...")
        exit()
    else:
        print(f"{Fore.LIGHTRED_EX}    Invalid! Please enter M or F")
        input(f"{Fore.LIGHTCYAN_EX}    Press Enter to continue...")
        time.sleep(1)
        clear()
        starter()


# check if name = main
if __name__ == "__main__":
    clear()
    starter()