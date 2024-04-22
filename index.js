'use strict';

//1st task
// const age = +prompt("Сколько вам лет?");
// let checkAge = (age >= 18) ? true : 'Родители разрешили?' + ` ${age} `;
// console.log(checkAge);

// //2nd task
// let pow = (a, b) => {return a ** b;}
// console.log(pow(2, 10));

// //3rd task
// function ask(question, yes, no) {
//     if (confirm(question)) yes()
//     else no();
//   }
  
//   ask(
//     "Вы согласны?", 
//     (yes) => { alert("Вы согласились."); }, 
//     (no) => { alert("Вы отменили выполнение."); }
// );

// //4th task
// let arr = [5, 2, 1, -10, 8];
// arr.sort((a,b) => b-a);
// alert(arr); // 8, 5, 2, 1, -10

// //5th task
// let vasya = { name: "Вася", age: 25 };
// let petya = { name: "Петя", age: 30 };
// let masha = { name: "Маша", age: 28 };

// let users = [ vasya, petya, masha ];

// let names = ['Вася', 'Петя', 'Маша'];

// let ages = [25, 30, 28];
// alert( ages ); 


/////////////////////
// 6th task
// let vasya = { name: "Вася", surname: "Пупкин", id: 1 };
// let petya = { name: "Петя", surname: "Иванов", id: 2 };
// let masha = { name: "Маша", surname: "Петрова", id: 3 };

// let users = [ vasya, petya, masha ];

// let usersMapped = users.map(user => 
//     (
//         {
//             fullName: ${user.name} ${user.surname}, id: user.id
//         }
//     )
// );

// alert( usersMapped[0].id ) // 1
// alert( usersMapped[0].fullName ) // Вася Пупкин
///////////////////////////

//7th task
// let vasya = { name: "Вася", age: 30 };
// let petya = { name: "Петя", age: 30 };
// let masha = { name: "Маша", age: 30 };

// let arr = [ vasya, petya, masha ];

// function getAverageAge(arr) {
//     let sumAge = 0;
//     for (let i = 0; i < arr.length; i++) {
//       sumAge += arr[i].age;
//     }
//     return sumAge / arr.length;
//   }
  
// alert( getAverageAge(arr) );