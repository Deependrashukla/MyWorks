// mongodb+srv://sdeependrashukla093:<db_password>@deepcluster.xssie.mongodb.net/?retryWrites=true&w=majority&appName=deepCluster


// const express = require("express");
// const app = express();
// const mongoose =require("mongoose");
// const Todo = require("./models/todo.model")
// const port = 4000;



// app.use (express.json())

// app.get("/todos", (req, res) => {
//   res.send(todos);
//   console.log("Called todo API to fetch todos");
// }); 


// app.post("/todos/add", async (req, res) => {
//     console.log("Called todo API to add")
//     const {title, description, status} = req.body;
//     try{
//       const todo = await Todo.create({title: title, description: description, status: status});
//       res.status(200).send(todo);
//     }catch (e){
//       console.log(e);
//       res.status(400).send(e)
//     }
//   });




// mongoose.connect("mongodb+srv://sdeependrashukla093:deependra2003@deepcluster.xssie.mongodb.net/?retryWrites=true&w=majority&appName=deepCluster")
// .then(() => {
//     app.listen(port, () => {
//         console.log(`Database has been connected and Listening on port ${port}`);
//       });
// })
// .catch(err => {
//     console.log(err);
// });














// ############################################ nwe code #############




// mongodb+srv://sdeependrashukla093:<db_password>@deepcluster.xssie.mongodb.net/?retryWrites=true&w=majority&appName=deepCluster

const express = require("express");
const app = express();
const mongoose = require("mongoose");
const Todo = require("./models/todo.model");
const port = 4000;

app.use(express.json());

// GET All Todos
app.get("/todos", async (req, res) => {
  try {
    const todos = await Todo.find({});
    res.status(200).send(todos);
    console.log("Called todo API to fetch todos");
  } catch (e) {
    console.log(e);
    res.status(500).send(e);
  }
});

// GET Todo by ID
app.get("/todos/:id", async (req, res) => {
  try {
    const todo = await Todo.findById(req.params.id);
    if (!todo) {
      return res.status(404).send({ message: "Todo not found" });
    }
    res.status(200).send(todo);
    console.log(`Called todo API to fetch ${req.params.id}`);
  } catch (e) {
    console.log(e);
    res.status(500).send(e);
  }
});

// POST Add a New Todo
app.post("/todos/add", async (req, res) => {
  console.log("Called todo API to add");
  const { title, description, status } = req.body;
  try {
    const todo = await Todo.create({ title, description, status });
    res.status(200).send(todo);
    console.log("Todo added successfully");
  } catch (e) {
    console.log(e);
    res.status(400).send(e);
  }
});

// DELETE Todo by ID
app.delete("/todos/:id", async (req, res) => {
  try {
    const todo = await Todo.findByIdAndDelete(req.params.id);
    if (!todo) {
      return res.status(404).send({ message: "Todo not found" });
    }
    res.status(200).send({ message: "Todo deleted successfully" });
    console.log(`Called todo API to delete ${req.params.id}`);
  } catch (e) {
    console.log(e);
    res.status(500).send(e);
  }
});

// PUT Update Todo by ID
app.put("/todos/:id", async (req, res) => {
  const { title, description, status } = req.body;
  try {
    const todo = await Todo.findByIdAndUpdate(
      req.params.id,
      { title, description, status },
      { new: true, runValidators: true }
    );
    if (!todo) {
      return res.status(404).send({ message: "Todo not found" });
    }
    res.status(200).send(todo);
    console.log(`Called todo API to update ${req.params.id}`);
  } catch (e) {
    console.log(e);
    res.status(400).send(e);
  }
});

mongoose
  .connect(
    "mongodb+srv://sdeependrashukla093:deependra2003@deepcluster.xssie.mongodb.net/?retryWrites=true&w=majority&appName=deepCluster"
  )
  .then(() => {
    app.listen(port, () => {
      console.log(`Database has been connected and Listening on port ${port}`);
    });
  })
  .catch((err) => {
    console.log(err);
  });






  // ################################# Code for token generation  ###############



// const express = require("express");
// const jwt = require("jsonwebtoken");
// const mongoose = require("mongoose");
// const Todo = require("./models/todo.model");
// const app = express();
// const port = 4000;

// app.use(express.json());

// // Secret key for signing JWTs
// const SECRET_KEY = "DeependraKey123TokenGenerator";

// // Middleware to verify JWT
// const authenticateToken = (req, res, next) => {
//   const token = req.headers["authorization"];
//   if (!token) return res.status(401).send({ message: "Access Denied" });

//   jwt.verify(token, SECRET_KEY, (err, user) => {
//     if (err) return res.status(403).send({ message: "Invalid Token" });
//     req.user = user;
//     next();
//   });
// };

// // Simulated user for login demonstration
// const user = { id: 1, username: "testuser" };

// // Login Route to generate JWT
// app.post("/login", (req, res) => {
//   const { username, password } = req.body;

//   // Check username and password (replace this with real authentication logic)
//   if (username !== "deependra" || password !== "deep123") {
//     return res.status(403).send({ message: "Invalid credentials" });
//   }

//   // Generate JWT
//   const token = jwt.sign({ id: user.id, username: user.username }, SECRET_KEY, {
//     expiresIn: "1h", // Token expires in 1 hour
//   });

//   res.status(200).send({ token });
// });

// // Protect the GET /todos route with JWT middleware
// app.get("/todos", authenticateToken, async (req, res) => {
//   try {
//     const todos = await Todo.find({});
//     res.status(200).send(todos);
//   } catch (e) {
//     console.log(e);
//     res.status(500).send(e);
//   }
// });

// // Other routes remain the same...
// // Add authenticateToken to any route you want to protect

// mongoose
//   .connect(
//     "mongodb+srv://sdeependrashukla093:deependra2003@deepcluster.xssie.mongodb.net/?retryWrites=true&w=majority&appName=deepCluster"
//   )
//   .then(() => {
//     app.listen(port, () => {
//       console.log(`Database connected and server running on port ${port}`);
//     });
//   })
//   .catch((err) => {
//     console.log(err);
//   });

