$("form#main").validate({
    rules: {
        username: {
            minlength: 3,
            maxlength: 20,
            required: true
        },
        password: {
            required: true
        },
        url: {
            required: true,
            url:true
        }
    },
    highlight: function(element) {
    var id_attr = "#" + $( element ).attr("id") + "1";
    $(element).closest('input').removeClass('has-success').addClass('has-error');
    $(id_attr).removeClass('glyphicon-ok').addClass('glyphicon-remove');
    },
    unhighlight: function(element) {
    var id_attr = "#" + $( element ).attr("id") + "1";
    $(element).closest('input').removeClass('has-error').addClass('has-success');
    $(id_attr).removeClass('glyphicon-remove').addClass('glyphicon-ok'); 
    },
    errorPlacement: function(error, element) {} 
});