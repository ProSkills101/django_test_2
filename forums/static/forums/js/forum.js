$(function() {
    let $elTopicBtn = $('.topic-attach');
    let topicid = $elTopicBtn.data('topicid');
    let topicFormCard = topicid ? '.topic-form-card-' + topicid : '.topic-form-card';
    let $elTopicFormCard = $(topicFormCard);
    $elTopicBtn.on('click', (evt) => {
      evt.preventDefault();
      $elTopicFormCard.toggleClass('d-none');
    });
  
    let $elTopicForm = $('.topic-form')
    let forumid = $elTopicForm.data('forumid');
    let $elSubmitBtn = $elTopicForm.find('.submit');
    let $elTitle = $elTopicForm.find('input[name="title"]');
    let $elHtml = $elTopicForm.find('textarea[name="html"]');
    let editor = CKEDITOR.replace($elHtml[0], { height: 200, width: 'auto'});
    
    $elSubmitBtn.on('click', (evt) => {
      evt.preventDefault();
      let formData = $elTopicForm.serializeArray();
      let html = editor.getData();
      formData.push({ name: 'html', value: html });
  
      //let token = $("input[name='csrfmiddlewaretoken']").val();
      //formData.push({ name: 'csrfmiddlewaretoken', value: token });
  
      $.ajax({
        method: 'POST',
        url: '/forums/forum/' + forumid + '/topic/create/',
        data: formData
      }).then(function(data) {
        console.log(data)
        let errors = data.errors || {};
        console.log($elTitle.next());
        if (errors.title) $elTitle.addClass('is-invalid');
        if (errors.html) $elHtml.addClass('is-invalid');
  
        if (data.status === 200) location.reload();
      });
    });
  });