
function update_count(count, elem) {
	elem.nextAll('.count').text('Current Length: ' + count);
}

function tinymce_callback( e ) {
	var charcount = $(tinyMCE.activeEditor.getDoc().body).text().replace('\n', '').replace('\r', '').length;
	update_count(charcount, $('#' + tinyMCE.activeEditor.id));
}

tinyMCE.init({
  mode : "textareas",
	editor_selector : "tinymce",
	handle_event_callback : "tinymce_callback"
});


$(document).ready( function () {
	var counterElems = $('.counter')
	counterElems.each( function (i) {
		elem = $(counterElems[i]);
		
		// insert counter text
		elem.after('<div class="count"></div>');
		
		if ( !elem.hasClass('tinymce') ) {
			elem.keyup( function ( e ) {
				update_count($(this).val().length, elem);
			});
		}
	});
});
