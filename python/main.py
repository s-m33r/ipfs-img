from flask import Flask, request, jsonify
from PIL import Image
import w3storage, io

app = Flask(__name__)

@app.route('/ipfsgur', methods=['POST'])
def ipfsgur():

    #getting tags
    payload = request.form.to_dict()
    public = payload['public']
    print(public)

    #reading file without saving using PIL library
    file = request.files['image']
    img = Image.open(file.stream)
    with open('token.txt', 'r') as f:
        token = f.read()

    #uploading to web3.storage
    w3 = w3storage.API(token=token.strip())

    #converting image to temporary bytes and uploading it to web3.storage
    image_bytes = io.BytesIO()
    img.save(image_bytes, format=img.format)
    image_bytes = image_bytes.getvalue()
    imageID = w3.post_upload((image_bytes))

    if str(public).lower() == "true":
        with open('public_cids.txt', 'a') as f:
            f.write(f"{imageID}\n")

    #returning CID
    return jsonify({'Content_ID': imageID})

@app.route('/images', methods=['GET'])
def getimages():
    with open('token.txt', 'r') as f:
        token = f.read()
    w3 = w3storage.API(token=token.strip())
    all_images = w3.user_uploads()
    public_images = []
    with open('public_cids.txt', 'r') as f:
        public_cids = f.readlines()
    for i in all_images:
        if f'{i["cid"]}\n' in public_cids:
            public_images.append(i['cid'])
    return public_images

if __name__ == "__main__":
    app.run(debug=True, port=8200)