$(function() {
    let $elTopicBtn = $('.forum-topic-btn');
    $elTopicBtn.each(function(idx) {
      let $el = $(this);
      let topicid = $el.data('topicid');
      let topicFormCard = topicid ? '.topic-form-card-' + topicid : '.topic-form-card';
      let $elTopicFormCard = $(topicFormCard);
      $el.on('click', (evt) => {
        evt.preventDefault();
        $elTopicFormCard.toggleClass('d-none');
      });
    });
    
    let $elTopicForm = $('.topic-form');
    $elTopicForm.each(function(idx) {
      let $el = $(this);  
      let forumid = $el.data('forumid');
      let topicid = $el.data('topicid');
      let $elSubmitBtn = $el.find('.submit');
      let $elTitle = $el.find('input[name="title"]');
      let $elHtml = $el.find('textarea[name="html"]');
      let editor = CKEDITOR.replace($elHtml[0], { height: 200, width: 'auto'});
  
      $elSubmitBtn.on('click', (evt) => {
        evt.preventDefault();
        let formData = $el.serializeArray();
        let html = editor.getData();
        formData.push({ name: 'html', value: html });
  
        //let token = $("input[name='csrfmiddlewaretoken']").val();
        //formData.push({ name: 'csrfmiddlewaretoken', value: token });
  
        $.ajax({
          method: 'POST',
          url: '/forums/forum/' + forumid + '/topic/' + topicid + '/update/',
          data: formData
        }).then(function(data) {
          console.log(data)
          let errors = data.errors || {};
          if (errors.title) $elTitle.addClass('is-invalid');
          if (errors.html) $elHtml.addClass('is-invalid');
  
          if (data.status === 200) location.reload();
        });
      });
    });
  
    // posts
    
    let $elPostBtn = $('.forum-post-btn');
    $elPostBtn.each(function(idx) {
      let $el = $(this);
      let postid = $el.data('postid');
      let postFormCard = postid ? '.post-form-card-' + postid : '.post-form-card';
      let $elPostFormCard = $(postFormCard);
      $el.on('click', (evt) => {
        evt.preventDefault();
        $elPostFormCard.toggleClass('d-none');
      });
    });
    
    let $elPostForm = $('.post-form');
    $elPostForm.each(function(idx) {
      let $el = $(this);  
      let forumid = $el.data('forumid');
      let topicid = $el.data('topicid');
      let postid = $el.data('postid');
      let $elSubmitBtn = $el.find('.submit');
      let $elHtml = $el.find('textarea[name="html"]');
      let editor = CKEDITOR.replace($elHtml[0], { height: 200, width: 'auto'});
  
      $elSubmitBtn.on('click', (evt) => {
        evt.preventDefault();
        let formData = $el.serializeArray();
        let html = editor.getData();
        formData.push({ name: 'html', value: html });
  
        //let token = $("input[name='csrfmiddlewaretoken']").val();
        //formData.push({ name: 'csrfmiddlewaretoken', value: token });
  
        let url = postid ? '/forums/forum/' + forumid + '/topic/' + topicid + '/post/' + postid + '/update/'
          : '/forums/forum/' + forumid + '/topic/' + topicid + '/post/create/';
  
        $.ajax({
          method: 'POST',
          url,
          data: formData
        }).then(function(data) {
          console.log(data)
          let errors = data.errors || {};
          if (errors.html) $elHtml.addClass('is-invalid');
  
          if (data.status === 200) location.reload();
        });
      });
    });
    
  });