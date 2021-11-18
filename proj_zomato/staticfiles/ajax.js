$(function (){
    var $user = $('#name');
    var $rest = $('#restaurant');
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
            dishes: $check_list.val(),
        }
    
        $.ajax({
            type: 'POST',
            url: '/restaurant/'+$rest+'/',
            data: details,
            success: function(){
                alert('Place')
            }
        });
    });
});