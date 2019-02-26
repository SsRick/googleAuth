<?php
if ($_GET["code"]) {
    echo "code " . $_GET['code'] . "<br />";
    file_put_contents('code.txt', $_GET['code'], FILE_APPEND | LOCK_EX);
    $postData = array('code' => $_GET['code']);
    $ch       = curl_init('https://kdl7hllpzh.execute-api.us-west-2.amazonaws.com/testing');

    curl_setopt_array($ch, array(
        CURLOPT_POST           => true,
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_HTTPHEADER     => array(
            'Authorization: none',
            'Content-Type: application/json',
        ),
        CURLOPT_POSTFIELDS     => json_encode($postData),
    ));
    $response = curl_exec($ch);
    header("Location: success.html", true, 301);
    exit();
}
