(function ($) {

	"use strict";

	// Window Resize Mobile Menu Fix
//	mobileNav();

	// Menu Dropdown Toggle
	if ($('.menu-trigger').length) {
		$(".menu-trigger").on('click', function () {
			$(this).toggleClass('active');
			$('.header-area .nav').slideToggle(200);
		});
	}

	// Menu elevator animation
//	$('a[href*=\\#]:not([href=\\#])').on('click', function () {
//		if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
//			var targetHash = this.hash;
//			var target = $(this.hash);
//			target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
//			if (target.length) {
//				var width = $(window).width();
//				if (width < 991) {
//					$('.menu-trigger').removeClass('active');
//					$('.header-area .nav').slideUp(200);
//				}
//				$('html,body').animate({
//					scrollTop: (target.offset().top)
//				}, 700, 'swing', function () {
//					window.location.hash = targetHash;
//				});
//				return false;
//			}
//		}
//	});

	// Page loading animation
	$(window).on('load', function () {
		if ($('.cover').length) {
			$('.cover').parallax({
				imageSrc: $('.cover').data('image'),
				zIndex: '1'
			});
		}

		$("#preloader").animate({
			'opacity': '0'
		}, 600, function () {
			setTimeout(function () {
				$("#preloader").css("visibility", "hidden").fadeOut();
			}, 300);
		});
	});


	// Window Resize Mobile Menu Fix
//	$(window).on('resize', function () {
//		mobileNav();
//	});


	// Window Resize Mobile Menu Fix
//	function mobileNav() {
		var width = $(window).width();
		$('.infa-ul').on('click', function () {
			if (width < 992) {
				$('.prod-ul ul').removeClass('active');
				$(this).find('ul').toggleClass('active');
			}
		});
		$('.prod-ul').on('click', function () {
			if (width < 992) {
				$('.infa-ul ul').removeClass('active');
				$(this).find('ul').toggleClass('active');
			}
		});
//	}


})(window.jQuery);