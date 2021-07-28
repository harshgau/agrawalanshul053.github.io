$(function() {
  // Button will be disabled until we type anything inside the input field
  const source = document.getElementById('autoComplete');
  const inputHandler = function(e) {
    if(e.target.value==""){
      $('.movie-button').attr('disabled', true);
    }
    else{
      $('.movie-button').attr('disabled', false);
    }
  }
  source.addEventListener('input', inputHandler);

  $('.movie-button').on('click',function(){
    var shloka_input = $('.movie').val();
    // alert(shloka_input);
    if (shloka_input=="") {
      $('.results').css('display','none');
      $('.fail').css('display','block');
    }
    else{
      movie_recs(shloka_input);
    }
  });
});

// will be invoked when clicking on the recommended movies
function recommendcard(e){
  var shloka_input = e.getAttribute('shloka_input'); 
  load_details(shloka_input);
}


// passing the movie name to get the similar movies from python's flask
function movie_recs(shloka_input){
  $.ajax({
    type:'POST',
    url:"/recommend",
    data:{'name':shloka_input},
    dataType: 'html',
    complete: function(){
      $("#loader").delay(500).fadeOut();
    },
    success: function(response) {
      $('.results').html(response);
      $('#autoComplete').val('');
      $(window).scrollTop(0);
    },
  }); 
}