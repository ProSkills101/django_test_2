$(function() {
    let $elUploadBtn = $('#btnUpload');
    let $elUploadCard = $('#uploadCard');
    $elUploadBtn.on('click', (evt) => {
      evt.preventDefault();
      $elUploadCard.toggleClass('d-none');
    });
  
  
    let token = $("input[name='csrfmiddlewaretoken']").val();
    //console.log(token);
  
    let $elFileinput = $("#userFile");
    $elFileinput.fileinput({
      dropZoneEnabled: false,
      theme: "fa",
      uploadUrl: "/files/fileupload",
      allowedFileTypes: ['image'],
      allowedFileExtensions: ["jpg", "png", "gif"],
      ajaxSettings: {
        headers: { "X-CSRFToken": token },
      },
      uploadExtraData: {
        'desc': '',
        'tag': ''
      }
    });
  
    $elFileinput.on('filebatchpreupload', function(event, data) {
      let desc = $('#inputDesc').val();
      let tag = $('#inputTag').val();
      data.extra.desc = desc;
      data.extra.tag = tag;
      //console.log(data);
    });
  
    $elFileinput.on('fileuploaded', function(event, data) {
      location.reload();
    });
    
  });