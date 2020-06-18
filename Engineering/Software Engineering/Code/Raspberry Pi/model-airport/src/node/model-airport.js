let {PythonShell} = require('python-shell');

let options = {
	pythonOptions: ['-u'],
	mode : 'text'
};

let pyshell = new PythonShell('../python/QuickConnect.py', options);

pyshell.on('message', function(message){
	console.log(message);
	if(message.includes("[Input]")){
		if(message.includes("Ready?")){
			pyshell.send("Y");
		}
	}
	
	//Code below tests model airport software
	if(message.includes("ATC Requesting Departure;Type \"SA202 Runway 09 Line Up And Wait\"")){
		pyshell.send("SA202 Runway 09 Line Up And Wait");
	}
	if(message.includes("ATC Runway 09 Line Up And Wait;Type \"SA202 Cleared For Takeoff\"")){
		pyshell.send("SA202 Cleared For Takeoff");
	}
	
});
