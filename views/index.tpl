<!doctype html>
<html lang="en">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Lunch Choice Maker</title>
<!-- <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script> -->
<!-- <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css"> -->
<!-- <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script> -->

<link rel="stylesheet" href="../css/bootstrap.min.css">
<!-- <script src="../js/jquery&#45;migrate&#45;1.4.1.min.js"></script> -->
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js">
<script src="../js/bootstrap.min.js"></script>

<link rel="stylesheet" href="../css/styles.css">
<script type="text/javascript">
    $(document).ready(function(){
        $("button#generate").click(function(){
            $.ajax({
                type: 'GET',
                url: 'lunch_choice_maker',
                success: function(data) {
                    $("p#msg").text(data);
                }
            });
        });
    });
</script>
</head>

<body>
<div id = "background">
    <div id = "background_transparent">
        <div id="content" style="text-align: center; padding: 0.5em;">
            <br/>
            <h1 id="logo" style="font-family: futura; letter-spacing: 0; font-size: 2em; margin-top: 1em; margin-bottom: 1.2em;">
                Quay Lunch Choice Maker
            </h1>
            <br/>

            <button id="generate" type="button" class="btn btn-primary" style="font-size:2em;">
            Generate Lunch Choice
            </button>
            <br/><br/>

            <p id="msg" style="font-size:2em;"></p>
            <br/><br/><br/>

            <p style="font-size:1.5em;">Lunch Options:</p>
            {{ !lunch_options }}

            <br/><br/>
            <p style="font-size:1.5em;">Add New Lunch Options:</p>
            <form action="add_lunch_choice" method="post" style="font-size: 1.5em; text-align:center; width:80%; margin:0 auto;">
            <input type="text" name="restaurant" style="width:100%;">
            <input class="btn btn-info" type="submit" value="Submit" style="margin-top:20px;">
            </form>
        </div>
    </div>
</div>
</body>
</html>
