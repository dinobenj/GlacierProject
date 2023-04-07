import * as mongoDB from "mongodb";
import * as dotenv from "dotenv";

export const collections: { users?: mongoDB.Collection } = {}

export async function connectToDatabase () {
      dotenv.config();
   
      const client: mongoDB.MongoClient = new mongoDB.MongoClient(process.env.DB_CONN_STRING as string);
              
      await client.connect();
          
      const db: mongoDB.Db = client.db(process.env.DB_NAME);
     
      const gamesCollection: mongoDB.Collection = db.collection(process.env.GAMES_COLLECTION_NAME as string);
   
    collections.users = gamesCollection;
         
           console.log(`Successfully connected to database: ${db.databaseName} and collection: ${gamesCollection.collectionName}`);
   }
