

$(".buttonSend").click(sendText)


function sendText () {


    var text = $(".textArea").val()


    dados = {text:text}

    $.post("http://localhost:8000/results",dados).fail(function(){console.log("FAIL....")}).always(function(){

        setTimeout(

            function (){

                console.log("waiting")

            }, 1400
        )

        
    }

    ) 


}