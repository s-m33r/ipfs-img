# IPFSgur

![web homepage](https://i.imgur.com/BQoj7pg.png)
<a href="https://asciinema.org/a/555433" target="_blank"><img src="https://asciinema.org/a/555433.svg" /></a>

A decentralised, censorship-resistant image hosting app using IPFS and Filecoin (web3.storage).

## Features
- Decentralised
- Minimalist
- Cross platform

---

## Installation and Usage
* CLI  
Download the latest binary release from the Github releases page, then:
```
chmod +x ipfsgur
./ipfsgur help
```

* Web  
Hosted demo: [https://myipfsgur.pythonanywhere.com/](https://myipfsgur.pythonanywhere.com/)  
[demo video](https://vimeo.com/793806077)  
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
