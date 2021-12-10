#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
#
# Written by Chris Arceneaux
# GitHub: https://github.com/carceneaux
# Website: https://arsano.ninja
#
# Note: Script was tested on Ubuntu 20.04 headless
#
# Requirements:
#   - Python 3.9+
#       - selenium
#       - argparse
#   - Mozilla Firefox
#   - GeckoDriver - WebDriver for Firefox

"""
Python script for automating the download of the VSPC management agent install file.
"""

import os
import time
import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

def main():
    parser = argparse.ArgumentParser(description='Python script for automating the download of the VSPC management agent install file.')
    parser.add_argument('--vspc', '-v', type=str, required=True,
                        help='Veeam Service Provider Console [FQDN:port]. For example: "vspc.contoso.lab:1280"')
    parser.add_argument('--os', '-o', type=str, required=True,
                        choices=['windows', 'linux', 'macos'],
                        help='Management Agent Operating System')
    parser.add_argument('--company_id', '-c', type=str, required=True,
                        help='VSPC Company ID. For example: "cfc0080c-597c-476f-accd-e595d3954285"')
    parser.add_argument('--is_x86', '-x', type=bool, required=False, default=False,
                        help='Only valid for "windows" agent. Default is 64-bit: False')
    parser.add_argument('--validity_period', '-V', type=int, required=False, default=365,
                        help='Number of days credentials are valid in downloaded file. Default: 365 days')
    parser.add_argument('--username', '-u', type=str, required=True,
                        help='VSPC Username')
    parser.add_argument('--password', '-p', type=str, required=True,
                        help='VSPC Password')
    parser.add_argument('--directory', '-d', type=str, required=False, default=os.getcwd(),
                        help='Set default download directory: "/Users/chris/Downloads"')

    args = parser.parse_args()

    try:        
        # initializing chrome settings
        options = webdriver.FirefoxOptions()
        options.headless = True
        #options.add_argument("accept_untrusted_certs=true")
        options.set_preference("browser.download.folderList", 2)
        options.set_preference("browser.download.manager.showWhenStarting", False)
        options.set_preference("browser.download.dir", args.directory)
        options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")

        # initializing selenium
        url = "https://" + args.vspc
        browser = webdriver.Firefox(options=options)
        browser.get(url)

        # waiting until user/pass textboxes have loaded
        WebDriverWait(browser, 30).until(lambda x: x.find_element(By.XPATH, "//input[@type='text']"))

        # logging into vspc
        browser.find_element(By.XPATH, "//input[@type='text']").send_keys(args.username)
        browser.find_element(By.XPATH, "//input[@type='password']").send_keys(args.password)
        browser.find_element(By.CLASS_NAME, "vm-Button").click();

        # waiting until login process has completed
        WebDriverWait(browser, 30).until(lambda x: x.find_element(By.CLASS_NAME, "x-toolbar"))

        # generating download url - setting OS

        if(args.os == "windows"):
            url += "/Agent/DownloadAgent"
        elif(args.os == "linux"):
            url += "/Agent/DownloadLinuxAgent"
        elif(args.os == "macos"):
            url += "/Agent/DownloadMacAgent"
        else:
            raise Exception("OS-specified is not a valid version")

        # setting validity period (in days)
        url += f'?ValidPeriod={args.validity_period}'

        # setting 32-bit/64-bit (only applies to Windows)
        if(args.os == "windows"):
            url += f'&IsX86={args.is_x86}'

        # setting company id
        url += f'&CompanyId={args.company_id}'

        # accessing mgmt agent download url
        #print(url)  #for debugging purposes
        browser.get(url)

        # waiting until download confirmation box pops up
        WebDriverWait(browser, 30).until(lambda x: x.find_element(By.CLASS_NAME, "vm-Button"))

        # downloading mgmt agent
        browser.find_element(By.CLASS_NAME, "vm-Button").click();

        # waiting 60 seconds for the download to complete. a cleaner method would be to monitor the download directory for the file and wait until the download has been completed
        time.sleep(60)

    except Exception as err:
        browser.quit()
        raise Exception(err)

    finally:
        browser.quit()
        return 0

# Start program
if __name__ == "__main__":
    main()