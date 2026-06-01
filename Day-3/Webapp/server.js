const express = require("express");
const app = express();
const PORT = 8080;
app.get('/', (req, res) => {
    res.send(`<h1>Hello from Kapil!</h1>
        <p>Pod Names: 
            ${process.env.HOSTNAME}
        </p>`
    );

});

app.listen(PORT, () => {
    console.log(`Server is running on Port ${PORT}`);
});