var app = {}

app.addNavigationLinks = function(){
	$('nav.primary')
		.find('select')
		.each(function(){
			$(this).on('change', function(e){
				var value = $(this).val();
				if( value ){ window.location = value; }
			});
		});
}

app.addPageResize = function(){
	var button = $('#button-resize'),
		body = $('body'),
		cookie = $.cookie('resize');

	if( ! cookie ) {
		body.addClass('fixed');
		$.cookie('resize', 'fixed', { expires: 30, path: '/' });
	}else{
		body.addClass(cookie);
	}

	button.on('click', function(){
		cookie = $.cookie('resize');

		if( cookie == 'fluid' ){
			body
				.addClass('fixed')
				.removeClass('fluid');
			$.cookie('resize', 'fixed', { expires: 30, path: '/' });
		}else{
			body
				.addClass('fluid')
				.removeClass('fixed');
			$.cookie('resize', 'fluid', { expires: 30, path: '/' });
		}
	});
}


// Document ready

$(document).ready(function(){
	app.addNavigationLinks();
	app.addPageResize();
});
