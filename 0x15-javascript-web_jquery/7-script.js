$.getJSON('https://swapi.co/api/people/5/?format=json', function (oki) {
  $('DIV#character').text(oki.name);
});
