
$(document).ready(function($) {

	"use strict";

	$(window).ready(function(){
		$('.loader-box-one, .loader-box-two').fadeOut();
		$('body').removeClass('fixed');
   });

	new WOW().init(); 

	$(window).on( 'scroll', function(){
		if ($(window).scrollTop() >= 100) {
		  $('.site-header-one').addClass('sticky-header-one');
		 }
		 else {
		  $('.site-header-one').removeClass('sticky-header-one');
		 }
	});
	$(window).on( 'scroll', function(){
		if ($(window).scrollTop() >= 100) {
		  $('.site-header-two').addClass('sticky-header-two');
		 }
		 else {
		  $('.site-header-two').removeClass('sticky-header-two');
		 }
	});

	$(".search-icon-one a").on( 'click', function(){
		$(".search-input-one").fadeToggle(300);
		$(".search-input-one .black-shadow-one").fadeIn();
	});
	$(".search-input-one .black-shadow-one").on( 'click', function(){
		$(this).fadeOut();
		$(".search-input-one").fadeOut(300);
	});
	$(".search-icon-two a").on( 'click', function(){
		$(".search-input-two").fadeToggle(300);
		$(".search-input-two .black-shadow-two").fadeIn();
	});
	$(".search-input-two .black-shadow-two").on( 'click', function(){
		$(this).fadeOut();
		$(".search-input-two").fadeOut(300);
	});

	$('.partners-slider').slick({
		infinite: true,
		slidesToShow: 6,
		slidesToScroll: 1,
		prevArrow: '<button class="slick-arrow-team prev-arrow"><i class="fa fa-chevron-left" aria-hidden="true"></i></button>',
		nextArrow: '<button class="slick-arrow-team next-arrow"><i class="fa fa-chevron-right" aria-hidden="true"></i></button>',
		dots: false,
		arrows: false,
		autoplay: true,
		autoplaySpeed: 2000,
		responsive: [
		  {
			  breakpoint: 1200,
			  settings: {
				  slidesToShow: 4,
			  }
		  },
		  {
			  breakpoint: 992,
			  settings: {
				  slidesToShow: 3,
			  }
		  },
		  {
			  breakpoint: 768,
			  settings: {
				  slidesToShow: 3,
			  }
		  },
		  {
			breakpoint: 576,
			settings: {
				slidesToShow: 2,
			}
		  },
		  {
			  breakpoint: 376,
			  settings: {
				  slidesToShow: 1,
			  }
		  }
	  ]
	  });

	$('.team-slider').slick({
		infinite: true,
		slidesToShow: 4,
		slidesToScroll: 1,
		prevArrow: '<button class="slick-arrow prev-arrow color-arrow"><i class="fa fa-chevron-left"></i></button>',
		nextArrow: '<button class="slick-arrow next-arrow color-arrow"><i class="fa fa-chevron-right"></i></button>',
		arrows: false,
		dots: true,
		autoplay: true,
		autoplaySpeed: 2000,
		responsive: [
		  {
			  breakpoint: 1200,
			  settings: {
				  slidesToShow: 3,
			  }
		  },
		  {
			  breakpoint: 992,
			  settings: {
				  slidesToShow: 3,
			  }
		  },
		  {
			  breakpoint: 768,
			  settings: {
				  slidesToShow: 2,
			  }
		  },
		  {
			breakpoint: 576,
			settings: {
				slidesToShow: 1,
			}
		  },
		  {
			  breakpoint: 376,
			  settings: {
				  slidesToShow: 1,
			  }
		  }
	  ]
	  });

	$('.testimonial-slider-one').slick({
		infinite: true,
		slidesToShow: 2,
		slidesToScroll: 1,
		prevArrow: '<button class="slick-arrow prev-arrow color-arrow"><i class="fa fa-chevron-left"></i></button>',
		nextArrow: '<button class="slick-arrow next-arrow color-arrow"><i class="fa fa-chevron-right"></i></button>',
		arrows: false,
		dots: true,
		autoplay: true,
		autoplaySpeed: 2000,
		responsive: [
		  {
			  breakpoint: 1200,
			  settings: {
				  slidesToShow: 2,
			  }
		  },
		  {
			  breakpoint: 992,
			  settings: {
				  slidesToShow: 2,
			  }
		  },
		  {
			  breakpoint: 768,
			  settings: {
				  slidesToShow: 1,
			  }
		  },
		  {
			  breakpoint: 376,
			  settings: {
				  slidesToShow: 1,
			  }
		  }
	  ]
	  });

	$('.testimonial-slider-two').slick({
		infinite: true,
		slidesToShow: 1,
		slidesToScroll: 1,
		prevArrow: '<button class="slick-arrow prev-arrow color-arrow"><i class="fa fa-chevron-left"></i></button>',
		nextArrow: '<button class="slick-arrow next-arrow color-arrow"><i class="fa fa-chevron-right"></i></button>',
		arrows: false,
		dots: true,
		autoplay: true,
		autoplaySpeed: 2000,
		responsive: [
		  {
			  breakpoint: 1200,
			  settings: {
				  slidesToShow: 1,
			  }
		  },
		  {
			  breakpoint: 992,
			  settings: {
				  slidesToShow: 1,
			  }
		  },
		  {
			  breakpoint: 768,
			  settings: {
				  slidesToShow: 1,
			  }
		  },
		  {
			  breakpoint: 376,
			  settings: {
				  slidesToShow: 1,
			  }
		  }
	  ]
	  });

		$(".toggle-button-one").on( 'click', function(){
			$(".main-navigation-one").toggleClass('toggle-menu-one');
			$(".header-menu-one .black-shadow-one").fadeToggle();
		});
		$(".main-navigation-one ul li a").on( 'click', function(){
			$(".main-navigation-one").removeClass('toggle-menu-one');
			$(".header-menu-one .black-shadow-one").fadeOut();
		});
		$(".main-navigation-one ul li.sub-items-one>a").on( 'click', function(){
			$(".main-navigation-one").addClass('toggle-menu-one');
			$(".header-menu-one .black-shadow-one").stop();
		});
		$(".header-menu-one .black-shadow-one").on( 'click', function(){
			$(this).fadeOut();
			$(".main-navigation-one").removeClass('toggle-menu-one');
		});
		$(".toggle-button-two").on( 'click', function(){
			$(".main-navigation-two").toggleClass('toggle-menu-two');
			$(".header-menu-two .black-shadow-two").fadeToggle();
		});
		$(".main-navigation-two ul li a").on( 'click', function(){
			$(".main-navigation-two").removeClass('toggle-menu-two');
			$(".header-menu-two .black-shadow-two").fadeOut();
		});
		$(".main-navigation-two ul li.sub-items-two>a").on( 'click', function(){
			$(".main-navigation-two").addClass('toggle-menu-two');
			$(".header-menu-two .black-shadow-two").stop();
		});
		$(".header-menu-two .black-shadow-two").on( 'click', function(){
			$(this).fadeOut();
			$(".main-navigation-two").removeClass('toggle-menu-two');
		});

		if ($(window).width() < 992) {

			$('body').on('click', '.main-navigation-one ul li.sub-items-one>a', function() {
				if (($(this).parent().hasClass('active-sub-menu-one'))) {
				$(this).parent().removeClass('active-sub-menu-one');
				$(this).parent().find('ul').slideUp();
				} else {
					$(this).parent().addClass('active-sub-menu-one');
					$(this).parent().find('ul').slideDown();
				}
			});
			$('body').on('click', '.main-navigation-two ul li.sub-items-two>a', function() {
				if (($(this).parent().hasClass('active-sub-menu-two'))) {
				$(this).parent().removeClass('active-sub-menu-two');
				$(this).parent().find('ul').slideUp();
				} else {
					$(this).parent().addClass('active-sub-menu-two');
					$(this).parent().find('ul').slideDown();
				}
			});

			$('.portfolio-slider-one').slick({
			infinite: true,
			slidesToShow: 2,
			slidesToScroll: 1,
			prevArrow: '<button class="slick-arrow prev-arrow color-arrow"><i class="fa fa-chevron-left"></i></button>',
			nextArrow: '<button class="slick-arrow next-arrow color-arrow"><i class="fa fa-chevron-right"></i></button>',
			dots: true,
			arrows: false,
			autoplay: false,
				autoplaySpeed: 2000,	
				responsive: [
				{
					breakpoint: 768,
					settings: {
						slidesToShow: 2,
					}
				},
				{
					breakpoint: 576,
					settings: {
						slidesToShow: 1,
					}
				}
			]	
			});

			$('.blog-slider-one').slick({
				infinite: true,
				slidesToShow: 2,
				slidesToScroll: 1,
				prevArrow: '<button class="slick-arrow prev-arrow color-arrow"><i class="fa fa-chevron-left"></i></button>',
				nextArrow: '<button class="slick-arrow next-arrow color-arrow"><i class="fa fa-chevron-right"></i></button>',
				dots: true,
				arrows: false,
				autoplay: false,
					autoplaySpeed: 2000,	
					responsive: [
					{
						breakpoint: 768,
						settings: {
							slidesToShow: 1,
						}
					},
					{
						breakpoint: 576,
						settings: {
							slidesToShow: 1,
						}
					}
				]	
				});

			$('.pricing-slider-two').slick({
				infinite: true,
				slidesToShow: 2,
				slidesToScroll: 1,
				prevArrow: '<button class="slick-arrow prev-arrow color-arrow"><i class="fa fa-chevron-left"></i></button>',
				nextArrow: '<button class="slick-arrow next-arrow color-arrow"><i class="fa fa-chevron-right"></i></button>',
				dots: true,
				arrows: false,
				autoplay: false,
					autoplaySpeed: 2000,	
					responsive: [
					{
						breakpoint: 768,
						settings: {
							slidesToShow: 1,
						}
					},
					{
						breakpoint: 576,
						settings: {
							slidesToShow: 1,
						}
					}
				]	
				});

		}

	$('.portfolio-slider-two').slick({
		infinite: true,
		slidesToShow: 3,
		slidesToScroll: 1,
		prevArrow: '<button class="slick-arrow prev-arrow color-arrow"><i class="fa fa-chevron-left"></i></button>',
		nextArrow: '<button class="slick-arrow next-arrow color-arrow"><i class="fa fa-chevron-right"></i></button>',
		arrows: false,
		dots: true,
		autoplay: true,
		autoplaySpeed: 2000,
		responsive: [
		  {
			  breakpoint: 1200,
			  settings: {
				  slidesToShow: 2,
			  }
		  },
		  {
			  breakpoint: 992,
			  settings: {
				  slidesToShow: 2,
			  }
		  },
		  {
			  breakpoint: 768,
			  settings: {
				  slidesToShow: 2,
			  }
		  },
		  {
			breakpoint: 576,
			settings: {
				slidesToShow: 1,
			}
		},
		  {
			  breakpoint: 376,
			  settings: {
				  slidesToShow: 1,
			  }
		  }
	  ]
	  });

	$('.my-work-slider').slick({
		infinite: true,
		slidesToShow: 3,
		slidesToScroll: 1,
		prevArrow: '<button class="slick-arrow prev-arrow color-arrow"><i class="fa fa-chevron-left"></i></button>',
		nextArrow: '<button class="slick-arrow next-arrow color-arrow"><i class="fa fa-chevron-right"></i></button>',
		arrows: false,
		dots: true,
		autoplay: true,
		autoplaySpeed: 2000,
		responsive: [
		  {
			  breakpoint: 1200,
			  settings: {
				  slidesToShow: 3,
			  }
		  },
		  {
			  breakpoint: 992,
			  settings: {
				  slidesToShow: 2,
			  }
		  },
		  {
			  breakpoint: 768,
			  settings: {
				  slidesToShow: 2,
			  }
		  },
		  {
			breakpoint: 576,
			settings: {
				slidesToShow: 1,
			}
		},
		  {
			  breakpoint: 376,
			  settings: {
				  slidesToShow: 1,
			  }
		  }
	  ]
	  });
   
});