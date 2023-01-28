from flask import Flask, request, jsonify
from PIL import Image
import w3storage, io

app = Flask(__name__)

@app.route('/ipfsgur', methods=['POST'])
def ipfsgur():

    #getting tags
    payload = request.form.to_dict()
    name_of_image = payload['name']
    public = payload['public']
    print(public, name_of_image)

    #reading file without saving using PIL library
    file = request.files['image']
    img = Image.open(file.stream)
    with open('token.txt', 'r') as f:
        token = f.read()

    #uploading to web3.storage
    w3 = w3storage.API(token=token)

    #converting image to temporary bytes and uploading it to web3.storage
    image_bytes = io.BytesIO()
    img.save(image_bytes, format=img.format)
    image_bytes = image_bytes.getvalue()
    imageID = w3.post_upload((name_of_image, image_bytes))

    #returning CID
    return jsonify({'msg':'success', 'Content_ID': imageID})

if __name__ == "__main__":
    app.run(debug=True, port=8200)