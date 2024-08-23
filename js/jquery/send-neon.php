<?php $admin_email = 'm.e.morozov1@gmail.com'



?>
<html>
<body>







<?php


$tel = $_POST["telephone"];
$email = $_POST["email"];
$message =  $_POST["message"];
$headers = 'From: oro' . "\r\n" .
    'Reply-To: m.e.morozov1@gmail.com' . "\r\n" .
    'X-Mailer: PHP/' . phpversion();


  if(@mail($admin_email, $tel, $message, $headers)) {
              // Set a 200 (okay) response code.
              http_response_code(200);
              echo "<img src='http://www.mycreditinfo.co.uk/assets/creditexpert/img/imgCheckSm.png'> Заявка отправлена.";
          } else {
              // Set a 500 (internal server error) response code.
              http_response_code(500);
              echo "Возникла проблема. Возможно вы захотите позвонить по тел. +79035181715, чтобы уточнить заказ. Спасибо.";
          }
?>
</body>
</html>
