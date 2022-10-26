$.ajax({
  type: 'GET',
  url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
  success: function (user) {
    $('DIV#character').text(user.name);
  },
});
