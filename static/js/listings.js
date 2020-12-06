var thread = null;
$(document).ready(function(){
    $(".nav-tab").click(function(){
        var theater_id = $(this).attr("data-theater-id");
        $("#searchfield").val("");
        var post_dict ={theater_id: theater_id}
        $.post("/get_listings", post_dict, function (data) {
            $("#listingsTable").html(data["movie_listing_details_raw"]);
        });
    });

    $('#searchfield').keydown(function(e) {
        if (e.keyCode == 13) {
            event.preventDefault();
            return false;
        }
    });
    $('#searchfield').keyup(function(e) {
        clearTimeout(thread);
        var $this = $(this); thread = setTimeout(function(){
            var theater_id = $(".nav-tabs .active .nav-tab").attr("data-theater-id");
            var search_term = $("#searchfield").val();
            var post_dict ={theater_id: theater_id, search_term: search_term};
            $.post("/get_listings", post_dict, function (data) {
                $("#listingsTable").html(data["movie_listing_details_raw"]);
            });
        }, 1000);
    });
});