import express from 'express';
const app=express();
app.get('/',(_request,response)=>response.type('html').send('<h1>maqarr-auto-e2e:javascript:ci-pass</h1>'));
app.listen(Number(process.env.PORT||8000),'0.0.0.0',()=>console.log('maqarr-auto-e2e:javascript:ci-pass ready'));
