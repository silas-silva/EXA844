const express = require('express');
const cors = require('cors');
const app = express();

const port = process.env.PORT || 3000


app.use(express.static("public"))
app.use(express.urlencoded({extended:true}))
app.use(express.json());


app.use((request, response, next) => { //configure in cors what can access the backend
    // * -> allow all URLs to access
    // 'url' -> permite 1 url acessar
    // ['url', 'url'] -> allow one or more URLs to access
    response.header("Access-Control-Allow-Origin", "*");
    response.header("Access-Control-Allow-Methods", "GET, PUT, POST, DELETE"); // Release which methods will be allowed access
    app.use(cors());
    next();
})


//rotas
app.get('/', (request, response) => {

});

//Listar alimentos entre M e N calorias
app.get('/menos_carbo', (request, response) => {
    const {menor_caloria, maior_caloria} = request.body
    dados = {"status": true}
    response.status(200).send(dados);
});

//Listar K alimentos menos carboidatros
app.get('/menos_carbo', (request, response) => {
    const {num} = request.body
    dados = {"status": true}
    response.status(200).send(dados);
});

//Listar K alimentos mais carboidatros
app.get('/mais_carbo', (request, response) => {
    const {num} = request.body
    dados = {"status": true}
    response.status(200).send(dados);
});

//Listar K alimentos menos Proteicos
app.get('/menos_prot', (request, response) => {
    const {num} = request.body
    dados = {"status": true}
    response.status(200).send(dados);
});

//Listar K alimentos mais Proteicos
app.get('/mais_prot', (request, response) => {
    const {num} = request.body
    dados = {"status": true}
    response.status(200).send(dados);
});

//Listar K alimentos menos Gordurosos
app.get('/menos_gord', (request, response) => {
    const {num} = request.body
    dados = {"status": true}
    response.status(200).send(dados);
});

//Listar K alimentos mais Gordurosos
app.get('/mais_gord', (request, response) => {
    const {num} = request.body
    dados = {"status": true}
    response.status(200).send(dados);
});


//Listar alimentos por nome
app.get('/alimentos_nome', (request, response) => {
    const {nome} = request.body
    dados = {"status": true}
    response.status(200).send(dados);
});


app.listen(port, (err) => {

    if (err) {
        console.log("❌ Não foi possível iniciar o servidor ❌");
    }else{
        console.log("Servidor iniciado")
    }
});