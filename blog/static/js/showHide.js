function toggle_visibility(id) {
   var toggle = document.getElementById(id);
   if(toggle.style.display == 'block')
      toggle.style.display = 'none';
   else
      toggle.style.display = 'block';
}
