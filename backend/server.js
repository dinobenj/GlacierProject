require('dotenv').config();
const express = require('express');
const app = express();
app.use(express.json());
const { MongoClient, ServerApiVersion, ConnectionClosedEvent } = require('mongodb');
const port = 3000;

// Get connection string from environment variable
const uri = process.env.mongoURI;
if (uri == null) {
  console.log("Error: No connection string found in .env file.\nPlease add a mongoURI variable to the .env file.");
  process.exit(1);
}

const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true, serverApi: ServerApiVersion.v1 });

// Get all the documents from a given collection
app.get('/documents/:collection', async function (req, res) {
  await client.connect();
  const collection = client.db("glac_db").collection(req.params.collection);

  console.log("Getting all documents from collection: " + req.params.collection);
  
  let data = await collection.find().toArray();
  
  res.send(data);
  
  console.log("Sent all documents.");

  client.close();
});



app.listen(port, () => {
  console.log('Server started. Listening on *:' + port + '...');
});

// // GET
// app.get('/db/:docNum', async function (req, res) {
//   await client.connect();
//   const collection = client.db("SteamProfile").collection("Profiles");

//   let docNum = Number(req.params.docNum);
//   console.log("Checking key " + docNum);

//   let query = { key: docNum };
//   let data = await collection.findOne(query);

//   console.log("Get on key " + docNum + ": " + data);
//   res.send(data);

//   client.close();
// });

// app.get('/db', async function (req, res) {
//   res.status(405);
//   console.log("Attempted get all documents");
//   res.send("Must GET on a key, getting all documents is currently not allowed.")
// });