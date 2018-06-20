$('#filter-button').click(function(){
    if(!$('#filters').hasClass('open')) {
        $(this).html('Close Filters')
        $('#filters').addClass('open')
    } else {
        $(this).html('Show Filters')
        $('#filters').removeClass('open')
    }
    $('#filters').slideToggle('slow')
});
