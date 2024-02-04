import sys
import requests
import os
from bs4 import *

def folder_create(images):
	try:
		folder_name = input("Enter folder name: ")
		os.mkdir(folder_name)
	except:
		print("Folder already exists with that name")
		folder_create()
	
	download_images(images, folder_name)

def download_images(images, folder_name):

	count = 0

	print("Total" + len(images) + "Image found!")


	if len(images) != 0:
		for i, image in enumerate(images):
			try:
				image_link = image["data-srcset"]
			except:
				try:
					image_link = image["data-src"]
				except:
					try:
						image_link = image["data-fallback-src"]
					except:
						try:
							image_link = image["src"]
						except:
							pass
			try:
				r = requests.get(image_link).content
				try:
					r = str(r, "utf-8")
				except UnicodeDecodeError:
					with open(f"{folder_name}/images{i+1}.jpg", "wb+") as f:
						f.write(r)
					count += 1
			except:
				pass
		if count == len(images):
			print("All images downloaded")
		else:
			print(f"Total {count} Images Downloaded Out of {len(images)}")

def main(url):
	r = requests.get(url)

	soup = BeautifulSoup(r.text, "html.parser")

	images = soup.find_all("img")

	folder_create(images)



url = input("input url please:  ")
main(url)