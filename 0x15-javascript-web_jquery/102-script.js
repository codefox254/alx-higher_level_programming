$(document).ready(function() {
  $('#btn_translate').click(function() {
    const languageCode = $('#language_code').val();
    $.ajax({
      url: 'https://www.fourtonfish.com/hellosalut/hello/',
      data: { lang: languageCode },
      method: 'GET',
      success: function(response) {
        $('#hello').text(response.hello);
      },
      error: function(xhr, status, error) {
        console.error('Error fetching translation:', error);
        $('#hello').text('Error fetching translation');
      }
    });
  });
});

