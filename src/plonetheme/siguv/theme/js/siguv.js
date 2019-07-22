$(document).ready(function () {

  $('.nav-toggler').on('click', function () {
    $('#collapsible-nav').toggleClass('active');
  });

  $('.nav-toggler').draggable({
    start: function (event, ui) {
      $('#collapsible-nav').addClass('active');
    },
  });

});
