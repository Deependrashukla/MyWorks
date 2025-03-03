
// const math = require('./math.js');
// const http = require("http");

// const server = http.createServer((req, res) => {
//     res.end("Hello, world!")
// })


// server.listen(3000, () => {
//     console.log("Server is running on port 3000")
// })

// // console.log(math.add(5, 7));
// // console.log(math.sub(10, 5));
// // console.log("hii Deependra");



// const express = require('express')
// const app = express()
// const port = 3000

// app.get('/', (req, res) => {
//   res.send('Hello World!')
// })

// app.listen(port, () => {
//   console.log(`Example app listening on port ${port}`)
// })

// ###########################################################                      #########################################################




// const fs = require('fs');

// const express = require('express')
// const cors = require('cors');
// const app = express();

// app.get('/', (req, res) => {
//     console.log("mene de diya")
//     res.send('Hello world!')
// })

// app.use(express.urlencoded({extended: false}));
// app.get('/api/', (req, res) => {
//     console.log("api ne bhi de diya")
//     fs.readFile("MOCK_DATA.json", "utf8", (err, data) => {
//         if (err) {
//             console.error(err)
//             return;
//         }
//             const jsonData = JSON.parse(data)
//         // jsonData.forEach(item => {
//         //     console.log(item)
//         // })
//         res.json(jsonData);
//     }) 
// })

// app.get('/test:id', (req,res) => {
//     res.send(req.params.id)
// })

// app.post('/add', (req, res) => {
//     const {a, b} = req.body;
//     res.send({result: parseInt(a) + parseInt(b)});
// });

// app.listen(3000, () => console.log('Server running on portal 3000'))


// ###################################### #####################################






const fs = require('fs');
const express = require('express');
const app = express();
const cors = require('cors');
app.use(cors());
const PORT = 3001;

// Middleware
app.use(express.json());
app.use(cors());

// Utility function to read and write JSON data
const readData = () => JSON.parse(fs.readFileSync('MOCK_DATA.json', 'utf8'));
const writeData = (data) => fs.writeFileSync('MOCK_DATA.json', JSON.stringify(data, null, 2));

// GET all items or item by ID using query parameter
app.get('/api', (req, res) => {
    try {
        const data = readData();
        const { id } = req.query;

        // Check if an ID is provided as a query parameter
        if (id) {
            const item = data.find(item => item.id === parseInt(id));
            if (item) {
                res.json(item);
            } else {
                res.status(404).send('Item not found');
            }
        } else {
            // No ID provided, return all items
            res.json(data);
        }
    } catch (error) {
        console.error(error);
        res.status(500).send('Error reading data');
    }
});

// POST - Add a new item
app.post('/api', (req, res) => {
    const newItem = req.body;
    const data = readData();
    newItem.id = data.length ? data[data.length - 1].id + 1 : 1; // Assign a new ID
    data.push(newItem);
    writeData(data);
    res.status(201).json(newItem);
});

// PUT - Update an item by ID
app.put('/api/:id', (req, res) => {
    const { id } = req.params;
    const updatedItem = req.body;
    let data = readData();
    const index = data.findIndex(item => item.id === parseInt(id));

    if (index !== -1) {
        data[index] = { ...data[index], ...updatedItem };
        writeData(data);
        res.json(data[index]);
    } else {
        res.status(404).send('Item not found');
    }
});

// DELETE - Remove an item by ID
app.delete('/api/:id', (req, res) => {
    const { id } = req.params;
    let data = readData();
    const newData = data.filter(item => item.id !== parseInt(id));

    if (data.length !== newData.length) {
        writeData(newData);
        res.send(`Item with ID ${id} deleted`);
    } else {
        res.status(404).send('Item not found');
    }
});




// Server
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
