<?php
############################################################
# script to check Best Buy stock of Apple Pencil           #
# sku number: 4538802                                      #
# you need a deverloper api key from Best Buy:             #
# https://developer.bestbuy.com                            #
# by: Jeremy A. Gibbs                                      #
# https://gist.github.com/jeremygibbs/1a6c248d12dda568d67d #
############################################################
error_reporting(E_ALL);
ini_set('display_errors', 'On');

// Let's check online availability
$json   = file_get_contents("http://api.bestbuy.com/v1/products(sku=4538802)?format=json&apiKey=<YOUR_API_KEY>");
$data   = json_decode($json,true);
$online = $data['products'][0]['onlineAvailability'] ? true : false;

//-- If online, send an email alert --//
if ($online) {
	$url     = $data['products'][0]['url'] ;
	$to      = '<YOUR@EMAIL.com>';
	$subject = 'Pencil available online at Best Buy';
	$message = "$url";
	mail($to, $subject, $message, null, '-f<YOUR@FROM_EMAIL.COM>'); 
}

//-- Let's check in-store availability --//
$instore = $data['products'][0]['inStoreAvailability'] ? true : false;

//-- If generally available in-store, search within a set distance of a particular location via lat/lon -//
//-- As an example, here is a search for within 200 miles of Oklahoma City, OK --//
if ($instore) {
	$json    = file_get_contents("http://api.bestbuy.com/v1/stores(area(28.534902,-81.313324,200))+products(sku=4538802)?apiKey=<YOUR_API_KEY>&format=json");
	$data    = json_decode($json,true);
	$stores  = $data['stores'];
	$message = "";
	$url     = "";
	
	//-- If available in-store within the search area, send an email alert -//
	if (count($stores)>0) {
		foreach($stores as $store) {
    		$name = $store['longName'];
			$dist     = $store['distance'];
			$url      = $store['products'][0]['url'] ;
			$message .= "$name, $dist miles from <LOCATION> \n\n";
    	}
	} else {
		$message .= "There are no Pencils in-store within <DISTANCE> miles of <LOCATION>. \n\n";
	}
}


//-- Write a simple html table (either for web viewing or in Panic's StatusBoard app) --//
$panic_online  = $online ?  "YES" : "NO";
$panic_instore = ($instore && count($stores) > 0) ? true : false;

$html = '
<html>
<style>	
.name {
	width: 50%;
	font-size: 22px;
}
.state {
	width: 50%;
	text-align: center;
	font-size: 22px;
}
</style>
<table data-refresh-every-n-seconds="300">
	<tr>
		<th class="name">Type</th>
		<th class="state">Availability</th>
	</tr>
	<tr>
		<td class="name">Online</td>
		<td class="state">'. $panic_online .'</td>
	</tr>
	<tr>
		<td class="name">In Store</td>';
	if (!$panic_instore) {
		$html .= '
		<td class="state">NO</td>
	</tr>';} else {
		$html .='
			<td class="state">YES</td>
			</tr>
			<tr>
			<th class="name">Store Name</th>
			<th class="state">Distance (miles)</th>
			</tr>';
			foreach($stores as $store) {
				$html .='
				<tr>
				<td class="name">'. $store["longName"] .'</td>
				<td class="state">'. $store["distance"] .'</td>
				</tr>';
			}
		}
$html  .= '</table></html>';
$output = fopen("/PATH/TO/YOUR/WEBFILES/status_bestbuy.html", "w");
fwrite($output, $html);
fclose($output);
?>