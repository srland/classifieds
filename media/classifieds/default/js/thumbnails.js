function setThumbnails() {
	img = $(document.createElement('img'));
	img.addClass('thumb-img');
	$('.thumbnail').mouseover( function (e) {
		img.attr({src: $(this).parent().attr('href')});
		img.css({display: 'none'});
		img.load( function () {
			var x = Math.max(0, e.pageX-(img.attr('width')/2));
			var y = Math.max(0, e.pageY-(img.attr('height')/2));
			img.css({position: 'absolute', left: x + 'px', top: y + 'px'});
			$('#allcontent').after(img);
			img.fadeIn("fast");
		});
		img.mouseout( function () { $('.thumb-img').hide(); } );
	});
}

$(document).ready(setThumbnails);
