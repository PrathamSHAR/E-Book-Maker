var text=1,img=1,shape=1,min=0;

function show(num,val){

    var div = document.getElementById("popups");
    if(div.style.display===""){
        div.style.display="block";
    if(num===1){
        div.querySelector(".text").style.display="block";
        div.querySelector(".media").style.display="none";
        div.querySelector(".shapes").style.display="none";
        div.querySelector(".emoji").style.display="none";
    }
    else if(num==2){
        div.querySelector(".text").style.display="none";
        div.querySelector(".media").style.display="block";
        div.querySelector(".shapes").style.display="none";
        div.querySelector(".emoji").style.display="none";
    }
    else if(num==3){
        div.querySelector(".text").style.display="none";
        div.querySelector(".media").style.display="none";
        div.querySelector(".shapes").style.display="block";
        div.querySelector(".emoji").style.display="none";
    }
    else{
        div.querySelector(".text").style.display="none";
        div.querySelector(".media").style.display="none";
        div.querySelector(".shapes").style.display="none";
        div.querySelector(".emoji").style.display="block";
    }
  }
  else{
    div.style.display="";
    if(num===1){
        div.querySelector(".text").style.display="block";
        div.querySelector(".media").style.display="none";
        div.querySelector(".shapes").style.display="none";
        div.querySelector(".emoji").style.display="none";
    }
    else if(num==2){
        div.querySelector(".text").style.display="none";
        div.querySelector(".media").style.display="block";
        div.querySelector(".shapes").style.display="none";
        div.querySelector(".emoji").style.display="none";
    }
    else if(num==3){
        div.querySelector(".text").style.display="none";
        div.querySelector(".media").style.display="none";
        div.querySelector(".shapes").style.display="block";
        div.querySelector(".emoji").style.display="none";
    }
    else{
        div.querySelector(".text").style.display="none";
        div.querySelector(".media").style.display="none";
        div.querySelector(".shapes").style.display="none";
        div.querySelector(".emoji").style.display="block";
    }
  }
}
function add_text(){
    var d1=document.createElement("div");
    var d2=document.createElement("div");
    d1.classList.add("divprop","_"+text);
    d2.innerHTML="Enter your Text";
    d2.contentEditable="true";
    d1.appendChild(d2);
    document.getElementById("active-page").appendChild(d1);
    focus_ele('divprop',text,'active-text');
    d1.setAttribute("onclick","focus_ele('divprop',"+text+",'active-text'"+")");
    text++;
}

function formatDoc(cmd,val=null){
    if(val){
        document.execCommand(cmd,false,val);
    }
    else{
        document.execCommand(cmd);
    }
}
function changebkg(col){
    var page=document.getElementById("active-page");
    page.style.backgroundColor=col;
}

function remove(val){
    var ele=document.getElementById('active-page').querySelector("#"+val);
    ele.remove();
}
document.querySelector(".popups>.media>.img-ele>.file").addEventListener("change",(e)=>{
    const files=e.target.files;
    for(let i=0;i<files.length;i++){
        if(!files[i].type.match("image"))continue;
        const picread= new FileReader();
        picread.addEventListener("load",function(e){
            const picfile=e.target;
            const div= document.createElement("div");
            div.innerHTML=`<img src="${picfile.result}" />`
            div.classList.add("image","_"+img);
            document.getElementById("active-page").appendChild(div);
            focus_ele('image',img,'active-img');
            div.setAttribute("onclick","focus_ele('"+div.classList[0]+"',"+img+",'active-img'"+")");
            img++;
            
        })
        picread.readAsDataURL(files[i]);
    }
})


function changeheight(val){
    var img=document.getElementById("active-page").querySelector("#active-img img")
    img.style.height=val+"px";
}
function changewidth(val){
    var img=document.getElementById("active-page").querySelector("#active-img img")
    img.style.width=val+"px";
}
function opacity(val){
    var img=document.getElementById("active-page").querySelector("#active-img")
    img.style.opacity=val+"%";
}
function focus_ele(main,val,sta){
    var div=document.getElementById("active-page").querySelectorAll("."+main)
    for(let i=0;i<div.length;i++){
      if(div[i].classList[1]==="_"+val){
        div[i].setAttribute("id",sta);
      }
      else{
        div[i].setAttribute("id","");
      }
    }
  }
  function addshape(val){
    var div = document.createElement("div");
    div.classList.add("div-shape","_"+shape,val);
    document.getElementById("active-page").appendChild(div);
    focus_ele('div-shape',shape,'active-shape');
    div.setAttribute("onclick","focus_ele('div-shape',"+shape+",'active-shape')");
    move('active-shape');
    shape++;
  }
  function add_sticker(src){
    var div=document.createElement("div");
    div.innerHTML="<img src=" + src + ">";
    div.classList.add("image","_"+img);
    document.getElementById("active-page").appendChild(div);
    focus_ele('image',img,'active-img');
    div.setAttribute("onclick","focus_ele('image',"+img+",'active-img')");
    move('active-img');
    img++;
  }
  const doc= new jsPDF();
  function screen(){
    document.querySelector(".save").style.cursor="none";
    document.querySelector(".final").style.cursor="none";
    html2canvas(document.querySelector('#active-page'),{allowTaint:true, useCORS:true,scale:3}).then ((canvas)=>{
            if(min==0){
                doc.addImage(canvas.toDataURL('img/png'),'PNG',5,5,200,285);
                min=1;
            }
            else{
                doc.addPage()
                doc.addImage(canvas.toDataURL('img/png'),'PNG',5,5,200,285);}
            });
            document.querySelector(".save").style.cursor="default";
  }

  function pdf(){
    window.open(doc.output('bloburl'));
  }