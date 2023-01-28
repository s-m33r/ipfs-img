import { Application, Router } from "https://deno.land/x/oak/mod.ts";
import Web3Storage from 'npm:web3.storage'

const HOST = '127.0.0.1';
const PORT = 8080;

const router = new Router();
const app = new Application();

const accessToken = prompt("web3.storage access token: ");
const storage = new Web3Storage({ accessToken })

// array containing upto 100 posts displayed on homepage
homepage = [
	"bafybeifoo7sevqsbpvjo3neomxyb5cawxpbd7i5sdbjdn5yyhk4tdya7eq",
	"bafybeibct5qwk2odv4rwd5atoss6pbzwprgxin2lvs7j4pgh4ttoyereci"
]

// API
// root
router.get("/", (context) => {
	context.response.body = "Welcome to ipfs-img!";
});

// view image - TODO DONE IN BROWSER. also verification if image was made available through ipfs-img

// homepage - displays most recent posts that had their privacy settings set to "Public"
router.get("/home", (context) => {
	context.response.body = { posts: homepage };
});

// post - add paste to web3.storage
router.post("/paste", async (context) => {
	const body = context.request.body();
	const cid = await storage.put([body]);
	console.log(cid);
})

app.use(router.routes());
app.use(router.allowedMethods());
console.log(`Listening on port ${PORT}`)
await app.listen( `${HOST}:${PORT}` );

