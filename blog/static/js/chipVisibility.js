/**
 * Shows a lab images and hide the others
 * @param {id} id0
 * @param {id} id1
 * @param {id} id2
 * @param {id} id3
 * @param {id} id4
 */

// function chip_visibility(id0, id1) {
// window.onload=function(){
//     var elemento=document.getElementById('link');
//     elemento.onmouseover = function(e) {
//
//     	// El contenido de esta funcion se ejecutara cuanso el mouse
//     	// pase por encima del elemento
//
//         // 	document.getElementById(id1).innerHTML="El ratón esta encima del recuadro";
//         document.getElementById('Chip_0').style.display='block'
//         document.getElementById('WaferFull').style.display='none'
//     };
//     elemento.onmouseout = function(e) {
//
//     	// El contenido de esta funcion se ejecutara cuanso el mouse
//     	// salga del elemento
//
//         // 	document.getElementById(id1).innerHTML="El ratón NO esta encima del recuadro";
//         document.getElementById('Chip_0').style.display='none'
//         document.getElementById('WaferFull').style.display='block'
//     };
// }

function chip_visibility(id0, id1) {
   var chip = document.getElementById(id0);
   var show = document.getElementById(id1);
   if(chip.style.display == 'block'){
      chip.style.display = 'none';
      show.style.display = 'block';
   }
   else {
      chip.style.display = 'block';
      show.style.display = 'none';
   }
}
