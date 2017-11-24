var apiai = require('apiai');
var app = apiai("d8cd9faa2fe14731b1187d05b7d6f409");
var request = app.textRequest('Tell me a joke', {
    sessionId: '<unique session id>'
});
request.on('response', function (response) {
    console.log(response);
});
request.on('error', function (error) {
    console.log(error);
});
request.end();
