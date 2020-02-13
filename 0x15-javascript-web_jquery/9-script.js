$.getJSON('https://fourtonfish.com/hellosalut/?lang=fr', function (oki) {
  $('#hello').text(oki.hello);
});
