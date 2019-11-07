<?php
	error_reporting(0);
	session_start();

	if (file_exists($_GET['p'].'.php'))
		include $_GET['p'].'.php';
	else if (isset($_GET['p']))
		include $_GET['p'];
	else
		echo '<script>location.href="./?p=create";</script>';
?>