let {PythonShell} = require('python-shell');

let options = {
	pythonOptions: ['-u'],
	mode : 'text'
};

let pyshell = new PythonShell('../python/QuickConnect.py', options);

pyshell.on('message', function(message){
	console.log(message);
	if(message.includes("[Input]")){
		pyshell.send("N");
	}
	
});
