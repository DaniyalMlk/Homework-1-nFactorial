'use strict';

//<script src="./index.js"></script>
//git branch nameOfYourBranch
//git checkout nameOfYourBranch
//git branch
//git add .
//git commit -m "message"
//git push

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

const ageTable = document.getElementById('age-table');
console.log(ageTable); 

const label = ageTable.getElementsByTagName('label');
console.log(label);

const td = ageTable.getElementsByTagName('td')[0];
console.log(td);

const search = document.querySelector('form[name="search"]');
console.log(search);

const firstInput = search.querySelector('input');
console.log(firstInput);

const lastInput = search.querySelector('input:last-child');
console.log(lastInput);


//Task 2
{/* <script>
  let body = document.body;

  body.innerHTML = "<!--" + body.tagName + "-->";

  alert( body.firstChild.data ); // что выведет?
</script> */}

//ВЫВЕЛ aler() с надписью BODY;