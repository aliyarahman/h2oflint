$(document).ready(function() {
});



 $('document').ready(function () {
      $("#id_wants_to_volunteer").on('change', function (e) {
          var volunteer = ($(this).val());
          if (volunteer == 'False') {
            $('.volunteer-questions').slideUp();
          }
          else {
            $('.volunteer-questions').slideDown(); 
          }
      });

      $("#id_making_donation").on('change', function (e) {
          var volunteer = ($(this).val());
          if (volunteer == 'False') {
            $('.donation-questions').slideUp();
          }
          else {
            $('.donation-questions').slideDown(); 
          }
      });

      $("#id_doing_park_and_serve").on('change', function (e) {
          var volunteer = ($(this).val());
          if (volunteer == 'False') {
            $('.parkandserve-questions').slideUp();
          }
          else {
            $('.parkandserve-questions').slideDown(); 
          }
      });

  });