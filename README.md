# IPFSgur

![web homepage](https://i.imgur.com/BQoj7pg.png)
<a href="https://asciinema.org/a/555433" target="_blank"><img src="https://asciinema.org/a/555433.svg" /></a>  
# [web demo video](https://vimeo.com/793806077)  
## [hosted demo](https://myipfsgur.pythonanywhere.com/)  

A decentralised, censorship-resistant image hosting service using IPFS and Filecoin (web3.storage).  

This project consists of an API and two frontends for that API - a CLI and a web frontend. Both are built to perform three operations: `upload`, `fetching` and `homepage view`. Users can upload an image and an IPFS content-ID is returned for that image. For the CLI, the homepage is loaded as previews of the images as ASCII art, along with their CIDs.  

**Why IPFS?**  
IPFS (Inter-Planetary File System) is  
>A peer-to-peer hypermedia protocol
>designed to preserve and grow humanity's knowledge
>by making the web upgradeable, resilient, and more open.  

Read more [here](https://ipfs.tech).  

## Features
- Decentralised
- Minimalist
- Cross platform

---

## Installation and Usage
* CLI  
Download the latest binary release (currently available only for Linux) from the Github releases page, then:
```
chmod +x ipfsgur
./ipfsgur help
```

* Web  
Hosted demo: [https://myipfsgur.pythonanywhere.com/](https://myipfsgur.pythonanywhere.com/)  

**Screenshots:**  
![upload page](https://i.imgur.com/8k93Ha8.png)
![find by CID page](https://i.imgur.com/OZqxRGR.png)

---

## Build Instructions for CLI
```
git clone https://github.com/s-m33r/ipfs-img
cd ipfs-img
cd cli2
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install pyinstaller
pyinstaller --onefile ipfsgur.py
chmod +x dist/ipfsgur
./dist/ipfsgur
```

## Authors
- [@s-m33r](https://www.github.com/s-m33r)  
- [@yashasnadigsyn](https://www.github.com/yashasnadigsyn)  
