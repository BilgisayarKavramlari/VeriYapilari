<?php
for($i=0;$i<21;$i++)
	$arr[$i]=rand(10,100000);
$max=$arr[0];
print_r($arr);
for($i=1;$i<21;$i++)
$max = $max<$arr[$i] ? $arr[$i] : $max;
echo "<br/>en böyük element: ".$max;
?>
