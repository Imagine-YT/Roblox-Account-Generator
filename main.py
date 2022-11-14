import os
import time
import random
import string
import ctypes

from pystyle import *
from colorama import Fore
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


def clear():
    print()
    os.system('cls' if os.name == 'nt' else 'clear')

def getUsername():
    if rndd == "true":
        # get a random username from usernames.txt using random module
        with open("data/usernames.txt", "r") as f:
            user = random.choice(f.read().splitlines())
            username = user + ''.join(random.choice(string.digits) for i in range(4))
            return username
    else:
        return jujuname



error = f"    {Fore.LIGHTYELLOW_EX}[{Fore.LIGHTRED_EX}!{Fore.LIGHTYELLOW_EX}]{Fore.RESET}"


success = f"    {Fore.LIGHTYELLOW_EX}[{Fore.LIGHTGREEN_EX}+{Fore.LIGHTYELLOW_EX}]{Fore.RESET}"


info = f"    {Fore.LIGHTYELLOW_EX}[{Fore.LIGHTBLUE_EX}~{Fore.LIGHTYELLOW_EX}]{Fore.RESET}"

def main():
    global counter
    counter = 0
    time.sleep(1)
    clear()
    banner = Center.XCenter(Colorate.Vertical(Colors.cyan_to_green, """

    ██████╗░░█████╗░██████╗░██╗░░░░░░█████╗░██╗░░██╗  ░██████╗░███████╗███╗░░██╗
    ██╔══██╗██╔══██╗██╔══██╗██║░░░░░██╔══██╗╚██╗██╔╝  ██╔════╝░██╔════╝████╗░██║
    ██████╔╝██║░░██║██████╦╝██║░░░░░██║░░██║░╚███╔╝░  ██║░░██╗░█████╗░░██╔██╗██║
    ██╔══██╗██║░░██║██╔══██╗██║░░░░░██║░░██║░██╔██╗░  ██║░░╚██╗██╔══╝░░██║╚████║
    ██║░░██║╚█████╔╝██████╦╝███████╗╚█████╔╝██╔╝╚██╗  ╚██████╔╝███████╗██║░╚███║
    ╚═╝░░╚═╝░╚════╝░╚═════╝░╚══════╝░╚════╝░╚═╝░░╚═╝  ░╚═════╝░╚══════╝╚═╝░░╚══╝

"""))
    print(banner)
    print(Center.XCenter(f"""{Fore.LIGHTRED_EX}
    >> {Fore.LIGHTCYAN_EX}Made By Imagine {Fore.LIGHTRED_EX}
    >> {Fore.LIGHTCYAN_EX}Version 2.0 {Fore.LIGHTRED_EX}
    >> {Fore.LIGHTCYAN_EX}Last Update: Funcaptcha Bypass {Fore.LIGHTRED_EX}
    >> {Fore.LIGHTCYAN_EX}Current Update: Made The UI Better - Added New Features And Removed The Buggy Ones {Fore.LIGHTRED_EX}
    >> {Fore.LIGHTCYAN_EX}Next Update: IDK {Fore.LIGHTRED_EX}
    >> {Fore.LIGHTCYAN_EX}Generating {Fore.LIGHTRED_EX}{countz} {Fore.LIGHTCYAN_EX}Accounts{Fore.RESET}

    """))

    for i in range(countz):
        ctypes.windll.kernel32.SetConsoleTitleW(f"Roblox Account Generator By Imagine#5120 | {counter}/{countz} Accounts Generated")
        if rndd == "true":
            username1 = getUsername()
            # username1 = getUsername()
            amount_a = len(username1)
            if amount_a > 19:
                print(f"{error} {Fore.LIGHTRED_EX}Username is too long, skipping...{Fore.RESET}")
                driver.quit()
                continue
            else:
                pass
        else:
            how_many = len(jujuname)
            if how_many > 14:
                print(Center.XCenter(f"{error} {Fore.LIGHTRED_EX}Username is too long! (Max 14 Characters Allowed)"))
                input(Center.XCenter(f"{Fore.LIGHTCYAN_EX}Press Enter to continue..."))
                time.sleep(1)
                clear()
                starter()
            else:
                username1 = jujuname + "_" + ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(5))

        options = Options()
        options.add_argument("log-level=3")
        # options.add_argument("--headless")
        # options.add_argument("--proxy-server=http://149.6.162.2:9999")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_extension("data/solver.crx")
        driver = webdriver.Chrome(options=options)
        driver.get("https://www.roblox.com")
        time.sleep(1)
        try:
            if driver.find(By.XPATH, "//button[contains(text(),'Accept All')]").is_displayed == True:
                driver.find_element(By.XPATH, "//button[contains(text(),'Accept All')]").click()
            else:
                pass
        except:
            pass
        print(Center.XCenter(f"{info} {Fore.LIGHTGREEN_EX}Generating An Account With The Username: {Fore.LIGHTRED_EX}" + username1))
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

        rand = random.random()
        #print(rand)
        if rand < 0.5:
            driver.find_element(By.XPATH, "//button[@id='MaleButton']").click()
            print(Center.XCenter(f"{info} {Fore.LIGHTCYAN_EX}Random Gender: {Fore.LIGHTRED_EX}Male{Fore.LIGHTCYAN_EX} Account{Fore.RESET}"))
        else:
            driver.find_element(By.XPATH, "//button[@id='FemaleButton']").click()
            print(Center.XCenter(f"{info} {Fore.LIGHTCYAN_EX}Random: {Fore.LIGHTRED_EX}Female{Fore.LIGHTCYAN_EX} Account{Fore.RESET}"))
        time.sleep(0.5)
        try:
            driver.find_element(By.XPATH, "//button[@id='signup-button']").click()
            time.sleep(3)
        except:
            print(Center.XCenter(f"{error} {Fore.LIGHTRED_EX}Error: {Fore.LIGHTCYAN_EX}Signup Error!{Fore.RESET}"))
            print(Center.XCenter(f"{error} {Fore.LIGHTRED_EX}Error: {Fore.LIGHTCYAN_EX}Skipping Account...{Fore.RESET}"))
            driver.quit()
            continue
        time.sleep(3)
        try:
            if driver.find(By.XPATH, "//p[@id='signup-usernameInputValidation']").text == "This username is already in use.":
                print(Center.XCenter(f"{error} {Fore.LIGHTRED_EX}Error: {Fore.LIGHTCYAN_EX}Username Is Taken!{Fore.RESET}"))
                print(Center.XCenter(f"{error} {Fore.LIGHTRED_EX}Error: {Fore.LIGHTCYAN_EX}Skipping Account...{Fore.RESET}"))
                driver.quit()
                continue
            else:
                pass
        except:
            pass
        try:
            if driver.find_element(By.XPATH, "//div[@id='GeneralErrorText']").text == "Sorry! An unknown error occurred. Please try again later.":
                print(Center.XCenter(f"{error} {Fore.LIGHTRED_EX}Error: {Fore.LIGHTCYAN_EX}Rate Limit!{Fore.RESET}"))
                print(Center.XCenter(f"{error} {Fore.LIGHTRED_EX}Time To Take A Nap For About 45 Minutes...{Fore.RESET}"))
                driver.quit()
                t = 2800
                while t:
                    mins, secs = divmod(t, 60)
                    timer = f'{info} {Fore.LIGHTCYAN_EX}Time Remaining: {Fore.LIGHTYELLOW_EX}' + '{mins:02d}:{secs:02d}'.format(mins=mins, secs=secs)
                    print(Center.XCenter(timer), end="\r")
                    

                    time.sleep(1)
                    t -= 1
                continue
            else:
                pass
        except:
            pass
        while driver.current_url != "https://www.roblox.com/home?nu=true":
            time.sleep(1)
        print(Center.XCenter(f"{success} {Fore.LIGHTCYAN_EX}Account Generated Successfully --> {Fore.LIGHTBLUE_EX}Username: {Fore.LIGHTRED_EX}{username1}"))
        counter += 1
        ctypes.windll.kernel32.SetConsoleTitleW(f"Roblox Account Generator By Imagine#5120 | {counter}/{countz} Accounts Generated")

        file = open("results/accounts.txt", "a")
        file.write(f"{username1}:ImagineOP@123\n")
        file.close()
        with open("results/cookies.txt", "a") as f:
            f.write(f'{driver.get_cookie(".ROBLOSECURITY")["value"]}\n')
        time.sleep(3)
        driver.quit()

