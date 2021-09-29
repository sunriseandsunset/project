function show(){

            let want_place=$("#place").val()
            $.ajax({
                type: 'GET',
                url: "/place?give_place="+want_place,
                data: {},


                success: function(response){
                    console.log(response)

                    console.log(response[0]['name'])

                    for(let i=0;i<response.length;i++)
                    {
                        let name=response[i]['name'];
                        let addr=response[i]['address'];
                        let longtitude=response[i]['longtitude'];
                        let latitude=response[i]['latitude'];

                        let temp_html=`<tr>
                                                <td>${name}</td>
                                                <td>${longtitude}</td>
                                                <td>${latitude}</td>
                                           </tr>`


                        $('#info').append(temp_html)
                    }


                    //alert(addr)


                },
                error: function(request, status, error){
                    alert('ajax 통신 실패')
                    alert(error);
                }
            })}


/*
function post(){
            let place=$("#place").val()
            $.ajax({
                type: 'POST',
                url: "/place",
                data: {place_give:place},


                success: function(response){
                    console.log(response['msg'])




                    //alert(addr)


                },
                error: function(request, status, error){
                    alert('ajax 통신 실패')
                    alert(error);
                }
            })
        }
        */
