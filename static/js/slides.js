
function show(){
   let con=document.getElementById("container");
   let item=document.getElementsByClassName("item");
   con.append(item[0]);
}
function showp(){
    let con=document.getElementById("container");
    let item=document.getElementsByClassName("item");
    con.prepend(item[item.length-1]);
 }
