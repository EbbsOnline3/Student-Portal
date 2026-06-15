window.onload = function() {
    const sidenavLinks = document.querySelectorAll('.sidenav a');
    sidenavLinks.forEach(link => {
        link.addEventListener('click', function() {
            sidenavLinks.forEach(l => l.classList.remove('side-active'));
            this.classList.add('side-active');
        });
    });
    
    $('#myModal').modal('show');
    $('#word-form').hide();
    $('.add-logo-form').hide();
    $('.edit-word, .edit-meaning').hide();
    $('.submit, .cancel').parent().hide();

    $("#all-words").click(function() {
      location.reload();
    });

    $("#add-word").click(function() {
      $('#word-form').show();
      $('.add-logo-form').hide();
    });

    $("#cancel").click(function() {
      $('#word-form').hide();
      location.reload();
    });

    $("#word-form").submit(function() {
      let word = $('#word').val().trim();
      let meaning = $('#meaning').val().trim();

      $.ajax({
        url: '/word',
        method: 'POST',
        data: JSON.stringify({ 
          word: word, 
          meaning: meaning 
        }),
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        success: function(response) {
          location.reload();
        },
        error: function(xhr, status, error) {
          console.log('Error adding word: ' + error);
        }
      });
    });

    // Handle delete button clicks
    $(".delete").click(function() {
      let word_id = $(this).attr('id');
      console.log('Deleting word with ID: ' + word_id);

      $.ajax({
        url: '/word/'+ word_id +'/delete',
        method: 'POST',
        data: JSON.stringify({ 
          word: word, 
          meaning: meaning 
        }),
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        success: function(response) {
          location.reload();
        },
        error: function(xhr, status, error) {
          console.log('Error deleting word: ' + error);
        }
      });
    });

    $(".edit").click(function() {
      let parent_tr = $(this).parents('tr');
      parent_tr.find('.edit-word, .edit-meaning').show();
      parent_tr.find('.submit, .cancel').parent().show();
      parent_tr.find('.word-word, .word-meaning').hide();
      parent_tr.find('.edit, .delete').parent().hide();
      
    });
    
    
    // Handle submit button clicks
    $(".update-form").submit(function() {
      let parent_tr = $(this).parents('tr');
      let word = parent_tr.find('.edit-word input').val().trim();
      let meaning = parent_tr.find('.edit-meaning textarea').val().trim();
      
      // if (word === '' || meaning === '') {
      //   alert('Word and meaning cannot be empty!');
      //   parent_tr.find('.edit-word, .edit-meaning').show();
      //   parent_tr.find('.submit, .cancel').parent().show();
      //   parent_tr.find('.word-word, .word-meaning').hide();
      //   return;
      // }
      
      let word_id = parent_tr.find('.submit').attr('id');
      
      console.log('Editing word with ID: ' + word_id);

      $.ajax({
        url: '/word/'+ word_id +'/update',
        method: 'POST',
        data: JSON.stringify({ 
          word: word, 
          meaning: meaning 
        }),
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        success: function(response) {
          location.reload();
        },
        error: function(xhr, status, error) {
          console.log('Error updating word: ' + error);
        }
      });
    });
    
    
    // Handle cancel button clicks
    $(".cancel").click(function() {
      let parent_tr = $(this).parents('tr');
      parent_tr.find('.edit-word, .edit-meaning').hide();
      parent_tr.find('.submit, .cancel').parent().hide();
      parent_tr.find('.word-word, .word-meaning').show();
      parent_tr.find('.edit, .delete').parent().show();
      $('.input').val('');
    });

    $('.add-logo').click(function (){
      $('.add-logo-form').show();
      $('#word-form').hide();
    })
      
    $('#cancel-logo').click(function (){
      $('.add-logo-form').hide();
    })
    
    $('#submit-logo').click(function (){
      let data = new FormData();
      data.append('file', $('#input-logo')[0].files[0]);

     
      $.ajax({
        url: '/logo',
        method: 'POST',
        data: data,
        processData: false,
        enctype: 'multipart/form-data',
        contentType: false,
        success: function(response) {
          location.reload();
        },
        error: function(xhr, status, error) {
          console.log('Error adding logo: ' + error);
        }
      });
    });

}


// window.onload = function() {
//     const wordForm = document.querySelector('#word-form');
//     wordForm.hidden = true;
// };

// document.querySelector('#add-word').addEventListener('click', function() {
//     $('#word-form').toggle();
// });