/* global $ */
$(document).ready(function() {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    method: 'GET',
    success: function(response) {
      const movies = response.results;
      const list = $('UL#list_movies');
      $.each(movies, function(index, movie) {
        list.append('<li>' + movie.title + '</li>');
      });
    },
    error: function(xhr, status, error) {
      console.error('Error fetching movies:', error);
      $('UL#list_movies').append('<li>Error fetching movies</li>');
    }
  });
});

