
function ajax_return(url, send_package, successFunc, errorFunc) {
    return $.ajax({
          url: url,
          data: JSON.stringify(send_package),
          type: "POST",
          dataType: "json",
          contentType: 'application/json',
          success: function(response) {
            console.log("success");
            successFunc(response)
          },
          error: function(xhr, status, error) {
              console.log("Data Retrival Failed ajax_return function going to ", url);
              errorFunc(error);
          },
      });   
  }


function search_form(){
    $('#table_here').html("<h3>Working...</h3>")
    var send_package = {
        "location": "webNavSearch",
        "package": $('#searchbar').val(),
        "numpage": $('#numpage').val()
    }
    url = "http://localhost:9000/pass_data"
    ajax_return(url, send_package, create_table, failpass)
    }

function failpass(error){
    console.log("ERROR: ", error)
    $('#table_here').text("Sorry... Something went wrong with the search")
}

function create_table(recieve_list){
    console.log("recieve_list", recieve_list)
    var request_table = ""
    request_table += '<form method="POST" id="myForm" action="/collection">'
    request_table += '<button id="render_button" class="btn btn-success btn-lg" type="submit">GET MEAL</button>'
    request_table +=  '<table class="table table-hover">\
                            <thead>\
                                <tr>\
                                <th scope="col">Select</th>\
                                <th style="width: 35%" scope="col">Recipie</th>\
                                <th scope="col">Image</th>\
                                </tr>\
                            </thead>\
                            <tbody>'

    for (const meal in recieve_list) {
        var meal_obj = {}
        meal_obj[meal] = recieve_list[meal]
        console.log("meal_obj", meal_obj)
        request_table += '<tr class="table-default" onclick="selectRow(this)"><td>'
        request_table +='<div class="form-check">'
        request_table +="<input class='form-check-input' name='chkbx' meal='"+meal+"' type='checkbox' value='"+JSON.stringify(meal_obj)+"'>\
                        </div></td>"
        request_table += '<td>'+meal+'</td>'
        request_table += '<td> <img height="150" width="200" src="'+recieve_list[meal]["image"]+'"></td></tr>'
    }                            
    request_table += '</tbody></table>'
    $('#table_here').html(request_table)
}

function selectRow(row){
    var firstInput = row.getElementsByTagName('input')[0];
    firstInput.checked = !firstInput.checked;
}


