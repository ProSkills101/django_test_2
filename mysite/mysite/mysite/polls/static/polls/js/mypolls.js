$(function() {
    $('.delete-btn').on('click', function(){
      let ans = confirm('Sure?');
      if (ans) {
        let $elDelBtn = $(this);
        let $elDelTokIn = $elDelBtn.prev();
        let question_id = $elDelBtn.data('qid');
        let token = $elDelTokIn.val();
  
        $.ajax({
          headers: { "X-CSRFToken": token },
          method: "DELETE",
          url: "/polls/mypolls/delete/" + question_id,
          data: {},
          dataType: 'json',
        })
        .done(function(data) {
          console.log(data);
          location.reload();
        });
      }
    });
  });