$(document).ready(function() {
    
    $('div.post-event').click(function(){
        var thisDiv = this;
        var postid = $(thisDiv).attr("data-postid");
        url_event_wAjax = '/posts/event_wAjax/' + postid;
        $.get(url_event_wAjax, {}, function(data){
            $('div.post-list').children('.selected').removeClass('selected');
            $(thisDiv).addClass('selected');
            $('#div_selected_post').html(data);
        });
    });
});

