var page=1;
function add_page(){
    var div=document.createElement("div");
    emoji=1;text=1;img=1;shape=1;
    div.classList.add('pages',"_"+page);
    document.body.appendChild(div);
    focus_page(page,'active-page')
    page++;
}
function focus_page(val,sta){
    var div=document.querySelectorAll(".pages");
    for(let i=0;i<div.length;i++){
      if(div[i].classList[1]==="_"+val){
        div[i].setAttribute("id",sta);
      }
      else{
        div[i].setAttribute("id","");
      }
    }
  }
  function previous(){
    var div=parseInt(document.getElementById("active-page").classList[1][1]);
    if(div-1<0){
      focus_page(page-1,'active-page');
    }
    else
    focus_page(div-1,'active-page');
  }
  function next(){
    var div=parseInt(document.getElementById("active-page").classList[1][1]);
    if(div+1==page){
        div=0;
        focus_page(div,'active-page');
    }
    else
    focus_page(div+1,'active-page');
  }