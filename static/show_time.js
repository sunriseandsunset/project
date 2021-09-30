function show() {
         console.log("test");
         var longitude = $("#longitude").val();
         var latitude = $("#latitude").val();
         var date = $("#locdate").val();
         console.log(longitude)
         console.log(latitude)
         console.log(date)


         $.ajax({
             type: "GET",
             url: "http://apis.data.go.kr/B090041/openapi/service/RiseSetInfoService/getLCRiseSetInfo?&longitude=" + longitude + "&latitude=" + latitude + "&locdate=" + date + "&dnYn=N&ServiceKey=/oZ4AFQEH6WdKfRkiTxU9cNH8VHjxNsZO3PeRFfdDwIQLI3TfmMbjfQvhRSJyrACs3w1ARppFgEkiz5ebTfibg==",
             dataType: 'xml',
             success: function (response) {
                 xmlParsing(response);

             },
             error: function (xhr, status, msg) { // 통신 실패시 호출해야하는 함수
                 console.log('상태값 : ' + status + ' Http에러메시지 : ' + msg);
             },

         });
     }

     function xmlParsing(data) {
         var infoList = ``;
         console.log(data)
         $(data).find('items').each(function (index, item) {


             infoList += `
				<tr>
					<td>${$(this).find('sunrise').text()}</td>
					<td>${$(this).find('sunset').text()}</td>

				</tr>
			`;
             $('#info').empty().append(infoList);

         });
     }