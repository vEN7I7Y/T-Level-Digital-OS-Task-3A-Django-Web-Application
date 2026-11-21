//funtion for the carbon footprint calculation
function carbon_print_calc() {
  //gets both form values on submission
  const carbon_data = document.getElementById("id_co2_data").value;
  const co2_emmissions = document.getElementById("id_co2_emmissions").value;
  //calculates it
  let result = co2_emmissions * carbon_data;
  //outputs it via an alert
  window.alert("Your Carbon Footprint is: " + result + "kw per day");
}

//funtion for the energy usage calculation
function energy_print_calc() {
  //gets both form values on submission
  const powerUsage = document.getElementById("id_power_usage").value;
  const timeOn = document.getElementById("id_time_on").value;
  //calculates it
  let result = powerUsage * timeOn;
  //outputs it via an alert
  window.alert("Your Power Usage per day is: " + result + "w");
}
