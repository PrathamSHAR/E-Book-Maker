var input = document.querySelector(".popups>.media>.sticker>.input-container input");
var output = document.querySelector(".popups>.media>.sticker>.output");
var sticker=1;
clearOutput();
document.querySelector(".popups>.media>.sticker>.input-container>.search-input").addEventListener("keyup", (e) => {
        /*only works when Enter key is clicked */
        
        if (e.which === 13) {
          output.innerHTML='';
          getData(input.value);
        }
   
      });
      document.querySelector(".popups>.media>.sticker>.input-container button").addEventListener("click", (e) => {
        output.innerHTML='';
        getData(input.value);
      });
      /*Get data from the API*/
      function getTrendingData() {
        var API_KEY = "zlMz5WQzzo-MhldKwKG7781kK5noX0zkSuEbZp_mnaQ";
        var url =
          "https://api.unsplash.com/search/photos/?"+"&query=computer"+"&per_page=30&client_id=" +
          API_KEY ; 
        fetch(url)
          .then((response) => response.json())
          .then((data) => showData(data.results));
      }
      function getData(input) {
        var API_KEY = "zlMz5WQzzo-MhldKwKG7781kK5noX0zkSuEbZp_mnaQ";
        var url =
          "https://api.unsplash.com/search/photos/?"+"&query="+input+"&per_page=30&client_id=" +
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
          div.innerHTML="<img src=" + src + "  height=100px width=100px>";
          output.appendChild(div);
          div.setAttribute("onclick","add_sticker('"+src+"')");
        });
      }
      /*clearing the ouptut*/
      function clearOutput() {
        output.innerHTML="";
        getTrendingData();
      }
