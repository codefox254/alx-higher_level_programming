/* global $ */
$(function() {
  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    method: 'GET',
    success: function(response) {
      $('DIV#hello').text(response.hello);
    },
    error: function(xhr, status, error) {
      console.error('Error fetching translation:', error);
      $('DIV#hello').text('Error fetching translation');
    }
  });
});

