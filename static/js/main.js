
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
    ajax_return(url, send_package, create_table, console.log)
    }

function create_table(recieve_list){
    var request_table = ""
    request_table =  '<table class="table table-hover">\
                            <thead>\
                                <tr>\
                                <th scope="col">Select</th>\
                                <th scope="col">Recipie</th>\
                                </tr>\
                            </thead>\
                            <tbody>'

    for (let i = 0; i < recieve_list.length; i++) {
        const meal = recieve_list[i];
        request_table += '<tr class="table-default"><td>'

        request_table +='<div class="form-check">\
                            <input class="form-check-input" type="checkbox" value="">\
                        </div></td>'  
        
        request_table += '<td>'+meal+'</td></tr>'  
    }

    request_table += '</tbody></table>'

    console.log("in return table: ", recieve_list)
    $('#table_here').html(request_table)
}
