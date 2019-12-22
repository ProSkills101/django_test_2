$(function() {
    let editor = CKEDITOR.replace('html', { height: 300, width: 'auto'});
  
    let $elUpdateBtn = $('#btnUpdate');
    let $elCancelBtn = $('#btnCancel');
    let $elBlogView = $('.blog-view');
    let $elBlogEdit = $('.blog-edit');
    $elUpdateBtn.on('click', (evt) => {
      evt.preventDefault();
      $elBlogView.toggleClass('d-none');
      $elBlogEdit.toggleClass('d-none');
    });
    $elCancelBtn.on('click', (evt) => {
      evt.preventDefault();
      $elBlogView.toggleClass('d-none');
      $elBlogEdit.toggleClass('d-none');
    });
  
    let $elForm = $('form');
    let $elSubmitBtn = $elForm.find('#btnSubmit');
    let $elTitle = $elForm.find('#title');
    let $elHtml = $elForm.find('#html');
    let blogId = $elForm.data('blogid')
    $elSubmitBtn.on('click', (evt) => {
      evt.preventDefault();
      let formData = $elForm.serializeArray();
      let html = editor.getData();
      formData.push({ name: 'html', value: html });
  
      let token = $("input[name='csrfmiddlewaretoken']").val();
      formData.push({ name: 'csrfmiddlewaretoken', value: token });
  
      $.ajax({
        method: 'POST',
        url: '/blogs/myblogs/update/' + blogId + '/',
        data: formData
      }).then(function(data) {
        console.log(data)
        let errors = data.errors || {};
        console.log($elTitle.next());
        if (errors.title) $elTitle.addClass('is-invalid');
        if (errors.html) $elHtml.addClass('is-invalid');
  
        if (data.status === 200) window.location.replace('/blogs/myblogs/' + blogId);
      });
    });
  });