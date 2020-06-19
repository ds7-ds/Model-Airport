console.log("Loading files...");
const proxySocket = require("ws");
let {PythonShell} = require('python-shell');



let options = {
	pythonOptions: ['-u'],
	mode : 'text'
};
let pyshell = new PythonShell('../python/QuickConnect.py', options);
const ws = new proxySocket("ws://model-airport.herokuapp.com");



ws.on('open', function open(){
	console.log("Connected to proxy server...");
	ws.send("Model Airport: RPiMAez");
});

ws.on('message', function incoming(msg){
	pyshell.send(msg);
});

pyshell.on('message', function(message){
	console.log(message);
	if(message.includes("[QuickConnect]")){
		if(message.includes("Ready?")){
			ws.send("Ready?");
		}
		else if(message.includes("Exiting...")){
			console.log("Exiting...");
		}
		else{
			console.log(message);
		}
	}
	else{
		ws.send(message);
	}
	
	//Code below tests model airport software
	/*
	if(message.includes("ATC Requesting Departure;Type \"SA202 Runway 09 Line Up And Wait\"")){
		pyshell.send("SA202 Runway 09 Line Up And Wait");
	}
	if(message.includes("ATC Runway 09 Line Up And Wait;Type \"SA202 Cleared For Takeoff\"")){
		pyshell.send("SA202 Cleared For Takeoff");
	}
	*/
});