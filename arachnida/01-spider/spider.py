import os
from bs4 import *
import sys
import requests


def make_directory():
	try:
		dir_name = input("Veuillez entrer le nom du dossier dans lequel les images seront sauvegardées: ")
		os.mkdir(dir_name)
	except:
		print("ERREUR: un dossier avec un nom similaire existe déja")
		make_directory()
	






def main():
	#make_directory()
	dir_name = "./sa"
	url = input("Veuillez entrer l'url a partir de laquel les photos seront télechargées: ")
	try:
		requete = requests.get(url)
	except:
		print("L'URL fournie n'a pas pu être atteinte / est erronée")
		exit()
	soup = BeautifulSoup(requete.text, "html.parser")
	images = soup.find_all("img")
	#print(images)
	for image in images:
		i = 0
		try:
			image_link = image["src"]
			r = requests.get(url + image_link).content
			with open(f"{dir_name}/images{i+1}.jpg", "wb+") as f:
				f.write(r)
			i += 1
		except:
			pass


main()