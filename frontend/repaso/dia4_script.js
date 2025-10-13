let nombre = "Soul";
const edad = 31;
let programador = true;

console.log("Hola " + nombre);
console.log("Tienes " + edad + " años.");
console.log("¿Eres programador? " + programador);

 nombre = "SoulRocker";
 programador = false;

console.log("Hola " + nombre);
console.log("¿Eres programador? " + programador);

let nombreReal = prompt("Cual es tu nombre real?");
let programadorReal = confirm("Eres programador?");
let edadReal = prompt("Cual es tu edad?");

if (nombre !== nombreReal && programador !== programadorReal && edad === edadReal ){
    console.log("Asique hablas con la verdad, puesto que te llamas " + nombreReal + ", tienes " + edadReal + " años y " + programadorReal + " eres programador.");
}
else {
    console.log("Asique mientas, No damos la bienvenida a mentirosos.");
}