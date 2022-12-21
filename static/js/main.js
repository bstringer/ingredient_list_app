
function ajax_return(url, send_package, successFunc, errorFunc) {
    url_send = "http://localhost:9000" + url
    console.log("url_send", url_send)
    return $.ajax({
          url: url_send,
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
    var send_package = $('#searchbar').val()
    console.log("send_package", send_package)
    url = "/pass_data"
    ajax_return(url, send_package, create_table, failpass)
    }

function failpass(error){
    console.log("ERROR: ", error)
    $('#table_here').text("Sorry... Something went wrong with the search")
}

function create_table(recieve_list){
    console.log("recieve_list", recieve_list)
    var request_table = ""
    request_table =  '<table class="table table-hover">\
                            <thead>\
                                <tr>\
                                <th scope="col">Select</th>\
                                <th style="width: 35%" scope="col">Recipie</th>\
                                <th scope="col">Image</th>\
                                </tr>\
                            </thead>\
                            <tbody>'


    for (const meal in recieve_list) {
        request_table += '<tr class="table-default"><td>'
        request_table +='<div class="form-check">\
                        <input id="'+meal+'" class="form-check-input" type="checkbox" value="">\
                        </div></td>'
        request_table += '<td>'+meal+'</td>'
        request_table += '<td> <img height="150" width="170" src="'+recieve_list[meal]+'"> </td></tr>'
    }                            

    request_table += '</tbody></table>'
    $('#table_here').html(request_table)
    render_button = '<button id="render_button" class="btn btn-info my-2 my-sm-0" onclick="render_menu()">Use</button>'
    $('#render_button_location').html(render_button)
}
