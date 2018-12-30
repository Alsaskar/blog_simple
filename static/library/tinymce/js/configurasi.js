tinymce.init({

    selector: ".textarea",
    theme: "modern",

    plugins: [
        "advlist autolink lists link image charmap print preview anchor",
        "searchreplace visualblocks code fullscreen",
        "insertdatetime media table contextmenu paste codesample media autosave"
    ],

    toolbar: "insertfile undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image codesample restoredraft",
    
    // setup: function(editor){
    //     uploadImageToServer(editor);
    // },

    codesample_languages: [
        {text: 'HTML/XML', value: 'markup'},
        {text: 'JavaScript', value: 'javascript'},
        {text: 'CSS', value: 'css'},
        {text: 'PHP', value: 'php'},
        {text: 'Ruby', value: 'ruby'},
        {text: 'Python', value: 'python'},
        {text: 'Java', value: 'java'},
        {text: 'C', value: 'c'},
        {text: 'C#', value: 'csharp'},
        {text: 'C++', value: 'cpp'}
    ],

    autosave_interval: "10s",

    // image_class_list: [ { title: 'image', value: 'image'} ],

});

// function uploadImageToServer(editor){
//    // create input and insert in the DOM
//    var inp = $('<input id="tinymce-uploader" type="file" name="pic" accept="image/*" style="display:none">');
//    $(editor.getElement()).parent().append(inp);

//    // add the image upload button to the editor toolbar
//    editor.addButton('imageupload', {
//      icon: 'image',
//      onclick: function(e) { // when toolbar button is clicked, open file select modal
//        inp.trigger('click');
//      }
//    });

//    // when a file is selected, upload it to the server
//    inp.on("change", function(e){
//      uploadFile(this, editor);
//    });
//  }

//  function uploadFile(inp, editor) {
//    var file_data = $(inp).prop('files')[0];   
//    var data = new FormData();                  
//    data.append('file', file_data);
    
//    $.ajax({
//      url: '/notlikesoft/proses/image_post.php',
//      type: 'POST',
//      data: data,
//      processData: false, // Don't process the files
//      contentType: false, // Set content type to false as jQuery will tell the server its a query string request
//      success: function(data, textStatus, jqXHR) {
//        data = JSON.parse(data);
//        editor.insertContent('<img class="img-thumbnail" src="' + data.url + '">');
//      },
//      error: function(jqXHR, textStatus, errorThrown) {
//        if(jqXHR.responseText) {
//          errors = JSON.parse(jqXHR.responseText).errors
//          alert('Error uploading image: ' + errors.join(", ") + '. Make sure the file is an image and has extension jpg/jpeg/png.');
//        }
//      }
//    });
//  }

