let {PythonShell} = require('python-shell');

let options = {
	pythonOptions: ['-u'],
	mode : 'text'
};

let pyshell = new PythonShell('../python/ModelAirportAuto.py', options);

pyshell.on('message', function(message){
	console.log(message);
});