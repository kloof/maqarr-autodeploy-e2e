import {createServer} from 'node:http';
const server=createServer((_request,response)=>{
  response.writeHead(200,{'Content-Type':'text/html'});
  response.end('<h1>maqarr-auto-e2e:typescript:v2</h1>');
});
server.listen(Number(process.env.PORT||8000),'0.0.0.0',()=>console.log('maqarr-auto-e2e:typescript:v2 ready'));
