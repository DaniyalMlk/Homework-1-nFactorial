'use strict';

//<script src="./index.js"></script>
//git branch nameOfYourBranch
//git checkout nameOfYourBranch
//git branch
//git add .
//git commit -m "message"
//git push

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


//1st Task
// function delay(ms) {
//     return new Promise(resolve => setTimeout(resolve, ms));
//   }
  
//   delay(3000).then(() => alert('выполнилось через 3 секунды'));

//2nd Task
// let promise = new Promise(function(resolve, reject) {
//     resolve(1);
  
//     setTimeout(() => resolve(2), 1000);
//   });
  
//   promise.then(alert);

// Код вывел '1'

//3rd Task
// promise.then(f1).catch(f2);

// promise.then(f1, f2);

//В двух примерах есть разница, к примеру в 1 промисе используется catch чтобы словить ошибку. В то время как во 2 промисе ошибка не задектетиться.
