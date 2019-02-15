<?php
   if( $_GET["code"]) {
      echo "code ". $_GET['code']. "<br />";
      file_put_contents('code.txt',$_GET['code'],FILE_APPEND | LOCK_EX);
      header("Location: success.html", true, 301);
      exit();
   }
?>