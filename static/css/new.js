var input = document.querySelector("input");
var output = document.querySelector(".out");
clearOutput();
document.querySelector("input").addEventListener("keyup", (e) => {
        /*only works when Enter key is clicked */
        
        if (e.which === 13) {
          output.innerHTML='';
          getData(input.value);
        }
       
      });
    
      /*Get data from the API*/
      
      function getData(val) {
        var API_KEY = "zlMz5WQzzo-MhldKwKG7781kK5noX0zkSuEbZp_mnaQ";
        var url =
          "https://api.unsplash.com/search/photos/?"+"&query="+val+"&per_page=20&client_id=" +
          API_KEY ; 
        fetch(url)
          .then((response) => response.json())
          .then((data) => showData(data.results));
          
      }

      function defaultData(){
        var API_KEY = "zlMz5WQzzo-MhldKwKG7781kK5noX0zkSuEbZp_mnaQ";
        var url =
          "https://api.unsplash.com/search/photos/?"+"&query=computer"+"&per_page=20&client_id=" +
          API_KEY ; 
        fetch(url)
          .then((response) => response.json())
          .then((data) => showData(data.results));
      }
      /*Display the output*/
      function showData(data) {
        data.forEach((element) => {
          var src = element.urls.regular;
          var div=document.createElement("div");
          div.classList.add("sticker-item");
          div.innerHTML="<img src=" + src + "  height=110px width=110px>";
          output.appendChild(div);
          div.setAttribute("onclick","add_sticker('"+src+"')");
        });
        return;
      }
      /*clearing the ouptut*/
      function clearOutput() {
        output.innerHTML=''
        defaultData();
      }
