# IPFSgur

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
**Video:**
[link here]()

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

## Screenshots
