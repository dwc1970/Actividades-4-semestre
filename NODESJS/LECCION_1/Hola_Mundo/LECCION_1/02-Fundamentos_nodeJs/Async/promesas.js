function hola(nombre) {
    return new Promise (function (resolve, reject){
        setTimeout(function () {
            console.log('hola '+nombre);
            resolve(nombre);
        }, 1000);
    })
}
  

function hablar(nombre){
    return new Promise( ( resolve, reject) =>{ // Usamos la sintaxis ES6
        setTimeout(function() {
            console.log('bla bla bla ');
            resolve(nombre);
            }, 1000);
    });
    
}


function adios(nombre) {
    return new Promise( ( resolve, reject) => {
        setInterval(function () {
            resolve('Adios '+ nombre);
            }, 1500);
    })
   
}

//Llamamos a la funcion
console.log('Iniciando el proceso...');
hola('Dario Walter Carrizo')
    .then(hablar)
    .then(Adios)
    .then((nombre) => {
        console.log('Terminando el proceso'); 
    })
    .catch(error =>{
        console.log('ha ocurrido un error : ');
        console.log(error);
    })
