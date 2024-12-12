const express = require("express");
const cors = require("cors");
const { MongoClient } = require("mongodb");

const app = express();
app.use(cors());
app.use(express.json());

const uri = 'mongodb+srv://<username>:<password>@cluster0.mongodb.net/myDatabase?retryWrites=true&w=majority';
const client = new MongoClient(uri);

app.get("/data", async (req, res) => {
    try {
        await client.connect();
        const database = client.db("myDatabase");
        const collection = database.collection("myCollection");
        const data = await collection.find().toArray();
        res.json(data);
    } catch (error) {
        res.status(500).send(error.message);
    }

});

app.listen(5000, () => {
    console.log("Server running on http://localhost:5000");
});
