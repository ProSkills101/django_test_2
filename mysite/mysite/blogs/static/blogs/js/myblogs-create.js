$(function() {
    let editor = CKEDITOR.replace('html', { height: 300, width: 'auto'});
  
    let $elSubmitBtn = $('#btnSubmit');
    let $elTitle = $('#title');
    let $elHtml = $('#html');
    $elSubmitBtn.on('click', (evt) => {
      evt.preventDefault();
      let formData = $('form').serializeArray();
      let html = editor.getData();
      formData.push({ name: 'html', value: html });
  
      let token = $("input[name='csrfmiddlewaretoken']").val();
      formData.push({ name: 'csrfmiddlewaretoken', value: token });
  
      $.ajax({
        method: 'POST',
        url: '/blogs/myblogs/create/',
        data: formData
      }).then(function(data) {
        console.log(data)
        let errors = data.errors || {};
        console.log($elTitle.next());
        if (errors.title) $elTitle.addClass('is-invalid');
        if (errors.html) $elHtml.addClass('is-invalid');
  
        if (data.status === 200) window.location.replace('/blogs/myblogs/' + data.blog_id);
      });
    });
  });