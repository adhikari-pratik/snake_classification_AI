var loadFile = function(event) {
  var output = document.getElementById('uploaded-image');
  output.src = URL.createObjectURL(event.target.files[0]);
  
  //display the image-container
  var imgContainer = document.getElementsByClassName("image-container");
  imgContainer[0].style.display = 'block';
  
  output.onload = function() {
    URL.revokeObjectURL(output.src) // free memory
  }
};
