window.onload = function() {
    $('#get-started-btn').click(function() {
      window.location.href = '/getstarted';
    })

    $('.students-table').hide();
    
    $('.form-signin').submit(function(e){
      e.preventDefault();
      let data = new FormData();
      data.append('file', $('#inputfile')[0].files[0]);
      
      console.log(data)
      let firstName = $('#input-first-name').val()
      let middleName = $('#input-middle-name').val()
      let lastName = $('#input-last-name').val()
      let email = $('#input-email').val()
      let dateOfBirth = $('#input-date-of-birth').val()
      let gender = $('.gender:checked').val()
      let phoneNumber = $('#input-number').val()
      let address = $('#input-address').val()
      let region = $('#region').val()
      let district = $('#district').val()
      let nextOfKing = $('#input-next-of-king').val()
      let academicScore = $('#wassce').val()

      
      $.ajax({
        url: '/getstarted/register',
        method: 'POST',
        data: JSON.stringify({ 
          firstName: firstName,
          middleName: middleName,
          lastName: lastName,
          email: email,
          dateOfBirth: dateOfBirth,
          gender: gender,
          phoneNumber: phoneNumber,
          address: address,
          region: region,
          district: district,
          nextOfKing: nextOfKing,
          academicScore: academicScore
        }),
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        success: function(response) {
          $('.form-signin').hide();
          $('.students-table').show();
          console.log('done')
        },
        error: function(status, error) {
          console.log('Error adding word: ' + error + status);
        }
      })
      
    })

    // $('.form-signin').submit(function(e){
    //   e.preventDefault();
    //   console.log('Form submitted')
    // })
}


// window.onload = function() {
//     const wordForm = document.querySelector('#word-form');
//     wordForm.hidden = true;
// };

// document.querySelector('#add-word').addEventListener('click', function() {
//     $('#word-form').toggle();
// });