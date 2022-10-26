$.ajax({
  type: 'GET',
  url: 'https://swapi-api.hbtn.io/api/films/?format=json',
  success: function (films) {
    const finalResult = films.results;
    $.each(finalResult, function (i, result) {
      $('UL#list_movies').append('<li>' + result.title + '</li>');
    });
  },
});
