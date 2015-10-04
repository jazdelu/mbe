$(document).ready(function(){

	// hide #back-top first
	$("#cd-top").hide();
	
	// fade in #back-top
	$(function () {
		$(window).scroll(function () {
			if ($(this).scrollTop() > 100) {
				$('#cd-top').fadeIn();
			} else {
				$('#cd-top').fadeOut();
			}
		});

		// scroll body to 0px on click
		$('#cd-top a').click(function () {
			$('body,html').animate({
				scrollTop: 0
			}, 800);
			return false;
		});
	});

});