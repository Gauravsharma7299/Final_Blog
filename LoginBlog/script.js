function changeFemaleImage() {
    var imgs = document.getElementById("myImage");
    imgs.classList.add("clicked");
  }
  function changeMaleImage() {
    var imgss = document.getElementById("myImages");
    imgss.classList.add("clicked");
  }

  const fm = document.getElementById('myImage');
  const m = document.getElementById('myImages');

		const buttonbalediv = document.getElementById('buttons');

		fm.addEventListener('click', function() {
			buttonbalediv.style.display = 'inline-block';
		});
    m.addEventListener('click', function() {
			buttonbalediv.style.display = 'inline-block';
		});
var inputField = document.getElementById('name');
var imageButton = document.getElementById('buttons');


// inputField.addEventListener('input', function() {
// if (inputField.value.length === 7) {
//  imageButton.disabled = false;} 
//  else {
// imageButton.disabled = true;
// }
// });
// function checkInput() {
//   const input = document.getElementById("name");
//   const imageContainer = document.getElementById("buttons");
//   const fm = document.getElementById('myImage');
//   if (input.value.length < null) {
//     imageContainer.style.display = "none";
//   } else {
//     imageContainer.style.display = "block";
//   }
// }


const inputTag = document.querySelector('#name');


const firstIcon = document.querySelector('#myImage');
const secondIcon = document.querySelector('#buttons');


firstIcon.addEventListener('click', function() {

  if (inputTag.value.trim() !== '') {
    
    secondIcon.style.display = 'block';
  }
});

// hide the second image icon initially
secondIcon.style.display = 'none';


  