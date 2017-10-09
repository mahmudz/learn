$(document).ready(function(){
	var apiKey = 'a806f370188b2c4caf03ef176df53a2c';
	var city = 'Dhaka';

	$.ajax({
		url			: "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+apiKey+"",
		type		: "GET",
		dataType	: "JSON",
		"success"    : function(data){
			console.log(data);
		}
	});
});