$(document).ready(function () {
   $.getJSON('http://localhost:8000/api/json_displaycategory', function (data) {
      $('#categoryid').append($('<option>').text('-Select Category-'))
      data.map((item) => {
         $('#categoryid').append($('<option>').text(item.categoryname).val(item.id));
      });
   });

   $('#categoryid').change(function () {
      $.getJSON('http://localhost:8000/api/display_json_subcategory', { cid: $("#categoryid").val() }, function (data) {
         $('#subcategoryid').empty()
         $('#subcategoryid').append($('<option>').text('-Select Brand-'))
         data.map((item) => {
            $('#subcategoryid').append($('<option>').text(item.subcategoryname).val(item.id));
         });
      });
   });
});

