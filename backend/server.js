const w3s = require('web3.storage');
var crypto = require('crypto');
var fs = require('fs')

const express = require('express')
const app = express()

const HOST = '127.0.0.1';
const PORT = 8080;

// creating web3 storage client object
const accessToken = fs.readFileSync('./access-token.txt', 'utf8');
console.log(accessToken);
const storage = new w3s.Web3Storage({ token: accessToken })

// array containing upto 100 posts displayed on homepage
homepage = [
	"bafybeifoo7sevqsbpvjo3neomxyb5cawxpbd7i5sdbjdn5yyhk4tdya7eq",
	"bafybeibct5qwk2odv4rwd5atoss6pbzwprgxin2lvs7j4pgh4ttoyereci"
]

// API
app.use(express.json());

app.get('/', function (req, res) {
  res.send("welcome to ipfs-img!");
});

app.post('/testing/pasteText', async (req, res) => {
	const body = req.body; // getting request body

  const filename = crypto.createHash('md5').update(toString(Math.random())).digest('hex'); // generating md1 hash of filename + 

  //console.log(body); // logging JSON contents and filename for debugging
  //console.log(filename);

  const filepath = `./tmp/${filename}.json`;
  fs.writeFileSync(filepath, JSON.stringify(body), 'utf-8');

  const files = await w3s.getFilesFromPath('./tmp/');

	const cid = await storage.put(files, {wrapWithDirectory: false}); // uploading to web3.storage

  if (cid) {
    fs.unlinkSync(filepath); // delete file if successful
  }

  res.send(cid); // send IPFS content ID as response string
});

app.post('/upload', async (req, res) => {

})


app.listen( PORT );