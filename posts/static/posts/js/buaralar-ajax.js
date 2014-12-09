$(document).ready(function() {

    $('.btn-view_details').click(function(){
        var thisButton = this;
        var postid = $(thisButton).attr("data-postid");
        url_event_wAjax = '/posts/event_wAjax/' + postid;
        $.get(url_event_wAjax, {}, function(data){
            $('div.post-list').children('.selected').removeClass('selected');
            $(thisButton).closest('div.post-event').addClass('selected');
            $('#div_selected_post').html(data);
        });
    });
});

