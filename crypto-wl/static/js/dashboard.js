$(function () {
  $("#content_wrapper").on("submit", "#crypto_form", function (event) {
    event.preventDefault();
    $.ajax({
      type: "POST",
      data: {
        form:  $(this).serialize(),
        csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').attr(
          "value"
        ),
      dataType: "json",
      error: function (request, error) {
        console.log(arguments);
        console.log(" Can't do because: " + error);
      },
      success: function (data) {
        $("#crypto_form").reset();
        $("#msg_queue").html(data.msg_list);
        $("#wactchlist_wrapper").html(data.html);
      },
    });
  });

  $("#id_name").chosen({no_results_text: "Oops, nothing found!"}); 
});