function toggle_visibility(id0, id1, id2, id3, id4) {
   var toggle = document.getElementById(id0);
   var hide1 = document.getElementById(id1);
   var hide2 = document.getElementById(id2);
   var hide3 = document.getElementById(id3);
   var hide4 = document.getElementById(id4);
   if(toggle.style.display == 'block')
      toggle.style.display = 'none';
   else
      toggle.style.display = 'block';
      hide1.style.display = 'none';
      hide2.style.display = 'none';
      hide3.style.display = 'none';
      hide4.style.display = 'none';
}
