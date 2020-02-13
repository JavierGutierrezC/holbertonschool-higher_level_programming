$.getJSON('https://swapi.co/api/films/?format=json', function (data) {
  let x;
  for (x = 0; x < data.results.length; x++) {
    $('UL#list_movies').append('<li></li>').text(data.results[x].title);
  }
});
