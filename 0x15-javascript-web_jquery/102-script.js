$(document).ready(function () {
  const inputValue = $('INPUT#language_code').val();
  const fullUrl = 'https://fourtonfish.com/hellosalut/' + `?lang=${inputValue}`;
  $('INPUT#btn_translate').click(function () {
    $.ajax({
      type: 'GET',
      url: fullUrl,
      success: function (word) {
        $('DIV#hello').text(word.hello);
      },
    });
  });
});
