import pyautogui
import time
import random
import os


def open_file_in_pycharm(file_path):
    # Opens file in default editor (ensure PyCharm is set as default for .py)
    os.system(f'start "" "{file_path}"')
    time.sleep(3)  # Wait for file to open


def type_code():
    code_snippets = [

        "for char in mailboxes[sequenceFromEmail]:\n"
        "            email_id.send_keys(char)\n"
        "            time.sleep(random.uniform(0.1, 0.5))\n"
        "        password = driver.find_element(By.XPATH,\n"
        "                                       '/html/body/div[2]/div/div[3]/div/div/div[2]/div[2]/form/div[4]/input')\n"
        "        for char in 'FlareAI@2025':\n"
        "            password.send_keys(char)\n"
        "            time.sleep(random.uniform(0.1, 0.5))\n"
        "        # password.send_keys('FlareAI@2025')\n"
        "        time.sleep(random.uniform(5, 10))\n"
        "        login = driver.find_element(By.XPATH,\n"
        "                                    '/html/body/div[2]/div/div[3]/div/div/div[2]/div[2]/form/div[5]/div/button')\n"
        "        login.click()\n"
        "        time.sleep(random.uniform(5, 10))\n"
        "        try:\n"
        "            openButton = driver.find_element(By.XPATH,\n"
        "                                             '/html/body/div[1]/div/div/section[1]/div/div[1]/div/div/button')\n"
        "            openButton.click()\n"
        "            time.sleep(random.uniform(5, 10))\n"
        "        except:\n"
        "            try:\n"
        "                driver.find_element(By.ID, 'launchActiveButton').click()\n"
        "            except:\n"
        "                pass\n"
        "            time.sleep(random.uniform(5, 10))\n"
        "finally:\n"
        "            compose = driver.find_element(\n"
        "                By.XPATH, '/html/body/div[1]/div[1]/div[2]/span[1]/a')\n"
        "            compose.click()\n"
        "            time.sleep(random.uniform(5, 10))\n"
        "            toMail = driver.find_element(By.XPATH,\n"
        "                                         '/html/body/div[1]/div[3]/div[2]/form/div[1]/div/div[2]/div/div/ul/li/input')\n"
        "            toMail.click()\n"
        "            toMail.send_keys(row['Email ID'])\n"
        "            # toMail.send_keys('yaswanthnelavai@gmail.com')\n"
        "            toMail.send_keys(Keys.TAB)\n"
        "            time.sleep(random.uniform(5, 10))\n"
        "            subject = driver.find_element(By.XPATH,\n"
        "                                          '/html/body/div[1]/div[3]/div[2]/form/div[1]/div/div[7]/div/input')\n"
        "            subject.click()\n"
        "            subject.send_keys(row['Subject'])\n"
        "            time.sleep(random.uniform(5, 10))\n"
        "            try:\n"
        "                mailBodyTextToHTML = driver.find_element(By.XPATH,\n"
        "                                                         '/html/body/div[1]/div[3]/div[2]/form/div[2]/div/a')\n"
        "                mailBodyTextToHTML.click()\n"
        "                time.sleep(random.uniform(5, 10))\n"
        "            except:\n"
        "                print('Mail Body is already HTML')\n"
        "                logging.info('Mail Body is already HTML')\n"
    ]
    snippet = random.choice(code_snippets)
    pyautogui.typewrite(snippet, interval=random.uniform(0.1, 0.9))
    time.sleep(1)
    pyautogui.hotkey('ctrl', 's')  # Save file


def switch_tabs():
    pyautogui.hotkey('ctrl', 'tab')
    time.sleep(1)


def scroll_editor():
    pyautogui.scroll(random.randint(-10, 10))
    time.sleep(1)


def main():
    files = ["C:\\Users\\servi\\PycharmProjects\\AdityaColdEmail\\check.py",
             "C:\\Users\\servi\\PycharmProjects\\AdityaColdEmail\\multithreading.py"]

    while True:
        time.sleep(10)
        action = random.choice(["write", "scroll"])

        if action == "write":
            type_code()
        elif action == "scroll":
            scroll_editor()
        # Random intervals to mimic natural work
        time.sleep(random.randint(3, 6))


if __name__ == "__main__":
    main()
