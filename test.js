// const express = require("express");
// const http = require("http");
// const socketIo = require("socket.io");

// const app = express();
// const server = http.createServer(app);
// const io = socketIo(server, {
//   cors: {
//     origin: "*", 
//     methods: ["GET", "POST"]
//   }
// });

// const PORT = 3000;


// app.get("/", (req, res) => {
//   res.sendFile(__dirname + "/index.html");
// });


// io.on("connection", (socket) => {
//     console.log("Client connected:", socket.id);

//     socket.on("user_mess", (userMessage) => {
//       console.log("Message received from client:", userMessage);

//       io.emit("user_mess", userMessage);
//     });
  

//     socket.on("bot_responses", (botResponse) => {
//       console.log("Bot response received from Python:", botResponse);
//       console.log(botResponse=="need legal advice")
//       if (botResponse == "need legal advice") {
//           io.emit("advice", "whattodo");
//       }

//       io.emit("bot_responses", botResponse) 
//     });
  
//     socket.on("userResponse", (response) => {
//       console.log("User responded:", response);

//       io.emit("userResponse", response); 
//     });
  
//     socket.on("disconnect", () => {
//       console.log("Client disconnected:", socket.id);
//     });
//   });

// // Start the server
// server.listen(PORT, () => {
//   console.log(`Server running at http://localhost:${PORT}`);
// });




























const express = require("express");
const http = require("http");
const ejs = require('ejs')
const socketIo = require("socket.io");
const fs = require("fs");

const app = express();
const server = http.createServer(app);
const io = socketIo(server, {
  cors: {
    origin: "*", 
    methods: ["GET", "POST"]
  }
});
app.set('view engine', 'ejs')
const PORT = 3000;
const chatHistoryFile = "chat_history.json";

// Load existing chat history or initialize an empty array if the file doesn't exist
let chatHistory = [];
if (fs.existsSync(chatHistoryFile)) {
  const data = fs.readFileSync(chatHistoryFile, "utf8");
  chatHistory = JSON.parse(data);
}

// Function to save chat history to JSON file
function saveChatHistory() {
  fs.writeFileSync(chatHistoryFile, JSON.stringify(chatHistory, null, 2));
}

// Route to serve the HTML file
app.get("/", (req, res) => {
  res.render('chatbot')
});

io.on("connection", (socket) => {
  console.log("Client connected:", socket.id);

  socket.on("user_mess", (userMessage) => {
    console.log("Message received from client:", userMessage);

    // Save user message to chat history and file
    chatHistory.push({ role: "User", message: userMessage });
    saveChatHistory();

    io.emit("user_mess", userMessage);
  });

  socket.on("bot_responses", (botResponse) => {
    console.log("Bot response received from Python:", botResponse);

    if (botResponse == "need legal advice") {
      io.emit("advice", "whattodo");
    }

    // Save bot response to chat history and file
    chatHistory.push({ role: "Bot", message: botResponse });
    saveChatHistory();

    io.emit("bot_responses", botResponse);
  });

  socket.on("userResponse", (response) => {
    console.log("User responded:", response);

    // Save user response to chat history and file
    chatHistory.push({ role: "User", message: response });
    saveChatHistory();

    io.emit("userResponse", response);
  });

  socket.on("disconnect", () => {
    console.log("Client disconnected:", socket.id);
  });
});

// Start the server
server.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});


























