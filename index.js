'use strict';

//<script src="./index.js"></script>
//git branch nameOfYourBranch
//git checkout nameOfYourBranch
//git branch
//git add .
//git commit -m "message"
//git push

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

// / DOM element onclick
// const btn = document.querySelector('.btn'),
//       btn1 = document.querySelectorAll('.btn')[1],
//       btn2 = document.querySelectorAll('.btn')[2],
//       body = document.querySelector('body'),
//       btns = document.querySelectorAll('.btn');


// // btn.onclick = function(){
// //     alert('Hello!')
// // }

// // btn.onclick = function(){
// //     alert('Hello again!');
// // }


// const alertShow = function(event){
//    console.log('My first click ')
//    event.target.remove();
//    btn.removeEventListener('click', alertShow)
// }

// btn.addEventListener('click', alertShow)

// // btn.addEventListener('click', (event)=>{
// //     event.target.remove();
// // });

// let i = 0

// const count = function(){
//     console.log(i, 'i increacing')
//     i++;
//     if(i===3){
//         btn1.removeEventListener('click', count);
//     }
// }

// btn1.addEventListener('click', count);

// btn2.addEventListener('mouseover', function(e){
//     console.log(e)
//     btn2.style.backgroundColor = 'black';
// })

// btn2.addEventListener('mouseout', function(e){
//     console.log(e)
//     btn2.style.backgroundColor = 'blue';
// })

// let s = ''
// body.addEventListener('keydown',(e)=>{
//     s+= e.key;
//     if(s === 'dalida'){
//         alert('you texted to Dalida');
//     }
// })

// btns.forEach(item=>{
//     item.addEventListener('click', ()=>{
//         console.log('count')
//     })
// });


////////////////////////////

//1st Task
// document.getElementById('hider').onclick = function() {
//     let text = document.getElementById('text');
//     text.style.visibility = 'hidden';  
// };

//2nd Task

// const button = document.querySelector('button');

// button.addEventListener("click", () => alert("1"));
// button.removeEventListener("click", () => alert("1"));
// button.onclick = () => alert(2);
//Ответ 1 и 2

//3rd Task

// let panes = document.querySelectorAll('.pane');

//     for(let pane of panes) {
//       pane.insertAdjacentHTML("afterbegin", '<button class="remove-button">[x]</button>');
//       pane.firstChild.onclick = () => pane.remove();
//     }
//Cори, код юзанул с песочницы, других вариантов в голову не пришло, решение понял прочитал как юзается insert