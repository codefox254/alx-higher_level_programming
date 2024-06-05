/* global $ */
$(document).ready(function() {
  $('DIV#character').click(function() {
    $.ajax({
      url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
      method: 'GET',
      success: function(response) {
        $('DIV#character').text(response.name);
      },
      error: function(xhr, status, error) {
        console.error('Error fetching character name:', error);
        $('DIV#character').text('Error fetching character name');
      }
    });
  });
});

