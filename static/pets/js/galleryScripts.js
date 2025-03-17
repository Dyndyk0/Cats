$(document).ready(function() {
    // Логика сохранения изображений
    $(".save-button").click(function(event) {
        event.preventDefault();
        var button = $(this);
        var catId = button.data('cat-id');
        var catUrl = button.data('cat-url');

        $.ajax({
            type: 'POST',
            url: 'https://doalexey.pythonanywhere.com/',
            data: {
                'cat_id': catId,
                'url': catUrl,
                'csrfmiddlewaretoken': '{{ csrf_token }}'
            },
           success: function(response) {
                if (response.status === 'success') {
                    button.text('Сохранено');
                    button.prop('disabled', true);
                    $('#message').remove();
                } else if (response.status === 'error'){
                    // display error message
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

    // Логика перезагрузки страницы
    $("#reload-button").click(function() {
        location.reload();
    });

    // Показ/скрытие кнопки "наверх"
    $(window).scroll(function() {
        if ($(this).scrollTop() > 100) {
            $('#scroll-to-top').fadeIn();
        } else {
            $('#scroll-to-top').fadeOut();
        }
    });

    // Скролл наверх при клике на кнопку и обновление страницы
    $('#scroll-to-top').click(function() {
        $('html, body').animate({ scrollTop: 0 }, 'slow', function() {
            //location.reload();
        });
        return false;
    });
});