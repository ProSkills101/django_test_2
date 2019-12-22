$(function() {
    $('#blog-table').on('click', '.delete-btn', (evt) => {
      evt.preventDefault();
      let ans = confirm('Sure?');
      if (!ans) return;
  
      let blogId = $(evt.target).data('blogid');
      $.ajax({
        method: 'DELETE',
        url: '/blogs/myblogs/delete/' + blogId + '/',
        data: {}
      }).then(function(data) {
        if (data.status === 200) window.location.reload();
      });
    });
  });