var http=require("http");
var fs= require("fs");
var index= fs.readFileSync("index.html");



var SerialPort= require("serialport");
const parsers= SerialPort.parsers;
const parser= new parsers.Readline({
    delimiter:"\r\n"

});

var port =new SerialPort ("COM6",{
    baudRate:9600,
    dataBits:8,
    parity:"none",
    stopBits:1,
    flowControl: false
    }
) //escribir puerto serial

port.pipe(parser);


var app= http.createServer(function(req,res){

    res.writeHead(200, {"Content-type": "text/html"});
    res.end(index);
})

var io= require("socket.io").listen(app);
io.on("connection",function(data){
    console.log("Node.js is listening");

});

parser.on("data", function(data){

    console.log(data);
    io.emit("data", data);

})

app.listen(3000);