// javascript

function swapConfig(x) {
    var radioName = document.getElementsByName(x.name);
    for(i = 0 ; i < radioName.length; i++){
      document.getElementById(radioName[i].id.concat("Form")).style.display="none";
    }
    document.getElementById(x.id.concat("Form")).style.display="initial";
  }

const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');

signUpButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});

// $.ajax({
//     url: '127.0.0.1:8000/hello',
//     type: 'get', // This is the default though, you don't actually need to always mention it
//     success: function(data) {
//         alert(data);
//     },
//     failure: function(data) { 
//         alert('Got an error');
//     }
// }); 

$(function (){
  var $user = $('#name');
  var $rest = $('#restaurant');
  var $rest1 = $rest.replace(' ','_');
  // var $price = 0 ; 
  var $check_list = [];
  // $("input[name='dish']").each(function() {
  //     if ($(this).attr('checked'))
  //     {
  //        checked = ($(this).val());
  //        $check_list.push(checked);
  //     }
  //     });
  // $("#price").each(function(){

  // });
  $('#place-order').on('click', function (){
      var details={
          user: $user.val(),
          restaurant: $rest.val(),
          dishes: $check_list.val()
      }
  
      $.ajax({
          type: 'POST',
          url: '/restaurant/'+$rest1+'/',
          data: details,
          success: function(newadditem){
              alert('Place')
          }
      });
  });
});
