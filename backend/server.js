const express = require("express");
const cors = require("cors");

const app = express();
app.use(cors());
app.use(express.json());

let tasks = [];

app.get("/tasks", (req, res) => {
    res.json(tasks.map((t, i) => [i, t]));
});

app.post("/tasks", (req, res) => {
    tasks.push(req.body.title);
    res.json({ success: true });
});

app.listen(3000, () => console.log("Backend running on port 3000"));