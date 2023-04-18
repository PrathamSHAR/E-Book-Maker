
var out = document.querySelector(".popups>.emoji>.emoji-container");
var emoji=1;
getEmoji();

      /*Get data from the API*/
      function getEmoji() {
        fetch('https://emoji-api.com/emojis?access_key=60dc2c30084bd6ead267ab9996930e96d647bca3')
        .then(res=>res.json()).then(data=>showEmoji(data));
      }
      
      /*Display the output*/
      function showEmoji(data) {
        data.forEach((element) => {
          var div=document.createElement("div");
          div.classList.add("emoji-item");
          div.innerHTML=element.character;
          div.style.fontSize='40px';
          out.appendChild(div);
          div.setAttribute("onclick","add_emoji('"+element.character+"')");
        });
      }

      function add_emoji(src){
        var div=document.createElement("div");
        div.classList.add("emoji-div","_"+emoji);
        div.innerHTML=src;
        div.style.fontSize='40px';
        document.getElementById("active-page").appendChild(div);
        document.querySelector(".popups>.emoji>.emoji-ele>.size").value="40";
        focus_ele('emoji-div',emoji,'active-emoji');
        div.setAttribute("onclick","focus_ele('emoji-div',"+emoji+",'active-emoji')");
        move('active-emoji');
        emoji++;
      }
      function changesize(val){
        var div=document.getElementById("active-page").querySelector("#active-emoji")
        div.style.fontSize=val+"px"
      }