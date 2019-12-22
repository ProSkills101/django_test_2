$(function() {
    let $elUpdateBtn = $('#btnUpdate');
    $elUpdateBtn.on('click', (evt) => {
      evt.preventDefault();
      let formData = $('form').serializeArray();
  
      let token = $("input[name='csrfmiddlewaretoken']").val();
      formData.push({ name: 'csrfmiddlewaretoken', value: token });
  
      $.ajax({
        method: 'POST',
        url: '/data/admin/nba/players/update/',
        data: formData
      }).then(function(data) {
        console.log(data)
        if (data.status === 200) window.location.reload();
      });
    });
  });