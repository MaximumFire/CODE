<?php
$servername = "ec2-52-18-116-67.eu-west-1.compute.amazonaws.com";
$username = "kecmmeicnbsdjt";
$password = "efe1b6cc8135fee09a8e91a7b51271697b43a88187bc80c39093cbb3cb3b50c9";

// Create connection
$conn = mysqli_connect($servername, $username, $password);

// Check connection
if (!$conn) {
  die("Connection failed: " . mysqli_connect_error());
}
echo "Connected successfully";
?> 