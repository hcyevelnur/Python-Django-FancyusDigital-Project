
$(document).ready(function($) {

	"use strict";
});

	var lFollowX = 0,
		lFollowY = 0,
		x = 0,
		y = 0,
		friction = 1 / 30;

	function moveBackground() {
		x += (lFollowX - x) * friction;
		y += (lFollowY - y) * friction;

		translate = 'translateX(' + x + 'px) translateY(' + y +'px)';

		$('.animate-this').css({
		'-webit-transform': translate,
		'-moz-transform': translate,
		'transform': translate
		});

		window.requestAnimationFrame(moveBackground);
	}

	$(window).on('mousemove click', function(e) {
		
		var isHovered = $('.animate-this:hover').length > 0;
		console.log(isHovered);
		
		if(!isHovered) {
			var lMouseX = Math.max(-100, Math.min(100, $(window).width() / 2 - e.clientX)),
					lMouseY = Math.max(-100, Math.min(100, $(window).height() / 2 - e.clientY));

			lFollowX = (20 * lMouseX) / 100;
			lFollowY = (10 * lMouseY) / 100;
		}
	});

	moveBackground();


	

