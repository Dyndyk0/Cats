$(document).ready(function() {
    // Логика удаления сохраненных изображений
    $(".save-button").click(function(event) {
        event.preventDefault();
        var button = $(this);
        var catId = button.data('cat-id');

        $.ajax({
            type: 'DELETE',
            url: '/saved/',
            contentType: 'application/json',
            data: JSON.stringify({
               'cat_id': catId,
                 'csrfmiddlewaretoken': '{{ csrf_token }}'
               }),
            success: function(response) {
                if (response.status === 'success') {
                    button.text('Удалено');
                    button.prop('disabled', true);
                     $('#message').remove();
                } else if (response.status === 'error'){
                   if ($('#message').length) {
                        $('#message').text(response.message);
                    } else {
                        let messageHtml = '<p style="color:red;" id="message">' + response.message + '</p>'
                        $(messageHtml).insertBefore('#cat-container');
                    }
                }
            },
            error: function(error) {
              console.log(error)
            }
        });
    });

    // Показ/скрытие кнопки "наверх"
    $(window).scroll(function() {
        if ($(this).scrollTop() > 100) {
            $('#scroll-to-top').fadeIn();
        } else {
            $('#scroll-to-top').fadeOut();
        }
    });

    // Скролл наверх при клике на кнопку
    $('#scroll-to-top').click(function() {
        $('html, body').animate({ scrollTop: 0 }, 'slow', function() {
            //location.reload();
        });
        return false;
    });
});