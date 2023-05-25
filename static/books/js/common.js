$(function(){
    // header 삽입
    $("header").load("../inc/header.html");

    // footer 삽입
    $("footer").load("../inc/footer.html");
    
    // video size
    var wid = $(document).width();
    var hei = wid / 16 * 9;
    $(".video-wrap iframe").height(hei);
});