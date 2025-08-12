const http = require('http');
const url = require('url');

http.createServer(function (req, res) {
    const query = url.parse(req.url, true).query;
    // Vulnerable: user input directly reflected without encoding
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.end("Hello " + query.name);
}).listen(8080);
