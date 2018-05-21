#!/user/bin/env python
import webbrowser
import os
import re


main_page_head = '''
<!DOCTYPE html>
<html>
<head >
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Movie trailers</title>

   <style>
img{
border-radius:50%;
}
    .modal {
    display: none;
    position: fixed;
    z-index:1;
    padding-top:100px;
    left:0;
    top:0;
    width:100%;
    height:100%;
    overflow:auto;
    background-color:rgb(0,0,0);
    background-color:rgba(0,0,0,0.4);
}


.modal-content {
    margin:5% auto;
    padding:20px;
    width:80%;
    min-height:500px;
}


.close {
    color: #aaa;
    float: right;
    font-size: 28px;
    font-weight: bold;
}

.close:hover,
.close:focus {
    background-color: black;
    text-decoration: none;
    cursor: pointer;
    padding-left:5px;
    padding-right:5px;
}

      .container{
        display: flex;
        flex-wrap:wrap;
        font-family:arial,cursive;
       }
     .box{
          width:100%;
          min-height:150px;
          cursor:pointer;
        }
      @media screen and (min-width :450px)  {
      div.s1:hover{
             border:1px;
             background-color:skyblue;
             }
       div.s2:hover{
             border:1px;
             background-color:black;
             }
       div.s3:hover{
             border:1px;
             background-color:grey;
             }
       div.s4:hover{
             border:1px;
             background-color:red;
             }
       div.s5:hover{
             border:1px;
             background-color:brown;
             }
       div.s6:hover{
             border:1px;
             background-color:pink;
                   }
       .s1{width:33%;}
       .s2{width:33%;}
       .s3{width:33%;}
       .s4{width:33%;}
       .s5{width:33%;}
       .s6{width:33%;}
       h1 {background-color:black;}
        }
      h1 {background-color:black;
         font-family:arial,italic;}
         </style>
         <div>
          <div id="myModal" class="modal">

           <div class="modal-content">
                <span class="close">&times;</span>
            <iframe id="f" width="100%" height="315" src="" frameborder="0"
            allow="autoplay; encrypted-media" allowfullscreen></iframe>
          </div>
        </div>
</div>
<script>
var modal = document.getElementById('myModal');


var span = document.getElementsByClassName("close")[0];


    onc = function(c) {
    modal.style.display = "block";
    c='https://www.youtube.com/embed/'+c;
    console.log(c);
    document.getElementById("f").setAttribute("src",c);
}


    span.onclick = function() {
        modal.style.display = "none";
}
span.onclick = function(){
            console.log("hello");
            var iframe = document.getElementById("f");
            iframe.src = iframe.src;
            modal.style.display = "none";
        }



   window.onclick = function(event) {
       if (event.target == modal) {
          modal.style.display = "none";
    }
}
</script>
</head>

'''
main_page_content = '''
<body style="text-align:center">
   <h1 style="color:white">MOVIE TRAILERS</h1>
   <div class="container">
   <div class="box s1" onclick="onc('6ZfuNTqbHE8')"> <img vspace="20"
   src="https://bit.ly/2IB8NDM" style="width:50%"height="300" hspace="20";>
   <h2 style="color:white;">AVENGERS</h2></div>
   <div class="box s2" onclick="onc('Z_PODraXg4E')"> <img vspace="20"
   src="https://bit.ly/2Iv371Y" style="width:50%"height="300" hspace="20">
   <h2 style="color:white;">HEY DIL HAI MUSHKIL</h2></div>
   <div class="box s3" onclick="onc('OiTiKOy59o4')"> <img vspace="20"
   src="https://bit.ly/2Izbk0Z" style="width:50%" height="300" hspace="20">
   <h2 style="color:white;">GRAVITY</h2>  </div>
   <div class="box s4" onclick="onc('KMWS5y2gZ6E')"> <img vspace="20"
   src="https://bit.ly/2rVcTQK" style="width:50%"height="300"  hspace="20">
   <h2 style="color:white;">BHARAT ANE NENU</h2></div>
   <div class="box s5" onclick="onc('FnCdOQsX5kc')"> <img vspace="20"
   src="https://bit.ly/2wfWg6K" style="width:50%"height="300"  hspace="20">
   <h2 style="color:white;">IT</h2></div>
   <div class="box s6" onclick="onc('Gdzif0Px_qY')"> <img vspace="20"
   src="https://bit.ly/2IC7R23" style="width:50%"height="300"  hspace="20">
   <h2 style="color:white;">Banglore Days</h2></div>
</body>
</html>
'''
kohli = '''
<div class="col-md-6 col-lg-4 movie-tile text-center"
data trailer-youtube-id="{trailer_youtube_id}"
data-toggle="modal" data target="#trailer">
    <img src="{poster_image_url}" width="80%" height="342">
    <h2 style="color:white;">{movie_title}</h2>
</div>
'''


def create_movie_tiles_content(movies):

    virat = ''
    for movie in movies:
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        virat += kohli.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id)
    return virat


def open_movies_page(movies):
    output_file = open('fresh_tomatoes.html', 'w')

    rendered_content = main_page_content.format(
                       movie_tiles=create_movie_tiles_content(movies))

    output_file.write(main_page_head + rendered_content)
    output_file.close()

    url = os.path.abspath(output_file.name)
    webbrowser.open('file://'+url, new=2)
    
