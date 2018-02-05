	$(document).ready(function() {
		//	<!-- Real-time Validation -->
			//	<!--Name can't be blank--> //text
				$('#input-text').on('change', function() {
                    var input = $(this);
                    var re = /^[a-zA-Z\s]+$/;
                    var is_name = re.test(input.val());
					if(is_name){input.removeClass("invalid").addClass("valid");}
					else{input.removeClass("valid").addClass("invalid");}
				});
				
			//	<!--Email must be an email -->
				$('#input-number').on('change', function() {
					var input=$(this);
                    //var re = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
                    var is_num = input.val();
                    var test = (!isNaN(parseFloat(is_num)) && isFinite(is_num));
					//var is_email=re.test(input.val());
                    if (test){input.removeClass("invalid").addClass("valid");}
					else{input.removeClass("valid").addClass("invalid");}
				});


				//<!--Website must be a website -->
                $('#input-email').on('change', function() {
                    var input = $(this);
                    var re = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
                    var is_email=re.test(input.val());
                    if (is_email) { input.removeClass("invalid").addClass("valid"); }
                    else { input.removeClass("valid").addClass("invalid"); }
				});
				
		//		<!--Message can't be blank -->
				//$('#contact_message').keyup(function(event) {
				//	var input=$(this);
				//	var message=$(this).val();
				//	console.log(message);
				//	if(message){input.removeClass("invalid").addClass("valid");}
				//	else{input.removeClass("valid").addClass("invalid");}	
				//});
		
		//	<!-- After Form Submitted Validation-->
			$("#submitbutton").click(function(event){
                var form_data = $("#inputform").serializeArray();
				var error_free=true;
				for (var input in form_data){
					var element=$("#input"+form_data[input]['name']);
					var valid=element.hasClass("valid");
					var error_element=$("span", element.parent());
                    if (!valid) { error_element.removeClass("error").addClass("error_show"); error_free=false;}
					else{error_element.removeClass("error_show").addClass("error");}
				}
				if (!error_free){
					event.preventDefault(); 
				}
				else{
                    alert('No errors: Form will be submitted');
                    event.preventDefault(); 
                }

                var email = $('#input-email').hasClass("valid");
                if (!email) {
                    $('#emailerror').removeClass("error").addClass("error_show");
                }
                else
                    $('#emailerror').removeClass("error_show").addClass("error");


                var number = $('#input-number').hasClass("valid");
                if (!number) {
                    $('#numbererror').removeClass("error").addClass("error_show");
                }
                else {
                    $('#numbererror').removeClass("error_show").addClass("error");

                }

                var text = $('#input-text').hasClass("valid");
                if (!text) {
                    $('#texterror').removeClass("error").addClass("error_show");
                }
                else {
                    $('#texterror').removeClass("error_show").addClass("error");
                }
                    
                $('#input-text').change();
                $('#input-number').change();
                $('#input-email').change();
                
            



			});
			
			
			
		});