def starter():
    ctypes.windll.kernel32.SetConsoleTitleW(f"Roblox Account Generator By Imagine#5120")
    global countz, jujuname, jondor, rndd#, byp_key
    print("\n")
    try:
        countz = int(input(Center.XCenter(f"{Fore.LIGHTCYAN_EX}How Many Accounts Do You Want To Create: {Fore.LIGHTRED_EX}")))
    except:
        print(Center.XCenter(f"{error} {Fore.LIGHTRED_EX}Please Enter A Valid Number!"))
        input(Center.XCenter(f"{Fore.LIGHTCYAN_EX}Press Enter to continue..."))
        time.sleep(1)
        clear()
        starter()
    time.sleep(0.5)
    rnd_usernam = input(Center.XCenter(f"{Fore.LIGHTCYAN_EX}Do You Want To Use Random Username? (Y/N): {Fore.LIGHTRED_EX}"))
    time.sleep(0.5)
    if rnd_usernam == "y" or rnd_usernam == "Y":
        rndd = "true"
    elif rnd_usernam == "n" or rnd_usernam == "N":
        rndd = "false"        
        jujuname = input(Center.XCenter(f"{Fore.LIGHTCYAN_EX}Enter Username: {Fore.LIGHTRED_EX}"))
        time.sleep(0.5)
    else:
        print(Center.XCenter(f"{error} {Fore.LIGHTRED_EX}Please Enter A Valid Option!"))
        input(Center.XCenter(f"{Fore.LIGHTCYAN_EX}Press Enter to continue..."))
        time.sleep(1)
        clear()
        starter()
    # byp_key = input(Center.XCenter(f"{Fore.LIGHTCYAN_EX}Enter Private Key (enter N if none)\n(Entering Random Letters Will Result In The Bypasser To Not Work Properly): {Fore.LIGHTRED_EX}"))
    time.sleep(0.5)

    print(Center.XCenter(f"{info} {Fore.LIGHTCYAN_EX}Starting... {Fore.RESET}"))
    jondor = "Random"
    main()
    input(Center.XCenter(f"{Fore.LIGHTCYAN_EX}Press Enter To Exit..."))
    exit()


if __name__ == "__main__":
    clear()
    global counter
    counter = 0
    starter()
