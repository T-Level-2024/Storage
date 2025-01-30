const express = require('express'); // Import Express
const app = express(); // Initialize Express
const PORT = 3000; // Port to listen on

// Serve static files from the 'public' folder
app.use(express.static('public'));

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running at http://localhost:${PORT}`);
});