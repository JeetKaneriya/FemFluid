import '../css/bootstrap.min.css';
import '../css/font-awesome.css';
import '../css/main.css';
import '../css/home.css';

(function ($) {

	"use strict";

    window.sr = new scrollReveal();

  // script for application animation starts
  var cw = $('.image-lid').width();
  $('.image-lid').css({'height':cw+'px'});

  $(window).on('resize', function () {
      var cw = $('.image-lid').width();
      $('.image-lid').css({'height':cw+'px'});
  });
  // script for application animation ends

  $(document).ready(function () {
    $('a[href^="#welcome"]').addClass('active');

    $(window).scroll(function (event) {
        var scrollPos = $(document).scrollTop() + 80;

        if (scrollPos === 0) {
            $('a[href^="#welcome"]').addClass('active');
            return;
        }
        $('.menu-item').not('[href=""]').not('[href*="_"]').not('[href*="paste"]').not('[href*="dev"]').not('[href*="test"]').not('[href*="prod"]').not('[href="javascript:;"]').each(function () {
            var currLink = $(this);
            var refElement = $(currLink.attr("href"));

            if (refElement.position().top <= scrollPos && refElement.position().top + refElement.height() > scrollPos) {
                $('.menu-item').removeClass("active");
                currLink.addClass("active");
            } else {
                currLink.removeClass("active");
            }
        });
    })
});

  //responsive header script
  var done = 0;
  $(window).scroll(function () {
    var scroll = $(window).scrollTop();
    var header = 1;
    if ($(window).width()>=992){
        if (scroll >= header) {
            headerDown();
        }
        else if (done) {
            headerUp();
        }
    }
    });

    function headerDown(){
        $(".header-area .main-nav .logo").css({
            'height': '32px',
            'margin-left': '0px',
            'transform': 'translateX(0%)',
            'margin-top': '17px',
            'float': 'left',
        });
        $(".header-area").css({
            'position': 'absolute',
            'height': '80px',
        });
        if(!done){
            $(".header-area .main-nav .nav").css({
                'margin-top': '60px',
                'opacity': '0',
            });
            $(".header-area .main-nav .nav").delay(100).animate({
                'opacity': '1',
                'margin-top': '5px',
                'margin-bottom': '0px',
            },{duration: 300});
            $(".header-area .main-nav .nav").delay(0).animate({
                'margin-top': '20px',
            },{duration: 300});
            $(".header-area .social li").css({
                'opacity':'0',
                'margin-top': '17px',
            });
            $(".header-area .social li").delay(150).animate({
                'opacity': '1',
            },{duration: 1000});
            done = 1;
        }
        $(".header-area .main-nav .nav").css({
            'margin-left': '11%',
            'position':'relative',
            'transform': 'translateX(0%)',
        });
        $(".header-area hr").css({
            'display': 'none',
        });
        $(".background-header").css({
            'height': '80px',
        });
        $(".slideshow-container ").css({
            'padding-top': '80px',
        });
    }

    function headerUp(){
        $(".header-area .main-nav .nav").stop();
        $(".header-area .main-nav .logo").css({
                'height': '100px',
                'margin-left': '50%',
                'transform': 'translateX(-50%)',
                'margin-top': '30px',
                'float': 'none',
            });
            $(".header-area").css({
                'position': 'relative',
            });
            $(".header-area .main-nav .nav").css({
                'position': 'absolute',
                'margin-left': '30%',
                'transform': 'translateX(-19%)',
                'margin-bottom': '10px',
                'opacity': '0',
            });
            if(done){
                $(".header-area .main-nav .nav").delay(0).animate({
                    'margin-top': '10px',
                },{duration: 0});
                $(".header-area .main-nav .nav").delay(50).animate({
                    'opacity': '1',
                });
                $(".header-area .social").css({'opacity': '0'});
                $(".header-area .social").delay(200).animate({
                    'opacity': '1',
                });
                done = 0;
            }
            $(".header-area hr").css({
                'display': 'block',
            });
            $(".header-area .social").css({
                'margin-top': '0',
            });
            $(".header-area .social li").css({
                'margin-top': '6px',
            });
            $(".background-header").css({
                'height': '221px',
            });
            $(".slideshow-container ").css({
                'padding-top': '221px',
            });
    }

})(window.jQuery);

var slideIndex = 0;
showSlides();

function showSlides() {
  var i;
  var slides = document.getElementsByClassName("mySlideshow");
  var dots = document.getElementsByClassName("dot");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";  
  }
  slideIndex++;
  if (slideIndex > slides.length) {slideIndex = 1}    
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" actived", "");
  }
  slides[slideIndex-1].style.display = "block";  
  dots[slideIndex-1].className += " actived";
  setTimeout(showSlides, 4000); // Change image every 2 seconds
}