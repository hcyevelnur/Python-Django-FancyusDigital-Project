$(document).ready(function($) {

	"use strict";

	var a = 0;
	var b = 0;
	$(window).on('scroll', function() {

	var oTop2 = $('#progress_bar').offset().top - window.innerHeight;
	if (b === 0 && $(window).scrollTop() > oTop2) {
		$(".skill-bar").each(function(){
		  $(this).find(".skill-bar-inner").animate({
			width: $(this).attr("data-width")
		  },3000);
		});
	}
	});

});