function show(){

            let want_area=$("#inputGroupSelect04").val()
            alert(want_area)
            $.ajax({
                type: 'GET',
                url: "/place?give_area="+want_area,
                data: {},


                success: function(response){
                    console.log(response)


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
