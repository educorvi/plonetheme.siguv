$(document).ready(function () {

  // Open Sidebar

  $('.navigation-handle').on('click', function (e) {
    $('#siguv-navigation').toggleClass('active');
  });

  // Open Dropdown Menu

  $('.nav-item').hover(function (e) {
    $(this).parent().find('.nav-item').removeClass('show');
    if ($(this).hasClass('dropdown')) {
      $(this).addClass('show');
    }
  });

  $(document).on('click', function (e) {
    if ($(e.target).is('.nav-item') === false) {
      $('.nav-item').removeClass('show');
    }
  });

});
