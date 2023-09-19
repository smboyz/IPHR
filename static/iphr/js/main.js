$(document).ready(function () {

    $(".owl-carousel").each(function () {
        $(this).owlCarousel({
            autoPlay: true,
            items: 1, //10 items above 1000px browser width
            loop: true,
            autoplay: true,

            autoplayTimeout: 3000,



        });
    });
    // Custom Navigation Events
    $(".next").click(function () { $(this).closest('.span12').find('.owl-carousel').trigger('owl.next'); })
    $(".prev").click(function () { $(this).closest('.span12').find('.owl-carousel').trigger('owl.prev'); })
});
$(document).ready(function () {

    $("#owl-demo-1").each(function () {
        $(this).owlCarousel({
            items: 4, //10 items above 1000px browser width
            loop: true,
            autoplay: true,
            nav: true,
            dots: true,
            margin: 14,
            center: false,
            

            autoplayTimeout: 3000,

        });
    });
    // Custom Navigation Events
    $(".next").click(function () { $(this).closest('.span12').find('.owl-carousel').trigger('owl.next'); })
    $(".prev").click(function () { $(this).closest('.span12').find('.owl-carousel').trigger('owl.prev'); })
});
$(document).ready(function () {

    $("#owl-demo-2").each(function () {
        $(this).owlCarousel({
            items: 2, //10 items above 1000px browser width
            loop: true,
            autoplay: true,
            nav: true,
            dots: true,

            autoplayTimeout: 3000,

        });
    });
    // Custom Navigation Events
    $(".next").click(function () { $(this).closest('.span12').find('.owl-carousel').trigger('owl.next'); })
    $(".prev").click(function () { $(this).closest('.span12').find('.owl-carousel').trigger('owl.prev'); })
});
