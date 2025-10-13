let edad = parseInt(prompt("Cuantos años tienes?"));
let tieneCarne = confirm("Tienes Carnet de coche?");
let nombre = prompt("Como te llamas?");
let coche = confirm("Tienes coche?");  

console.log("Hola "+ nombre + ", comprobando tus datos...");

if (coche && tieneCarne){
    console.log("Vale, puedes conducir.");
} else if ( coche && !tieneCarne){
    console.log("No puedes conducir sin carnet aun teniendo coche.");
} else if (!coche && tieneCarne){
    console.log("No tienes coche, pero al menos tienes carnet.");
} else {
    console.log("Sin coche y sin carnet, no se que quieres hacer");
}