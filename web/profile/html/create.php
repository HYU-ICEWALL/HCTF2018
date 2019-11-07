<?php
	// session_start();

	if(array_count_values($_POST)){
		if(isset($_FILES)){
			$allowed_ext = array('jpg','jpeg','png','gif');
			$ext = array_pop(explode('.', $_FILES['photo']['name']));

			if( !in_array($ext, $allowed_ext) ) {
				echo "허용되지 않는 확장자입니다. (jpg, jpeg, png, gif)";
				exit;
			}

			if (@getimagesize($_FILES['photo']['tmp_name']) !== false) {
				$dest = "user_img/" . md5('jeong.su_'.$_FILES['photo']['tmp_name']) . ".$ext";
				move_uploaded_file($_FILES['photo']['tmp_name'], $dest);
			} else {
				echo "이미지가 아닙니다. ";
				exit;
			}
		}

		$_SESSION['name'] = $_POST['name'];
		$_SESSION['message'] = $_POST['message'];
		$_SESSION['service'] = $_POST['service'];
		$_SESSION['email'] = $_POST['email'];
		$_SESSION['img'] = $dest;

		echo '<script>location.href="./?p=view";</script>';
		exit;
	}
?>
<!DOCTYPE html>
<html lang="en">
<head>
	<title>Create Your Profile</title>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
<!--===============================================================================================-->
	<link rel="icon" type="image/png" href="images/icons/favicon.ico"/>
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="vendor/bootstrap/css/bootstrap.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="fonts/font-awesome-4.7.0/css/font-awesome.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="vendor/animate/animate.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="vendor/css-hamburgers/hamburgers.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="vendor/animsition/css/animsition.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="vendor/select2/select2.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="vendor/daterangepicker/daterangepicker.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="css/util.css">
	<link rel="stylesheet" type="text/css" href="css/main.css">
<!--===============================================================================================-->
</head>
<body>


	<div class="container-contact100">
		<div class="wrap-contact100">
			<form class="contact100-form validate-form" method='POST' enctype='multipart/form-data'>
				<span class="contact100-form-title">
					Create Your Profile
				</span>

				<div class="wrap-input100 validate-input" data-validate="Name is required">
					<span class="label-input100">Your Name</span>
					<input class="input100" type="text" name="name" placeholder="Enter your name">
					<span class="focus-input100"></span>
				</div>

				<div class="wrap-input100 validate-input" data-validate = "Message is required">
					<span class="label-input100">About Me</span>
					<textarea class="input100" name="message" placeholder="About Me here..."></textarea>
					<span class="focus-input100"></span>
				</div>

				<div class="wrap-input100 validate-input" data-validate = "Valid email is required: ex@abc.xyz">
					<span class="label-input100">Email</span>
					<input class="input100" type="text" name="email" placeholder="Enter your email addess">
					<span class="focus-input100"></span>
				</div>

				<div class="wrap-input100 input100-select">
					<span class="label-input100">The best Language</span>
					<div>
						<select class="selection-2" name="service">
							<option>C/C++</option>
							<option>Javascript</option>
							<option>Python</option>
							<option>PHP</option>
							<option>Java</option>
							<option>Ruby</option>
						</select>
					</div>
					<span class="focus-input100"></span>
				</div>



				<div class="wrap-input100 validate-input" data-validate="Name is required">
					<span class="label-input100">Your Photo</span>
					<input class="input100" type="file" name="photo">
					<span class="focus-input100"></span>
				</div>

				<div class="container-contact100-form-btn">
					<div class="wrap-contact100-form-btn">
						<div class="contact100-form-bgbtn"></div>
						<button class="contact100-form-btn">
							<span>
								Submit
								<i class="fa fa-long-arrow-right m-l-7" aria-hidden="true"></i>
							</span>
						</button>
					</div>
				</div>
			</form>
		</div>
	</div>



	<div id="dropDownSelect1"></div>

<!--===============================================================================================-->
	<script src="vendor/jquery/jquery-3.2.1.min.js"></script>
<!--===============================================================================================-->
	<script src="vendor/animsition/js/animsition.min.js"></script>
<!--===============================================================================================-->
	<script src="vendor/bootstrap/js/popper.js"></script>
	<script src="vendor/bootstrap/js/bootstrap.min.js"></script>
<!--===============================================================================================-->
	<script src="vendor/select2/select2.min.js"></script>
	<script>
		$(".selection-2").select2({
			minimumResultsForSearch: 20,
			dropdownParent: $('#dropDownSelect1')
		});
	</script>
<!--===============================================================================================-->
	<script src="vendor/daterangepicker/moment.min.js"></script>
	<script src="vendor/daterangepicker/daterangepicker.js"></script>
<!--===============================================================================================-->
	<script src="vendor/countdowntime/countdowntime.js"></script>
<!--===============================================================================================-->
	<script src="js/main.js"></script>

	<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-23581568-13"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-23581568-13');
</script>

</body>
</html>
