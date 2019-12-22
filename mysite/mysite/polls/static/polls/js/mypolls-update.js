$(function() {
    $('.delete-choice-btn').on('click', function(){
      let ans = confirm('Sure?');
      if (ans) {
        let $elDelBtn = $(this);
        let $elDelTokIn = $elDelBtn.prev();
        let question_id = $elDelBtn.data('qid');
        let choice_id = $elDelBtn.data('qcid');
        let token = $elDelTokIn.val();
  
        $.ajax({
          headers: { "X-CSRFToken": token },
          method: "DELETE",
          url: "/polls/mypolls/delete/" + question_id + '/choice/' + choice_id,
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