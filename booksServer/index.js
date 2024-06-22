const app = require("./app.js");
const mongoose = require("mongoose");
const dotenv = require("dotenv");

dotenv.config();

const PORT = 8000;

// Connection URL
const mongoURI = "mongodb://mongo:27017/BooksDB"; // Change this to your MongoDB URI

mongoose
  .connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log("MongoDB connected"))
  .catch((err) => console.log(err));

app.listen(PORT, () => {
  console.log(`app listening on port ${PORT}`);
});
