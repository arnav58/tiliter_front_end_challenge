$(document).ready(function(){
    $(".nav-tab").click(function(){
        var theater_id = $(this).attr("data-theater-id");
        var post_dict ={theater_id: theater_id}
        $.post("/get_listings", post_dict, function (data) {
            $("#listingsTable").html(data["movie_listing_details_raw"]);
        })
    });
});