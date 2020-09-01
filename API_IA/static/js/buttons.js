

$(".buttonSend").click(sendText)


function sendText () {


    var text = $(".textArea").val()


    dados = {text:text}

    $.post("http://localhost:8000/results",dados).fail(function(){console.log("FAIL....")}).done(




    function(){

        location.reload();

    }
    )


    

}