const express = require('express');
const app = express();
const port = 3000;
const { MongoClient, ServerApiVersion, ConnectionClosedEvent } = require('mongodb');
require('dotenv').config();


app.use(express.json());

// Get connection string from environment variable
const uri = process.env.mongoURI;
const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true, serverApi: ServerApiVersion.v1 });

// Get all the games from my DB
app.get('/documents/:collection', async function (req, res) {
  await client.connect();
  const collection = client.db("glac_db").collection(req.params.collection);

  console.log("Getting all documents from collection: " + req.params.collection);

  let data = await collection.find().toArray();

  res.send(data);

  client.close();
});

app.listen(port, () => {
  console.log('Listening on *:3000');
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