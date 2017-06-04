/**
 * Created by Sunny on 4/6/2017.
 */

$(function () {
    $(window).scroll(function () {
        var topPos = $(".content .contact").position().top;
        var objHeight = $(".content .contact").outerHeight();
        var dialogHeight = $(".content .contact .dialog").outerHeight();
        console.log(`topPos=${topPos};objHeight=${objHeight};dialogHeight=${dialogHeight};scrollTop=${$(window).scrollTop()}`);
        console.log($(window).scrollTop() > topPos + objHeight - dialogHeight - 80 - 80);
        console.log($(window).scrollTop());
        console.log($(window).scrollTop());
        if ($(window).scrollTop() > topPos - 80 && $(window).scrollTop() < topPos + objHeight - dialogHeight - 80 - 80) {
            $(".content .contact .dialog").addClass("fixed");
            $(".content .contact .dialog").css({top: '0'});
        } else if ($(window).scrollTop() > topPos + objHeight - dialogHeight - 80 - 80) {
            $(".content .contact .dialog").removeClass("fixed");
            $(".content .contact .dialog").css({top: '780px'});
        } else {
            $(".content .contact .dialog").removeClass("fixed");
            $(".content .contact .dialog").css({top: '0'});
        }

    });

    $('.slick').slick({
        arrows: true,
        dots: true,
        infinite: true,
        speed: 300,
        slidesToShow: 1,
        autoPlay: true,
        dotsClass: 'slick-dots cust-slick-dots ',
        adaptiveHeight: true,
    });
});