$(function () {
    $('#inordertraversal').click(function () {
        var url = $(this).attr('data-url');
        var token = $(this).attr('data-token');
        var travel = $(this).attr('data-travel-type');
        console.log(travel);
        $.ajax({
            type: "POST",
            url: url,
            data: {
                'tree': $(this).attr('name'),
                'type': travel,
                'csrfmiddlewaretoken': token
            },
            dataType: "json",
            success: function (response) {
                // console.log(response);
                var obj = response.nodes;
                $('#inorder').empty();
                $.each(obj, function(k, v) {
                  $("#inorder").append("<slug class='badge badge-primary badge-pill mr-2'>"+v.value+"</slug>");
                });
                // let inData = response.nodes.map(item => item.value);
            },
            error: function (rs, e) {
                console.log(e);
            }
        });
    });
    $('#preordertraversal').click(function () {
        var url = $(this).attr('data-url');
        var token = $(this).attr('data-token');
        var travel = $(this).attr('data-travel-type');
        console.log(travel);
        $.ajax({
            type: "POST",
            url: url,
            data: {
                'tree': $(this).attr('name'),
                'type': travel,
                'csrfmiddlewaretoken': token
            },
            dataType: "json",
            success: function (response) {
                // console.log(response);
                var obj = response.nodes;
                $('#preorder').empty();
                $.each(obj, function(k, v) {
                  $("#preorder").append("<slug class='badge badge-primary badge-pill mr-2'>"+v.value+"</slug>");
                });
                // let inData = response.nodes.map(item => item.value);
            },
            error: function (rs, e) {
                console.log(e);
            }
        });
    });
    $('#postordertraversal').click(function () {
        var url = $(this).attr('data-url');
        var token = $(this).attr('data-token');
        var travel = $(this).attr('data-travel-type');
        console.log(travel);
        $.ajax({
            type: "POST",
            url: url,
            data: {
                'tree': $(this).attr('name'),
                'type': travel,
                'csrfmiddlewaretoken': token
            },
            dataType: "json",
            success: function (response) {
                // console.log(response);
                var obj = response.nodes;
                $('#postorder').empty();
                $.each(obj, function(k, v) {
                  $("#postorder").append("<slug class='badge badge-primary badge-pill mr-2'>"+v.value+"</slug>");
                });
                // let inData = response.nodes.map(item => item.value);
            },
            error: function (rs, e) {
                console.log(e);
            }
        });
    });
});