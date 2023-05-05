function move(val){
    var pos1=0,pos2=0,pos3=0,pos4=0;
    var d1=document.getElementById('active-page').querySelector("#"+val);
    d1.onmousedown=dragMouseDown;
    function dragMouseDown(e) {
        pos3 = e.clientX;
        pos4 = e.clientY;
        document.onmouseup = closeDragElement;
        document.onmousemove = elementDrag;
      }
    
      function elementDrag(e) {
        pos1 = pos3 - e.clientX;
        pos2 = pos4 - e.clientY;
        pos3 = e.clientX;
        pos4 = e.clientY;
        
        d1.style.top = (d1.offsetTop - pos2) + "px";
        d1.style.left = (d1.offsetLeft - pos1) + "px";
      }
    
      function closeDragElement() {
        document.onmouseup = null;
        document.onmousemove = null;
      }
    }
   