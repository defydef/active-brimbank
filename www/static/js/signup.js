$(function () {
  $(".js-signup").click(function () {
    $.ajax({
      url: '/signup_ajax_form/',
      type: 'get',
      dataType: 'json',
      // beforeSend: function () {
      //   $("#modal-signup").modal("show");
      // },
      success: function (data) {
        $("#modal-signup .modal-content").html(data.html_form);
      }
    });
  });

});

$("#modal-signup").on("submit", ".js-signup-submit", function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
        $("#modal-progress").modal("hide");
        $("#modal-confirmation").modal("show");
        }
        else {
          $("#modal-progress").modal("hide");
          $("#modal-signup .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  });