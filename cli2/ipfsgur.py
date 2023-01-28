import os
import json
import requests
from sys import argv
from hashlib import md5
import random
from mimetypes import guess_type

from rich.console import Console, OverflowMethod
from rich.prompt import Prompt, Confirm

from imgrender import render
from PIL import Image

API = "http://ipfsgur.pythonanywhere.com"
GATEWAY = "https://ipfs.io/ipfs"

console = Console()
error = Console( style="red bold" )

class Utils:

    help_text = """
IPFSgur CLI

OPTIONS:
    help - display this help text
    put  - upload a single file. returns an IPFS gateway link to the file
    get  - download an image from IPFS. also shows its preview in the terminsl

Default behaviour:
    Homepage - a list of ten most recent images on IPFSgur, rendered in the terminal along with links
    """

    def randomHash():
        hashObj = md5()
        hashObj.update(bytes(
            str( random.random() ), "utf-8"
        ))
        
        return hashObj.hexdigest()
    
    def checkIfImage(path):
        # basic filetype check
        if "image" not in str(guess_type(path)):
            error.print("not an image :O")
            return False

        return True


def homepage():
    """ displays the homepage """

    # getting list of IPFS CIDs on homepage
    with console.status("fetching CIDs..."):
        res = requests.get(f"{API}/images")

    responsedict = json.loads(res.text)
    cids = responsedict["cids"]
    
    filepath = Utils.randomHash()
    os.mkdir(filepath)

    # TODO: handle error response

    try:
        console.rule("IPFSgur")
        for cid in cids:
            url = f"{GATEWAY}/{cid}"

            
            # printing preview to console along with CID
            with console.status("fetching image..."):
                r = requests.get(url) # writing images to temporary file
                open( f"{filepath}/{cid}", "wb" ).write(r.content)

            console.print(f"[blue underline]{url}")
            render( f"{filepath}/{cid}", (console.size[1]//1.5, console.size[0]//3) )
            console.rule()

            os.remove(f"{filepath}/{cid}")

    except KeyboardInterrupt:
        pass

    os.rmdir(f"{filepath}")
    exit()


def uploadFile():
    """ upload a single file """
    imagePath = Prompt.ask("image path")

    try:
        img = { "image": open(imagePath, "rb" ) }
    except FileNotFoundError:
        error.print("nonexistent file path :(")
        exit()

    if not Utils.checkIfImage(imagePath):
        exit()
    
    payload = { "public": str(Confirm.ask("show in timeline?")).lower() }

    # POST request to API
    with console.status("sit back and relax..."):
        res = requests.post(
                f"{API}/ipfsgur",
                files=img,
                data=payload
        )

    response_json = json.loads(res.content)

    # printing link to GATEWAY
    console.print(f"[blue underline]{GATEWAY}/{response_json['Content_ID']}")


def getFile():
    """ general IPFS image fetching and terminal preview"""
    cid = Prompt.ask("image URL or CID")

    if '/' in cid:
        cid = cid.split('/')[-1]
        print("CID: " + cid)

    url = f"{GATEWAY}/{cid}"
    
    with console.status("fetching..."):
        r = requests.get(url) # writing images to temporary file
        open( cid, "wb" ).write(r.content)

    # TODO: Utils.checkIfImage fails for this. reason unknown. directly passing into render for now
    render( cid, (console.size[1]//1.5, console.size[0]//3) )


def main():
    if not len(argv) > 1:
        homepage()

    subcommand = argv[1]
    match subcommand:
        case "put":
            uploadFile()
        case "get":
            getFile()
        case "help":
            print(Utils.help_text)
        case _:
            homepage()

if __name__ == "__main__":
    main()

