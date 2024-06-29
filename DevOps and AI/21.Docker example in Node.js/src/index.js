const express = require('express');

const app = express();
const port = process.env.PORT || 3000;

// Express routes
app.get('/hello-world', (req, res) => {
  res.send("Hello world. My name is Wilfredo")
});

// Start server
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
