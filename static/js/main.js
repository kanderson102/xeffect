$(document).ready(function () {
//     //Initially load the habits, day_x_boolean, count
//     // GET /api/v1.0/habits

//     $('form').submit(function(event) {
//         //instert the new element in the DB
//     })
// })


function counter(change) {
    data = JSON.stringify({checked: change})
    console.log(data)
    $.ajax({
        type: "POST",
        //the url where you want to sent the userName and password to
        url: '/',
        dataType: 'json',
        contentType: 'application/json',
        // async: true,
        //json object to sent to the authentication url
        data: data,
        success: function (response) {
            console.log(response);
            alert("Thanks!");
            },
        error: function(error) {
            console.log(error);
            }
    });
    event.preventDefault();
};

function x_toggle(box) {
    if (box.innerHTML == "X") {
        box.innerHTML = "";
        return 1;
    } else {
        box.innerHTML = "X";
        return -1;
    }
};

document.getElementById("grid").addEventListener("click", function(e) {
    if(e.target && e.target.matches("td.box")) {
        var count_step = x_toggle(e.target)
        console.log(count_step)
        var habit = $(this).parent().parent().attr('id');
        counter(count_step)
    } else if(e.target && e.target.matches("td.results")) {
        box.innerHTML = "X";
    }
});

// function() {
//     $('a#input').bind('click', function() {
//         $.getJSON('/_background_process', {
//             var_name: $('input[name="variable"]').val(),
//         }),
//         function(data) {
//             $("result").text(data.result);
//         }
//     })
// }
});
