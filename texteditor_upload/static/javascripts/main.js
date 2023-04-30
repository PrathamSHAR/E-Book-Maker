var text=1,img=1,shape=1,min=0,i=0;
var cover_page='';

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
    if( document.getElementById("active-page").classList[1][1]==='0'){
        d2.innerHTML="This is your Cover Page";
    }
    else{
    d2.innerHTML="Enter your Text";
    }
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
  function capture(){
    screen();
    pdf();
  }
  function screen(){
    html2canvas(document.querySelector('#active-page'),{allowTaint:true, useCORS:true,scale:3}).then ((canvas)=>{
            
                if(min===0 ){
                    if(i!==parseInt(document.querySelector('#active-page').classList[1][1])){
                        alert("You forget to save Cover Page");
                    }
                    else{
                       doc.addImage(canvas.toDataURL('img/png'),'PNG',5,5,200,285);
                       
                       cover_page=canvas;
                       min=1;
                       i++;
                    }

                }
                else{
                   if(i>parseInt(document.querySelector('#active-page').classList[1][1])){
                        alert("Already saved!!!!")
                    }
                     else if(i!==parseInt(document.querySelector('#active-page').classList[1][1])){
                       
                        alert("You forget to save Page No."+i);
                    }
                    else{
                    doc.addPage();
                    doc.addImage(canvas.toDataURL('img/png'),'PNG',5,5,200,285);
                    i++;
                    }

                }
            
    });
}

  function pdf(){
    
    doc.setProperties({
        title: 'Book Preview',
        subject: 'This is the subject',
        author: 'James Hall',
        filename:'book',
        creator: 'MEEE'
    });
    var string = doc.output('bloburl');

var iframe = "<div style='display:inline-block;width:800px; height:500px; margin:20px;'><iframe width='100%' height='100%' src='" + string + "'></iframe></div>"
var div1="<div style='display:inline-block;'>Cover Page<br><a href='"+cover_page.toDataURL('img/png')+"' download><img src='"+cover_page.toDataURL('img/png')+"' height='500px' width='400px' border='1px solid gray'></a></div>"
var div="<div style='text-align:center;'> <h1>To Continue....Download your book and book cover</h1></div>"
var but="<div><a href='upload_Book/' target='_blank'><button>Click to proceed</button></a></div>"
var x = window.open();
x.document.open();
x.document.write(div)
x.document.write(div1)
x.document.write(iframe)
x.document.write(but)
x.document.close();
  }