const express = require("express");
const app = express();

const port = 4000;

todos = [
  { id: 1, title: "Do Task Number One" },
  { id: 2, title: "Do Task Number Two" },
  { id: 3, title: "Do Task Number Three" },
  { id: 4, title: "Do Task Number Four" },
];

app.use((req, res, next) => {
  console.log("Time:", Date.now());
  next();
});

app.use("/todos",(req, res, next) => {
  console.log("Time:", Date.now());
  next();
});

app.get("/todos", (req, res) => {
  res.send(todos);
  console.log("Called todo API to fetch todos");
});


app.use("/todos/:id",(req, res, next) => {
  console.log("id ka Time:", Date.now());
  next();
});


app.get("/todos/:id", (req, res) => {
  todos.forEach((todo) => {
    if (todo.id == req.params.id) {
      res.send(todo);
    }
  });
  console.log(`Called todo API to fetch ${req.params.id}`);
});

app.listen(port, () => {
  console.log(`Listening on port ${port}`);
});
