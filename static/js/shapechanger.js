var angle=0;
function shapeheight(val){
    var div=document.getElementById("active-shape");
    var shape=div.classList[2];
    if(shape==='triangle'){
        div.style.height=0+"px";
        div.style.width=0+"px";
        div.style.borderRight=(getComputedStyle(div).borderRight);
        div.style.borderLeft=(getComputedStyle(div).borderLeft);
        div.style.borderBottom=val+"px solid #555"; 
    }
    else if(shape==='trapezoid'){
        div.style.height=0+"px";
        div.style.width=(getComputedStyle(div).width);
        div.style.borderRight=(getComputedStyle(div).borderRight);
        div.style.borderLeft=(getComputedStyle(div).borderLeft);
        div.style.borderBottom=val+"px solid #555"; 
    }
    else{
        div.style.height=val+"px";
    }
}
function shapewidth(val){
    var div=document.getElementById("active-shape");
    var shape=div.classList[2];
    if(shape==='triangle'){
        val=val/2;
        div.style.height=0+"px";
        div.style.width=0+"px";
        div.style.borderRight= val+"px solid transparent";
        div.style.borderLeft=val+"px solid transparent";
        div.style.borderBottom=getComputedStyle(div).borderBottom; 
    }
    else if(shape==='trapezoid'){
        val=val-50;
        div.style.height=0+"px";
        div.style.width=val+"px";
        div.style.borderRight="25px solid transparent";
        div.style.borderLeft="25px solid transparent";
        div.style.borderBottom=(getComputedStyle(div).borderBottom); 
    }
    else{
        div.style.width=val+"px";
    }
}
function opacityshape(val){
    document.getElementById("active-shape").style.opacity=val+"%";
}
function setcolor(val){
    const div=document.getElementById("active-shape");
    if(div.classList[2]==='triangle' || div.classList[2]==='trapezoid'){
        div.style.borderBottomColor=val;
    }
    else{
        div.style.backgroundColor=val;
    }
}
function rotate(val){
    if(angle===360){
        angle=0;
    }
    angle+=val;
    var div=document.getElementById("active-shape");
    if(div.classList[2]==='parallelogram')
    rotparallelogram(angle);
    else
    div.style.transform="rotate("+angle+"deg)";
}
function rotparallelogram(val){
    var div=document.getElementById("active-shape");
    console.log(val)
    if(div.style.height===''){
        div.style.height=getComputedStyle(div).height;
        div.style.width=getComputedStyle(div).width;
    }
    if(val===90 || val===270){
        var t=div.style.height;
        div.style.height=div.style.width;
        div.style.width=t;
        div.style.transform="skew(0deg,-20deg)";
    }
    else{
        var t=div.style.height;
        div.style.height=div.style.width;
        div.style.width=t;
        div.style.transform="skew(20deg,0deg)";
    }
}
