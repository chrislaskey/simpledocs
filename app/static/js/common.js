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

$(document).ready(function(){
	app.addNavigationLinks();
});
