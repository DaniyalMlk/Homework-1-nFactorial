'use strict';

//1st task

const nameCafe = 'Daniyalcafe';
let placeCafe = 'Astana';
let countCafe = 3;
let isCafeHalal = true;
let address;

console.log (nameCafe);
console.log (placeCafe);
console.log (countCafe);
console.log (isCafeHalal);
console.log (address);


let Menu1 = {
    soup: 'pumpkin',
    meal: 'kebab',
    salad: 'cesar',
    drink: 'cola',

    alchocol: {
        alc1: 'vodka',
        alc2: 'beer'
    }
}

let Menu2 = {
    soup: 'cream-soup',
    meal: 'steak',
    salad: 'greece',
    drink: 'water',

    alchocol: {
        alc1: 'whisky',
        alc2: 'wine'
    }
}

Menu1.IsCafeNear = true;
Menu2.IsCafeNear = false;

delete Menu1.alchocol;
delete Menu2.salad;

console.log (Menu1);
console.log (Menu2);

//2nd task

let vehicle = {
    brandName: 'BMW',
    model: 'X5',
}

vehicle.brandName = 'M1';
delete vehicle.model;

console.log (vehicle);

//LAST task

let salaries = {
    Daniyal: 500,
    Samat: 500,
    Akezhan: 500
}

let sumTotal = 0;
for(let key in salaries) {
    sumTotal += salaries[key]
}
console.log(sumTotal);