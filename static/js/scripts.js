window.onload = function() {
    $('#get-started-btn').click(function() {
      window.location.href = '/getstarted';
    })

    $('.students-table').hide();
    $('.student-deatils-page').hide();
    
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
      let nextOfKin = $('#input-next-of-kin').val()
      let academicScore = $('#wassce').val()

      console.log(firstName, middleName, lastName, email, dateOfBirth, gender, address, phoneNumber, region, district, nextOfKin, academicScore)
      
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
          nextOfKin: nextOfKin,
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
          console.log('Error adding student: ' + error + status);
        }
      })
      
    })

    // Sending image
    $('.form-signin').submit(function(e){
      e.preventDefault();
      let data = new FormData();
      data.append('file', $('#inputfile')[0].files[0]);
      
      console.log(data)
      

      
      $.ajax({
        url: '/getstarted/register/profile',
        method: 'POST',
        data: data,
        encType: 'multipart/form-data',
        processData: false,
        contentType: false,
        success: function(response) {
          $('.form-signin').hide();
          $('.students-table').show();
          console.log('done')
        },
        error: function(status, error) {
          console.log('Error adding student: ' + error + status);
        }
      })
      
    })

    $('body').keydown(function(e){
      console.log(e.key)
      if (e.key === ("Enter")) {
        $('#submit-btn').click();
      }
    
    })
  
}


// window.onload = function() {
//     const wordForm = document.querySelector('#word-form');
//     wordForm.hidden = true;
// };

// document.querySelector('#add-word').addEventListener('click', function() {
//     $('#word-form').toggle();
// });