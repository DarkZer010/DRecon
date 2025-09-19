import requests
from colorama import init, Fore
import os
import sys
from urllib.parse import urlparse

init()

def subpastasAuto():
	try:
		os.system("cls" if sys.platform == "win32" else "clear")
		
		try:
			dominio = input(Fore.RED+"Digite o domínio: ")
			
			def validar_url():
				try:
					result = urlparse(dominio)
					return all([result.scheme, result.netloc])
				
				except ValueError:
					return False
				
			validar_url()
			
			subpastas = ["admin", "www", "blog", "shop", "Robots.txt", "admin/uploads", "index.php", "js", "passwords", "usernames", "downloads", "json", "backup", "config", "logs", "tmp"]
			
			for subpasta in subpastas:
				url = f"http://{dominio}/{subpasta}"
				
				response = requests.get(url)
				if response.status_code == 200:
					print(Fore.GREEN+f"\nSubpasta encontrada: {url}")
			
		except requests.exceptions.RequestException as e:
			 print(f"Erro ao testar {url}: {e}")
		     
	except KeyboardInterrupt:
	       print(Fore.RED+"Saindo...")
        
subpastasAuto()  
